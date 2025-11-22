# Production Deployment Guide

Complete guide for deploying the registration site to production.

## 🪟 Windows Server / IIS Deployment

**For IIS deployment on Windows Server**, see the detailed guide: **[DEPLOYMENT-IIS.md](DEPLOYMENT-IIS.md)**

This includes:
- IIS installation and configuration
- Website setup
- File permissions
- SSL/HTTPS configuration
- PowerShell commands
- Troubleshooting

---

## 🎯 Deployment Options

### Option 1: Direct Deployment (Simple)

**Best for**: Quick deployment, small sites

Deploy the entire `registration-site/` folder directly to your web server.

**Pros**:
- Simple and fast
- No build step needed
- All files available

**Cons**:
- Includes documentation and development files
- Larger file size
- Less clean structure

### Option 2: Production Build Folder (Recommended)

**Best for**: Production deployments, clean structure

Use the `dist/` folder created by the deployment script.

**Pros**:
- Clean, production-only files
- Smaller deployment size
- Clear separation of dev/prod
- Professional structure

**Cons**:
- Requires running build script
- Need to maintain build process

## 🚀 Quick Start: Production Build

### Step 1: Run Deployment Script

```bash
cd registration-site
./deploy.sh
```

This creates a `dist/` folder with only production files.

### Step 2: Review Configuration

Before deploying, update `dist/js/config.js` with production credentials:

```javascript
const DB_CONFIG = {
    type: 'supabase',
    supabase: {
        url: 'YOUR_PRODUCTION_SUPABASE_URL',
        anonKey: 'YOUR_PRODUCTION_ANON_KEY'
    },
    currentEventId: 'youthai-explorer-2025-nov'
};
```

### Step 3: Deploy to Web Server

Upload all files from `dist/` folder to your web server.

## 📦 What Gets Deployed

### Included in `dist/`:
- ✅ All HTML files (index.html, register.html, etc.)
- ✅ CSS stylesheets
- ✅ JavaScript files (including adapters)
- ✅ Assets (images, icons)
- ✅ Database schema (sql/supabase-schema.sql) - for reference

### Excluded from `dist/`:
- ❌ Documentation files (docs/)
- ❌ Archived SQL files (sql/archive/)
- ❌ Development scripts
- ❌ README files (except minimal production README)

## 🌐 Deployment Methods

### Method 1: FTP/SFTP Upload

1. Connect to your web server via FTP/SFTP
2. Navigate to your web root directory (e.g., `public_html/`, `www/`, `htdocs/`)
3. Upload all files from `dist/` folder
4. Maintain folder structure (css/, js/, assets/, etc.)

### Method 2: Git Deployment

If your server supports Git:

```bash
# On your server
cd /var/www/html
git clone https://github.com/your-username/newegg-ai-workshop.git
cd newegg-ai-workshop/registration-site
./deploy.sh
# Copy dist/ contents to web root
cp -r dist/* /var/www/html/
```

### Method 3: GitHub Pages

1. Push repository to GitHub
2. Go to repository **Settings** → **Pages**
3. Set source to `/registration-site/dist` folder
4. Site will be available at `https://username.github.io/newegg-ai-workshop/`

**Note**: For GitHub Pages, you may need to adjust paths if using a subdirectory.

### Method 4: Cloud Hosting (AWS S3, Netlify, Vercel)

#### AWS S3 + CloudFront

```bash
# Install AWS CLI if needed
aws s3 sync dist/ s3://your-bucket-name/ --delete
aws cloudfront create-invalidation --distribution-id YOUR_DIST_ID --paths "/*"
```

#### Netlify

1. Connect your GitHub repository
2. Set build command: `cd registration-site && ./deploy.sh`
3. Set publish directory: `registration-site/dist`
4. Deploy!

#### Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Run: `cd registration-site && vercel`
3. Follow prompts

## ✅ Pre-Deployment Checklist

- [ ] Run `./deploy.sh` to create production build
- [ ] Update `dist/js/config.js` with production database credentials
- [ ] Test registration form locally (open `dist/index.html` in browser)
- [ ] Verify all assets load correctly
- [ ] Check browser console for errors
- [ ] Test on mobile devices
- [ ] Verify database connection works
- [ ] Test form submission end-to-end
- [ ] Check rate limiting works
- [ ] Verify CAPTCHA (if implemented)
- [ ] Test registration deadline functionality

## 🔒 Security Checklist

Before going live:

- [ ] Update database credentials in `js/config.js`
- [ ] Verify RLS policies are set up correctly
- [ ] Test rate limiting protection
- [ ] Implement CAPTCHA (see `docs/SECURITY-ATTACK-PREVENTION.md`)
- [ ] Set up server-side rate limiting
- [ ] Enable HTTPS/SSL certificate
- [ ] Review and test input validation
- [ ] Set up monitoring and alerts

## 🧪 Testing After Deployment

1. **Functional Testing**:
   - Submit a test registration
   - Verify data appears in database
   - Test form validation
   - Test rate limiting

2. **Performance Testing**:
   - Check page load times
   - Test on slow connections
   - Verify assets load correctly

3. **Cross-Browser Testing**:
   - Chrome
   - Firefox
   - Safari
   - Edge
   - Mobile browsers

4. **Security Testing**:
   - Try to submit invalid data
   - Test rate limiting (try 10+ submissions)
   - Verify CAPTCHA works (if implemented)

## 📊 Post-Deployment Monitoring

### Monitor These Metrics:

1. **Registration Rate**:
   - Normal: Steady, organic growth
   - Alert: Sudden spikes (possible attack)

2. **Error Rate**:
   - Check browser console errors
   - Monitor database connection errors
   - Track validation failures

3. **Rate Limit Violations**:
   - Monitor how often rate limits are hit
   - Adjust limits if needed

4. **Database Health**:
   - Monitor Supabase dashboard
   - Check for unusual patterns
   - Review failed insertions

## 🔄 Updating Production

When you need to update the site:

1. Make changes in development
2. Test locally
3. Run `./deploy.sh` to rebuild
4. Upload new `dist/` files to server
5. Clear browser cache if needed
6. Test on production

## 🆘 Troubleshooting

### Issue: Forms not submitting

**Check**:
- Browser console for errors
- Database credentials in `js/config.js`
- Network tab for failed requests
- Supabase dashboard for API errors

### Issue: Assets not loading

**Check**:
- File paths are correct (relative paths)
- Files uploaded to correct directories
- Web server configuration allows file access
- Case sensitivity (Linux servers are case-sensitive)

### Issue: Database connection fails

**Check**:
- Supabase URL and anon key are correct
- RLS policies are set up
- Network connectivity
- Supabase project is active

### Issue: Rate limiting not working

**Check**:
- `js/rate-limiter.js` is loaded
- Browser localStorage is enabled
- No JavaScript errors in console

## 📚 Additional Resources

- [Setup Guide](SETUP.md) - Initial setup instructions
- [Security Guide](SECURITY.md) - Security best practices
- [Attack Prevention](SECURITY-ATTACK-PREVENTION.md) - Protection against attacks

## 💡 Tips

1. **Keep a backup**: Always backup your production `dist/` folder before updates
2. **Version control**: Tag releases in Git for easy rollback
3. **Staging environment**: Test on staging before production
4. **Monitor logs**: Set up logging and monitoring
5. **Document changes**: Keep a changelog of deployments

