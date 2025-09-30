# Personal Wellbeing Dashboard

A lightweight Python app to log daily wellbeing metrics — date, mood, sleep hours, weather, and notes — with data stored in CSV format. This project is designed as a personal tracking tool and also serves as a simple example of building a custom dashboard application.

## Features
- Quick entry for daily logs (date, mood, sleep hours, weather, notes)  
- Saves data to `data/wellbeing.csv` (private, ignored by GitHub)  
- Includes a `data/sample_wellbeing.csv` file with example entries for demonstration  
- Easy to extend or adapt for personal use  

## Data Format
The app expects a CSV with the following columns:

- `date` — in YYYY-MM-DD format  
- `mood` — integer (1 to 5 scale)  
- `sleep_hours` — float value for hours slept  
- `weather` — one of: sunny, cloudy, rainy, snowy, extreme hot, extreme cold  
- `notes` — free text  

See [`data/sample_wellbeing.csv`](data/sample_wellbeing.csv) for a working example.

## Getting Started
1. Install Python 3.10+  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
