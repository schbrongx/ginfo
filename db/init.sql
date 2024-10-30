CREATE USER replica WITH REPLICATION LOGIN PASSWORD 'replica_password';
SELECT PG_CREATE_PHYSICAL_REPLICATION_SLOT('replication_slot');

CREATE TABLE IF NOT EXISTS locations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  geom GEOMETRY(Point, 4326)
);

INSERT INTO locations (name, geom) VALUES 
('GEOINFO Applications AG', ST_GeomFromText('POINT(9.2892 47.3896)', 4326)),
('Th. Pesendorfer', ST_GeomFromText('POINT(9.3349 47.411)', 4326)),
('Café am Ring', ST_GeomFromText('POINT(9.374 47.4265)', 4326)),
('Kaffeehaus St. Gallen', ST_GeomFromText('POINT(9.3836 47.4251)', 4326)),
('Kafi Franz', ST_GeomFromText('POINT(9.382 47.4246)', 4326)),
('Gnuss', ST_GeomFromText('POINT(9.3802 47.4244)', 4326));
