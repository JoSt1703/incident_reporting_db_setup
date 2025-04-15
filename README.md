# Cybersecurity Incident Reporting – MongoDB

This project is part of a Master's thesis at ETH Zurich. The aim of the thesis is to explore the potential and requirements for **positive incidence reporting** in cybersecurity.

While incident reporting is a well-established practice in many organizations, it typically focuses on **negative events** such as breaches, failures, or vulnerabilities.

However, there is also value in capturing **positive cybersecurity incidents** — such as successful defense operations, resilience during attacks, or well-implemented best practices. These "positive" stories can offer insights into what contributes to secure and stable operations.

This repository contains a **Docker-based prototype** for a MongoDB database to store and explore both positive and negative incident reports.

---

## Project Setup (Local)

### 1. Prerequisites

- Docker  
- Docker Compose

---

### 2. Environment Configuration

Create a `.env` file in the project root:

```
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=adminPW
```

**Important:** Add `.env` to your `.gitignore` file to avoid exposing secrets.

---

### 3. Start the Service

```
docker compose up -d
```

---

### 4. Stop the Service

```
docker compose down
```

---

## Access

### MongoDB

- **Host:** `localhost`  
- **Port:** `27017`  
- **URI:**

```
mongodb://admin:adminPW@localhost:27017
```

You can connect using:

- [MongoDB Compass](https://www.mongodb.com/products/compass)
- Command-line:

```
docker exec -it mongodb mongosh -u admin -p adminPW
```

---

## Data Persistence

MongoDB data is stored in a Docker volume:

```yaml
volumes:
  mongo_data:
```

This ensures data is retained across container restarts.

---

## Automatic Collection Setup

MongoDB will automatically create the following collections on startup:

- `positive_incidents`
- `negative_incidents`

These collections are defined in an `init.js` script, which is mounted into the container using the `docker-entrypoint-initdb.d` mechanism. You can insert unstructured JSON documents into either collection without defining a schema.

Example script content:

```js
// mongo-init/init.js

db = db.getSiblingDB('incidents');

db.createCollection("positive_incidents");
db.createCollection("negative_incidents");

db.positive_incidents.createIndex({ _id: 1 }, { unique: true });
db.negative_incidents.createIndex({ _id: 1 }, { unique: true });
```

Make sure the script is located in a `mongo-init` folder and referenced in `docker-compose.yml`:

```yaml
volumes:
  - ./mongo-init:/docker-entrypoint-initdb.d:ro
```

---

## VM Deployment (University Internal Server)

To deploy on a VM within the university network:

1. **Transfer the project folder to the VM**
2. **Update the `.env` file** with strong credentials
3. **Update port bindings** in `docker-compose.yml` to bind only to the VM’s internal IP:

```yaml
ports:
  - "10.x.x.x:27017:27017"   # MongoDB
```

4. **Configure the firewall (UFW example)** to allow internal access only:

```
sudo ufw allow from 10.0.0.0/16 to any port 27017
```

5. **Start the service:**

```
docker compose up -d
```

---

## Security Recommendations

- Do **not** expose MongoDB to the public internet.
- If external access is needed:
  - Use a reverse proxy (e.g., NGINX) with access controls.
  - Or run behind a VPN (WireGuard, Tailscale, etc.).
- Back up the MongoDB volume regularly if the data is valuable.

---

## License

This project is for academic use as part of a Master's thesis and is not intended for production use without additional security hardening.
