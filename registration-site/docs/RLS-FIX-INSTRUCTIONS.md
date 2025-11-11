# Fix RLS Policy Error - Step by Step

## The Problem
You're seeing this error:
```
new row violates row-level security policy for table "workshop_registrations"
```

This means Supabase's Row Level Security (RLS) is blocking INSERT operations.

## Quick Fix (5 minutes)

### Step 1: Open Supabase Dashboard
1. Go to [supabase.com](https://supabase.com)
2. Log in to your account
3. Select your project: `newegg-ai-workshop` (or your project name)

### Step 2: Open SQL Editor
1. Click **"SQL Editor"** in the left sidebar
2. Click **"New query"** button (top right)

### Step 3: Copy and Paste This SQL

Copy the entire contents of `fix-rls-policy.sql` or use this:

```sql
-- Fix RLS Policy for workshop_registrations
-- This allows anonymous users to insert registrations

-- First, drop any existing policies
DROP POLICY IF EXISTS "Allow public inserts" ON workshop_registrations;
DROP POLICY IF EXISTS "Restrict reads" ON workshop_registrations;

-- Create policy to allow anonymous users to INSERT
CREATE POLICY "Allow public inserts" ON workshop_registrations
  FOR INSERT
  TO anon, authenticated
  WITH CHECK (true);

-- Create policy to restrict SELECT (only authenticated users can read)
CREATE POLICY "Restrict reads" ON workshop_registrations
  FOR SELECT
  TO authenticated
  USING (true);
```

### Step 4: Run the SQL
1. Click **"Run"** button (or press Cmd/Ctrl + Enter)
2. You should see: "Success. No rows returned"

### Step 5: Verify It Worked
Run this query to check:

```sql
SELECT 
    policyname,
    cmd,
    roles
FROM pg_policies 
WHERE tablename = 'workshop_registrations';
```

**Expected Result:**
- `Allow public inserts` | `INSERT` | `{anon,authenticated}`
- `Restrict reads` | `SELECT` | `{authenticated}`

### Step 6: Test the Form
1. Go back to your registration page
2. Refresh the page (hard refresh: Cmd+Shift+R)
3. Fill out and submit the form
4. It should work now! ✅

## Alternative: Check Current Policies

If you want to see what policies currently exist:

```sql
SELECT * FROM pg_policies WHERE tablename = 'workshop_registrations';
```

## Troubleshooting

### Still getting errors?
1. **Check if RLS is enabled:**
   ```sql
   SELECT tablename, rowsecurity 
   FROM pg_tables 
   WHERE tablename = 'workshop_registrations';
   ```
   `rowsecurity` should be `true`

2. **Check if policies exist:**
   ```sql
   SELECT * FROM pg_policies WHERE tablename = 'workshop_registrations';
   ```

3. **Disable RLS temporarily (for testing only):**
   ```sql
   ALTER TABLE workshop_registrations DISABLE ROW LEVEL SECURITY;
   ```
   ⚠️ **Warning:** Only use this for testing. Re-enable RLS after testing.

4. **Re-enable RLS:**
   ```sql
   ALTER TABLE workshop_registrations ENABLE ROW LEVEL SECURITY;
   ```

## What This Does

- ✅ **Allows public inserts**: Anyone can submit registrations (needed for your form)
- 🔒 **Protects data**: Only authenticated users can read registrations
- ✅ **Secure**: Your data is still protected from public access

## Need More Help?

- Check Supabase logs: Dashboard → Logs → API Logs
- Verify your anon key is correct in `js/config.js`
- Make sure you're using the correct Supabase project

