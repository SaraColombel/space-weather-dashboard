CREATE TABLE IF NOT EXISTS plasma (
    time_tag TEXT PRIMARY KEY,
    density REAL,
    speed REAL
);

CREATE TABLE IF NOT EXISTS mag (
    time_tag TEXT PRIMARY KEY,
    bz_gsm REAL
);

CREATE TABLE IF NOT EXISTS kp (
    time_tag TEXT PRIMARY KEY,
    kp_index REAL
);