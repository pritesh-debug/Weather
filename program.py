#Install package
#pip install wwo-hist
#pip install google-cloud-storage

#Import Package
from wwo_hist import retrieve_hist_data
from pprint import pprint
from google.cloud import storage

#hours 1 hourly, 3 hourly or 24 hourly (day average)
frequency=24

#1 week's data
start_date = '03-MAY-2021'
end_date = '10-MAY-2021'

#API key from https://www.worldweatheronline.com/developer/api/
api_key = '8901689f949343adbe8213100211205'

#Location
location_list = ['california','detroit']

#location_label- If true, all column names will have city name as prefix
#export_csv - If false, no csv file will be exported to current directory.
#store_df - If true, retrieved dataframe(s) will be stored as list in the work space.

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)


#Service Account key for GCS authentication 
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'keys1.json'

#Upload from local to GCS
#Bucket Name: weatherdata_de_ca1
#2 Csv: detroit.csv,california.csv
storage_client = storage.Client()
def upload_to_bucket(blob_name, file_path, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    return blob

upload_to_bucket('Detroit', 'detroit.csv', 'weatherdata_de_ca1')
upload_to_bucket('California', 'california.csv', 'weatherdata_de_ca1')