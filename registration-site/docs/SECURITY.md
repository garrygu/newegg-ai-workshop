# Security Guide

## 🛡️ Attack Prevention

**Important**: See **[SECURITY-ATTACK-PREVENTION.md](SECURITY-ATTACK-PREVENTION.md)** for comprehensive protection against:
- Script-based spam attacks
- Rate limiting (client & server-side)
- CAPTCHA integration
- IP-based throttling
- Bot detection strategies

---

# Database Access & Security Guide

## 🔒 Is Using JavaScript Secure?

**Short answer: Yes, when properly configured with Row Level Security (RLS).**

### Current Security Setup

✅ **Safe for INSERT (Registration Form)**
- The `anon` key in JavaScript is **safe** for inserting data
- RLS policies control what can be inserted
- Public can only INSERT new registrations (not read existing ones)

❌ **Protected for SELECT (Reading Data)**
- Current RLS policy: Only authenticated users can read
- Public users (using anon key) **cannot** read registration data
- This protects student/parent personal information

## 📊 How to Access the Database

### Option 1: Supabase Dashboard (Recommended for Admins)

**Best for:** Viewing, managing, and exporting registrations

1. Log into [supabase.com](https://supabase.com)
2. Select your project
3. Go to **Table Editor** → `workshop_registrations`
4. View, filter, sort, and export data
5. **Secure:** Requires Supabase account login

**Features:**
- View all registrations
- Filter by event, status, date
- Export to CSV
- Edit records (if needed)
- See real-time updates

### Option 2: SQL Editor (For Queries)

**Best for:** Custom queries and reports

1. In Supabase dashboard → **SQL Editor**
2. Write SQL queries:

```sql
-- View all registrations for current event
SELECT * FROM workshop_registrations 
WHERE workshop_event_id = 'youthai-explorer-2025-nov'
ORDER BY created_at DESC;

-- Count registrations by status
SELECT status, COUNT(*) as count
FROM workshop_registrations
WHERE workshop_event_id = 'youthai-explorer-2025-nov'
GROUP BY status;

-- View waitlisted students
SELECT student_name, student_email, parent_email, created_at
FROM workshop_registrations
WHERE workshop_event_id = 'youthai-explorer-2025-nov'
  AND status = 'waitlisted'
ORDER BY created_at;
```

### Option 3: Service Role Key (Server-Side Only)

**Best for:** Backend applications, admin tools

⚠️ **NEVER expose this in client-side JavaScript!**

```javascript
// Server-side only (Node.js, Python, etc.)
const { createClient } = require('@supabase/supabase-js');

const supabaseAdmin = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY // Secret key
);

// Can read/write everything (bypasses RLS)
const { data } = await supabaseAdmin
  .from('workshop_registrations')
  .select('*');
```

### Option 4: Authenticated User Access (Future)

**Best for:** Allowing specific users to view data

You could create an admin authentication system:

```sql
-- Allow authenticated admins to read
CREATE POLICY "Admins can read" ON workshop_registrations
  FOR SELECT
  TO authenticated
  USING (
    EXISTS (
      SELECT 1 FROM admin_users 
      WHERE admin_users.user_id = auth.uid()
    )
  );
```

## 🔐 Security Model Explained

### Row Level Security (RLS) Policies

Our current setup:

```sql
-- ✅ Public can INSERT (for registration form)
CREATE POLICY "Allow public inserts" ON workshop_registrations
  FOR INSERT TO anon, authenticated
  WITH CHECK (true);

-- 🔒 Only authenticated users can SELECT (read)
CREATE POLICY "Restrict reads" ON workshop_registrations
  FOR SELECT TO authenticated
  USING (true);
```

**What this means:**
- ✅ Anyone can submit registrations (INSERT)
- ❌ Only logged-in users can view registrations (SELECT)
- ✅ Data is protected from public access
- ✅ Anon key is safe to use in JavaScript

### Why Anon Key is Safe

1. **Limited Permissions**: Anon key only allows what RLS policies permit
2. **No Read Access**: Current policy blocks SELECT for anonymous users
3. **Insert Only**: Can only create new records, not read existing ones
4. **Standard Practice**: This is how Supabase is designed to work

## 🛡️ Additional Security Recommendations

### 1. Rate Limiting (Prevent Spam)

Add to your Supabase project:
- Go to **Settings** → **API** → **Rate Limiting**
- Set limits on INSERT operations

### 2. Input Validation

✅ Already implemented in `forms.js`:
- Email validation
- Phone validation
- Required field checks
- Duplicate prevention

### 3. Environment Variables (Production)

For production, consider:

```javascript
// Use environment variables instead of hardcoding
const SUPABASE_CONFIG = {
  url: process.env.SUPABASE_URL || window.SUPABASE_URL,
  anonKey: process.env.SUPABASE_ANON_KEY || window.SUPABASE_ANON_KEY
};
```

### 4. HTTPS Only

- Always serve your site over HTTPS
- Supabase requires HTTPS for production

## 📋 Accessing Data - Quick Reference

| Method | Access Level | Use Case |
|--------|-------------|----------|
| **Supabase Dashboard** | Full (with login) | Admin viewing/managing |
| **SQL Editor** | Full (with login) | Custom queries/reports |
| **Service Role Key** | Full (server-side) | Backend applications |
| **Anon Key (JS)** | INSERT only | Registration form |
| **Authenticated Users** | SELECT (if policy allows) | Admin dashboard |

## 🚨 What NOT to Do

❌ **Don't expose service_role key in JavaScript**
- This bypasses all security
- Anyone could read/write all data

❌ **Don't disable RLS**
- This removes all security
- Makes data publicly accessible

❌ **Don't allow public SELECT**
- Would expose student/parent personal information
- Violates privacy regulations

## ✅ Current Setup is Secure

Your current configuration:
- ✅ RLS enabled
- ✅ Public can INSERT (needed for registration)
- ✅ Public cannot SELECT (protects data)
- ✅ Anon key safe for client-side use
- ✅ Unique constraints prevent duplicates

## 🔄 If You Need to Read Data from JavaScript

If you need to build an admin dashboard accessible via JavaScript:

1. **Create authentication system** (Supabase Auth)
2. **Create admin role table**
3. **Update RLS policy** to allow authenticated admins to read
4. **Use authenticated Supabase client** in your admin dashboard

Example admin policy:
```sql
CREATE POLICY "Admins can read all" ON workshop_registrations
  FOR SELECT
  TO authenticated
  USING (
    auth.jwt() ->> 'role' = 'admin'
  );
```

## 📞 Need Help?

- Supabase Docs: [supabase.com/docs/guides/auth/row-level-security](https://supabase.com/docs/guides/auth/row-level-security)
- Security Best Practices: [supabase.com/docs/guides/database/postgres/security](https://supabase.com/docs/guides/database/postgres/security)

