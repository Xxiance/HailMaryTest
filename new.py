import requests
import time

def cycle_through_apod_pictures(start_yymmdd, end_yymmdd, api_key="DEMO_KEY"):
    # Base URL for the new WordPress APOD API
    url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
    
    # Pass your API key and date range parameters
    params = {
        "api_key": api_key,
        "date_from": start_yymmdd,
        "date_to": end_yymmdd
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        picture_list = response.json()
        
        if not picture_list:
            print("No pictures found for this date range.")
            return

        print(f"--- Found {len(picture_list)} pictures. Cycling through them... ---\n")
        
        for i, apod_data in enumerate(picture_list, 1):
            print(f"[{i}/{len(picture_list)}] ----------------------------------------")
            print(f"Title: {apod_data.get('title')}")
            print(f"Date: {apod_data.get('date')}")
            print(f"Image URL: {apod_data.get('hdurl') or apod_data.get('url')}")
            print(f"Explanation: {apod_data.get('explanation')}\n")
            
            time.sleep(3)
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Insert your actual NASA API key here
    MY_API_KEY = "7j8NR8CJdjBgjrQTrCFQMcNmmQD7rh8rd9qzJfPG"
    
    # Format: YYMMDD
    cycle_through_apod_pictures(
        start_yymmdd="070122", 
        end_yymmdd="070122", 
        api_key=MY_API_KEY
    )