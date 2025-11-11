# Registration Site Setup Guide

Complete guide for setting up and deploying the Newegg AI Workshop registration site.

## Quick Start

1. **Configure Database** - See [Database Setup](#database-setup) below
2. **Update Configuration** - Edit `js/config.js` with your database credentials
3. **Deploy** - Copy files to your web server or use GitHub Pages

## Database Setup

### Option 1: Supabase (Recommended)

Supabase is the easiest option with a free tier and built-in security.

#### Step 1: Create Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign up (free account works)
2. Click **"New Project"**
3. Fill in:
   - **Name**: `newegg-ai-workshop` (or your choice)
   - **Database Password**: Create a strong password (save it!)
   - **Region**: Choose closest to your users
4. Click **"Create new project"** and wait 2-3 minutes

#### Step 2: Set Up Database Schema

1. In Supabase dashboard, click **"SQL Editor"** (left sidebar)
2. Open `sql/supabase-schema.sql` in this project
3. Copy the **entire contents** and paste into SQL Editor
4. Click **"Run"** (or press Cmd/Ctrl + Enter)
5. You should see "Success. No rows returned"

#### Step 3: Get API Credentials

1. In Supabase dashboard, go to **"Settings"** → **"API"**
2. Copy:
   - **Project URL** (looks like: `https://xxxxx.supabase.co`)
   - **anon public** key (long string starting with `eyJ...`)

#### Step 4: Configure the Site

1. Open `js/config.js`
2. Update the `DB_CONFIG` object:
   ```javascript
   const DB_CONFIG = {
       type: 'supabase',
       supabase: {
           url: 'YOUR_PROJECT_URL_HERE',
           anonKey: 'YOUR_ANON_KEY_HERE'
       },
       // ...
   };
   ```

#### Step 5: Test

1. Open `register.html` in your browser
2. Fill out the registration form
3. Submit and check Supabase dashboard → **Table Editor** → `workshop_registrations`
4. You should see your test registration!

### Option 2: MySQL or MSSQL

The site supports MySQL and MSSQL through the adapter pattern. See `docs/DATABASE-SWITCHING.md` for details.

## Security

**Important**: Read `docs/SECURITY.md` for security best practices, especially regarding:
- Row Level Security (RLS) policies
- API key protection
- Database access controls

## Deployment

### Option 1: Static Web Hosting

1. Copy the entire `registration-site/` folder to your web server
2. Ensure all relative paths work correctly
3. Configure your web server to serve the files
4. Test the registration form

### Option 2: GitHub Pages

1. Push the repository to GitHub
2. Go to repository **Settings** → **Pages**
3. Set source to `/registration-site` folder
4. Site will be available at `https://username.github.io/newegg-ai-workshop/registration-site/`

## Troubleshooting

### Registration Not Saving

1. Check browser console for errors
2. Verify database credentials in `js/config.js`
3. Check Supabase dashboard → **Logs** for API errors
4. Verify RLS policies are set up correctly (see `sql/supabase-schema.sql`)

### RLS Policy Issues

If you see "row-level security policy" errors:
1. Check `sql/supabase-schema.sql` for the correct RLS policies
2. Verify policies are enabled in Supabase dashboard → **Authentication** → **Policies**
3. See archived troubleshooting files in `sql/archive/` if needed

## File Structure

```
registration-site/
├── index.html              # Landing page
├── about.html              # About page
├── register.html           # Registration form
├── confirmation.html       # Confirmation page
├── terms.html              # Terms & conditions
├── admin-view.html         # Admin view (requires auth setup)
├── css/                    # Stylesheets
├── js/                     # JavaScript files
│   ├── config.js          # Database configuration
│   ├── adapters/          # Database adapters
│   └── ...
├── assets/                 # Images, icons
├── sql/                    # SQL schemas
│   ├── supabase-schema.sql # Main database schema
│   └── archive/           # Troubleshooting SQL files
└── docs/                   # Documentation
    ├── SETUP.md              # This file
    ├── SECURITY.md           # Security guide
    └── DATABASE-SWITCHING.md # Database adapter guide
```

## Support

For issues or questions:
- Check `docs/SECURITY.md` for security-related questions
- Check `docs/DATABASE-SWITCHING.md` for database adapter questions
- Review browser console and Supabase logs for errors

