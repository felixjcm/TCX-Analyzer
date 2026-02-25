# TCX Analysis 🏃‍♂️📊

A Python-based tool designed to analyze activity data from TCX files. This project extracts GPS, timing, and heart rate data and enables basic analytics to give a text based dashboard. The basic functionality opens up a plethora of other features like a simple ELO-style rating system and more.

## Features

- **TCX Parsing:** Seamlessly reads Garmin, Polar, or Strava compatible `.tcx` files.
- **Performance Metrics:** Calculates total distance, duration, average heart rate, and speed. (Will be expanded)
- **Runner-Centric Pace:** Automatically converts raw speed into the standard running pace format (min/km).
- **Modular Design:** Separate modules for parsing and analysis for easy scalability.

## Sample Output
------------------------------
RUNNING PERFORMANCE SUMMARY
------------------------------
Distance:  10.02 km
Duration:  52.15 min
Avg HR:    162 bpm
Pace:      5:12 min/km
Speed:     11.53 km/h
------------------------------

## Project Structure

The project is split into three main components:

1. `fun_tcx_parser.py`: Handles XML extraction from the TCX file.
2. `fun_tcx_basic_analysis.py`: Processes the raw data into human-readable metrics.
3. `main.py`: The entry point that ties the logic together.

## Disclaimer

This has nothing to do with sports science. It is a fun project to practice and play around using my own Activity data. A rating system and quantification like this can take away from the enjoyment of exercise and should therefore be used consciously. Please use serious training analysis tools and stay sceptical.
