# Simulated Device Monitoring and Alert System
 
**Student Name:** Renz Rey R. Guillen
**Student Number:**  2601346
**Section:** 1CPE-B
 
## Project Description
The Simulated Device Monitoring and Alert System is a terminal-based program in the Python language that monitors, classifies and analyzes CPU core temperature metrics in real-time. Users can interactively control the readings, set hardware workload state according to determined thermal thresholds and also calculate statistical analysis summaries to maintain the stability of the system.

## Features
- View all stored temperature readings with indexed unit labels.
- Add a new reading (whole numbers from 0 to 100 only).
- Classify every reading automatically into operational tiers (NORMAL, WARNING, CRITICAL).
- Generate a numerical summary and overall status.
- Reject invalid menu choices and invalid readings.

## Requirements
- Python 3
 
## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: `python device_monitor.py`  
   *(On macOS or Linux, type: `python3 device_monitor.py`)*
 
## Sample Output
```text
CPU CORE MONITORING SYSTEM

[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 1

CURRENT READINGS
----------------
Reading 1: 30 °C
Reading 2: 28 °C
Reading 3: 35 °C
Reading 4: 40 °C
Reading 5: 60 °C
 ```

## Test Cases
I performed 14 tests. 14 passed and 0 failed. 
Full details are in test_cases.md..

## Known Limitations
-Readings are held entirely in volatile RAM memory loops and wipe cleanly when the instance terminates.

-The application processes integer numeric entries only and rejects floating-point/decimal temperature data points.

## Reflection
This activity has helped me to learn how to use python to create reliable console applications. Triggered good input validation is the lesson learned here: how to deal with non-standard inputs and boundary cases before the program errors. Moreover, by using the separate functions, the logic was much easier to code, the calculations much easier, and it was much easier to be sure that all test cases would be executed successfully.