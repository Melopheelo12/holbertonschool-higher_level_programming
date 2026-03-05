-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create the table states in the database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);