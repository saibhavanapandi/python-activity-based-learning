#Algorithm
1. Start the program.
2. Enter the travel budget in the base currency (for example, INR).
3. Enter the number of travel expense categories.
4. For each category, enter:
   - Expense category, such as accommodation, food, transport, or shopping.
   - Expense amount.
   - Currency code.
   - Exchange rate to the base currency.
5. Enter the currency conversion fee percentage.
6. Convert each expense into the base currency using the supplied exchange rate.
7. Calculate the conversion fee for each expense.
8. Add the conversion fee to the converted expense.
9. Calculate the total travel expenditure, including fees.
10. Compare total expenditure against the planned budget.
11. Identify the largest expense category based on total cost, including fees.
12. Display the itemized expense report, total expenditure, budget balance or overspending, and largest expense category.
13. Stop the program.


                             #flowchart

                                               START
                    |
                    v
          Enter Travel Budget
                    |
                    v
       Enter Number of Expense Categories
                    |
                    v
        Enter Category, Amount, Currency
             and Exchange Rate
                    |
                    v
       Convert Expense to Base Currency
                    |
                    v
         Calculate Conversion Fee
                    |
                    v
       Calculate Total Expense Including Fee
                    |
                    v
           More Categories?
             /          \
           Yes           No
            |             |
            v             v
      Enter Next      Calculate Total
       Expense         Expenditure
                          |
                          v
                 Identify Largest Category
                          |
                          v
                  Compare with Budget
                    /           \
             Within Budget    Over Budget
                    \           /
                     v         v
                 Display Expense Report
                          |
                          v
                         STOP


                         #code

                         
# Multi-Currency Travel Budget Analysis

def main():
    print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

    budget = float(input("Enter travel budget (INR): "))
    fee_rate = float(input("Enter conversion fee percentage: "))
    n = int(input("Enter number of expense categories: "))

    if budget < 0 or not 0 <= fee_rate <= 100 or n <= 0:
        print("Invalid budget, fee percentage, or category count.")
        return

    expenses = []
    total_spending = 0.0

    for i in range(n):
        print(f"\nExpense Category {i + 1}")

        category = input("Enter category name: ")
        currency = input("Enter currency code (e.g., USD, EUR): ").upper()
        amount = float(input("Enter expense amount: "))
        rate = float(input("Enter exchange rate to INR: "))

        if amount < 0 or rate <= 0:
            print("Invalid amount or exchange rate. Try again.")
            continue

        converted_amount = amount * rate
        conversion_fee = converted_amount * fee_rate / 100
        total_cost = converted_amount + conversion_fee

        expenses.append({
            "category": category,
            "currency": currency,
            "amount": amount,
            "rate": rate,
            "converted": converted_amount,
            "fee": conversion_fee,
            "total": total_cost
        })

        total_spending += total_cost

    print("\n" + "=" * 85)
    print("             TRAVEL EXPENSE REPORT (INR)")
    print("=" * 85)
    print(
        f"{'Category':<16}{'Currency':<10}{'Original':>12}"
        f"{'Converted':>14}{'Fee':>12}{'Total INR':>14}"
    )
    print("-" * 85)

    for e in expenses:
        print(
            f"{e['category']:<16}{e['currency']:<10}"
            f"{e['amount']:>12.2f}{e['converted']:>14.2f}"
            f"{e['fee']:>12.2f}{e['total']:>14.2f}"
        )

    print("-" * 85)
    print(f"Travel budget:       Rs. {budget:.2f}")
    print(f"Total expenditure:   Rs. {total_spending:.2f}")

    difference = budget - total_spending

    if difference >= 0:
        print(f"Budget remaining:    Rs. {difference:.2f}")
        print("Status: WITHIN BUDGET")
    else:
        print(f"Amount over budget:  Rs. {-difference:.2f}")
        print("Status: OVER BUDGET")

    if expenses:
        largest = max(expenses, key=lambda e: e["total"])
        print(f"Largest expense:     {largest['category']}")
        print(f"Expense amount:      Rs. {largest['total']:.2f}")
    else:
        print("No valid expenses were entered.")

    print("=" * 85)


if __name__ == "__main__":
    main()
                            

                            #output


                            MULTI-CURRENCY TRAVEL BUDGET ANALYSIS
Enter travel budget (INR): 100000
Enter conversion fee percentage: 2
Enter number of expense categories: 4

Expense Category 1
Enter category name: Hotel
Enter currency code (e.g., USD, EUR): EUR
Enter expense amount: 300
Enter exchange rate to INR: 95

Expense Category 2
Enter category name: Food
Enter currency code (e.g., USD, EUR): USD
Enter expense amount: 200
Enter exchange rate to INR: 83

Expense Category 3
Enter category name: Transport
Enter currency code (e.g., USD, EUR): GBP
Enter expense amount: 150
Enter exchange rate to INR: 110

Expense Category 4
Enter category name: Shopping
Enter currency code (e.g., USD, EUR): USD
Enter expense amount: 250
Enter exchange rate to INR: 83

=====================================================================================
             TRAVEL EXPENSE REPORT (INR)
=====================================================================================
Category        Currency      Original     Converted         Fee     Total INR
-------------------------------------------------------------------------------------
Hotel           EUR             300.00      28500.00      570.00      29070.00
Food            USD             200.00      16600.00      332.00      16932.00
Transport       GBP             150.00      16500.00      330.00      16830.00
Shopping        USD             250.00      20750.00      415.00      21165.00
-------------------------------------------------------------------------------------
Travel budget:       Rs. 100000.00
Total expenditure:   Rs. 83997.00
Budget remaining:    Rs. 16003.00
Status: WITHIN BUDGET
Largest expense:     Hotel
Expense amount:      Rs. 29070.00
=====================================================================================