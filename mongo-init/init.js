db = db.getSiblingDB('incidents');

// Create collections
db.createCollection("positive_incidents");
db.createCollection("negative_incidents");

// Enforce unique ID
db.positive_incidents.createIndex({ _id: 1 }, { unique: true });
db.negative_incidents.createIndex({ _id: 1 }, { unique: true });

// Insert placeholder docs to ensure collection creation
db.positive_incidents.insertOne({ _id: "placeholder-pos", created: new Date(), init: true });
db.negative_incidents.insertOne({ _id: "placeholder-neg", created: new Date(), init: true });
