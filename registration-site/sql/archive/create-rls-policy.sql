-- Step 1: Create RLS Policies for workshop_registrations
-- Run this FIRST in Supabase SQL Editor

-- Drop existing policies if they exist
DROP POLICY IF EXISTS "Allow public inserts" ON workshop_registrations;
DROP POLICY IF EXISTS "Restrict reads" ON workshop_registrations;

-- Create policy to allow anonymous users to INSERT (for registration form)
CREATE POLICY "Allow public inserts" ON workshop_registrations
  FOR INSERT
  TO anon, authenticated
  WITH CHECK (true);

-- Create policy to restrict SELECT (only authenticated users can read)
CREATE POLICY "Restrict reads" ON workshop_registrations
  FOR SELECT
  TO authenticated
  USING (true);

-- This should return "Success. No rows returned"

