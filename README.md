# EUTicketWiki - European Railway Travel Guide

A comprehensive wiki-style guide for English-speaking tourists traveling by train across Europe.

Built with **Vue.js 3**, **Vite**, and **Docker** for modern, fast, and scalable deployment.

## Overview

EUTicketWiki provides essential information about European railway systems, ticket types, booking platforms, popular routes, and travel tips to help tourists navigate Europe by train efficiently and affordably.

## Features

- **Country Railway Guides**: Detailed information about railway systems in major European countries
- **Ticket Types Guide**: Understanding different ticket types (single, return, passes, etc.)
- **Booking Platforms**: Comparison of major booking websites and apps
- **Popular Routes**: Classic European train routes and scenic journeys
- **Travel Tips**: Practical advice for train travel in Europe
- **Station Information**: Major railway stations and their facilities
- **Modern Tech Stack**: Built with Vue.js 3 and Vite for fast, responsive performance
- **Docker Support**: Easy deployment with Docker and docker-compose

## Technology Stack

- **Frontend Framework**: Vue.js 3 with Composition API
- **Build Tool**: Vite 5
- **Router**: Vue Router 4
- **Web Server**: Nginx (production)
- **Containerization**: Docker & Docker Compose

## Getting Started

### Prerequisites

- **Node.js 18+** and **npm 9+** (for local development)
- **Docker** and **Docker Compose** (for containerized deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/ChasingDucky/EUTicket.git
   cd EUTicket
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   ```
   http://localhost:3000
   ```

The app will hot-reload when you make changes to the source files.

### Docker Development

Run the development server in a Docker container with hot-reload:

```bash
docker-compose --profile dev up
```

Access the app at `http://localhost:3000`

To stop:
```bash
docker-compose --profile dev down
```

### Docker Production Deployment

Build and run the optimized production container with Nginx:

```bash
# Using docker-compose (recommended)
docker-compose --profile prod up -d

# Or build manually
docker build -t euticketwiki:latest .
docker run -d -p 80:80 --name euticketwiki euticketwiki:latest
```

Access the app at `http://localhost`

To stop:
```bash
docker-compose --profile prod down
```

### Available Scripts

- `npm run dev` - Start Vite development server with hot-reload
- `npm run build` - Build optimized production bundle
- `npm run preview` - Preview production build locally

## Project Structure

```
EUTicketWiki/
├── src/                        # Source code
│   ├── main.js                # Application entry point
│   ├── App.vue                # Root component
│   ├── router/
│   │   └── index.js          # Vue Router configuration
│   ├── components/           # Reusable components
│   │   ├── Header.vue        # Header with dynamic subtitle
│   │   ├── Navigation.vue    # Main navigation
│   │   └── Footer.vue        # Footer component
│   ├── views/                # Page components
│   │   ├── Home.vue          # Homepage
│   │   ├── countries/        # Country guides
│   │   │   ├── Index.vue     # Countries overview
│   │   │   ├── France.vue    # France guide
│   │   │   └── Germany.vue   # Germany guide
│   │   ├── tickets/          # Ticket information
│   │   │   └── Index.vue     # Tickets & passes guide
│   │   ├── routes/           # Popular routes
│   │   │   └── Index.vue     # Routes overview
│   │   └── tips/             # Travel tips
│   │       └── Index.vue     # Tips & advice
│   └── assets/
│       └── style.css         # Global styles
├── public/                    # Static assets (served as-is)
├── Dockerfile                # Multi-stage production build
├── Dockerfile.dev            # Development container
├── docker-compose.yml        # Docker Compose configuration
├── nginx.conf                # Nginx server configuration
├── vite.config.js            # Vite build configuration
├── package.json              # Node.js dependencies
└── index-new.html            # HTML entry point
```

## Docker Configuration

### Development Container (`Dockerfile.dev`)
- Based on Node.js 20 Alpine
- Hot-reload enabled
- Volume mounting for live code updates
- Exposes port 3000

### Production Container (`Dockerfile`)
- Multi-stage build for minimal image size
- Stage 1: Build Vue.js app with Vite
- Stage 2: Serve with Nginx
- Optimized static assets
- Health check endpoint at `/health`
- Exposes port 80

### Nginx Configuration
- Gzip compression enabled
- Security headers configured
- Static asset caching (1 year)
- SPA routing support (fallback to index.html)
- Health check endpoint

## Development

### Adding New Pages

1. Create a new Vue component in `src/views/`
2. Add route to `src/router/index.js`
3. Update navigation in `src/components/Navigation.vue` if needed

### Styling

Global styles are in `src/assets/style.css`. Component-specific styles can be added using `<style scoped>` in Vue components.

## Deployment

### Production Best Practices

1. **Environment Variables**: Configure via `.env` files (not included in repo)
2. **Reverse Proxy**: Use nginx or Traefik in front of the container
3. **SSL/TLS**: Configure HTTPS with Let's Encrypt
4. **CDN**: Consider using a CDN for static assets
5. **Monitoring**: Add health check monitoring

### Health Check

The production container includes a health check endpoint:
```bash
curl http://localhost/health
# Response: "healthy"
```

## Contributing

This is an open wiki project. Contributions and updates are welcome to keep information current and accurate.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - Free to use and modify

## Useful Resources

### Official Railway Operators
- [Rail Europe](https://www.raileurope.com) - Multi-country booking
- [Deutsche Bahn](https://www.bahn.com) - German Railways
- [SNCF](https://www.sncf.com) - French Railways
- [Trenitalia](https://www.trenitalia.com) - Italian Railways

### Rail Passes
- [Eurail](https://www.eurail.com) - For non-European residents
- [Interrail](https://www.interrail.eu) - For European residents

### Planning Tools
- [Seat61](https://www.seat61.com) - Comprehensive rail travel guide
- [Trainline](https://www.trainline.com) - Multi-operator booking

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/ChasingDucky/EUTicket).

---

**Happy Train Travels! 🚄**
