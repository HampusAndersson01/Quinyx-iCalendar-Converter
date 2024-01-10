# Quinyx Schedule to iCalendar Converter

This Python script fetches your work schedule from Quinyx API and creates an iCalendar file (.ics) for easy integration with your calendar applications.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hampusandersson01/quinyx-icalendar-converter.git
    ```

2. Navigate to the project directory:

    ```bash
    cd quinyx-icalendar-converter
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script with the following command:

```bash
python main.py <year> <bearer_token>
```

Replace `<year>` with the desired year (e.g., 2024) and `<bearer_token>` with your actual Quinyx bearer token.

### How to obtain the bearer token

1. Log in to your Quinyx account.
2. Open the Developer Tools in your browser.
3. Go to the "Network" tab.
4. Refresh the page.
5. Look for the API request related to your schedule (URL contains "shift?").
6. In the request headers, find the "Authorization" field. Copy the value after "Bearer ".

Example:

```bash
python main.py 2024 {bearer token}
```

This will fetch your work schedule from Quinyx for the specified year and generate an iCalendar file named `work_schedule_<year>_{bearer_token[:8]}.ics`.
