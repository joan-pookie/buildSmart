# BuildSmart CLI

BuildSmart CLI is a command-line interface application designed to help manage construction projects efficiently. It allows you to manage **clients, workers, projects, and project assignments** in a simple and structured way using **Python**, **SQLAlchemy**, and **Click**, with data stored in an **SQLite** database.

project demonstration 
             https://youtu.be/v8HRyrurdV0

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Database Structure](#database-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Clients](#clients)
  - [Workers](#workers)
  - [Projects](#projects)
  - [Assignments](#assignments)
- [Example Workflow](#example-workflow)
- [Author](#author)

---

## Overview

BuildSmart CLI provides a relational database management system for construction projects. The database enforces relationships between **clients, projects, workers, and project assignments**, ensuring data consistency and making it easy to track who is working on which project for which client.

---

## Features

- Add, list, and delete clients
- Add, list, and delete workers
- Add, list, and delete projects
- Assign workers to projects
- View all assignments
- Fully relational database with foreign key constraints

---

## Database Structure

The application contains four main tables:

### Clients
- `id`: Primary key
- `name`: Client name
- `email`: Client email (unique)
- **Relationships**: A client can have multiple projects.

### Workers
- `id`: Primary key
- `name`: Worker name
- `role`: Worker role
- **Relationships**: A worker can be assigned to multiple projects through project assignments.

### Projects
- `id`: Primary key
- `name`: Project name
- `client_id`: Foreign key referencing `clients.id`
- `description`: Optional project description
- **Relationships**: Each project belongs to a client and can have multiple workers assigned.

### Project Assignments
- `id`: Primary key
- `project_id`: Foreign key referencing `projects.id`
- `worker_id`: Foreign key referencing `workers.id`
- **Relationships**: Connects workers to projects, supporting many-to-many relationships.

**Summary of Relationships:**

- **Client → Projects**: One-to-many
- **Project → Worker**: Many-to-many via ProjectAssignments
- **Worker → Projects**: Many-to-many via ProjectAssignments

Author
Joan Pookie
Software Engineering Student
