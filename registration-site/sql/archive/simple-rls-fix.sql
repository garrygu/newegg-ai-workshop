-- SIMPLE RLS FIX - Run this if policies don't exist
-- This is the minimal fix needed

-- Make sure RLS is enabled
ALTER TABLE workshop_registrations ENABLE ROW LEVEL SECURITY;

-- Drop any existing policies
DROP POLICY IF EXISTS "Allow public inserts" ON workshop_registrations;
DROP POLICY IF EXISTS "Restrict reads" ON workshop_registrations;
DROP POLICY IF EXISTS "Public can insert" ON workshop_registrations;
DROP POLICY IF EXISTS "Anyone can insert" ON workshop_registrations;

-- Create the INSERT policy (THIS IS THE KEY ONE)
CREATE POLICY "Allow public inserts" 
ON public.workshop_registrations
FOR INSERT
TO public
WITH CHECK (true);

-- Create the SELECT policy (optional, but good for security)
CREATE POLICY "Restrict reads" 
ON public.workshop_registrations
FOR SELECT
TO authenticated
USING (true);

-- Verify it worked
SELECT 
    policyname,
    cmd,
    roles::text
FROM pg_policies 
WHERE tablename = 'workshop_registrations';

