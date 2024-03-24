ClubCal

# Features

- Google Sheets Integration: Pulls data from a Google Sheet at every app launch, ensuring your schedule is always current.
- Data Parsing: Sophisticated parsing system organizes events by date and handles empty cells intelligently.
- Interactive Calendar: A Tkinter-based graphical user interface that allows for easy viewing and editing of your schedule.
- Local Data Storage: Merges online updates with local notes, providing a personalized scheduling experience.

# Setup Instructions

Clone the Repository:

git clone <https://github.com/yourusername/ClubCal.git>

Install Dependencies:

Navigate to the ClubCal directory and install the required Python packages:

pip install -r requirements.txt

Google Sheets API Setup:

Follow the steps here (<https://developers.google.com/sheets/api/quickstart/python>) to enable the Sheets API and download your credentials.json file into the ClubCal folder.

Running ClubCal:

With the dependencies installed and the Sheets API set up, you can now run ClubCal:

python clubcal.py

# Usage

Upon launching ClubCal, enter the ID of the Google Sheet you wish to integrate with. The app will display your schedule in an interactive calendar. You can add personal notes to any date, which are saved locally and displayed alongside your Google Sheets data.

# Dependencies

- Python 3.x
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- Tkinter

ClubCal is a testament to what can be achieved when technology is applied to solve real-life challenges. We hope this tool helps you manage your time more effectively and brings a new level of organization to your daily life.
