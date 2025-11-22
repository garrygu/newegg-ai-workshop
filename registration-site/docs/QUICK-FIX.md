# Quick Fix for RLS Error

## The Error
```
new row violates row-level security policy for table "workshop_registrations"
```

## Fastest Solution (Copy & Paste)

1. **Open Supabase Dashboard** → **SQL Editor**

2. **Copy and paste this ENTIRE block:**

```sql
-- Drop all existing policies
DO $$ 
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT policyname FROM pg_policies WHERE tablename = 'workshop_registrations') 
    LOOP
        EXECUTE 'DROP POLICY IF EXISTS "' || r.policyname || '" ON workshop_registrations';
    END LOOP;
END $$;

-- Create INSERT policy
CREATE POLICY "Allow public inserts" 
ON workshop_registrations
FOR INSERT
TO anon, authenticated
WITH CHECK (true);

-- Create SELECT policy  
CREATE POLICY "Restrict reads" 
ON workshop_registrations
FOR SELECT
TO authenticated
USING (true);
```

3. **Click "Run"**

4. **You should see:** "Success. No rows returned"

5. **Test your form** - it should work now!

## Alternative: Use Table Editor

If SQL Editor isn't working:

1. Go to **Table Editor** → `workshop_registrations`
2. Click the **"Policies"** or **"RLS"** tab
3. Click **"New Policy"**
4. Choose **"For full customization"**
5. Set:
   - **Policy name:** `Allow public inserts`
   - **Allowed operation:** `INSERT`
   - **Target roles:** `anon`, `authenticated`
   - **USING expression:** Leave empty
   - **WITH CHECK expression:** `true`
6. Click **"Review"** then **"Save policy"**

Repeat for SELECT policy:
- **Policy name:** `Restrict reads`
- **Allowed operation:** `SELECT`
- **Target roles:** `authenticated`
- **USING expression:** `true`
- **WITH CHECK expression:** Leave empty

## Still Not Working?

1. **Check if table exists:**
   - Table Editor → Should see `workshop_registrations` table

2. **Check RLS is enabled:**
   - Table Editor → `workshop_registrations` → Settings
   - "Enable Row Level Security" should be ON

3. **Verify your Supabase credentials:**
   - Check `js/config.js` has correct URL and anon key

4. **Clear browser cache:**
   - Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)

