import pandas as pd
import requests
# Load CSV file
csv_file = "for_dictionary.csv"  # Change to your file path
df = pd.read_csv(csv_file)

# Convert to dictionary (ward_name as key, rest as values in list format)
data_dict = df.set_index("ward_name").T.to_dict("list")

# Print result
tosend = (data_dict['C V Raman Nagar'])


url = "http://0.0.0.0:8000/points"  # Change to your server address

# Define the JSON payload
payload = {
    "a": tosend[0],
    "b": tosend[1],
    "c": tosend[2],
    "d": tosend[3],
    "e": tosend[4],
}


# Set headers for JSON data
headers = {
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

