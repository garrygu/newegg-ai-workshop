-- Fix RLS Policies - Explicit Schema and Correct Syntax
-- The policies exist but might be on wrong schema or have wrong syntax

-- Step 1: Check which schema the table is in
SELECT 
    table_schema,
    table_name
FROM information_schema.tables 
WHERE table_name = 'workshop_registrations';

-- Step 2: Drop policies from ALL possible schemas
DROP POLICY IF EXISTS "Allow public inserts" ON public.workshop_registrations;
DROP POLICY IF EXISTS "Allow public inserts" ON workshop_registrations;
DROP POLICY IF EXISTS "Restrict reads" ON public.workshop_registrations;
DROP POLICY IF EXISTS "Restrict reads" ON workshop_registrations;

-- Step 3: Recreate with explicit public schema and correct syntax
CREATE POLICY "Allow public inserts" 
ON public.workshop_registrations
FOR INSERT
TO anon, authenticated
WITH CHECK (true);

-- Step 4: Alternative - Try with 'public' role (more permissive)
-- Uncomment this and comment out Step 3 if Step 3 doesn't work
-- CREATE POLICY "Allow public inserts" 
-- ON public.workshop_registrations
-- FOR INSERT
-- TO public
-- WITH CHECK (true);

-- Step 5: Recreate SELECT policy
CREATE POLICY "Restrict reads" 
ON public.workshop_registrations
FOR SELECT
TO authenticated
USING (true);

-- Step 6: Verify with full details
SELECT 
    schemaname,
    tablename,
    policyname,
    permissive,
    roles::text,
    cmd,
    qual,
    with_check
FROM pg_policies 
WHERE tablename = 'workshop_registrations';

