# Mini RDBMS Demo (Flask + SQLAlchemy)

This project demonstrates a **simplified relational database management
system (RDBMS) interface** built using **Flask** and **SQLAlchemy**.

The goal of this project is **not** to reimplement a full database
engine, but to showcase a strong understanding of **relational database
concepts** and how they are applied in real-world systems.

------------------------------------------------------------------------

## Features

-   Relational table definitions\
-   Multiple column data types\
-   Primary keys and foreign keys\
-   Unique constraints and indexing\
-   Full CRUD operations\
-   Basic JOIN queries\
-   SQL-like query execution (REPL-style endpoint)\
-   Simple web API demonstrating database usage

------------------------------------------------------------------------

## Technologies Used

-   Python\
-   Flask\
-   SQLAlchemy\
-   SQLite

------------------------------------------------------------------------

## Database Design

### Tables

**Users** - `id` (Primary Key) - `name` - `email` (Unique, Indexed)

**Posts** - `id` (Primary Key) - `title` - `content` - `user_id`
(Foreign Key → Users)

This structure allows relational operations such as **JOINs** between
users and their posts.

------------------------------------------------------------------------

## Example SQL Queries

``` sql
SELECT * FROM users;

SELECT users.name, posts.title
FROM users
JOIN posts ON users.id = posts.user_id;
```

------------------------------------------------------------------------

## API Endpoints

-   `POST /users` -- Create a user\
-   `GET /users` -- Retrieve users\
-   `PUT /users/<id>` -- Update a user\
-   `DELETE /users/<id>` -- Delete a user\
-   `GET /users/<id>/posts` -- Join users and posts

------------------------------------------------------------------------

## SQL-like REPL

The project exposes an endpoint that allows executing raw SQL queries
against the database, simulating a **basic interactive REPL**.

------------------------------------------------------------------------

## Scope Clarification

The database storage, query execution, and transaction handling are
provided by SQLite via SQLAlchemy.

This project focuses on: - Relational modeling\
- Constraints and indexing\
- Querying and joins\
- Practical database integration

------------------------------------------------------------------------

## How to Run

``` bash
pip install flask flask-sqlalchemy
python app.py
```

------------------------------------------------------------------------

## Author

**Samuel Gitau**
