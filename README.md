# Job-Finder

Job-Finder is a Django-based job board application. The database running underneath is PostgreSQL, and the entire stack can be launched via Docker Compose.

## How to Run the Project

### Prerequisites

- You must have [Docker](https://docs.docker.com/get-docker/) installed.
- You must have [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd Job-Finder
   ```

2. **Start the application with Docker Compose**:
   ```bash
   docker compose up -d --build
   ```
   This will:
   - Build the `web` container (incorporating required Python dependencies and Django settings).
   - Start the `db` container which uses `postgres:15` to host the PostgreSQL database.
   - Run the initial Django database migrations to set up your tables automatically.
   
3. **Access the application**:
   Open a web browser and navigate to:
   [http://localhost:8000](http://localhost:8000)

4. **Stop the application**:
   If you wish to stop the application gracefully without deleting the data (since database files are persisted in a Docker volume):
   ```bash
   docker compose down
   ```

### Troubleshooting
- If changes to static files or Python files aren't taking effect, run `docker compose up --build -d` to rebuild the underlying images.
- If the application starts but throws database errors, ensure the `db` container has fully initialized by checking its logs: `docker compose logs db`.
