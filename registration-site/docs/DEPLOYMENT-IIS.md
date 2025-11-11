# IIS Deployment Guide for Windows Server

Complete guide for deploying the Newegg AI Workshop registration site to IIS (Internet Information Services) on Windows Server.

## 📋 Prerequisites

- Windows Server with IIS installed
- Administrator access
- Production database credentials ready
- Domain name or IP address configured (optional)

## 🔧 Step 1: Install IIS (if not already installed)

### On Windows Server:

1. Open **Server Manager**
2. Click **Add Roles and Features**
3. Select **Web Server (IIS)**
4. Install required features:
   - Web Server
   - Common HTTP Features (Static Content, Default Document, Directory Browsing)
   - Health and Diagnostics
   - Security (Request Filtering)
   - Performance (Static Content Compression)

### Or via PowerShell (as Administrator):

```powershell
Install-WindowsFeature -name Web-Server -IncludeManagementTools
Install-WindowsFeature -name Web-Static-Content
Install-WindowsFeature -name Web-Default-Doc
Install-WindowsFeature -name Web-Dir-Browsing
```

## 📁 Step 2: Prepare Production Files

### Option A: Use Production Build (Recommended)

1. **Run deployment script** (from your development machine):
   ```bash
   cd registration-site
   ./deploy.sh
   ```

2. **Update production config**:
   - Edit `dist/js/config.js` with production database credentials
   - Update Supabase URL and anon key

3. **Copy `dist/` folder** to Windows Server:
   - Via network share, FTP, or RDP file transfer
   - Place in: `C:\inetpub\wwwroot\newegg-ai-workshop\` (or your preferred location)

### Option B: Direct Copy

1. Copy entire `registration-site/` folder to Windows Server
2. Update `js/config.js` with production credentials

## 🌐 Step 3: Create IIS Website

### Method 1: Using IIS Manager (GUI)

1. **Open IIS Manager**:
   - Press `Win + R`, type `inetmgr`, press Enter
   - Or: Server Manager → Tools → Internet Information Services (IIS) Manager

2. **Create Application Pool** (optional but recommended):
   - Right-click **Application Pools** → **Add Application Pool**
   - Name: `NeweggAIWorkshop`
   - .NET CLR version: **No Managed Code** (static site)
   - Managed pipeline mode: **Integrated**
   - Click **OK**

3. **Create Website**:
   - Right-click **Sites** → **Add Website**
   - **Site name**: `Newegg AI Workshop`
   - **Application pool**: Select `NeweggAIWorkshop` (or DefaultAppPool)
   - **Physical path**: `C:\inetpub\wwwroot\newegg-ai-workshop\dist` (or your path)
   - **Binding**:
     - Type: **http** (or **https** if SSL configured)
     - IP address: **All Unassigned** (or specific IP)
     - Port: **80** (or **443** for HTTPS)
     - Host name: Your domain name (e.g., `workshop.newegg.com`) or leave blank
   - Click **OK**

### Method 2: Using PowerShell (as Administrator)

```powershell
# Create application pool
New-WebAppPool -Name "NeweggAIWorkshop"

# Set application pool to No Managed Code (for static site)
Set-ItemProperty IIS:\AppPools\NeweggAIWorkshop -Name managedRuntimeVersion -Value ""

# Create website
New-Website -Name "NeweggAIWorkshop" `
    -ApplicationPool "NeweggAIWorkshop" `
    -PhysicalPath "C:\inetpub\wwwroot\newegg-ai-workshop\dist" `
    -Port 80

# Or with host name
New-Website -Name "NeweggAIWorkshop" `
    -ApplicationPool "NeweggAIWorkshop" `
    -PhysicalPath "C:\inetpub\wwwroot\newegg-ai-workshop\dist" `
    -Port 80 `
    -HostHeader "workshop.newegg.com"
```

## ⚙️ Step 4: Configure IIS Settings

