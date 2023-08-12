# Stream Processing: Near real-time data pipeline analyzing user's logs from a recruitment platform

## Introduction
A recruitment platform deals with massive amount of user's interaction logs daily, the company is interested in finding insights from candidates activities for their buisiness development. This project is born to handle that in a near real-time manner.

### Technology used
- Pyspark
- Kafka
- Airflow
- Grafana
- Docker
- Python

## Architecture
![image](https://github.com/Thang285/A_near_realtime_data_pipeline_analyzing_log_from_an_recruitment_plaform/assets/116457922/b07af45b-514f-4ed9-9276-a5cb849a6ea7)

### Log data
Raw log data from webites is stored in Cassandra then processed with Spark. Processed data is finalized with data from MySQL and would be stored in MySQL. After that, Grafana would take data from MySQL to generate dashboards
Initially, Log data contains:
```sh
.
root
 |-- create_time: string (nullable = false)
 |-- bid: integer (nullable = true)
 |-- bn: string (nullable = true)
 |-- campaign_id: integer (nullable = true)
 |-- cd: integer (nullable = true)
 |-- custom_track: string (nullable = true)
 |-- de: string (nullable = true)
 |-- dl: string (nullable = true)
 |-- dt: string (nullable = true)
 |-- ed: string (nullable = true)
 |-- ev: integer (nullable = true)
 |-- group_id: integer (nullable = true)
 |-- id: string (nullable = true)
 |-- job_id: integer (nullable = true)
 |-- md: string (nullable = true)
 |-- publisher_id: integer (nullable = true)
 |-- rl: string (nullable = true)
 |-- sr: string (nullable = true)
 |-- ts: string (nullable = true)
 |-- tz: integer (nullable = true)
 |-- ua: string (nullable = true)
 |-- uid: string (nullable = true)
 |-- utm_campaign: string (nullable = true)
 |-- utm_content: string (nullable = true)
 |-- utm_medium: string (nullable = true)
 |-- utm_source: string (nullable = true)
 |-- utm_term: string (nullable = true)
 |-- v: integer (nullable = true)
 |-- vp: string (nullable = true)
```
### Processing data 
- Scrutinize log data and select useful information such as ```["create_time"]``` , ```["bid"]```, ```["custom_track"]```, ```["campaign_id"]```, ```["job_id"]```, ```["publisher_id"]```, ```["ts"]```
- Replace null values with 0
- Do some basic calculations for further in-dept analysis
- Store processed data into MySQL
- use Airflow to monitor and automate spark job
- 
