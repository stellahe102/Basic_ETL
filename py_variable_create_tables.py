# variables containing sql statments to drop tables
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
users_table_drop = "DROP TABLE IF EXISTS users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artists_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# variables containing sql statments to create tables
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
    songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY,
    start_time TIMESTAMP REFERENCES time(start_time),
    user_id INT REFERENCES users(user_id),
    level VARCHAR NOT NULL,
    song_id VARCHAR REFERENCES songs(song_id),
    artist_id VARCHAR REFERENCES artists(artist_id),
    session_id INT NOT NULL,
    location VARCHAR,
    user_agent TEXT
    )""")

users_table_create = ("""CREATE TABLE IF NOT EXISTS users(
    user_id INT CONSTRAINT users_pk PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender CHAR(1),
    level VARCHAR NOT NULL    
    )""")

songs_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
    song_id VARCHAR CONSTRAINTS song_pk PRIMARY KEY,
    title VARCHAR,
    artist_id VARCHAR REFERENCES artists(artist_id),
    year INT CHECK (year >= 0),
    duration FLOAT
    )""")
    
artists_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
    artist_id VARCHAR CONSTRAINT artists_pk PRIMARY KEY
    name VARCHAR,
    location VARCHAR,
    latitude DECIMAL(9,6),
    longtitude DECIMAL(9,6)
    )""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
    start_time TIMESTAMP CONSTRAINT time_pk PRIMARY KEY,
    hour INT NOT NULL CHECK (hour >= 0),
    day INT NOT NULL CHECK (day >= 0),
    week INT NOT NULL CHECK (week >= 0),
    month INT NOT NULL CHECK (month >= 0),
    year INT NOT NULL CHECK (year >= 0),
    weekday VARCHAR NOT NULL
    )""")

# variables containing sql statments to insert records
songplay_table_insert = ("""INSERT INTO songplays 
    VALUES(default, %s, %s, %s, %s, %s, %s, %s, %s)""")

users_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING
    """)

songs_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration)
    VALUES(%s, %s, %s, %s, %s)""")

artists_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longtitude)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO UPDATE SET
    location = EXCLUDED.location
    latitude = EXCLUDED.latitude,
    longtitude = EXCLUDED.longtitude""")

time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING""")
# variable to pull song_id, artist_id based on song name, artist name and length
# this is needed to insert the data to the songplays tables

song_select = ("""
    SELECT songs.song_id, artists.artist_id
    FROM songs
    JOIN artists
        ON songs.artist_id = artists.artist_id
    WHERE
        songs.title = %s
        AND artists.name = %s
        AND songs.duration = %s
    """)

# list variable for drop tables and create tables sequentially
create_table_queries = [
    songplay_table_create,
    songs_table_create,
    users_table_create,
    artists_table_create,
    time_table_create
    ]
drop_table_queries = [
    songplay_table_drop,
    songs_table_drop,
    users_table_drop,
    artists_table_drop,
    time_table_drop
    ]
insert_table_queries = [
    songplay_table_insert,
    users_table_insert,
    songs_table_insert,
    artists_table_insert,
    time_table_insert
    ]
