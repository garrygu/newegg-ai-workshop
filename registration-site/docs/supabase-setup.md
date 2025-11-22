# Supabase Setup Guide for Registration Site

## Database Schema

### Table: `workshop_registrations`

This table stores all workshop registrations. Each student can have multiple registrations (one per workshop/event), but only one registration per student per event.

```sql
CREATE TABLE workshop_registrations (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  
  -- Student Information
  student_name TEXT NOT NULL,
  student_email TEXT NOT NULL,
  student_grade TEXT NOT NULL,
  student_experience TEXT NOT NULL,
  
  -- Parent/Guardian Information
  parent_name TEXT NOT NULL,
  parent_email TEXT NOT NULL,
  parent_phone TEXT NOT NULL,
  
  -- Workshop Information
  workshop_level TEXT NOT NULL,
  workshop_event_id TEXT NOT NULL, -- Unique identifier for each workshop event
  motivation TEXT NOT NULL,
  
  -- Status
  status TEXT DEFAULT 'registered' CHECK (status IN ('registered', 'waitlisted', 'confirmed', 'cancelled')),
  
  -- Metadata
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  
  -- Constraints
  UNIQUE(student_email, workshop_event_id) -- One registration per student per event
);

-- Create index for faster queries
CREATE INDEX idx_workshop_event ON workshop_registrations(workshop_event_id);
CREATE INDEX idx_student_email ON workshop_registrations(student_email);
CREATE INDEX idx_status ON workshop_registrations(status);

-- Create updated_at trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_workshop_registrations_updated_at 
    BEFORE UPDATE ON workshop_registrations 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();
```

### Table: `workshop_events` (Optional - for managing events)

If you want to manage multiple workshop events:

```sql
CREATE TABLE workshop_events (
  id TEXT PRIMARY KEY, -- e.g., 'youthai-explorer-2025-nov'
  name TEXT NOT NULL, -- e.g., 'YouthAI Explorer Level - November 2025'
  workshop_level TEXT NOT NULL,
  max_capacity INTEGER NOT NULL DEFAULT 12,
  start_date DATE,
  end_date DATE,
  location TEXT,
  status TEXT DEFAULT 'open' CHECK (status IN ('open', 'full', 'closed', 'completed')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## Setup Instructions

### 1. Create Supabase Project

1. Go to [supabase.com](https://supabase.com)
2. Sign up or log in
3. Click "New Project"
4. Fill in project details:
   - Name: `newegg-ai-workshop` (or your preferred name)
   - Database Password: (save this securely)
   - Region: Choose closest to your users
5. Wait for project to be created

### 2. Create Database Tables

1. Go to your Supabase project dashboard
2. Click on "SQL Editor" in the left sidebar
3. Open the file `supabase-schema.sql` in this directory
4. Copy and paste the entire SQL content
5. Click "Run" to create the tables and set up RLS policies

### 3. Get API Keys

1. Go to "Settings" → "API" in your Supabase dashboard
2. Copy the following:
   - **Project URL** (e.g., `https://xxxxx.supabase.co`)
   - **anon/public key** (for client-side use)
   - **service_role key** (keep secret - for server-side only)

### 4. Set Up Row Level Security (RLS)

For the registration form, you'll want to allow inserts but restrict reads:

```sql
-- Enable RLS
ALTER TABLE workshop_registrations ENABLE ROW LEVEL SECURITY;

-- Allow anyone to insert (for registration form)
CREATE POLICY "Allow public inserts" ON workshop_registrations
  FOR INSERT
  TO anon, authenticated
  WITH CHECK (true);

-- Restrict reads (only authenticated users or via service role)
CREATE POLICY "Restrict reads" ON workshop_registrations
  FOR SELECT
  TO authenticated
  USING (true);
```

### 5. Configure Supabase Credentials

1. Open the file `js/config.js` in this directory
2. Replace the placeholder values:
   - `YOUR_SUPABASE_PROJECT_URL` → Your Supabase project URL
   - `YOUR_SUPABASE_ANON_KEY` → Your Supabase anon/public key
3. Update `currentEventId` if needed (currently set to `'youthai-explorer-2025-nov'`)

**Important:** 
- The `anonKey` is safe to use in client-side code (it's designed for public use)
- Never commit your `service_role` key to version control
- For production, consider using environment variables or a backend API

## Current Workshop Event ID

For the current YouthAI Explorer Level workshop (November 2025), use:
- Event ID: `youthai-explorer-2025-nov`

You can change this in the form submission code.

## Testing

After setup, test the registration form to ensure data is being saved correctly. Check the Supabase dashboard → Table Editor → `workshop_registrations` to see submitted registrations.

