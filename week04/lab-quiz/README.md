# Week 4 Lab - Savings Goal Planner (`lab04_savings_planner.py`)

This script simulates a monthly savings plan with interest calculations, input validations, and a capped 60-month simulation loop.

## Test Run
* **Input:** 
  * Starting balance: `1000`
  * Monthly deposit: `500`
  * Monthly interest rate (%): `1`
  * Savings goal: `3000`
* **Result:** Reached the goal in **4 months** with a final balance of **3070.80** and a total interest of **70.80**.

## What Was Changed After Testing
* Initially, the simulation loop printed table rows even if the starting balance already met or exceeded the goal. 
* **Change Made:** Added a conditional check right at the beginning (`if balance >= goal:`) to immediately output the success message and skip printing empty table rows when the starting balance is already sufficient.
