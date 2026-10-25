# 🩸 Blood Donor Finder

A simple beginner-friendly project that helps people find potential blood donors based on blood group and location.

## About the project

The project has two versions that work together:

- **Python (command line):** `blood_donor.py`
- **Web page (browser):** `blood_donor.html`

## Features

- Register as a donor (name, blood group, age, weight, city, contact number)
- Eligibility check: age 18-65, weight at least 50 kg, no donation in the last 3 months
- Search for donors by blood group, using blood group compatibility (for example, O- can donate to many groups)
- Donors in the same city are shown first
- Donors are saved in `donors.csv`

## Files

| File | What it does |
|------|--------------|
| `blood_donor.py` | Command-line app (menu: Need Blood, Donate Blood, Exit) |
| `blood_donor.html` | Web version. Open it in any browser |
| `donors.csv` | Donor data (no header). Columns: name, blood group, city, contact |

## How to run

**Python version**

1. Install Python 3 from python.org
2. Download or clone this repository:
   `git clone https://github.com/shibanghiroy-debug/blood-donor-finder.git`
3. Open a terminal in the project folder and run:
   `python blood_donor.py`

**Web version**

1. Double-click `blood_donor.html` to open it in a browser
2. On the **All Donors** tab, click **Import donors.csv** to load the sample donors

> Note: The web version saves donors in your browser. Use **Export** to download a `donors.csv` that the Python program can use.

## Blood group compatibility

| Patient needs | Can receive from |
|---------------|------------------|
| A+ | A+, A-, O+, O- |
| A- | A-, O- |
| B+ | B+, B-, O+, O- |
| B- | B-, O- |
| AB+ | All groups |
| AB- | A-, B-, AB-, O- |
| O+ | O+, O- |
| O- | O- |

## Disclaimer

This is a student project made for learning. The eligibility rules are simple examples and are not medical advice. For real donations, please contact a hospital or blood bank.

## 🌐 Live demo

Try the web version here: [Blood Donor Finder (live)](https://shibanghiroy-debug.github.io/blood-donor-finder/blood_donor.html)

## Team

Made for a hackathon by: *Anshika Rathi, Shreya Kandlwal, Shibanghi Roy, Deeksha Grover*
