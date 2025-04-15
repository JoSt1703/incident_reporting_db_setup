# Cybersecurity Incident Reporting – MongoDB

This project is part of a Master's thesis at ETH Zurich. The aim of the thesis is to explore the potential and requirements for **positive incidence reporting** in cybersecurity.

While incident reporting is a well-established practice in many organizations, it typically focuses on **negative events** such as breaches, failures, or vulnerabilities.

However, there is also value in capturing **positive cybersecurity incidents** — such as successful defense operations, resilience during attacks, or well-implemented best practices. These "positive" stories can offer insights into what contributes to secure and stable operations.

This repository contains a **Docker-based prototype** for a MongoDB database and web interface to store and explore both positive and negative incident reports.

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
MONGO_INITDB_ROOT_PASSWORD=admin_pw
```

**Important:** Add `.env` to your `.gitignore` file to avoid exposing secrets.

---

### 3. Start the Services

```
docker compose up -d
```

---

### 4. Stop the Services

```
docker compose down
```

---

## Access

### MongoDB

- Host: `localhost`  
- Port: `27017`  
- URI:

```
mongodb://admin:admin_pw@localhost:27017
```

Use this to connect from:
- MongoDB Compass
- Backend applications

---

### Mongo Express (Web UI)

- URL: [http://localhost:8081](http://localhost:8081)

---

## 📂 Data Persistence

MongoDB data is stored in a Docker volume:

```yaml
volumes:
  mongo_data:
```

This ensures data is retained across container restarts.

---

## 💻 VM Deployment (University Internal Server)

To deploy on a VM within the university network:

1. **Transfer the project folder to the VM**

2. **Update the `.env` file with strong credentials**

3. **Update port bindings in `docker-compose.yml`** to bind only to the VM’s internal IP:

```yaml
ports:
  - "10.x.x.x:8081:8081"     # Mongo Express
  - "10.x.x.x:27017:27017"   # MongoDB
```

4. **Configure the firewall (UFW example)** to allow internal access only:

```
sudo ufw allow from 10.0.0.0/16 to any port 27017
sudo ufw allow from 10.0.0.0/16 to any port 8081
```

5. **Start the services:**

```
docker compose up -d
```

---

## 🔐 Security Recommendations

- Do **not** expose MongoDB or Mongo Express to the public internet.
- If external access is needed:
  - Use a reverse proxy (e.g., NGINX) with Basic Auth.
  - Or run behind a VPN (WireGuard, Tailscale, etc.).
- Back up the MongoDB volume regularly if the data is valuable.

---

## 📌 License

This project is for academic use as part of a Master's thesis and is not intended for production use without additional security hardening.