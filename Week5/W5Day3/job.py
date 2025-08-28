import requests
import json

# Replace with your Adzuna credentials
APP_ID = "d461f071"
APP_KEY = "de399d2305d9102cb5356bb5dbc7aa13	"

# API endpoint (this example uses GB - United Kingdom, you can change to 'us', 'in', etc.)
url = f"https://api.adzuna.com/v1/api/jobs/gb/search/1"

# Parameters (you can filter by keyword, location, etc.)
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 5,     # number of results per page
    "what": "python developer", # job keyword
    "where": "london",          # location
    "content-type": "application/json"
}

# Make request
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Print jobs nicely
    for i, job in enumerate(data.get("results", []), start=1):
        print(f"\n🔹 Job {i}")
        print(f"Title: {job.get('title')}")
        print(f"Company: {job.get('company', {}).get('display_name')}")
        print(f"Location: {job.get('location', {}).get('display_name')}")
        print(f"Salary: {job.get('salary_min')} - {job.get('salary_max')}")
        print(f"URL: {job.get('redirect_url')}")

    # Save to JSON file
    with open("adzuna_jobs.json", "w") as f:
        json.dump(data, f, indent=2)

    print("\n📂 Jobs saved to adzuna_jobs.json")
else:
    print("❌ Error:", response.status_code, response.text)
