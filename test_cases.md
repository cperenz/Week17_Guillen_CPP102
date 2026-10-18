# Software Test Specification & Execution Report

**System under Test:** CPU Core / Device Monitoring and Alert System  
**Tester:** Renz Rey Guillen
**Date:** October 18, 2026  
**Status:** PASS (14/14 Passed)

---

## Test Results

| TC | Action / Input | Expected Result | Actual Result | Pass/Fail |
|:---|:---|:---|:---|:---:|
| **TC01** | Choose 1 | Five readings: 30, 28, 35, 40, 60 | Displayed 5 readings correctly. | Pass |
| **TC02** | Choose 2, enter `33` | Reading added successfully | Reading added successfully | Pass |
| **TC03** | Choose 2, enter `abc` | Invalid input. Enter a whole number only. | Invalid input message shown | Pass |
| **TC04** | Choose 2, enter `-5` | Invalid reading. Value from 0 to 100. | Invalid reading message shown | Pass |
| **TC05** | Choose 2, enter `101` | Invalid reading. Value from 0 to 100. | Invalid reading message shown | Pass |
| **TC06** | Choose 2, enter `0` | Reading added successfully | Reading added successfully | Pass |
| **TC07** | Choose 2, press `[Enter]` | Invalid input. Reading cannot be empty. | Empty check message shown | Pass |
| **TC08** | Choose 3 | Classify 30, 28, 35, 40 (NORMAL), 60 (WARNING) | Classification correct | Pass |
| **TC09** | Choose 4 | Display monitoring summary | Summary displayed correctly | Pass |
| **TC10** | Choose 5 | Display thank-you message and exit | Program exited gracefully | Pass |
| **TC11** | Choose 6 at menu | Invalid choice. Enter 1 to 5. | Invalid choice message shown | Pass |
| **TC12** | Choose 2, enter `59` | Reading added; classified as WARNING | Reading added successfully | Pass |
| **TC13** | Choose 2, enter `80` | Reading added; classified as CRITICAL | Reading added successfully | Pass |
| **TC14** | Choose 2, enter `-` | Invalid input. Enter a whole number only. | Invalid input message shown | Pass |

---

## Defect Analysis & Fixes

### Hardest Test Case Encountered: TC14 (Standalone Sign `-`)
* **Issue:** Entering a single hyphen (`-`) bypassed string length checks in the loop-based validation, causing the program to crash with an uncaught `ValueError: invalid literal for int()`.
* **Solution:** Simplified the validation logic by using Python's built-in `text.isdigit()` check, ensuring that only non-empty, positive digit inputs pass through before parsing.