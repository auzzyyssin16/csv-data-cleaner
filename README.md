# CSV Data Cleaner
A Python tool that cleans and standardises customer data from a CSV file.

## Features
- Removes duplicate entries based on email
- Formats phone numbers to only digits
- Outputs a clean CSV file

## How to Run
1. Install Python 3
2. Download this repository
3. Add your CSV file or use the included `sample_customers.csv`
4. Open a terminal and run:
python csv_cleaner.py
5. The cleaned CSV will be saved as `cleaned_customers.csv`

## Example
**Before:**
Alice Smith,ALICE@example.com,0400 123 456
Bob Jones,bob@example.com,0400123456
Charlie Lee,charlie@example.com,0400-123-456
Alice Smith,alice@example.com,0400 123 456

**After:**
Alice Smith,alice@example.com,0400123456
Bob Jones,bob@example.com,0400123456
Charlie Lee,charlie@example.com,0400123456
