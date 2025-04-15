# Cybersecurity Incident Reporting – MongoDB & PySpark

This project is part of a Master's thesis at ETH Zurich. The aim of the thesis is to explore the potential and requirements for **positive incidence reporting** in cybersecurity.

While incident reporting is a well-established practice in many organizations, it typically focuses on **negative events** such as breaches, failures, or vulnerabilities.

However, there is also value in capturing **positive cybersecurity incidents** — such as successful defense operations, resilience during attacks, or well-implemented best practices. These "positive" stories can offer insights into what contributes to secure and stable operations.

This repository contains a **Docker-based prototype** for a MongoDB database and a PySpark-powered Jupyter Notebook to explore both positive and negative incident reports.

---

## Project Setup (Local)

### 1. Prerequisites

- Docker  
- Docker Compose  
- `.env` file in project root:

```
MONGO_INITDB_ROOT_USERNAME=admin  
MONGO_INITDB_ROOT_PASSWORD=adminPW
```

**Important:** Add `.env` to your `.gitignore` file to avoid exposing secrets.

---

### 2. Start the Services

```bash
docker compose up -d
```

This will start both:

- MongoDB on `localhost:27017`
- Jupyter Lab with PySpark on `localhost:8888`

Get the Jupyter token using:

```bash
docker logs jupyter_spark
```

---

### 3. Stop the Services

```bash
docker compose down
```

---

## Jupyter Notebook

A prebuilt notebook is included at:

```
notebooks/01_mongo_spark_demo.ipynb
```

This notebook:

- Connects to MongoDB
- Inserts test data into `positive_incidents` and `negative_incidents`
- Reads both collections via PySpark
- Performs basic analytics (e.g. counts by year)

Start Jupyter Lab and open the notebook in your browser:

```
http://localhost:8888
```

---

## MongoDB Access

You can access MongoDB directly via:

```bash
docker exec -it mongodb mongosh -u admin -p adminPW
```

Inside the shell:

```js
use incidents
show collections
db.negative_incidents.find().pretty()
```

Or connect via MongoDB Compass using:

```
mongodb://admin:adminPW@localhost:27017
```

---
### Python Script for Bulk Import

You can import JSON incident reports into MongoDB using a helper script:

```
python3 insert_incidents.py [positive|negative]
```

This script reads all `.json` files from the `./data/` folder and inserts them into either the `positive_incidents` or `negative_incidents` collection based on the argument you provide. It uses your `.env` file to retrieve the MongoDB credentials securely.

#### Python Requirements

Before running the script, install the required Python package:

```
pip install pymongo python-dotenv
```

Make sure your `.env` is in the same directory

---

## Security Tips

- Do **not** expose MongoDB or Jupyter to the public internet.
- Use a VPN, SSH tunnel, or proxy with basic auth if external access is needed.
- Regularly back up your MongoDB volume if storing real data.

---

## License

This project is for academic purposes and is not hardened for production use.


