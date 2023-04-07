

CREATE TABLE IF NOT EXISTS Users (
    userId SERIAL PRIMARY KEY,
    firstName varchar(255) NOT NULL,
    phone bigint NOT NULL
);

INSERT INTO Users(firstName, phone) VALUES 
('Nguyen', 12321312321),
('Yamamoto', 432723472346);


