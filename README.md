# MIS203 Basic Programming
Week 1
* **Name:** Uğur Eren Yeter
* **Student Number:** 2404109017
* **Department:** Management Information Systems
* **Course Name:** MIS203 Basic Programming

---

### AI Usage Note
* **AI Tool Used:** Gemini
* **Prompt Used:** "Create a simple Python program that asks the user for Name, Department, Age, and Career Goal, then prints a formatted Student Profile."
* **What did you change?:** I verified the user input formatting and adjusted the output layout to cleanly present the student profile details.

Week 2
**AI Tool Used**: Gemini-
**Prompt Used**:"Write a Python program named grade_calculator.py using an infinite while True loop that asks for student names and scores, handles invalid scores with continue, calculates letter grades, exits with break when 'q' is entered, and displays the total student count and average score rounded to two decimal places."-
**What did you change?:** I adjusted the input formatting, added comments to explain each block of logic, and ensured the conditional checks matched the exact grading criteria.- 
**What does break do in your program?:** The `break` statement exits the infinite `while True` loop immediately when the user enters 'q' as the student name.


##**week 3**
- **AI Tool Used:** Gemini
- **Prompt Used:** "Write a Python program named ticket_office.py that sells cinema tickets in a continuous loop until the user types 'q' or 'Q' to quit. Ask for customer name, age, day, and student status with input validation using continue statements. Apply pricing based on weekday/weekend and strictly ordered discount rules (Free <6, Senior >=65, Child 6-12, Student <=25, Standard). Format output with 2 decimal places and output summary statistics upon termination."
- **What did you change?:** I adjusted the prompt strings to match the exact spacing required by the specification and added case handling with `.lower()` and `.strip()` for user inputs.
- **Tests:**
  1. Input: Name="Can", Age=5, Day="weekend", Student="no" -> Result: `Can: 0.00 TRY (Free)` (Boundary test for age under 6)
  2. Input: Name="Deniz", Age=12, Day="weekday", Student="no" -> Result: `Deniz: 120.00 TRY (Child)` (Boundary test for age 12 upper limit)
  3. Input: Name="Mert", Age=26, Day="weekday", Student="yes" -> Result: `Mert: 200.00 TRY (Standard)` (Boundary test for student age over 25)
- **Why does the order of the rules matter?:** The order matters because Python evaluates `if / elif` statements sequentially and stops at the first matching condition. If the Student rule were placed before the Child rule, a 10-year-old student would receive a 30% discount instead of the higher 40% Child discount.

**Week 4**
*AI Tool Used*: Gemini

*Prompt Used*: "Write a Python program named carbon_tracker.py that calculates an eco-friendly sustainability score based on user commute habits and recycling practices. Import and use the datetime and random libraries. The program should ask for the user's name, format and display the current date and time using strftime, evaluate user inputs using conditional statements, output a total score out of 60 with customized feedback, and provide a daily random sustainability tip using random.choice()."

*What did you change?*: I structured the code into clean, modular functions (show_welcome_message, calculate_score, get_random_tip, and main), added robust input handling for invalid choices, and ensured clean output formatting.

*Tests:*

Input: Name="Uğur", Commute="1" (Public Transport), Recycling="1" (Definitely yes) -> Result: Score: 60 / 60 (Congratulations! You are a true eco-friendly individual.)

Input: Name="Eren", Commute="2" (Private Car), Recycling="3" (No) -> Result: Score: 15 / 60 (Time to pay a bit more attention to our daily habits!)

Input: Commute="invalid" -> Result: "Invalid choice! No points added for this question." (Ensured program handles incorrect inputs gracefully without crashing).

*Why does the order of the score evaluation rules matter?*: The order matters because Python evaluates if-elif statements sequentially from top to bottom and stops at the first condition that evaluates to true. Checking the highest score threshold first ensures that high scorers are correctly categorized before lower bounds are checked.