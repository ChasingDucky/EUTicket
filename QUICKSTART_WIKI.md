# Wiki.js Quick Start Guide

Get started with Wiki.js for multi-user collaborative editing in 5 minutes!

## Prerequisites

- Docker and Docker Compose installed
- 2GB free RAM
- Port 3000 available

## Step 1: Start Wiki.js (2 minutes)

```bash
# 1. Copy environment configuration
cp .env.wiki.example .env.wiki

# 2. (Optional) Edit .env.wiki to set a strong database password
nano .env.wiki

# 3. Start Wiki.js with Docker Compose
docker-compose -f docker-compose.wiki.yml up -d

# 4. Wait for services to start (~60 seconds)
docker-compose -f docker-compose.wiki.yml logs -f wiki
# Press Ctrl+C when you see "HTTPS Server on port 3443: [ DISABLED ]"
```

## Step 2: Complete Setup Wizard (2 minutes)

1. **Open browser:** http://localhost:3000

2. **Create Administrator Account:**
   - Email: `your-email@example.com`
   - Password: (set a strong password)
   - Site URL: `http://localhost:3000` (or your domain)

3. **Click "Install"** and wait ~30 seconds

4. **Complete!** You'll be redirected to the admin dashboard

## Step 3: Create Your First Page (1 minute)

1. **Click "+ New Page"** in the top-right

2. **Set page details:**
   - Path: `/test`
   - Title: `Test Page`
   - Editor: **Markdown**

3. **Add content:**
   ```markdown
   # Welcome to EUTicketWiki!

   This is a test page to verify Wiki.js is working.

   ## Features

   - Multi-user editing ✅
   - Version control ✅
   - Rich markdown support ✅
   ```

4. **Click "Create"**

5. **View your page** at http://localhost:3000/test

## Step 4: Invite Collaborators (Optional)

1. **Admin Dashboard** (click avatar → Administration)

2. **Users & Groups** → **Users** → **+ New User**

3. **Create user:**
   - Name: Collaborator name
   - Email: their-email@example.com
   - Provider: Local
   - Password: (set temporary password)
   - Groups: **Editors** (can edit all pages)

4. **Send them:**
   - URL: http://localhost:3000
   - Email & temporary password
   - Ask them to change password on first login

## What's Next?

### Migrate Existing Content

See [WIKI_MIGRATION_GUIDE.md](WIKI_MIGRATION_GUIDE.md) for:
- Converting Vue.js content to Markdown
- Importing existing country guides
- Setting up Git sync for backups

### Customize Your Wiki

**Admin → Theme:**
- Upload logo
- Change colors
- Set site title to "EUTicketWiki"

**Admin → Navigation:**
- Create navigation menu
- Add links to main sections:
  - Countries
  - Tickets & Passes
  - Routes
  - Travel Tips

**Admin → Rendering:**
- Enable page comments
- Configure editors (Markdown, WYSIWYG, etc.)

### Enable Git Backup (Recommended)

1. **Create GitHub repository** for wiki content

2. **Admin → Storage → Git**

3. **Configure:**
   - Repository URL: `https://github.com/YourUsername/euticket-wiki-content`
   - Authentication: Personal Access Token
   - Branch: `main`
   - Sync: Bi-directional

4. **Test:** Make a page edit → check GitHub for auto-commit!

## Common Commands

```bash
# View logs
docker-compose -f docker-compose.wiki.yml logs -f wiki

# Restart Wiki.js
docker-compose -f docker-compose.wiki.yml restart wiki

# Stop Wiki.js
docker-compose -f docker-compose.wiki.yml down

# Backup database
docker exec euticketwiki-postgres pg_dump -U wikijs wikijs > backup.sql

# View running containers
docker-compose -f docker-compose.wiki.yml ps
```

## Troubleshooting

### Port 3000 already in use

```bash
# Check what's using port 3000
lsof -i :3000

# Option 1: Stop the conflicting service
# Option 2: Change Wiki.js port in docker-compose.wiki.yml
```

### Can't access http://localhost:3000

```bash
# Check if Wiki.js is running
docker-compose -f docker-compose.wiki.yml ps

# Check logs for errors
docker-compose -f docker-compose.wiki.yml logs wiki

# Restart Wiki.js
docker-compose -f docker-compose.wiki.yml restart
```

### Database connection error

```bash
# Check if PostgreSQL is healthy
docker-compose -f docker-compose.wiki.yml ps

# View database logs
docker-compose -f docker-compose.wiki.yml logs db

# Restart both services
docker-compose -f docker-compose.wiki.yml restart
```

### Forgot admin password

```bash
# Stop Wiki.js
docker-compose -f docker-compose.wiki.yml down

# Remove database volume (WARNING: deletes all data)
docker volume rm euticket_postgres-data

# Start fresh
docker-compose -f docker-compose.wiki.yml up -d

# Go through setup wizard again
```

## Production Deployment

For production use:

1. **Set strong passwords in `.env.wiki`:**
   ```bash
   # Generate random password
   openssl rand -base64 32
   ```

2. **Use HTTPS** (required for security):
   - Option 1: Cloudflare Tunnel (easiest)
   - Option 2: Let's Encrypt with nginx-proxy
   - Option 3: Reverse proxy (Traefik, Caddy)

3. **Regular backups:**
   ```bash
   # Automated backup script
   0 2 * * * docker exec euticketwiki-postgres pg_dump -U wikijs wikijs > /backups/wiki-$(date +\%Y\%m\%d).sql
   ```

4. **Enable Git sync** for content version control

## Resources

- **Wiki.js Documentation:** https://docs.requarks.io/
- **Community Forum:** https://github.com/requarks/wiki/discussions
- **Migration Guide:** [WIKI_MIGRATION_GUIDE.md](WIKI_MIGRATION_GUIDE.md)

## Need Help?

- Check [WIKI_MIGRATION_GUIDE.md](WIKI_MIGRATION_GUIDE.md) for detailed setup
- View Wiki.js logs: `docker-compose -f docker-compose.wiki.yml logs -f`
- Visit Wiki.js community: https://github.com/requarks/wiki/discussions

---

**Happy collaborating! 🚀**
