-- Diagnostic Script - Check Current RLS Status
-- Run this FIRST to see what's wrong

-- 1. Check if table exists
SELECT 'Table exists: ' || COUNT(*)::text as status
FROM information_schema.tables 
WHERE table_name = 'workshop_registrations';

-- 2. Check if RLS is enabled
SELECT 
    'RLS Status: ' || CASE WHEN rowsecurity THEN 'ENABLED' ELSE 'DISABLED' END as status
FROM pg_tables 
WHERE tablename = 'workshop_registrations';

-- 3. List ALL current policies
SELECT 
    'Current Policies:' as info,
    policyname,
    cmd as operation,
    roles::text as allowed_roles
FROM pg_policies 
WHERE tablename = 'workshop_registrations';

-- If no policies are returned, that's the problem!

