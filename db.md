### Setting up our database

* Access your database
* Create a new database and give it a name, for example `lctdb`
* Create the necessary tables
  ```
  CREATE DATABASE lctdb;
  ```
* Create the tables needed
  ```
  CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    INDEX (email)
  );
  ```
  ```
  CREATE TABLE posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    text VARCHAR(1000),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX (user_id)
  );
  ```
* Update the `.env` file with the DB_NAME, PASSWORD, and USERNAME

### Future Work
* Integrate Alembic or similar so we can run migrations on project setup
