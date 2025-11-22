-- Step 2: Verify RLS Policies (run this AFTER creating them)
-- This query checks if the policies were created successfully

SELECT 
    policyname,
    cmd,
    roles
FROM pg_policies 
WHERE tablename = 'workshop_registrations';

-- Expected result:
-- policyname: "Allow public inserts" | cmd: "INSERT" | roles: {anon,authenticated}
-- policyname: "Restrict reads" | cmd: "SELECT" | roles: {authenticated}

