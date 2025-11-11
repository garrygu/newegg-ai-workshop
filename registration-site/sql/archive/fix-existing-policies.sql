-- Fix Existing Policies - They exist but might not be working correctly
-- The issue might be with the WITH CHECK clause or schema

-- Drop existing policies
DROP POLICY IF EXISTS "Allow public inserts" ON public.workshop_registrations;
DROP POLICY IF EXISTS "Restrict reads" ON public.workshop_registrations;

-- Recreate with explicit schema and simpler WITH CHECK
CREATE POLICY "Allow public inserts" 
ON public.workshop_registrations
FOR INSERT
TO anon, authenticated
WITH CHECK (true);

-- Alternative: Try with 'public' role instead
-- CREATE POLICY "Allow public inserts" 
-- ON public.workshop_registrations
-- FOR INSERT
-- TO public
-- WITH CHECK (true);

-- Recreate SELECT policy
CREATE POLICY "Restrict reads" 
ON public.workshop_registrations
FOR SELECT
TO authenticated
USING (true);

-- Verify
SELECT policyname, cmd, roles::text, with_check::text
FROM pg_policies 
WHERE tablename = 'workshop_registrations';

