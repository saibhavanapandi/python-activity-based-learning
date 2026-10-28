#Algorithm
1. Start the program.
2. Input the total classes conducted, classes attended, and required attendance percentage.
3. Validate the input values.
4. Calculate current attendance percentage using:
\[
\text{Attendance \%}=\frac{\text{Classes Attended}}{\text{Total Classes}}\times100
\]

5. Check whether the current attendance meets the eligibility threshold.
6. Input the expected future attendance rate for each scenario.
7. For each scenario, calculate the minimum number of future classes needed to reach the threshold.
8. If the future attendance rate cannot achieve the threshold, display that recovery is impossible under that scenario.
9. Display the current percentage, eligibility status, and required future classes for each scenario.
10. Stop.

                      #flowchart

             START
               |
               v
     Input attendance details
               |
               v
       Validate input values
               |
               v
          Inputs valid?
          /          \
        No            Yes
        |              |
        v              v
   Display error   Calculate current
        |          attendance percentage
        |              |
        |              v
        |     Is threshold reached?
        |          /         \
        |        Yes          No
        |         |            |
        |         v            v
        |   Display eligible  Select scenario
        |                      |
        |                      v
        |              Simulate future classes
        |                      |
        |                      v
        |              Threshold reached?
        |                 /         \
        |               Yes          No
        |                |            |
        |                v            v
        |           Display minimum  Continue until
        |           classes needed   search limit
        |                |            |
        |                +-----+------+
        |                      |
        +----------------------+
                               |
                               v
                              STOP




                              #code


                              
# Filename: attendance_recovery_computation.py

from math import ceil

print("ATTENDANCE RECOVERY COMPUTATION")
print("-" * 40)

total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
eligibility = float(input("Enter required attendance percentage: "))

if (
    total_classes < 0
    or attended_classes < 0
    or attended_classes > total_classes
    or not 0 < eligibility <= 100
):
    print("Invalid input. Please enter valid attendance details.")

else:
    current_percentage = (
        attended_classes / total_classes * 100
        if total_classes > 0 else 0
    )

    print(f"\nCurrent attendance: {current_percentage:.2f}%")
    print(f"Required attendance: {eligibility:.2f}%")

    if total_classes == 0:
        print("No classes have been conducted yet.")
    elif current_percentage >= eligibility:
        print("Status: Eligible based on current attendance.")
    else:
        print("Status: Attendance recovery required.")

    # Each scenario is (classes attended, total classes in a cycle).
    # Examples: (1, 1) = attend all; (4, 5) = attend 4 out of 5.
    scenarios = [
        ("Attend every class", 1, 1),
        ("Attend 4 out of every 5 classes", 4, 5),
        ("Attend 3 out of every 4 classes", 3, 4),
        ("Attend 1 out of every 2 classes", 1, 2)
    ]

    print("\nATTENDANCE RECOVERY SCENARIOS")
    print("-" * 68)

    for name, attended_per_cycle, cycle_length in scenarios:
        print(f"\nScenario: {name}")

        if current_percentage >= eligibility and total_classes > 0:
            print("No recovery needed; current attendance is sufficient.")
            continue

        future_attended = 0
        future_classes = 0
        found = False
        max_search = 100000

        for future_classes in range(1, max_search + 1):
            # Repeat the scenario's attendance pattern.
            position = (future_classes - 1) % cycle_length

            if position < attended_per_cycle:
                future_attended += 1

            new_total = total_classes + future_classes
            new_attended = attended_classes + future_attended
            new_percentage = new_attended / new_total * 100

            if new_percentage + 1e-9 >= eligibility:
                found = True
                break

        if found:
            print(f"Minimum future classes required: {future_classes}")
            print(f"Classes attended during recovery: {future_attended}")
            print(f"Projected attendance: {new_percentage:.2f}%")
        else:
            print(
                "Threshold cannot be reached within the search limit "
                "under this attendance pattern."
            )

    print("\nNote: Scenarios use repeating attendance patterns.")


                             #output

                             ATTENDANCE RECOVERY COMPUTATION
----------------------------------------
Enter total classes conducted: 40
Enter classes attended: 24
Enter required attendance percentage: 75

Current attendance: 60.00%
Required attendance: 75.00%
Status: Attendance recovery required.

ATTENDANCE RECOVERY SCENARIOS
--------------------------------------------------------------------

Scenario: Attend every class
Minimum future classes required: 24
Classes attended during recovery: 24
Projected attendance: 75.00%

Scenario: Attend 4 out of every 5 classes
Minimum future classes required: 120
Classes attended during recovery: 96
Projected attendance: 75.00%

Scenario: Attend 3 out of every 4 classes
Threshold cannot be reached within the search limit under this attendance pattern.

Scenario: Attend 1 out of every 2 classes
Threshold cannot be reached within the search limit under this attendance pattern.

Note: Scenarios use repeating attendance patterns.
                    