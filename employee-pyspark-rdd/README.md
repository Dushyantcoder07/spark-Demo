# Employee PySpark RDD Project

## Description

This project uses PySpark RDDs to process employee data from a CSV file.

## Operations Performed

* Read employee data using RDD
* Sort employees by salary in descending order
* Calculate total salary by department
* Find top 3 highest-paid employees
* Save top 3 employees to an output file

## Dataset

| ID | Name   | Department | Salary |
| -- | ------ | ---------- | ------ |
| 1  | Amit   | IT         | 55000  |
| 2  | Rahul  | HR         | 40000  |
| 3  | Neha   | IT         | 65000  |
| 4  | Priya  | Finance    | 70000  |
| 5  | Karan  | IT         | 50000  |
| 6  | Simran | HR         | 45000  |
| 7  | Rohit  | Finance    | 60000  |

## Build Docker Image

```bash
docker build -t employee-pyspark-rdd .
```

## Run Docker Container

```bash
docker run --rm employee-pyspark-rdd
```

## Output

* Sorted employee list by salary
* Department-wise salary totals
* Top 3 highest-paid employees saved to output/top_3_employees.txt

## Screenshot
