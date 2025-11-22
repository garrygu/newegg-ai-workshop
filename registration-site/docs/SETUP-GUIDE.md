# Database Setup Guide - Connect to Real Database

Follow these steps to connect your registration site to a real database.

## Option 1: Supabase (Recommended - Easiest)

### Step 1: Create Supabase Project

1. Go to [supabase.com](https://supabase.com)
2. Sign up or log in (free account works)
3. Click **"New Project"**
4. Fill in:
   - **Name**: `newegg-ai-workshop` (or your choice)
   - **Database Password**: Create a strong password (save it!)
   - **Region**: Choose closest to your users
5. Click **"Create new project"**
6. Wait 2-3 minutes for project to initialize

### Step 2: Set Up Database Tables

1. In Supabase dashboard, click **"SQL Editor"** (left sidebar)
2. Open the file `supabase-schema.sql` in this directory
3. Copy the **entire contents** of the file
4. Paste into the SQL Editor
5. Click **"Run"** (or press Cmd/Ctrl + Enter)
6. You should see "Success. No rows returned"

### Step 3: Get Your API Credentials

1. In Supabase dashboard, go to **"Settings"** → **"API"**
2. You'll see:
   - **Project URL**: `https://xxxxx.supabase.co`
   - **anon public key**: Long string starting with `eyJ...`

### Step 4: Configure Your Site

1. Open `js/config.js` in your project
2. Replace the placeholder values:

```javascript
const DB_CONFIG = {
    type: 'supabase',
    
    supabase: {
        url: 'https://YOUR_PROJECT_ID.supabase.co',  // ← Your Project URL
        anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'  // ← Your anon key
    },
    
    currentEventId: 'youthai-explorer-2025-nov'
};
```

3. Save the file

### Step 5: Test the Connection

1. Open `register.html` in your browser
2. Fill out the registration form
3. Submit it
4. Check Supabase dashboard → **"Table Editor"** → `workshop_registrations`
5. You should see your test registration!

## Option 2: MySQL (Requires Backend API)

### Step 1: Set Up MySQL Database

1. Create a MySQL database (local or cloud)
2. Run the SQL schema (convert from PostgreSQL to MySQL)
3. Note your connection details:
   - Host
   - Database name
   - Username
   - Password

### Step 2: Create Backend API

You'll need to create a REST API that connects to MySQL. See `DATABASE-SWITCHING.md` for API endpoint requirements.

### Step 3: Configure

1. Update `js/config.js`:
```javascript
const DB_CONFIG = {
    type: 'mysql',
    mysql: {
        apiUrl: 'https://your-api.com/api'  // Your backend API URL
    }
};
```

2. Load MySQL adapter in `register.html`:
```html
<script src="js/adapters/mysql-adapter.js"></script>
```

## Option 3: MSSQL (Requires Backend API)

Similar to MySQL - requires a backend API. See `DATABASE-SWITCHING.md` for details.

## Quick Checklist for Supabase

- [ ] Created Supabase account
- [ ] Created new project
- [ ] Ran SQL schema in SQL Editor
- [ ] Got Project URL and anon key
- [ ] Updated `js/config.js` with credentials
- [ ] Tested registration form
- [ ] Verified data appears in Supabase Table Editor

## Troubleshooting

### "Supabase client not initialized"
- Check that `js/config.js` has correct URL and anon key
- Make sure Supabase JS library is loaded before other scripts
- Check browser console for specific errors

### "Failed to insert"
- Check Row Level Security (RLS) policies are set up
- Verify the SQL schema ran successfully
- Check browser console for error details

### "Already registered" error
- This is expected if student email already exists for the event
- Check Supabase Table Editor to see existing registrations

## Security Notes

✅ **Safe to use**: The `anon` key in JavaScript is safe for client-side use
✅ **Protected**: RLS policies prevent public users from reading data
✅ **Secure**: Only you (via Supabase login) can view registrations

## Next Steps After Setup

1. Test registration form thoroughly
2. Set up email notifications (optional - Supabase Edge Functions)
3. Create admin dashboard to view registrations
4. Set up automated waitlist notifications

## Need Help?

- Supabase Docs: [supabase.com/docs](https://supabase.com/docs)
- SQL Schema: See `supabase-schema.sql`
- Security: See `SECURITY.md`

