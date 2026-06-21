# Python Version App (Dockerized)

## Project Overview

This project demonstrates a simple Dockerized Python application using the `python:3.12-slim` base image.

The application prints:

* Python Version
* Current Date
* Current Time
* Current Date & Time (IST)

---

## Project Structure

```text
python-version-app/
│
├── app.py
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## Build Docker Image

```bash
docker build -t python-version-app .
```

---

## Run Docker Container

```bash
docker run --rm python-version-app
```

---

## Sample Output

```text
Python Version: 3.12.13 (main, Jun 11 2026, 01:09:00) [GCC 14.2.0]

Current Date & Time (IST): 2026-06-21 18:20:00 IST
Current Date: 2026-06-21
Current Time: 18:20:00
```

---

## Docker Base Image

```text
python:3.12-slim
```

---

## Author

Dushyant Sisodiya

```

**Note:** After running the container successfully, take a screenshot of the terminal output and insert it below the **Sample Output** section before pushing to GitHub, since your teacher specifically asked for a sample output screenshot.  
```
