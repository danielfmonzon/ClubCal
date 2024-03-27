# Club Calendar GUI

# Features

- Google Sheets Integration: Pulls data from a Google Sheet at every app launch, ensuring your schedule is always up-to-date.
- Data Parsing: Sophisticated parsing system organizes events by date and handles empty cells intelligently.
- Interactive Calendar: A Tkinter-based graphical user interface that allows for easy viewing of your schedule as well as adding personal notes.
- Local Data Storage: Merges online updates with local notes, providing a personalized scheduling experience.

# Setup (Option 1)

Navigate to the repository page:

<https://github.com/danielfmonzon/ClubCal>

Click Calendar

Click dist

Click GUI.exe

Click "Download raw file"

Run GUI.exe from your downloads

# Setup (Option 2)

Clone the Repository:

git clone <https://github.com/yourusername/ClubCal.git>

Install Dependencies:

Navigate to the ClubCal directory and install the required Python packages:

pip install -r requirements.txt

Google Sheets API Setup:

Enable the Google Drive and Google Sheets APIs by following this guide: <https://www.youtube.com/watch?v=cnPlKLEGR7E>

If you are having issues, follow the steps here (<https://developers.google.com/sheets/api/quickstart/python>) to enable the Sheets API and download your credentials.json file into the ClubCal folder.

Running ClubCal:

With the dependencies installed and the Sheets API set up, you can now run calGUI:

python calGUI.py

# Usage

Upon launching ClubCal, the app will display your schedule in an interactive calendar. You can add personal notes to any date, which are saved locally and displayed alongside your Google Sheets data. Each time you relaunch the app, your calendar's data will be synced up with the sheet again.

# Dependencies

- Python 3.x
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- Tkinter

# Developers and Information

This program was crafted by Daniel Monzon, Sushanth Kumar Vutukuri, and Caleb Oxborough for a Mini-Hack event hosted by UF's Open-Source Club. We had a blast working on this project, and look forward to developing more small apps in a competitive environment in the future!

Demo: <https://www.youtube.com/watch?v=LRFbXm8VAfY>

# Add on LinkedIn

Daniel Monzon:
- <https://www.linkedin.com/in/daniel-monzon15/>

Sushanth Kumar Vutukuri:
- <https://www.linkedin.com/in/sushanth-kumar-vutukuri-999043244/>

Caleb Oxborough:
- <https://www.linkedin.com/in/caleb-oxborough/>
