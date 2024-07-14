# carsome-webscraping

This project scrapes data from [www.carsome.my/buy_car](https://www.carsome.my/buy-car) website and saves the results in a CSV file.

## Runtime Environment

- **Python Version**: 3.10
- **Docker Image**: python:3.10-slim

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/EVARYNKUMT/carsome-webscrap-docker.git
   ```
2. Build and run docker
   ```sh
   docker build -t carsomewebscraping .
   docker run -d -p 4000:80 carsomewebscraping
   ```
   
## Usage

1. Run the application
   ```sh
   python scrap.py
   ```
## Example Output File

After running the script, an output file named `carsome_buycar_[YYYYmmddHHMM].csv` will be generated in the /app directory of the project. This file contains the scraped data in a structured format.

### File Format Details

- **Format**: CSV (Comma-Separated Values)
- **Separator**: `|` (pipe)
- **Fields Enclosed By**: `"` (double quotes)

### Example Content

Here is an example of the content you might find in `carsome_buycar_202407140317.csv`:

```plaintext
"car_name"|"car_mileage"|"car_transmission"|"car_location"|"car_price"|"car_instalment_mth_amt"
"2015 Mercedes-Benz A2001.6"|"92,635 km"|"Automatic"|"Selangor"|"83,500"|"RM 915/mo"
"2010 Volkswagen Golf GTi 2.0"|"174,632 km"|"Automatic"|"Selangor"|"47,500"|"RM 521/mo"
"2017 Honda Jazz E i-VTEC 1.5"|"118,070 km"|"Automatic"|"Negeri Sembilan"|"47,800"|"RM 524/mo"
```
## Contact

Evaryn K.
evaryn.kumt@gmail.com

Project Link: https://github.com/EVARYNKUMT/carsome-webscraping


## Data Use License

This project includes functionality for web scraping. The data obtained through web scraping is owned by the respective website owners and is subject to their terms of use. Users of this software are responsible for ensuring that their use of the scraped data complies with the website's terms of service and applicable laws.
