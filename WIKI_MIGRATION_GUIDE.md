# Migration Guide: Vue.js → Wiki.js Multi-User Wiki

This guide explains how to migrate from the current Vue.js single-page application to Wiki.js, a modern collaborative wiki platform.

## Why Wiki.js?

**Current Limitations:**
- ❌ Content hardcoded in Vue components (requires developer to edit)
- ❌ No multi-user editing support
- ❌ No version control/history for content
- ❌ Requires Git commits to update content

**Wiki.js Benefits:**
- ✅ **Multi-user editing** with user authentication and permissions
- ✅ **Real-time collaborative editing** (multiple editors at once)
- ✅ **Version history** with Git integration (automatic commits)
- ✅ **Rich Markdown editor** with WYSIWYG option
- ✅ **User management** (admin, editor, viewer roles)
- ✅ **Search** built-in across all content
- ✅ **Modern UI** similar to Notion or Confluence
- ✅ **No coding required** for content updates

## Quick Start

### 1. Start Wiki.js with Docker

```bash
# Copy environment file
cp .env.wiki.example .env.wiki

# Edit .env.wiki and set a strong DB_PASSWORD
nano .env.wiki

# Start Wiki.js
docker-compose -f docker-compose.wiki.yml up -d

# Wait ~60 seconds for initialization
# Access Wiki.js at http://localhost:3000
```

### 2. Initial Setup (First Time Only)

1. **Open browser:** http://localhost:3000
2. **Create administrator account:**
   - Email: your-email@example.com
   - Password: (set strong password)
   - Site URL: http://localhost:3000 (or your domain)
3. **Complete setup wizard** (accept defaults)

### 3. Configure User Permissions

**Admin Panel → Administration → Users & Groups**

**Recommended Setup:**
- **Administrators:** Full access to everything
- **Editors:** Can create/edit all pages
- **Viewers:** Read-only access
- **Public:** Choose if unauthenticated users can view

### 4. Enable Git Sync (Optional but Recommended)

**Why:** Automatic backup to GitHub, version control

**Setup:**
1. **Admin → Storage → Git**
2. **Create new GitHub repository** for wiki content
3. **Generate GitHub Personal Access Token:**
   - GitHub → Settings → Developer Settings → Personal Access Tokens
   - Select: `repo` scope
4. **Configure in Wiki.js:**
   - Repository URL: `https://github.com/YourUsername/euticket-wiki-content`
   - Authentication: Personal Access Token
   - Username: Your GitHub username
   - Token: (paste token)
   - Branch: `main`
   - Sync Direction: **Bi-directional** (both push and pull)
   - Sync Interval: Every 5 minutes

Now all content changes automatically commit to GitHub!

## Migrating Existing Content

### Option 1: Manual Migration (Recommended for Learning)

**For each country guide:**

1. **Create new page in Wiki.js:**
   - Click **+ New Page**
   - Path: `/countries/france` (example)
   - Title: `France Railway Guide`
   - Editor: **Markdown**

2. **Convert Vue template to Markdown:**

**Example: France.vue → Markdown**

**Vue Component (before):**
```vue
<template>
  <div class="country-guide">
    <h1>🇫🇷 France Railway Guide</h1>
    <div class="info-box">
      <h3>Quick Facts</h3>
      <ul>
        <li><strong>Operator:</strong> SNCF</li>
      </ul>
    </div>
  </div>
</template>
```

**Markdown (after):**
```markdown
# 🇫🇷 France Railway Guide

> **Quick Facts**
>
> - **Operator:** SNCF
> - **Website:** sncf.com
```

**Tables convert directly:**
```markdown
| Route | Duration | Price |
|-------|----------|-------|
| Paris - Lyon | 2h | €25-80 |
```

**Info boxes become blockquotes:**
```markdown
> ⚠️ **IMPORTANT:** Always validate your ticket!
>
> Remember to punch your ticket before boarding!
```

