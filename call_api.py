import requests

def send_api_request(query):
    url = f"http://209.38.83.187/sent_query/{query}"
    response = requests.post(url)

    if response.status_code == 200:
        # Download the file
        #with open("report.md", 'wb') as f:
         #   f.write(response.content)
        #print("File downloaded successfully!")
        return response.content
    else:
        return (" api failed to respond , TRY AGAIN")

# Example usage with query "list all tables"
#query = "list%20all%20tables"
#send_api_request(query)