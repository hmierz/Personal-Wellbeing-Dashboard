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

## License
This project is licensed under the MIT License.  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
