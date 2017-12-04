CREATE TABLE general
(
  id                SERIAL PRIMARY KEY,
  name              CHAR(50)  NOT NULL ,
  email             CHAR(50)  NOT NULL ,
  subscription_date DATE  NOT NULL 
);
