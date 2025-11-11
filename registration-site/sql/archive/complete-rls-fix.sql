-- Complete RLS Fix for workshop_registrations
-- Run this ENTIRE script in Supabase SQL Editor
-- This will fix the RLS policy issue step by step

-- Step 1: Check if table exists (should return 1 row)
SELECT COUNT(*) as table_exists 
FROM information_schema.tables 
WHERE table_name = 'workshop_registrations';

-- Step 2: Check current RLS status
SELECT tablename, rowsecurity 
FROM pg_tables 
WHERE tablename = 'workshop_registrations';

-- Step 3: Enable RLS (if not already enabled)
ALTER TABLE workshop_registrations ENABLE ROW LEVEL SECURITY;

-- Step 4: Drop ALL existing policies (clean slate)
DO $$ 
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT policyname FROM pg_policies WHERE tablename = 'workshop_registrations') 
    LOOP
        EXECUTE 'DROP POLICY IF EXISTS "' || r.policyname || '" ON workshop_registrations';
    END LOOP;
END $$;

-- Step 5: Create INSERT policy (allows public registration)
CREATE POLICY "Allow public inserts" 
ON workshop_registrations
FOR INSERT
TO anon, authenticated
WITH CHECK (true);

-- Step 6: Create SELECT policy (restricts reads to authenticated users)
CREATE POLICY "Restrict reads" 
ON workshop_registrations
FOR SELECT
TO authenticated
USING (true);

-- Step 7: Verify policies were created
SELECT 
    policyname,
    cmd,
    roles,
    qual,
    with_check
FROM pg_policies 
WHERE tablename = 'workshop_registrations'
ORDER BY policyname;

-- Expected output:
-- "Allow public inserts" | INSERT | {anon,authenticated} | null | true
-- "Restrict reads" | SELECT | {authenticated} | true | null

