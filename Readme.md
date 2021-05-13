Get weather for your city (or any US city of your choice), as well as weather from Detroit, Michigan, every day for 1 week have it load to S3/Google Cloud Storage (GCS) 
location.

Location Selected: Detroit and California
API Used: https://www.worldweatheronline.com/developer/api/
Time: 3rd May - 10th May 2021
Technologies: Python, Google Cloud storage(GCS) and Bigquery

GCS is publicly accessible and stored in CSV format (Allusers, AuthenticatedUsers): 
Bucket(https://console.cloud.google.com/storage/browser/weatherdata_de_ca1)
Direct data download link from GCS bucket: 
California Data: https://storage.googleapis.com/weatherdata_de_ca1/California
Detroit Data: https://storage.googleapis.com/weatherdata_de_ca1/Detroit

Command to load CSV from GCS to Bigquery:
bq load --allow_quoted_newlines --allow_jagged_rows --skip_leading_rows=1 --field_delimiter=',' gothic-avenue-275113:WeatherData.weather_daily_table gs://weatherdata_de_ca1/Detroit
        
bq load --allow_quoted_newlines --allow_jagged_rows --skip_leading_rows=1 --field_delimiter=',' gothic-avenue-275113:WeatherData.weather_daily_table gs://weatherdata_de_ca1/California

Insert command in Google Bigquery:
CREATE TABLE WeatherData.weather_daily_table (
	date_time STRING
	,maxtempC INT64
	,mintempC INT64
	,totalSnow_cm FLOAT64
	,sunHour FLOAT64
	,uvIndex INT64
	,moon_illumination INT64
	,moonrise STRING
	,moonset STRING
	,sunrise STRING
	,sunset STRING
	,DewPointC INT64
	,FeelsLikeC INT64
	,HeatIndexC INT64
	,WindChillC INT64
	,WindGustKmph INT64
	,cloudcover INT64
	,humidity INT64
	,precipMM FLOAT64
	,pressure INT64
	,tempC INT64
	,visibility INT64
	,winddirDegree INT64
	,windspeedKmph INT64
	,location STRING
	)

Query Executed and Tested: 
SELECT * FROM `gothic-avenue-275113.WeatherData.weather_daily_table2`
ORDER BY date_time,location


Publish the data to Tableau public:
https://public.tableau.com/profile/pritesh6361#!/vizhome/WeatherObservation/Dashboard1?publish=yes

