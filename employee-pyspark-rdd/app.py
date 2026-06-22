from pyspark.sql import SparkSession
import os

spark = SparkSession.builder \
    .appName("EmployeeRDDProject") \
    .getOrCreate()

sc = spark.sparkContext

# Read CSV as RDD
rdd = sc.textFile("employee.csv")

header = rdd.first()

employees = rdd.filter(lambda row: row != header) \
               .map(lambda row: row.split(","))

print("\n========== SORT BY SALARY DESC ==========\n")

sorted_employees = employees.sortBy(
    lambda x: int(x[3]),
    ascending=False
)

for emp in sorted_employees.collect():
    print(emp)

print("\n========== DEPARTMENT TOTAL SALARY ==========\n")

department_salary = employees.map(
    lambda x: (x[2], int(x[3]))
).reduceByKey(
    lambda a, b: a + b
)

for dept in department_salary.collect():
    print(dept)

print("\n========== TOP 3 HIGHEST PAID EMPLOYEES ==========\n")

top3 = sorted_employees.take(3)

for emp in top3:
    print(emp)

os.makedirs("output", exist_ok=True)

with open("output/top3_employees.txt", "w") as file:
    for emp in top3:
        file.write(",".join(emp) + "\n")

print("\nTop 3 employees saved successfully!")

spark.stop()