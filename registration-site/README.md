# Newegg AI Workshop - Registration Site

Modern, high-tech registration microsite for the Newegg AI Workshop program. **Built entirely with AI coding tools** 🤖

## Features

- 🎨 **Modern Design** - Newegg-inspired styling with high-tech aesthetic
- 📱 **Responsive** - Works perfectly on all devices
- 🚀 **Fast & Lightweight** - Pure HTML/CSS/JS, no heavy frameworks
- 🔗 **Curriculum Integration** - Direct links to curriculum files in parent repo
- 📝 **Registration System** - Complete waitlist/registration with database integration
- ✨ **Smooth Animations** - Professional scroll animations and transitions
- 🗄️ **Flexible Database** - Supports Supabase, MySQL, and MSSQL via adapter pattern
- ⏰ **Deadline Management** - Automatic registration closure with countdown timer
- ✅ **Form Validation** - Real-time validation and formatting

## Quick Start

1. **Setup Database** - See [docs/SETUP.md](docs/SETUP.md) for detailed instructions
2. **Configure** - Edit `js/config.js` with your database credentials
3. **Deploy** - Copy to web server or use GitHub Pages

## File Structure

```
registration-site/
├── index.html              # Landing page
├── about.html              # About page with curriculum details
├── register.html           # Registration form
├── confirmation.html       # Registration confirmation page
├── terms.html              # Terms & conditions
├── admin-view.html         # Admin view (requires auth setup)
│
├── css/                   # Stylesheets
│   ├── main.css          # Main stylesheet
│   └── components.css    # Component styles
│
├── js/                    # JavaScript
│   ├── config.js         # Database configuration
│   ├── db-adapter.js     # Database adapter base class
│   ├── db-factory.js     # Database factory
│   ├── forms.js          # Form handling
│   ├── form-validation.js # Form validation utilities
│   ├── registration-status.js # Deadline management
│   ├── main.js           # Main JavaScript
│   └── adapters/         # Database adapters
│       ├── supabase-adapter.js
│       ├── mysql-adapter.js
│       └── mssql-adapter.js
│
├── assets/                # Assets
│   ├── images/           # Images (including Newegg logo)
│   └── icons/            # Icons
│
├── sql/                   # Database schemas
│   ├── supabase-schema.sql # Main Supabase schema
│   └── archive/         # Archived troubleshooting SQL files
│
└── docs/                  # Documentation
    ├── SETUP.md          # Setup guide
    ├── SECURITY.md          # Security best practices
    └── DATABASE-SWITCHING.md # Database adapter guide
```

## Configuration

### Database Configuration

Edit `js/config.js` to configure your database:

```javascript
const DB_CONFIG = {
    type: 'supabase',  // 'supabase', 'mysql', or 'mssql'
    supabase: {
        url: 'YOUR_SUPABASE_URL',
        anonKey: 'YOUR_SUPABASE_ANON_KEY'
    },
    currentEventId: 'youthai-explorer-2025-nov'
};
```

### Workshop Events

Configure workshop events in `js/config.js`:

```javascript
const WORKSHOP_EVENTS = {
    'event-id': {
        name: 'Workshop Name',
        level: 'Explorer Level',
        maxCapacity: 12,
        startDate: '2025-11-15',
        endDate: '2025-12-20',
        registrationDeadline: '2025-11-10',
        registrationDeadlineTime: '23:59'
    }
};
```

## Documentation

- **[Setup Guide](docs/SETUP.md)** - Complete setup instructions
- **[Security Guide](docs/SECURITY.md)** - Security best practices
- **[Attack Prevention](docs/SECURITY-ATTACK-PREVENTION.md)** - Protection against spam and malicious attacks
- **[Database Switching](docs/DATABASE-SWITCHING.md)** - How to switch database backends
- **[Easiest Deployment](docs/DEPLOYMENT-EASIEST.md)** - Quick deployment options (Netlify, Vercel, etc.)
- **[IIS Deployment](docs/DEPLOYMENT-IIS.md)** - Windows Server / IIS deployment guide

## Deployment

### 🚀 Easiest Deployment Options

**For the quickest deployment**, see **[Easiest Deployment Guide](docs/DEPLOYMENT-EASIEST.md)**

**Recommended**: **Netlify** (drag-and-drop, 2 minutes, free)

**Other easy options**:
- Vercel (similar to Netlify)
- GitHub Pages (free for public repos)
- Cloudflare Pages (excellent performance)

### Quick Deploy (Production Build)

1. **Create production build**:
   ```bash
   cd registration-site
   ./deploy.sh
   ```

2. **Update configuration**: Edit `dist/js/config.js` with production credentials

3. **Deploy**: Upload all files from `dist/` folder to your web server

See **[Deployment Guide](docs/DEPLOYMENT.md)** for detailed instructions.

### Direct Deployment (Simple)

1. Copy the `registration-site/` folder to your web server
2. Ensure all relative paths work correctly
3. Configure your web server to serve the files
4. Update database configuration in `js/config.js`

### GitHub Pages

1. Push the repository to GitHub
2. Go to repository **Settings** → **Pages**
3. Set source to `/registration-site/dist` folder (if using build) or `/registration-site`
4. Site will be available at `https://username.github.io/newegg-ai-workshop/`

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Built with AI 🤖

This entire website was designed, coded, and deployed using AI coding assistants. From the responsive layout and modern UI to the database integration and form validation—every aspect was built with AI collaboration.

See the [About page](about.html#built-with-ai) for more details about the AI development process.

## License

© 2025 Newegg AI Workshop. All rights reserved.
