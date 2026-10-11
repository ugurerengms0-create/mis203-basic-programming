# Lab 03 - Order Approval System

## Test Boundary Cases Table (Stretch Task)

| Scenario | Unit Price (TRY) | Requested Qty | Available Stock | Member? (y/n) | Total Price | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Just Below 500 TRY** | 499.0 | 1 | 10 | y | 499.00 TRY | Approved standard order (No discount). Final: 499.00 TRY |
| **Exactly at 500 TRY** | 500.0 | 1 | 10 | y | 500.00 TRY | Approved with 10% member discount. Final: 450.00 TRY |
| **Above 500 TRY** | 500.0 | 2 | 10 | y | 1000.00 TRY | Approved with 10% member discount. Final: 900.00 TRY |
| **Insufficient Stock** | 100.0 | 15 | 10 | y | - | **Order Rejected**: Insufficient stock! (No price shown) |

## Testing Note & Code Change

- **Test Ran:** Tested the boundary values around 500 TRY (specifically 499 TRY vs 500 TRY) with `is_member = True`.
- **Change Made:** Refactored the code to simplify the `is_member` input handling using a clear `if-else` statement and ensured the condition `total_price >= 500` correctly grants the discount at exactly 500 TRY.
