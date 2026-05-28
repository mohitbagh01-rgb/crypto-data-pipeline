import requests as req


url = "https://www.zebapi.com/api/v1/market"

def get_data(url=url):
    try:
        response = req.get(url)
        
        if response.status_code != 200:
            print("Request failed:", response.status_code)
            return None
        
        data = response.json()
        return data
    
    except Exception as e:
        print("Error occurred:", e)
        return None

    print("data ingested successfully")

