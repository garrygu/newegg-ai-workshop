# Security: Attack Prevention Guide

This guide covers protections against malicious attacks, including script-based spam and injection attacks.

## 🛡️ Current Protections

### 1. Client-Side Rate Limiting ✅

**Location**: `js/rate-limiter.js`

**Protection**:
- Maximum 5 registration attempts per 15-minute window
- 1-hour lockout after exceeding limit
- Uses browser localStorage (per-browser protection)
- Automatic cleanup of old attempts

**Limitations**:
- Can be bypassed by clearing browser data
- Different browsers = different limits
- **Not sufficient alone** - must be combined with server-side protection

### 2. Input Validation ✅

**Location**: `js/form-validation.js`

**Protections**:
- Email format validation
- Phone number format validation
- Name format validation (letters only, min length)
- Grade validation
- Real-time validation feedback

### 3. Database Constraints ✅

**Location**: `sql/supabase-schema.sql`

**Protections**:
- Unique constraint on `(student_email, workshop_event_id)` - prevents duplicate registrations
- NOT NULL constraints on required fields
- CHECK constraints on status values
- Email format validation at database level

### 4. Row Level Security (RLS) ✅

**Location**: `sql/supabase-schema.sql`

**Protections**:
- Public can only INSERT (not SELECT/UPDATE/DELETE)
- Prevents reading other users' data
- Limits what data can be inserted

## ⚠️ Additional Protections Needed

### 1. Server-Side Rate Limiting (CRITICAL)

**Current Status**: ❌ Not implemented

**Why Needed**: Client-side rate limiting can be easily bypassed by:
- Clearing browser data
- Using different browsers
- Using scripts that don't respect localStorage
- Using multiple IP addresses

**Recommended Solutions**:

#### Option A: Supabase Edge Functions (Recommended)

Create a Supabase Edge Function that acts as a proxy:

```typescript
// supabase/functions/register/index.ts
import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const RATE_LIMIT_WINDOW = 15 * 60 * 1000 // 15 minutes
const MAX_ATTEMPTS = 5

serve(async (req) => {
  // Get client IP
  const clientIP = req.headers.get('x-forwarded-for') || req.headers.get('x-real-ip') || 'unknown'
  
  // Check rate limit (store in Redis or Supabase)
  const attempts = await checkRateLimit(clientIP)
  
  if (attempts >= MAX_ATTEMPTS) {
    return new Response(
      JSON.stringify({ error: 'Too many attempts. Please try again later.' }),
      { status: 429, headers: { 'Content-Type': 'application/json' } }
    )
  }
  
  // Increment rate limit counter
  await incrementRateLimit(clientIP)
  
  // Process registration...
})
```

#### Option B: Backend API with Rate Limiting

Use a backend service (Node.js, Python, etc.) with rate limiting middleware:

```javascript
// Using express-rate-limit
const rateLimit = require('express-rate-limit');

const registrationLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 requests per window
  message: 'Too many registration attempts, please try again later.',
  standardHeaders: true,
  legacyHeaders: false,
});

app.post('/api/register', registrationLimiter, async (req, res) => {
  // Handle registration
});
```

### 2. CAPTCHA Protection (HIGHLY RECOMMENDED)

**Current Status**: ❌ Not implemented

**Why Needed**: Prevents automated bot attacks

**Recommended**: Google reCAPTCHA v3 (invisible, better UX)

#### Implementation Steps:

