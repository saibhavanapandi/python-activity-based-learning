#Algorithm
1. Start the program.
2. Input the number of scholarship applicants.
3. For each applicant, enter:
   - Student name and roll number.
   - Aggregate marks (percentage).
   - Subject-wise marks.
   - Attendance percentage.
   - Annual family income.
4. Check the eligibility criteria:
   - Aggregate marks must be at least 75%.
   - Every subject mark must be at least 40%.
   - Attendance must be at least 75%.
   - Annual family income must not exceed ₹2,50,000.
5. If all conditions are satisfied, mark the student as eligible; otherwise, mark the student as ineligible.
6. Sort eligible students using these ranking rules:
   - Higher aggregate marks rank first.
   - If aggregate marks are equal, higher attendance ranks first.
   - If attendance is also equal, lower annual family income ranks first.
   - If all three are equal, lower roll number ranks first.
7. Display all eligible students in ranked order.
8. Display the ineligible students and their reasons for rejection.
9. Stop the program.


#flowchart
             START
               |
               v
    Enter Number of Applicants
               |
               v
      Enter Student Details
               |
               v
 Enter Aggregate, Subject Marks,
     Attendance and Income
               |
               v
      Aggregate >= 75%?
          /         \
        No           Yes
        |             |
        v             v
  Mark Ineligible  Every Subject
                   Mark >= 40%?
                   /         \
                 No           Yes
                 |             |
                 v             v
           Mark Ineligible  Attendance
                           >= 75%?
                           /      \
                         No        Yes
                         |          |
                         v          v
                   Mark Ineligible  Income
                                <= Rs. 250000?
                                 /        \
                               No          Yes
                               |            |
                               v            v
                         Mark Ineligible  Mark Eligible
                               |            |
                               +-----+------+
                                     |
                                     v
                            More Applicants?
                              /         \
                            Yes          No
                             |            |
                             v            v
                       Enter Student   Rank Eligible
                          Details       Students
                                          |
                                          v
                                  Higher Aggregate
                                          |
                                          v
                                  Higher Attendance
                                          |
                                          v
                                   Lower Income
                                          |
                                          v
                                  Lower Roll Number
                                          |
                                          v
                              Display Final Results
                                          |
                                          v
                                         STOP


        #code
        
# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000


def check_eligibility(student):
    reasons = []

    if student["aggregate"] < MIN_AGGREGATE:
        reasons.append("Aggregate marks below 75%")

    if any(mark < MIN_SUBJECT_MARK
           for mark in student["subjects"]):
        reasons.append("Subject mark below 40%")

    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if student["income"] > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 2,50,000")

    return reasons


def main():
    students = []

    n = int(input("Enter number of applicants: "))

    for i in range(n):
        print(f"\nEnter details of applicant {i + 1}")

        roll = int(input("Roll number: "))
        name = input("Student name: ")
        aggregate = float(input("Aggregate percentage: "))

        count = int(input("Number of subjects: "))
        subjects = []

        for j in range(count):
            mark = float(input(f"Subject {j + 1} mark: "))
            subjects.append(mark)

        attendance = float(input("Attendance percentage: "))
        income = float(input("Annual family income (Rs.): "))

        student = {
            "roll": roll,
            "name": name,
            "aggregate": aggregate,
            "subjects": subjects,
            "attendance": attendance,
            "income": income
        }

        student["reasons"] = check_eligibility(student)
        students.append(student)

    eligible = [
        s for s in students if not s["reasons"]
    ]

    # Merit order:
    # 1. Higher aggregate
    # 2. Higher attendance
    # 3. Lower family income
    # 4. Lower roll number
    eligible.sort(
        key=lambda s: (
            -s["aggregate"],
            -s["attendance"],
            s["income"],
            s["roll"]
        )
    )

    print("\n===== SCHOLARSHIP ELIGIBILITY RESULTS =====")

    if eligible:
        print("\nEligible Students - Merit Ranking")
        print("-" * 75)
        print(f"{'Rank':<6}{'Roll':<8}{'Name':<18}"
              f"{'Aggregate':<13}{'Attendance':<13}{'Income':<10}")

        for rank, s in enumerate(eligible, start=1):
            print(
                f"{rank:<6}{s['roll']:<8}{s['name']:<18}"
                f"{s['aggregate']:<13.2f}"
                f"{s['attendance']:<13.2f}"
                f"{s['income']:<10.0f}"
            )
    else:
        print("\nNo students are eligible.")

    ineligible = [
        s for s in students if s["reasons"]
    ]

    print("\nIneligible Students")
    for s in ineligible:
        print(f"\n{s['roll']} - {s['name']}")
        for reason in s["reasons"]:
            print(f"  - {reason}")

    print("\n===== END OF RESULTS =====")


if __name__ == "__main__":
    main()

#output

Enter number of applicants: 4

Enter details of applicant 1
Roll number: 101
Student name: Anu
Aggregate percentage: 90
Number of subjects: 2
Subject 1 mark: 85
Subject 2 mark: 88
Attendance percentage: 90
Annual family income (Rs.): 180000

Enter details of applicant 2
Roll number: 102
Student name: Bala
Aggregate percentage: 90
Number of subjects: 2
Subject 1 mark: 80
Subject 2 mark: 85
Attendance percentage: 90
Annual family income (Rs.): 200000

Enter details of applicant 3
Roll number: 103
Student name: Chitra
Aggregate percentage: 80
Number of subjects: 2
Subject 1 mark: 75
Subject 2 mark: 30
Attendance percentage: 85
Annual family income (Rs.): 150000

Enter details of applicant 4
Roll number: 104
Student name: Deepa
Aggregate percentage: 72
Number of subjects: 2
Subject 1 mark: 70
Subject 2 mark: 75
Attendance percentage: 80
Annual family income (Rs.): 150000

===== SCHOLARSHIP ELIGIBILITY RESULTS =====

Eligible Students - Merit Ranking
---------------------------------------------------------------------------
Rank  Roll    Name              Aggregate    Attendance   Income
1     101     Anu               90.00        90.00        180000
2     102     Bala              90.00        90.00        200000

Ineligible Students

103 - Chitra
  - Subject mark below 40%

104 - Deepa
  - Aggregate marks below 75%

===== END OF RESULTS =====