### 4.1 Set Default Document

1. Select your website in IIS Manager
2. Double-click **Default Document**
3. Ensure `index.html` is in the list (should be first)
4. If not, click **Add** and enter `index.html`

### 4.2 Enable Directory Browsing (Optional)

1. Select your website
2. Double-click **Directory Browsing**
3. Click **Disable** (recommended for security)

### 4.3 Configure MIME Types

Ensure these MIME types are configured:

1. Select your website
2. Double-click **MIME Types**
3. Verify these exist (they should by default):
   - `.html` → `text/html`
   - `.css` → `text/css`
   - `.js` → `application/javascript`
   - `.json` → `application/json`
   - `.svg` → `image/svg+xml`
   - `.png` → `image/png`
   - `.jpg` → `image/jpeg`

### 4.4 Enable Static Content Compression

1. Select your website
2. Double-click **Compression**
3. Enable **Enable dynamic content compression** (optional)
4. Enable **Enable static content compression** (recommended)
5. Click **Apply**

### 4.5 Configure Error Pages (Optional)

1. Select your website
2. Double-click **Error Pages**
3. For 404 errors, you can set a custom page or redirect to `index.html`

## 🔒 Step 5: Set File Permissions

### Set IIS_IUSRS Permissions

1. **Navigate to your site folder** in File Explorer:
   - Right-click the folder → **Properties**
   - Go to **Security** tab
   - Click **Edit**

2. **Add IIS_IUSRS** (if not present):
   - Click **Add**
   - Type: `IIS_IUSRS`
   - Click **Check Names** → **OK**

3. **Set Permissions**:
   - Select **IIS_IUSRS**
   - Check **Read & Execute**
   - Check **List folder contents**
   - Check **Read**
   - Click **OK**

### Or via PowerShell:

```powershell
$folderPath = "C:\inetpub\wwwroot\newegg-ai-workshop\dist"
$acl = Get-Acl $folderPath
$permission = "IIS_IUSRS","ReadAndExecute","ContainerInherit,ObjectInherit","None","Allow"
$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule $permission
$acl.SetAccessRule($accessRule)
Set-Acl $folderPath $acl
```

## 🔐 Step 6: Configure SSL/HTTPS (Recommended)

### Option A: Use Existing SSL Certificate

1. In IIS Manager, select your website
2. Click **Bindings** in the right panel
3. Click **Add**
4. Type: **https**
5. Port: **443**
6. SSL certificate: Select your certificate
7. Click **OK**

### Option B: Request Let's Encrypt Certificate

Use tools like:
- **win-acme** (Windows ACME Simple)
- **Certify The Web**

## 🧪 Step 7: Test the Deployment

### Test Locally:

1. Open browser on the server
2. Navigate to: `http://localhost` (or your configured host name)
3. Verify:
   - Homepage loads correctly
   - All CSS styles apply
   - JavaScript works (check browser console)
   - Images load
   - Registration form works
   - Database connection works

### Test from Network:

1. From another machine, navigate to: `http://SERVER_IP` or `http://your-domain.com`
2. Verify same items as above

### Common Issues:

**Issue**: 403 Forbidden
- **Fix**: Check file permissions (IIS_IUSRS needs Read access)

**Issue**: 404 Not Found
- **Fix**: Check physical path is correct, verify `index.html` exists

**Issue**: CSS/JS not loading
- **Fix**: Check MIME types, verify file paths are relative

**Issue**: Database connection fails
- **Fix**: Verify `js/config.js` has correct credentials, check browser console

## 📊 Step 8: Configure Monitoring (Optional)

### Enable Logging:

1. Select your website in IIS Manager
2. Double-click **Logging**
3. Configure:
   - Format: **W3C**
   - Directory: Default or custom path
   - Log file rollover: Daily (recommended)

### View Logs:

Logs are typically in: `C:\inetpub\logs\LogFiles\W3SVC[SiteID]\`

## 🔄 Step 9: Update Process

When you need to update the site:

1. **Stop the website** (optional, for zero downtime):
   ```powershell
   Stop-Website -Name "NeweggAIWorkshop"
   ```

2. **Backup current files**:
   ```powershell
   Copy-Item "C:\inetpub\wwwroot\newegg-ai-workshop\dist" -Destination "C:\inetpub\wwwroot\newegg-ai-workshop\dist_backup_$(Get-Date -Format 'yyyyMMdd')" -Recurse
   ```

3. **Copy new files** to the site directory

4. **Start the website**:
   ```powershell
   Start-Website -Name "NeweggAIWorkshop"
   ```

5. **Test** the updated site

## 🛡️ Security Best Practices

### 1. Remove Unnecessary Features

Disable features you don't need:
- Directory Browsing (should be disabled)
- ASP.NET (if not using)
- PHP (if not using)

### 2. Configure Request Filtering

1. Select your website
2. Double-click **Request Filtering**
3. Configure:
   - Maximum allowed content length
   - File extensions (allow only needed)
   - Hidden segments (protect sensitive files)

### 3. Set Security Headers

Add to `web.config` (create if doesn't exist):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <system.webServer>
    <httpProtocol>
      <customHeaders>
        <add name="X-Content-Type-Options" value="nosniff" />
        <add name="X-Frame-Options" value="DENY" />
        <add name="X-XSS-Protection" value="1; mode=block" />
        <add name="Referrer-Policy" value="strict-origin-when-cross-origin" />
      </customHeaders>
    </httpProtocol>
  </system.webServer>
</configuration>
```

### 4. Enable HTTPS Only

1. Select your website
2. Click **SSL Settings**
3. Check **Require SSL**
4. Set **SSL certificate** if not already set

## 📝 Quick Reference Commands

### PowerShell Commands:

```powershell
# List all websites
Get-Website

# Start website
Start-Website -Name "NeweggAIWorkshop"

# Stop website
Stop-Website -Name "NeweggAIWorkshop"

# Restart website
Restart-WebAppPool -Name "NeweggAIWorkshop"

# Check website status
Get-Website -Name "NeweggAIWorkshop"

# View application pools
Get-WebAppPoolState -Name "NeweggAIWorkshop"
```

## 🆘 Troubleshooting

### Check IIS Status:

```powershell
Get-Service W3SVC
```

### View Event Logs:

```powershell
Get-EventLog -LogName Application -Source "IIS*" -Newest 20
```

### Test Configuration:

```powershell
# Test IIS configuration
C:\Windows\System32\inetsrv\appcmd.exe list site
```

### Common Error Codes:

- **500.19**: Configuration error (check web.config)
- **500.0**: Application pool issue
- **403.14**: Directory browsing disabled (normal)
- **404.0**: File not found (check paths)

## 📚 Additional Resources

- [IIS Official Documentation](https://docs.microsoft.com/en-us/iis/)
- [IIS PowerShell Cmdlets](https://docs.microsoft.com/en-us/powershell/module/iisadministration/)
- [IIS Security Best Practices](https://docs.microsoft.com/en-us/iis/manage/configuring-security/)

## ✅ Deployment Checklist

- [ ] IIS installed and configured
- [ ] Production files copied to server
- [ ] `js/config.js` updated with production credentials
- [ ] Website created in IIS Manager
- [ ] Application pool configured
- [ ] File permissions set (IIS_IUSRS)
- [ ] Default document set to `index.html`
- [ ] MIME types configured
- [ ] SSL/HTTPS configured (recommended)
- [ ] Site tested locally
- [ ] Site tested from network
- [ ] Registration form tested end-to-end
- [ ] Database connection verified
- [ ] Security headers configured
- [ ] Logging enabled
- [ ] Backup process established

---

**Need Help?** Check the main [Deployment Guide](DEPLOYMENT.md) for general deployment information.



