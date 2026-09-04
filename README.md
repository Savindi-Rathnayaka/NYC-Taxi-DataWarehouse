# NYC Taxi Data Warehouse 🚕📊

## 📌 Project Overview

This project develops a **Data Warehouse for NYC Yellow Taxi trip data** for January 2026.

The project follows a **star schema** approach and uses Python for data cleaning and transformation, SQLite for data warehousing, SQL for business analysis, and Matplotlib for data visualization.

The main objective is to transform raw taxi trip data into a structured data warehouse that can be used to identify useful business insights about taxi demand, revenue, pickup locations, payment methods, and travel patterns.

---

## 🎯 Objectives

* Clean and prepare raw NYC taxi trip data
* Handle missing and invalid values
* Transform the data into analytical dimensions and facts
* Build a star-schema-based data warehouse
* Store the warehouse using SQLite
* Perform SQL-based business analysis
* Visualize important taxi travel patterns
* Extract useful business insights from the data

---

## 🗂️ Dataset

**Dataset:** NYC Yellow Taxi Trip Data
**Period:** January 2026

The dataset contains information such as:

* Pickup and drop-off datetime
* Passenger count
* Trip distance
* Pickup and drop-off locations
* Rate code
* Payment type
* Fare amount
* Tip amount
* Total amount
* Airport fee
* Congestion surcharge
* Trip duration

---

## 🏗️ Data Warehouse Design

The data warehouse follows a **star schema** consisting of:

### Fact Table

**`fact_trip`**

Contains individual taxi trip records and measurable business information.

Key attributes include:

* `trip_id`
* `date_key`
* `pickup_location_id`
* `dropoff_location_id`
* `passenger_count`
* `trip_distance`
* `fare_amount`
* `tip_amount`
* `total_amount`
* `trip_duration_minutes`
* `payment_type`

### Dimension Tables

**`dim_date`**

Provides date-related information such as:

* Date
* Year
* Month
* Day
* Day of week
* Month name

**`dim_zone`**

Provides taxi zone information such as:

* Location ID
* Borough
* Zone
* Service zone

---

## 🔄 ETL Process

The project follows an ETL workflow:

### 1. Extract

Raw NYC Yellow Taxi data is loaded from a Parquet file using Pandas.

### 2. Transform

The data is cleaned and transformed by:

* Handling missing values
* Removing duplicate records
* Identifying invalid trip durations
* Creating date and time attributes
* Creating dimension tables
* Creating the fact table
* Generating surrogate-style keys for analytical use

### 3. Load

The transformed data is stored in:

* CSV files
* SQLite database

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **SQL**
* **SQLite**
* **Jupyter Notebook**
* **VS Code**
* **Parquet**

---

## 📊 Data Analysis

SQL queries were used to analyze:

* Total number of taxi trips
* Total revenue
* Average trip distance
* Average trip duration
* Trips by pickup hour
* Top pickup zones
* Trips and revenue by payment type
* Daily revenue

---

## 📈 Visualizations

The project includes visualizations for:

1. **NYC Taxi Trips by Pickup Hour**
2. **Daily NYC Taxi Revenue – January 2026**
3. **Top 10 NYC Taxi Pickup Zones**
4. **NYC Taxi Trips by Payment Type**

These visualizations help identify demand patterns and important business trends.

---

## 💡 Key Insights

The analysis identified several useful patterns:

* **6:00 PM** was the busiest pickup hour.
* **4:00 AM** recorded the lowest number of trips.
* Taxi demand was particularly high during the evening period.
* Certain NYC pickup zones generated significantly higher trip volumes than others.
* Payment methods showed different patterns in terms of trip volume and revenue.
* Daily revenue varied throughout January 2026.

---

## 📁 Project Structure

```text
NYC_Taxi_DataWarehouse/
│
├── data/
│   ├── yellow_tripdata_2026-01.parquet
│   ├── dim_date.csv
│   ├── dim_zone.csv
│   ├── fact_trip.csv
│   └── nyc_taxi_dw.db
│
├── notebooks/
│   └── your_notebook.ipynb
│
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project in VS Code

Open the `NYC_Taxi_DataWarehouse` folder in VS Code.

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib pyarrow
```

### 4. Open the Jupyter Notebook

Navigate to:

```text
notebooks/
```

and open the project notebook.

### 5. Run the notebook

Run the cells in order to perform:

**Data Loading → Data Cleaning → Transformation → Data Warehouse Creation → SQL Analysis → Visualization**

---

## ✅ Project Validation

The final data warehouse was validated by checking:

* Missing values
* Duplicate records
* Fact table record count
* Dimension table record counts
* Date key relationships
* Pickup and drop-off zone relationships
* SQLite database tables

The final warehouse contains approximately **3.68 million cleaned taxi trip records**.

---

## 🏁 Conclusion

The NYC Taxi Data Warehouse successfully transforms raw taxi trip data into a structured analytical data warehouse.

The combination of **Python, SQL, SQLite, and data visualization** provides an effective solution for analyzing taxi demand, revenue, locations, payment methods, and travel behavior.

This project demonstrates practical skills in:

**Data Cleaning → ETL → Data Warehousing → SQL Analysis → Data Visualization**


```
