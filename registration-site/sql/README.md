# SQL Files

## Main Schema

- **`supabase-schema.sql`** - Complete database schema for Supabase, including:
  - Table creation (`workshop_registrations`)
  - Row Level Security (RLS) policies
  - Indexes for performance
  - Comments and documentation

## Archive

The `archive/` folder contains troubleshooting SQL files that were used during development to fix RLS policy issues. These are kept for reference but are not needed for normal operation.

If you encounter RLS policy issues, refer to the main `supabase-schema.sql` file first, as it contains the correct, final policies.




