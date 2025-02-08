import requests
from bs4 import BeautifulSoup
import json

# List of sections to scrape
sections = ["A", "B", "C", "D", "E", "F", "G", "H", "I","J","K", "L", "M", "N","O", "P", "Q","R", "S", "T","U","V", "W","X","Y","Z"]

# Base URL of the Wikipedia page
base_url = "https://en.wikipedia.org/wiki/List_of_places_in_New_York:_"

# List to store all the scraped data
all_places = []

# Loop through each section
for section in sections:
    url = f"{base_url}{section}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the data
    table = soup.find("table", {"class": "wikitable"})
    if not table:
        print(f"No table found for section {section}")
        continue

    # Extract the rows of the table
    rows = table.find_all("tr")

    # Loop through the rows and extract data
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all("td")
        if len(cols) == 5:
            place_name = cols[0].get_text(strip=True)
            number_of_counties = cols[1].get_text(strip=True)
            counties = cols[2].get_text(strip=True)
            lower_zip = cols[3].get_text(strip=True)
            upper_zip = cols[4].get_text(strip=True)
            
            # Add the data to the list
            all_places.append({
                "Name of Place": place_name,
                "Number of Counties": number_of_counties,
                "Counties": counties,
                "Lower Zip Code": lower_zip,
                "Upper Zip Code": upper_zip
            })

# Save the data to a JSON file
output_file = "florida_places.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(all_places, file, ensure_ascii=False, indent=4)

print(f"Data has been saved to '{output_file}'")