3. **Save page** → Wiki.js auto-commits to Git!

### Option 2: Automated Migration Script

I can create a Python script to automatically convert Vue components to Markdown:

```bash
# Install dependencies
pip install beautifulsoup4 markdownify

# Run migration script
python migrate_vue_to_markdown.py

# Import generated .md files to Wiki.js via Admin → Tools → Import
```

### Content Structure Recommendation

```
EUTicketWiki/
├── Home                          (main landing page)
├── Countries/
│   ├── France                    (from France.vue)
│   ├── Germany                   (from Germany.vue)
│   ├── Italy                     (from Italy.vue)
│   ├── Netherlands               (from Netherlands.vue)
│   ├── Belgium                   (from Belgium.vue)
│   ├── Sweden                    (from Sweden.vue)
│   └── (more countries...)
├── Tickets-and-Passes/
│   ├── Eurail-Pass
│   ├── Interrail-Pass
│   └── Regional-Passes
├── Routes/
│   ├── Popular-International-Routes
│   └── Day-Trips
└── Travel-Tips/
    ├── Booking-Strategies
    ├── Station-Navigation
    └── Budget-Travel-Tips
```

## Multi-User Collaboration Features

### 1. User Roles

**Create users:**
- Admin → Users → **+ New User**

**Assign roles:**
- **Administrator:** Full control (you)
- **Editor:** Can edit all pages (contributors, travel experts)
- **Viewer:** Read-only (public users)

### 2. Page Permissions

**Per-page access control:**
- Edit any page → **Page Actions** → **Properties** → **Permissions**
- Choose: Public, Specific Groups, or Private

**Example:**
- Published guides: Public read, Editors can write
- Draft guides: Only Editors

### 3. Collaborative Editing

**Real-time editing:**
- Multiple users can edit different pages simultaneously
- Each user sees others' changes in real-time
- Conflict resolution built-in

**Comments:**
- Enable page comments for feedback
- Admin → Rendering → Comments → Enable

### 4. Review Workflow (Optional)

**Approval process for content:**
1. Admin → Rendering → **Approval**
2. Enable page moderation
3. Editors create pages → **Submit for Approval**
4. Administrators review and publish

## Customization

### 1. Change Theme

**Admin → Theme**
- Choose from built-in themes
- Customize colors, logo, favicon

### 2. Add Custom Logo

**Admin → Theme → Logo**
- Upload `euticketwiki-logo.png`
- Set site title: "EUTicketWiki"

### 3. Navigation Menu

**Admin → Navigation**
- Create custom navigation structure
- Add links to main country pages
- Create sections (Countries, Tickets, Routes, Tips)

**Example navigation:**
```yaml
- Home
- Countries
  - France
  - Germany
  - Italy
  - Netherlands
  - Belgium
  - Sweden
- Tickets & Passes
- Routes
- Travel Tips
```

### 4. Add Analytics (Optional)

**Admin → Analytics**
- Google Analytics
- Matomo
- Or custom tracking code

## Comparison: Vue.js vs Wiki.js

| Feature | Vue.js (Current) | Wiki.js (New) |
|---------|------------------|---------------|
| **Content Editing** | Requires developer + Git | Anyone with login via web UI |
| **Multi-user** | ❌ No | ✅ Yes (simultaneous editing) |
| **Version Control** | Manual Git commits | ✅ Automatic Git sync |
| **Permissions** | ❌ None | ✅ User roles & page permissions |
| **Search** | ❌ No | ✅ Built-in full-text search |
| **Mobile Editing** | ❌ No | ✅ Yes (responsive editor) |
| **WYSIWYG Editor** | ❌ No | ✅ Yes (+ Markdown) |
| **Comments** | ❌ No | ✅ Optional per page |
| **Page History** | Git history only | ✅ Visual diff viewer |
| **Setup Complexity** | Low | Medium (requires database) |
| **Performance** | Fast (static) | Fast (cached, CDN-ready) |

## Production Deployment

