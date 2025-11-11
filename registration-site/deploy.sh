#!/bin/bash
# Deployment script for Newegg AI Workshop Registration Site
# Creates a production-ready dist/ folder with only necessary files

set -e  # Exit on error

echo "🚀 Building production deployment..."

# Clean previous build
rm -rf dist
mkdir -p dist

# Copy HTML files
echo "📄 Copying HTML files..."
cp *.html dist/

# Copy CSS files
echo "🎨 Copying CSS files..."
mkdir -p dist/css
cp css/*.css dist/css/

# Copy JavaScript files
echo "💻 Copying JavaScript files..."
mkdir -p dist/js
cp -r js/*.js dist/js/
mkdir -p dist/js/adapters
cp js/adapters/*.js dist/js/adapters/

# Copy assets
echo "🖼️  Copying assets..."
mkdir -p dist/assets/images
cp -r assets/images/* dist/assets/images/ 2>/dev/null || true
mkdir -p dist/assets/icons
cp -r assets/icons/* dist/assets/icons/ 2>/dev/null || true

# Copy only essential SQL file (for reference, not needed for deployment)
echo "🗄️  Copying database schema..."
mkdir -p dist/sql
cp sql/supabase-schema.sql dist/sql/ 2>/dev/null || true

# Copy web.config for IIS (if exists)
echo "⚙️  Copying IIS configuration..."
cp web.config dist/ 2>/dev/null || true

# Create a minimal README for production
echo "📝 Creating production README..."
cat > dist/README.md << 'EOF'
# Newegg AI Workshop - Registration Site

## Production Deployment

This folder contains the production-ready files for the registration site.

### Files Included
- HTML pages (index.html, register.html, about.html, etc.)
- CSS stylesheets
- JavaScript files
- Assets (images, icons)
- Database schema (sql/supabase-schema.sql) - for reference only

### Configuration Required

Before deploying, update `js/config.js` with your production database credentials:
- Supabase URL
- Supabase anon key
- Workshop event configuration

### Deployment

1. Upload all files in this folder to your web server
2. Ensure your web server is configured to serve static files
3. Test the registration form
4. Monitor for any errors

### Support

For setup instructions, see the main repository documentation.
EOF

echo ""
echo "✅ Production build complete!"
echo ""
echo "📦 Files ready in: dist/"
echo ""
echo "📊 Build summary:"
echo "   - HTML files: $(find dist -name '*.html' | wc -l | tr -d ' ')"
echo "   - CSS files: $(find dist -name '*.css' | wc -l | tr -d ' ')"
echo "   - JS files: $(find dist -name '*.js' | wc -l | tr -d ' ')"
echo "   - Total size: $(du -sh dist | cut -f1)"
echo ""
echo "🚀 Next steps:"
echo "   1. Review dist/js/config.js and update with production credentials"
echo "   2. Upload dist/ folder contents to your web server"
echo "   3. Test the registration form"
echo ""

