import sys
import requests
from icalendar import Calendar, Event
from datetime import datetime

def fetch_and_save_schedule(api_url, headers, output_file):
    # Make the API request
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        # Parse the API response
        data = response.json()

        # Create a new iCalendar
        cal = Calendar()

        # Iterate over each schedule entry in the API response
        for schedule_entry in data["schedule"]:
            # Extract relevant information
            start_datetime = datetime.strptime(schedule_entry["startDate"], "%Y-%m-%d %H:%M:%S")
            end_datetime = datetime.strptime(schedule_entry["endDate"], "%Y-%m-%d %H:%M:%S")
            category_name = schedule_entry["categoryName"]
            description = schedule_entry["description"]

            # Create a new event
            event = Event()
            event.add('summary', category_name)
            event.add('dtstart', start_datetime)
            event.add('dtend', end_datetime)
            event.add('description', description)

            # Add the event to the calendar
            cal.add_component(event)

        # Save the calendar to a single file
        with open(output_file, 'wb') as f:
            f.write(cal.to_ical())

        print(f"Work schedule for {start_date} to {end_date} added to '{output_file}' file.")
    else:
        print(f"Failed to retrieve the schedule for {start_date} to {end_date}. Status code: {response.status_code}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <year> <bearer_token>")
        sys.exit(1)

    # Extract the year and bearer token from the command-line arguments
    year = int(sys.argv[1])
    bearer_token = sys.argv[2]

    # Set up the request headers with the bearer token
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    # Define the start and end dates for the specified year
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    # API endpoint URL for the specified year
    api_url = f"https://app.quinyx.com/api/2.0/user/shift?fromDate={start_date}&includeMyShiftsFromSharedUnits=1&shiftType=39&toDate={end_date}&unitIds=9613"

    # Specify the output file with the year and bearer token
    output_file = f'work_schedule_{year}_{bearer_token[:8]}.ics'

    # Call the function to fetch and save the schedule
    fetch_and_save_schedule(api_url, headers, output_file)
