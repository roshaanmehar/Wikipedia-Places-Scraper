# New York Places Scraper

## Table of Contents
- [Project Description](#project-description)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Installation Guide](#installation-guide)
- [Usage Instructions](#usage-instructions)
- [Customization Options](#customization-options)
- [Data Considerations](#data-considerations)
- [Future Roadmap](#future-roadmap)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Disclaimer](#disclaimer)

---

## Project Description

This project is a web scraping tool designed to extract information about places in New York from Wikipedia. The script systematically scrapes different alphabetical sections and extracts detailed data, including the number of counties, associated county names, and ZIP code ranges.

I developed this script as a supplementary tool for my primary data scraper, with the goal of enhancing data integrity and completeness. One of the challenges I faced was ensuring that no valuable data points were left uncollected.
Through research, I discovered that geographical divisions in the United States, while loosely defined, often rely on "places" as identifiable locations. Unlike postal codes, which are standardized by the postal service but offer limited coverage, "places" can be more reliably recognized and mapped using resources like Google Maps.
By leveraging a comprehensive list of places for each state, I could significantly reduce the chances of missing any data. Although this approach introduces some redundancy (up to 98% overlap), it ensures that all possible leads are accounted for.
This script generates a JSON file containing a detailed list of all places in a given state, serving as a valuable resource for more thorough and efficient data scraping.
---

## Key Features

- Scrapes structured data from Wikipedia pages by section.
- Extracts information such as place names, number of counties, county names, and ZIP codes.
- Saves the extracted data into a JSON file for further use or analysis.
- Automatically handles multiple alphabetical sections of Wikipedia.

---

## Technologies Used

- **Python**: Core programming language.
- **BeautifulSoup**: For parsing HTML and web scraping.
- **Requests**: For making HTTP requests to fetch web pages.
- **JSON**: For structured data storage.

---
### This is the Wikipedia Page in question to be scraped:
<div>
   <img src="https://github.com/roshaanmehar/Wikipedia-Places-Scraper/blob/main/websitescreenshot1.png" width="500">
<img src="https://github.com/roshaanmehar/Wikipedia-Places-Scraper/blob/main/websitescreenshot2.png" width="500">
   </div>

   
## Installation Guide

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Create a `requirements.txt` file containing the dependencies `requests` and `beautifulsoup4`.)*

---

## Usage Instructions

1. Run the script using:
   ```bash
   python scrape_places.py
   ```
2. The script will automatically loop through all alphabetical sections and scrape the required data.
3. After completion, the data will be saved in `florida_places.json`.

---

## If the code ran without any problems the output on the terminal should look something like this:
<img src="https://github.com/roshaanmehar/Wikipedia-Places-Scraper/blob/main/terminaloutput.png" width="500">
- No table found for X means that, there were no places in New York, whose name started with the letter X.

## Customization Options

To customize the scraping process:
- **Sections to Scrape:** Modify the `sections` list in the script to target specific alphabetical sections.
- **Target URL:** Update the `base_url` to point to a different state's Wikipedia page if necessary.
- **Output File:** Change the `output_file` variable to store the data in a custom file location.

---

## Data Considerations

- The script relies on Wikipedia's consistent table structure for accurate data extraction. Any changes to the page layout may require updates to the parsing logic.
- Data extracted includes:
  - Place Name
  - Number of Counties
  - County Names
  - Lower and Upper ZIP Codes
  
Ensure the target Wikipedia page is accessible and formatted as expected before running the script.

## The output data should look something like this:
<img src="https://github.com/roshaanmehar/Wikipedia-Places-Scraper/blob/main/samplecode.png" width="500">


---

## Future Roadmap

- Add support for dynamic identification of table structure.
- Implement error handling for incomplete or malformed data rows.
- Include logging for better script monitoring.
- Expand scraping to other states.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests on the GitHub repository.

---

## Acknowledgements

- [Wikipedia](https://en.wikipedia.org) for providing detailed place information.
- The developers and contributors of `BeautifulSoup` and `Requests`.

---

## Disclaimer

This project is for educational and informational purposes only. Please ensure compliance with Wikipedia's terms of service and scraping policies.

