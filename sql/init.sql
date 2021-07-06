-- Always run on startup. Mainly meant for running on other systems where the database does not exist.
CREATE TABLE IF NOT EXISTS collab_data (
    rc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dc_id INTEGER NOT NULL,
    data_placement varchar(255) NOT NULL UNIQUE,
    collab_name varchar(20) NOT NULL UNIQUE
);