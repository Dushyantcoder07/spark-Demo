# Sales Data Analysis Using PySpark DataFrame

## Project Description

This project demonstrates how to use PySpark DataFrames to process sales data from a CSV file. The application is containerized using Docker and executes automatically when the container starts.

## Dataset

The dataset contains product sales information with the following columns:

* product_id
* product_name
* category
* sales

## Operations Performed

1. Read the CSV file into a PySpark DataFrame.
2. Sort all products by sales in descending order.
3. Display the top 3 products with the highest sales.
4. Filter products with sales greater than 80,000.
5. Save the filtered results as a CSV file.

## Technologies Used

* Python 3.12
* PySpark
* Docker
* Java (JDK)

## Project Structure

sales-dataframe-app/

├── app.py

├── sales.csv

├── requirements.txt

├── Dockerfile

├── README.md

├── screenshot.png

└── output/

    └── high_sales_products/

## Build Docker Image

```bash
docker build -t sales-dataframe-app .
```

## Run Docker Container

```bash
docker run --rm sales-dataframe-app
```

## Expected Output

* Products sorted by sales in descending order.
* Top 3 highest-selling products.
* Products with sales greater than 80,000.
* Filtered data saved to the output folder.

## Screenshot

Add the terminal output screenshot below.

![Application Output](Screenshot%20(207).png)

## Author

Dushyant Sisodiya
