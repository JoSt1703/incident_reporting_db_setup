db = db.getSiblingDB('incidents');

// Create collections
db.createCollection("positive_incidents");
db.createCollection("negative_incidents");

// Optional: enforce unique `_id` if you want strict uniqueness
db.positive_incidents.createIndex({ _id: 1 }, { unique: true });
db.negative_incidents.createIndex({ _id: 1 }, { unique: true });
