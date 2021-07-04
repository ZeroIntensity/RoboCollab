CREATE TABLE IF NOT EXISTS collab_data (
    rc_id int NOT NULL,
    dc_id int NOT NULL,
    data_placement varchar(255) NOT NULL,
    collab_name varchar(255) NOT NULL,
    PRIMARY KEY (rc_id)
);