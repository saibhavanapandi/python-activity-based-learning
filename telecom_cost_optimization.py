#Algorithm
1. Start the program.
2. Enter the user's monthly data usage in GB, call usage in minutes, SMS usage, required validity in days, and budget.
3. Enter the available mobile plans and their details:
   - Plan name and base price.
   - Included data, call minutes, and SMS.
   - Plan validity in days.
   - Excess charges for additional data, calls, and SMS.
4. For each plan, calculate excess usage:
   - Excess data = maximum of (actual data − included data, 0).
   - Excess calls = maximum of (actual calls − included calls, 0).
   - Excess SMS = maximum of (actual SMS − included SMS, 0).
5. Calculate the total cost by adding the base price and excess charges.
6. Check whether the plan meets the validity requirement and budget.
7. If the plan satisfies both conditions, mark it as eligible.
8. Compare all eligible plans and select the plan with the lowest total cost.
9. Display the plan costs, excess charges, eligible plans, and most economical plan.
10. If no plan is eligible, display a suitable message.
11. Stop the program.
#flowchart
                START
                  |
                  v
        Enter Usage Requirements
                  |
                  v
         Enter Available Plans
                  |
                  v
           Select a Plan
                  |
                  v
       Calculate Excess Data,
        Calls and SMS Charges
                  |
                  v
         Calculate Total Cost
                  |
                  v
       Check Validity Requirement
                  |
                  v
          Cost <= Budget?
            /          \
          No            Yes
          |              |
          v              v
     Ineligible     Mark Eligible
          |              |
          +-------+------+
                  |
                  v
           More Plans?
            /        \
          Yes         No
           |           |
           v           v
      Select Next   Any Eligible
         Plan?        Plans?
                      /     \
                    No       Yes
                    |         |
                    v         v
             Display No    Find Lowest
             Eligible Plan Total Cost
                              |
                              v
                      Display Best Plan
                              |
                              v
                             STOP

 #code

# Multi-Plan Telecommunications Cost Optimization

def main():
    data_usage = float(input("Enter monthly data usage (GB): "))
    call_usage = int(input("Enter monthly call usage (minutes): "))
    sms_usage = int(input("Enter monthly SMS usage: "))
    required_validity = int(input("Enter required validity (days): "))
    budget = float(input("Enter your budget (Rs.): "))

    n = int(input("Enter number of mobile plans: "))
    plans = []

    for i in range(n):
        print(f"\nEnter details for Plan {i + 1}")

        name = input("Plan name: ")
        price = float(input("Base price (Rs.): "))
        included_data = float(input("Included data (GB): "))
        included_calls = int(input("Included calls (minutes): "))
        included_sms = int(input("Included SMS: "))
        validity = int(input("Validity (days): "))

        data_rate = float(input("Extra charge per GB (Rs.): "))
        call_rate = float(input("Extra charge per call minute (Rs.): "))
        sms_rate = float(input("Extra charge per SMS (Rs.): "))

        excess_data = max(0, data_usage - included_data)
        excess_calls = max(0, call_usage - included_calls)
        excess_sms = max(0, sms_usage - included_sms)

        data_charge = excess_data * data_rate
        call_charge = excess_calls * call_rate
        sms_charge = excess_sms * sms_rate

        total_cost = price + data_charge + call_charge + sms_charge

        eligible = (
            validity >= required_validity
            and total_cost <= budget
        )

        plans.append({
            "name": name,
            "price": price,
            "validity": validity,
            "excess_data": excess_data,
            "excess_calls": excess_calls,
            "excess_sms": excess_sms,
            "data_charge": data_charge,
            "call_charge": call_charge,
            "sms_charge": sms_charge,
            "total_cost": total_cost,
            "eligible": eligible
        })

    print("\n===== PLAN COST COMPARISON =====")

    for plan in plans:
        print(f"\nPlan: {plan['name']}")
        print(f"Base price: Rs. {plan['price']:.2f}")
        print(f"Excess data: {plan['excess_data']:.2f} GB")
        print(f"Excess call minutes: {plan['excess_calls']}")
        print(f"Excess SMS: {plan['excess_sms']}")
        print(f"Data charges: Rs. {plan['data_charge']:.2f}")
        print(f"Call charges: Rs. {plan['call_charge']:.2f}")
        print(f"SMS charges: Rs. {plan['sms_charge']:.2f}")
        print(f"Total cost: Rs. {plan['total_cost']:.2f}")

        if plan["validity"] < required_validity:
            print("Status: Ineligible - insufficient validity")
        elif plan["total_cost"] > budget:
            print("Status: Ineligible - exceeds budget")
        else:
            print("Status: Eligible")

    eligible_plans = [
        plan for plan in plans if plan["eligible"]
    ]

    print("\n===== FINAL RECOMMENDATION =====")

    if eligible_plans:
        best_plan = min(
            eligible_plans,
            key=lambda plan: plan["total_cost"]
        )

        print("Most economical eligible plan:",
              best_plan["name"])
        print(f"Total cost: Rs. {best_plan['total_cost']:.2f}")
        print(f"Validity: {best_plan['validity']} days")
        print(f"Budget remaining: Rs. "
              f"{budget - best_plan['total_cost']:.2f}")
    else:
        print("No plan satisfies both validity and budget constraints.")


if __name__ == "__main__":
    main()


          #output


          
Enter monthly data usage (GB): 2
Enter monthly call usage (minutes): 500
Enter monthly SMS usage: 100
Enter required validity (days): 28
Enter your budget (Rs.): 300
Enter number of mobile plans: 3

Enter details for Plan 1
Plan name: Plan A
Base price (Rs.): 199
Included data (GB): 1.5
Included calls (minutes): 400
Included SMS: 100
Validity (days): 28
Extra charge per GB (Rs.): 50
Extra charge per call minute (Rs.): 0.5
Extra charge per SMS (Rs.): 1

Enter details for Plan 2
Plan name: Plan B
Base price (Rs.): 249
Included data (GB): 2.5
Included calls (minutes): 600
Included SMS: 100
Validity (days): 28
Extra charge per GB (Rs.): 50
Extra charge per call minute (Rs.): 0.5
Extra charge per SMS (Rs.): 1

Enter details for Plan 3
Plan name: Plan C
Base price (Rs.): 149
Included data (GB): 1
Included calls (minutes): 300
Included SMS: 50
Validity (days): 14
Extra charge per GB (Rs.): 40
Extra charge per call minute (Rs.): 0.5
Extra charge per SMS (Rs.): 1

===== PLAN COST COMPARISON =====

Plan: Plan A
Base price: Rs. 199.00
Excess data: 0.50 GB
Excess call minutes: 100
Excess SMS: 0
Data charges: Rs. 25.00
Call charges: Rs. 50.00
SMS charges: Rs. 0.00
Total cost: Rs. 274.00
Status: Eligible

Plan: Plan B
Base price: Rs. 249.00
Excess data: 0.00 GB
Excess call minutes: 0
Excess SMS: 0
Data charges: Rs. 0.00
Call charges: Rs. 0.00
SMS charges: Rs. 0.00
Total cost: Rs. 249.00
Status: Eligible

Plan: Plan C
Base price: Rs. 149.00
Excess data: 1.00 GB
Excess call minutes: 200
Excess SMS: 50
Data charges: Rs. 40.00
Call charges: Rs. 100.00
SMS charges: Rs. 50.00
Total cost: Rs. 339.00
Status: Ineligible - insufficient validity

===== FINAL RECOMMENDATION =====
Most economical eligible plan: Plan B
Total cost: Rs. 249.00
Validity: 28 days
Budget remaining: Rs. 51.00