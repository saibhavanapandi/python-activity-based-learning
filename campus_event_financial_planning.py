#Algorithm
1. Start the program.
2. Input the event name and expected number of participants.
3. Enter the event expenses:
   - Venue cost.
   - Equipment cost.
   - Catering cost per participant.
   - Transport cost per participant.
   - Certificate cost per participant.
4. Enter the available sponsorship amount and registration fee per participant.
5. Calculate fixed costs by adding venue and equipment costs.
6. Calculate variable cost per participant by adding catering, transport, and certificate costs.
7. Calculate total event cost using fixed costs and variable costs for the expected participants.
8. Calculate the amount that must be collected from registrations after deducting sponsorship.
9. Calculate the required registration contribution per participant.
10. Calculate the sponsorship shortfall, if the sponsorship is less than the total event cost.
11. Calculate the minimum number of registrations needed to break even using the registration fee and variable cost per participant.
12. Display the expense breakdown, total cost, sponsorship shortfall, participant contribution, and break-even registration count.
13. Stop the program.


                  #flowchart

                                    START
                    |
                    v
          Enter Event Details
                    |
                    v
        Enter Venue and Equipment Costs
                    |
                    v
       Enter Catering, Transport and
            Certificate Costs
                    |
                    v
       Enter Sponsorship and Registration Fee
                    |
                    v
        Calculate Fixed and Variable Costs
                    |
                    v
         Calculate Total Event Cost
                    |
                    v
       Calculate Sponsorship Shortfall
                    |
                    v
       Calculate Required Participant
               Contribution
                    |
                    v
        Calculate Break-Even Registrations
                    |
                    v
          Is Break-Even Possible?
              /           \
            Yes            No
             |              |
             v              v
      Display Minimum   Display Cannot
       Registrations    Break Even
              \          /
               v        v
          Display Financial Report
                    |
                    v
                   STOP


                   #code

                   
# Campus Event Financial Planning System

import math


def main():
    print("CAMPUS EVENT FINANCIAL PLANNING")

    event_name = input("Enter event name: ")
    participants = int(input("Enter expected participants: "))

    if participants <= 0:
        print("Participants must be greater than zero.")
        return

    venue = float(input("Enter venue cost (Rs.): "))
    equipment = float(input("Enter equipment cost (Rs.): "))
    catering = float(input("Enter catering cost per participant (Rs.): "))
    transport = float(input("Enter transport cost per participant (Rs.): "))
    certificate = float(input("Enter certificate cost per participant (Rs.): "))
    sponsorship = float(input("Enter available sponsorship (Rs.): "))
    registration_fee = float(input("Enter registration fee per participant (Rs.): "))

    if min(venue, equipment, catering, transport,
           certificate, sponsorship, registration_fee) < 0:
        print("Costs, sponsorship, and registration fee cannot be negative.")
        return

    # Calculate costs
    fixed_cost = venue + equipment
    variable_per_person = catering + transport + certificate
    variable_cost = variable_per_person * participants
    total_cost = fixed_cost + variable_cost

    # Sponsorship shortfall against total event cost
    shortfall = max(0, total_cost - sponsorship)

    # Required participant contribution for expected attendance
    contribution_per_person = shortfall / participants

    # Break-even registration count
    net_contribution = registration_fee - variable_per_person
    amount_to_cover = max(0, fixed_cost - sponsorship)

    if amount_to_cover == 0:
        break_even = 0
        break_even_message = "Sponsorship covers all fixed costs."
    elif net_contribution > 0:
        break_even = math.ceil(amount_to_cover / net_contribution)
        break_even_message = f"{break_even} registrations required."
    else:
        break_even = None
        break_even_message = (
            "Break-even is not possible at this fee "
            "with the current sponsorship."
        )

    # Financial report
    print("\n========== EVENT FINANCIAL REPORT ==========")
    print("Event:", event_name)
    print("Expected participants:", participants)

    print("\n--- Expense Breakdown ---")
    print(f"Venue cost: Rs. {venue:.2f}")
    print(f"Equipment cost: Rs. {equipment:.2f}")
    print(f"Catering cost: Rs. {catering:.2f}")
    print(f"Transport cost: Rs. {transport:.2f}")
    print(f"Certificate cost: Rs. {certificate:.2f}")
    print(f"Total event cost: Rs. {total_cost:.2f}")

    print("\n--- Funding Analysis ---")
    print(f"Sponsorship: Rs. {sponsorship:.2f}")
    print(f"Sponsorship shortfall: Rs. {shortfall:.2f}")
    print(
        "Required contribution per expected participant: "
        f"Rs. {contribution_per_person:.2f}"
    )
    print(f"Registration fee: Rs. {registration_fee:.2f}")
    print(f"Break-even analysis: {break_even_message}")

    if break_even is not None:
        if break_even <= participants:
            print("Break-even is achievable within expected attendance.")
        else:
            print("Break-even exceeds expected attendance.")

    # Expected financial outcome
    expected_revenue = sponsorship + registration_fee * participants
    balance = expected_revenue - total_cost

    print("\n--- Expected Financial Outcome ---")
    print(f"Total expected funding: Rs. {expected_revenue:.2f}")
    print(f"Surplus / deficit: Rs. {balance:.2f}")

    if balance >= 0:
        print("Status: EVENT IS FINANCIALLY VIABLE")
    else:
        print("Status: ADDITIONAL FUNDING IS REQUIRED")

    print("============================================")


if __name__ == "__main__":
    main()


                      #output


                      CAMPUS EVENT FINANCIAL PLANNING
Enter event name: College Tech Fest
Enter expected participants: 100
Enter venue cost (Rs.): 20000
Enter equipment cost (Rs.): 10000
Enter catering cost per participant (Rs.): 200
Enter transport cost per participant (Rs.): 50
Enter certificate cost per participant (Rs.): 30
Enter available sponsorship (Rs.): 20000
Enter registration fee per participant (Rs.): 500

========== EVENT FINANCIAL REPORT ==========
Event: College Tech Fest
Expected participants: 100

--- Expense Breakdown ---
Venue cost: Rs. 20000.00
Equipment cost: Rs. 10000.00
Catering cost: Rs. 20000.00
Transport cost: Rs. 5000.00
Certificate cost: Rs. 3000.00
Total event cost: Rs. 58000.00

--- Funding Analysis ---
Sponsorship: Rs. 20000.00
Sponsorship shortfall: Rs. 38000.00
Required contribution per expected participant: Rs. 380.00
Registration fee: Rs. 500.00
Break-even analysis: 46 registrations required.
Break-even is achievable within expected attendance.

--- Expected Financial Outcome ---
Total expected funding: Rs. 70000.00
Surplus / deficit: Rs. 12000.00
Status: EVENT IS FINANCIALLY VIABLE
============================================