### Using Docker (Recommended)

**1. Set environment variables:**
```bash
# Edit .env.wiki with production values
DB_PASSWORD=<strong-random-password>
SESSION_SECRET=<generate-with-openssl-rand>
PUBLIC_URL=https://euticketwiki.com
```

**2. Use HTTPS (Let's Encrypt):**
```yaml
# Add nginx-proxy and letsencrypt to docker-compose.wiki.yml
# Or use Cloudflare Tunnel for easy HTTPS
```

**3. Start production:**
```bash
docker-compose -f docker-compose.wiki.yml up -d
```

### Alternative: Managed Hosting

**Wiki.js Cloud:** https://wiki.js.org/cloud
- Fully managed Wiki.js hosting
- $5-20/month depending on usage
- No setup required
- Automatic backups

**Alternatives:**
- Deploy to Railway.app (PostgreSQL + Node.js)
- Deploy to Heroku
- Deploy to AWS/DigitalOcean

## Backup & Recovery

### Automatic Backups (via Git)

If Git sync is enabled:
- **Content:** Auto-backed up to GitHub every 5 minutes
- **Restore:** Clone Git repo and import to new Wiki.js instance

### Database Backup

```bash
# Backup PostgreSQL database
docker exec euticketwiki-postgres pg_dump -U wikijs wikijs > backup.sql

# Restore database
cat backup.sql | docker exec -i euticketwiki-postgres psql -U wikijs wikijs
```

### Full Backup (Recommended)

```bash
# Backup everything (database + uploads + content)
docker-compose -f docker-compose.wiki.yml down
tar -czf euticketwiki-backup-$(date +%Y%m%d).tar.gz postgres-data/ wiki-data/ wiki-repo/
docker-compose -f docker-compose.wiki.yml up -d
```

## Migration Checklist

- [ ] Start Wiki.js with Docker
- [ ] Complete initial setup (admin account)
- [ ] Configure Git sync (optional but recommended)
- [ ] Create user accounts for collaborators
- [ ] Set up user roles and permissions
- [ ] Migrate content from Vue.js to Markdown
  - [ ] France guide
  - [ ] Germany guide
  - [ ] Italy guide
  - [ ] Netherlands guide
  - [ ] Belgium guide
  - [ ] Sweden guide
- [ ] Customize theme and logo
- [ ] Set up navigation menu
- [ ] Configure page permissions
- [ ] Test collaborative editing
- [ ] Set up backups (Git + database)
- [ ] Deploy to production (if needed)
- [ ] Train users on Wiki.js editor

## Support & Resources

**Wiki.js Documentation:** https://docs.requarks.io/
**Community Forum:** https://github.com/requarks/wiki/discussions
**Discord:** https://discord.wiki.js.org/

## FAQs

**Q: Can I keep the Vue.js version while testing Wiki.js?**
A: Yes! They run on different ports (Vue on 5000, Wiki.js on 3000). You can run both simultaneously.

**Q: Will existing content be lost?**
A: No, the Vue.js code remains untouched. Wiki.js is a separate system.

**Q: Can non-technical users edit content?**
A: Yes! Wiki.js has a visual WYSIWYG editor (like Google Docs) and a Markdown editor.

**Q: How many users can edit simultaneously?**
A: Unlimited. Wiki.js supports real-time collaborative editing.

**Q: Is it free?**
A: Yes, Wiki.js is open source (AGPL-3.0). Self-hosting is free. Cloud hosting costs money.

**Q: Can I migrate back to Vue.js later?**
A: Yes, you can export all content as Markdown files and convert back.

## Next Steps

1. **Start Wiki.js:** `docker-compose -f docker-compose.wiki.yml up -d`
2. **Access:** http://localhost:3000
3. **Create admin account** and explore
4. **Try creating a test page** to get familiar
5. **Migrate one country guide** as a proof of concept
6. **Invite collaborators** once comfortable

Good luck with your Wiki.js migration! 🚀
