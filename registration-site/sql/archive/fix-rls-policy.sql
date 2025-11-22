-- Fix RLS Policy for workshop_registrations
-- Run this in Supabase SQL Editor if you're getting RLS errors

-- First, drop existing policies
DROP POLICY IF EXISTS "Allow public inserts" ON workshop_registrations;
DROP POLICY IF EXISTS "Restrict reads" ON workshop_registrations;

-- Create policy to allow anonymous users to INSERT
CREATE POLICY "Allow public inserts" ON workshop_registrations
  FOR INSERT
  TO anon, authenticated
  WITH CHECK (true);

-- Create policy to restrict SELECT (only authenticated users)
CREATE POLICY "Restrict reads" ON workshop_registrations
  FOR SELECT
  TO authenticated
  USING (true);

-- Verify the policies were created
SELECT 
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    qual,
    with_check
FROM pg_policies 
WHERE tablename = 'workshop_registrations';

