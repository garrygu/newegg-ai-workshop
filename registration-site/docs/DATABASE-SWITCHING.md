# Switching Database Backends

This registration site uses a flexible database adapter pattern, making it easy to switch between different database systems.

## Current Setup: Supabase (PostgreSQL)

The site is currently configured to use Supabase. To switch to MySQL or MSSQL, follow the steps below.

## How to Switch Databases

### Step 1: Update Configuration

Edit `js/config.js` and change the `type`:

```javascript
const DB_CONFIG = {
    type: 'mysql',  // Change from 'supabase' to 'mysql' or 'mssql'
    // ... rest of config
};
```

### Step 2: Load Appropriate Adapter

In `register.html`, uncomment the adapter you need:

**For MySQL:**
```html
<script src="js/adapters/mysql-adapter.js"></script>
```

**For MSSQL:**
```html
<script src="js/adapters/mssql-adapter.js"></script>
```

### Step 3: Configure Database Connection

**For MySQL/MSSQL:** You'll need a backend API. Update the config:

```javascript
mysql: {
    apiUrl: 'https://your-api.com/api'  // Your backend endpoint
}
```

## Database Adapter Architecture

```
forms.js (Form Submission)
    ↓
db-factory.js (Creates adapter)
    ↓
DatabaseAdapter (Interface)
    ↓
├── SupabaseAdapter (Direct connection)
├── MySQLAdapter (Via REST API)
└── MSSQLAdapter (Via REST API)
```

## Backend API Requirements (for MySQL/MSSQL)

If switching to MySQL or MSSQL, you'll need to create a backend API with these endpoints:

### 1. Check Existing Registration
```
POST /api/registrations/check
Body: { studentEmail, eventId }
Response: { registration: {...} | null }
```

### 2. Get Registration Count
```
GET /api/registrations/count?eventId=xxx
Response: { count: 12 }
```

### 3. Insert Registration
```
POST /api/registrations
Body: { student_name, student_email, ... }
Response: { registration: {...} }
Error 409: Duplicate registration
```

### 4. Get All Registrations (Admin)
```
GET /api/registrations?eventId=xxx
Response: { registrations: [...] }
```

## Example Backend Implementation

### Node.js/Express Example (MySQL)

```javascript
const express = require('express');
const mysql = require('mysql2/promise');

const app = express();
app.use(express.json());

const pool = mysql.createPool({
    host: 'your-mysql-host',
    user: 'your-user',
    password: 'your-password',
    database: 'workshop_db'
});

// Check existing registration
app.post('/api/registrations/check', async (req, res) => {
    const { studentEmail, eventId } = req.body;
    const [rows] = await pool.execute(
        'SELECT id, status FROM workshop_registrations WHERE student_email = ? AND workshop_event_id = ?',
        [studentEmail, eventId]
    );
    res.json({ registration: rows[0] || null });
});

// Get count
app.get('/api/registrations/count', async (req, res) => {
    const { eventId } = req.query;
    const [rows] = await pool.execute(
        'SELECT COUNT(*) as count FROM workshop_registrations WHERE workshop_event_id = ? AND status = "registered"',
        [eventId]
    );
    res.json({ count: rows[0].count });
});

// Insert registration
app.post('/api/registrations', async (req, res) => {
    try {
        const [result] = await pool.execute(
            'INSERT INTO workshop_registrations (student_name, student_email, ...) VALUES (?, ?, ...)',
            [req.body.student_name, req.body.student_email, ...]
        );
        res.json({ registration: { id: result.insertId, ...req.body } });
    } catch (error) {
        if (error.code === 'ER_DUP_ENTRY') {
            res.status(409).json({ code: 'DUPLICATE', message: 'Already registered' });
        } else {
            res.status(500).json({ error: error.message });
        }
    }
});
```

## Database Schema Compatibility

All adapters expect the same data structure. Your MySQL/MSSQL tables should match:

```sql
-- MySQL/MSSQL equivalent
CREATE TABLE workshop_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- or IDENTITY for MSSQL
    student_name VARCHAR(255) NOT NULL,
    student_email VARCHAR(255) NOT NULL,
    student_grade VARCHAR(50) NOT NULL,
    student_experience VARCHAR(50) NOT NULL,
    parent_name VARCHAR(255) NOT NULL,
    parent_email VARCHAR(255) NOT NULL,
    parent_phone VARCHAR(50) NOT NULL,
    workshop_level VARCHAR(100) NOT NULL,
    workshop_event_id VARCHAR(100) NOT NULL,
    motivation TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'registered',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_registration (student_email, workshop_event_id)
);
```

## Benefits of This Architecture

✅ **No Code Changes**: Switch databases by changing config only
✅ **Easy Testing**: Test with Supabase, deploy with MySQL
✅ **Future-Proof**: Add new database types easily
✅ **Separation of Concerns**: Database logic isolated from form logic

## Migration Checklist

When switching databases:

- [ ] Update `DB_CONFIG.type` in `js/config.js`
- [ ] Load appropriate adapter script in HTML
- [ ] Configure database connection (Supabase) or API URL (MySQL/MSSQL)
- [ ] Create database tables with matching schema
- [ ] Set up backend API (if using MySQL/MSSQL)
- [ ] Test registration form submission
- [ ] Test duplicate prevention
- [ ] Test capacity/waitlist logic
- [ ] Verify data is being saved correctly

## Current Status

- ✅ Supabase adapter: Fully implemented and working
- ⚠️ MySQL adapter: Requires backend API setup
- ⚠️ MSSQL adapter: Requires backend API setup

The form submission code (`forms.js`) doesn't need any changes when switching databases!

