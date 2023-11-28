# Promotheus Assignment

1. Export the metrics (like request per second, memory usage, cpu usage etc) in the existing mini project given to Interns

2. Install Prometheus and Grafana using Docker (with docker-compose)

3. Configure prometheus (scrape configs) such way that it can scrape the metrics from default metric path of the application job

4. Validate the entire configuration to check if the data is coming or not in Prometheus UI

5. Create the Dashboards in Grafana on top of the metrics exported by adding the Prometheus as a Datasource.



# Setting up Prometheus and Grafana with Docker for Flask Application Metrics
This guide will walk you through the process of exporting metrics from a Flask application using Prometheus and visualizing them in Grafana. The Flask application includes basic metrics such as request per second and CPU usage.

# Prerequisites
<ul><li>Docker installed on your machine</li></ul>

# Steps

<h3><b>Step 1: Create Flask Application</b></h3>
Create a Flask application with metrics instrumentation. Create app.py file and add the python code into that file

<h3><b>Step 2: Create Docker Compose File</b></h3>
Create a docker-compose.yml file in the project directory.

<h3><b>Step 3: Create Prometheus Configuration</b></h3
Create a prometheus.yml file in the project directory

<h3><b>Step 4: Build and Run the Containers</b></h3>
Run the following command to build and start the Docker containers:<br><br>


`$docker-compose up --build`


<h3><b>Step 5: Access Prometheus UI</b></h3>
Open your browser and navigate to http://localhost:9090 to access the Prometheus UI. Verify that metrics are being scraped from the Flask application. Check the "Targets" page to ensure that your application is successfully scraping metrics.

<h3><b>Step 6: Access Grafana UI</b></h3>
Access Grafana UI at http://localhost:3000 (login with admin/admin). Add Prometheus as a data source:

<ul><li>Go to "Configuration" > "Data Sources" > "Add your first data source".</li>
<li>Choose Prometheus and set the URL to http://prometheus:9090.</li></ul>

<b>Create Grafana Dashboards:</b>
<ul><li>Go to "Create" > "Dashboard".</li>
<li>Add a new panel, choose Prometheus as the data source, and use queries to visualize your metrics.</li></ul>

<h3><b>Step 7: Select and Run Queries</b></h3>
<b><ul><li>Query for Total Requests</li></ul></b>
<ol><li>Under the "Metric" field, start typing 'flask_requests_total'.</li>
<li>Grafana will provide suggestions; select 'flask_requests_total'.</li></ol>

<b><ul><li>Query for CPU Usage</li></ul></b>
<ol><li>Under the "Metric" field, start typing 'flask_cpu_usage_percent'.</li>
<li>Select flask_cpu_usage_percent.</li></ol>

Click "Apply" to see the visualization on the dashboard.

# Screenshots

<b><ul><li>Prometheus Targets Page: Overview of Monitored Targets</li></ul></b>

![image](https://github.com/kshrikant7/Prometheus_Assignment/assets/65910406/5f170ac6-77d0-4e69-8b7b-60862ff9b7b8)

<br>
<b><ul><li>Dashboard in Grafana: Visualizing Flask Application Metrics</li></ul></b>
1. flask_cpu_usage_percentage

<br>![image](https://github.com/kshrikant7/Prometheus_Assignment/assets/65910406/2f8d168e-3b20-4825-9447-06e4c2311af1)

<br>
2. process_cpu_seconds_total

<br>![image](https://github.com/kshrikant7/Prometheus_Assignment/assets/65910406/6d94f2e5-6ab1-4604-babf-df803b5b5958)

<b><ul><li>Metrics</li></ul>
![image](https://github.com/kshrikant7/Prometheus_Assignment/assets/65910406/5b53553f-4f0c-4011-965b-70ff5a141bd2)


