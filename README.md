# Fetch and Post Countries Script

## Overview
Features:
1. Fetches country data from a GraphQL API.
2. Saves all countries to a CSV file (`countries.csv`).
3. Posts one country's details to a REST API.
4. Handles errors like 403 Forbidden and 500 Internal Server Error.

## Requirements
- Python 3.x (3.11.9 has been used)
- `requests` module

## Installation
Install dependencies:


## Error Handling
- **403 Forbidden:** Logs the error and skips the request.
- **500 Internal Server Error:** Retries with exponential backoff (2s, 4s, 8s, etc.).


## Usage
Run the script:
```python integration.py```
