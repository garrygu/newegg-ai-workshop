# Supabase Integration - Quick Start

## Overview

The registration form is now integrated with Supabase to save registration data. The system is designed to:

- ✅ Save registrations to Supabase database
- ✅ Support multiple workshop events (same or different levels)
- ✅ Allow students to register for multiple workshops
- ✅ Prevent duplicate registrations (one student = one record per event)
- ✅ Automatically handle waitlist when capacity is reached (12 students)

## Quick Setup (5 minutes)

### 1. Create Supabase Project
- Go to [supabase.com](https://supabase.com) and create a free account
- Create a new project
- Wait for project to initialize (~2 minutes)

### 2. Set Up Database
- In Supabase dashboard, go to **SQL Editor**
- Open `supabase-schema.sql` file
- Copy and paste the SQL into the editor
- Click **Run** to create tables and policies

### 3. Get Your Credentials
- Go to **Settings** → **API**
- Copy your **Project URL** and **anon public key**

### 4. Configure the Site
- Open `js/config.js`
- Replace `YOUR_SUPABASE_PROJECT_URL` with your project URL
- Replace `YOUR_SUPABASE_ANON_KEY` with your anon key
- Save the file

### 5. Test It!
- Open `register.html` in your browser
- Fill out and submit the form
- Check Supabase dashboard → **Table Editor** → `workshop_registrations` to see your data

## Database Schema

### `workshop_registrations` Table

| Column | Type | Description |
|--------|------|-------------|
| `id` | UUID | Primary key (auto-generated) |
| `student_name` | TEXT | Student's full name |
| `student_email` | TEXT | Student's email (used for duplicate check) |
| `student_grade` | TEXT | Grade level |
| `student_experience` | TEXT | Coding/AI experience level |
| `parent_name` | TEXT | Parent/guardian name |
| `parent_email` | TEXT | Parent/guardian email |
| `parent_phone` | TEXT | Parent/guardian phone |
| `workshop_level` | TEXT | Workshop level (e.g., "Explorer Level") |
| `workshop_event_id` | TEXT | Unique event identifier |
| `motivation` | TEXT | Why student is interested |
| `status` | TEXT | 'registered', 'waitlisted', 'confirmed', 'cancelled' |
| `created_at` | TIMESTAMP | Registration timestamp |
| `updated_at` | TIMESTAMP | Last update timestamp |

**Unique Constraint:** `(student_email, workshop_event_id)` - ensures one registration per student per event

## How It Works

1. **Form Submission**: When parent submits the form, data is collected
2. **Duplicate Check**: System checks if student is already registered for this event
3. **Capacity Check**: Counts current registrations for the event
4. **Status Assignment**: 
   - If under capacity (12): status = 'registered'
   - If at/over capacity: status = 'waitlisted'
5. **Save to Database**: Data is inserted into Supabase
6. **User Feedback**: Success message shows registration or waitlist status

## Managing Multiple Events

To add a new workshop event:

1. Update `js/config.js`:
   ```javascript
   currentEventId: 'youthai-explorer-2026-jan' // New event ID
   ```

2. Add event details to `WORKSHOP_EVENTS`:
   ```javascript
   'youthai-explorer-2026-jan': {
       name: 'YouthAI Explorer Level - January 2026',
       level: 'Explorer Level',
       maxCapacity: 12,
       startDate: '2026-01-15',
       endDate: '2026-02-12'
   }
   ```

3. The same student can register for multiple events - each will be a separate record

## Viewing Registrations

### In Supabase Dashboard:
1. Go to **Table Editor** → `workshop_registrations`
2. View all registrations with filters and sorting

### Query Examples:
```sql
-- All registrations for current event
SELECT * FROM workshop_registrations 
WHERE workshop_event_id = 'youthai-explorer-2025-nov';

-- Registered vs Waitlisted count
SELECT status, COUNT(*) 
FROM workshop_registrations 
WHERE workshop_event_id = 'youthai-explorer-2025-nov'
GROUP BY status;

-- All registrations for a specific student
SELECT * FROM workshop_registrations 
WHERE student_email = 'student@example.com';
```

## Security

- ✅ Row Level Security (RLS) enabled
- ✅ Public can INSERT (for registration form)
- ✅ Only authenticated users can SELECT (protects data)
- ✅ Unique constraint prevents duplicate registrations
- ✅ Anon key is safe for client-side use

## Troubleshooting

**"Supabase client not initialized"**
- Check that `js/config.js` has correct credentials
- Ensure Supabase JS library is loaded before other scripts

**"Already registered" error**
- This is expected - prevents duplicate registrations
- Check existing registrations in Supabase dashboard

**Data not saving**
- Check browser console for errors
- Verify RLS policies are set up correctly
- Ensure anon key has INSERT permission

## Next Steps

- Set up email notifications (Supabase Edge Functions)
- Create admin dashboard to view/manage registrations
- Add export functionality (CSV/Excel)
- Set up automated waitlist notifications

For detailed setup instructions, see `supabase-setup.md`.