1. **Get reCAPTCHA Keys**:
   - Go to [Google reCAPTCHA Admin](https://www.google.com/recaptcha/admin)
   - Register your site
   - Get Site Key and Secret Key

2. **Add to HTML** (`register.html`):

```html
<!-- Add before closing </head> -->
<script src="https://www.google.com/recaptcha/api.js?render=YOUR_SITE_KEY"></script>

<!-- Add to form -->
<div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY" data-size="invisible"></div>
```

3. **Verify in JavaScript** (`js/forms.js`):

```javascript
// Before form submission
const recaptchaToken = await grecaptcha.execute('YOUR_SITE_KEY', {action: 'register'});

// Send token to server for verification
const verifyResponse = await fetch('/api/verify-recaptcha', {
  method: 'POST',
  body: JSON.stringify({ token: recaptchaToken })
});

if (!verifyResponse.ok) {
  alert('CAPTCHA verification failed. Please try again.');
  return;
}
```

4. **Server-Side Verification**:

```javascript
// Verify token with Google
const verifyURL = `https://www.google.com/recaptcha/api/siteverify?secret=${SECRET_KEY}&response=${token}`;
const response = await fetch(verifyURL);
const data = await response.json();

if (!data.success || data.score < 0.5) {
  // Block registration
  return res.status(400).json({ error: 'CAPTCHA verification failed' });
}
```

### 3. IP-Based Throttling

**Current Status**: ❌ Not implemented

**Implementation**: Use Supabase Edge Functions or backend API to track IP addresses:

```typescript
// Track IP-based attempts
const ipAttempts = await getIPAttempts(clientIP);
if (ipAttempts >= MAX_ATTEMPTS_PER_IP) {
  return new Response(
    JSON.stringify({ error: 'Too many attempts from this IP address' }),
    { status: 429 }
  );
}
```

### 4. Honeypot Fields

**Current Status**: ❌ Not implemented

**Simple but effective**: Add hidden fields that bots will fill but humans won't:

```html
<!-- Add to form (hidden with CSS) -->
<input type="text" name="website" style="position: absolute; left: -9999px;" tabindex="-1" autocomplete="off">

<!-- In JavaScript -->
if (formData.get('website')) {
  // Bot detected - silently reject
  return;
}
```

### 5. Request Fingerprinting

**Current Status**: ❌ Not implemented

Track additional signals:
- Browser fingerprint
- Time between form load and submission (bots submit too fast)
- Mouse movement patterns
- Typing patterns

### 6. Email Verification

**Current Status**: ⚠️ Partial (recommended but not enforced)

**Recommendation**: Send verification email before accepting registration:

```javascript
// After form submission
1. Generate verification token
2. Send email with verification link
3. Only mark as registered after email verification
4. Expire unverified registrations after 24 hours
```

### 7. Monitoring & Alerting

**Current Status**: ❌ Not implemented

**Recommendation**: Set up alerts for:
- Unusual spike in registrations
- Multiple registrations from same IP
- Failed validation attempts
- Rate limit violations

**Supabase Dashboard**:
- Go to **Logs** → **API Logs**
- Set up alerts for error rates > threshold

## 🚨 Immediate Actions Required

### High Priority (Do First)

1. ✅ **Client-side rate limiting** - Already implemented
2. ⚠️ **Add CAPTCHA** - Implement Google reCAPTCHA v3
3. ⚠️ **Server-side rate limiting** - Implement via Supabase Edge Function or backend API

### Medium Priority

4. ⚠️ **IP-based throttling** - Track and limit by IP address
5. ⚠️ **Email verification** - Require email verification before acceptance
6. ⚠️ **Honeypot fields** - Add hidden fields to catch bots

### Low Priority (Nice to Have)

7. ⚠️ **Request fingerprinting** - Advanced bot detection
8. ⚠️ **Monitoring & alerting** - Set up dashboards and alerts

## 📊 Testing Your Protections

### Test Rate Limiting

```javascript
// In browser console
for (let i = 0; i < 10; i++) {
  // Try to submit form 10 times quickly
  document.getElementById('registrationForm').dispatchEvent(new Event('submit'));
}
// Should block after 5 attempts
```

### Test CAPTCHA

1. Use automated tools to submit forms
2. Verify CAPTCHA blocks automated submissions
3. Verify legitimate users can still register

### Test Database Constraints

```sql
-- Try to insert duplicate
INSERT INTO workshop_registrations (student_email, workshop_event_id, ...)
VALUES ('test@example.com', 'event-id', ...);

-- Try again with same email/event
-- Should fail with unique constraint violation
```

## 🔍 Monitoring Checklist

- [ ] Set up Supabase dashboard alerts
- [ ] Monitor registration rate (should be steady, not spikes)
- [ ] Check for patterns (same IP, same email domain, etc.)
- [ ] Review failed validation attempts
- [ ] Monitor rate limit violations
- [ ] Track CAPTCHA scores (low scores = bots)

## 📚 Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Supabase Security Best Practices](https://supabase.com/docs/guides/platform/security)
- [Google reCAPTCHA Documentation](https://developers.google.com/recaptcha)
- [Rate Limiting Strategies](https://cloud.google.com/architecture/rate-limiting-strategies-techniques)

## ⚡ Quick Implementation Guide

See `docs/SETUP.md` for step-by-step implementation of:
- CAPTCHA integration
- Server-side rate limiting
- Email verification




