#Algorithm
1. Start the program.
2. Input the student's name and number of subjects.
3. For each subject, input the subject name, marks obtained, maximum marks, and minimum passing marks.
4. Validate that marks are within the permitted range.
5. Check whether the student has passed each subject.
6. If the student has failed a subject, check whether the marks required to pass are within the permitted grace-mark limit.
7. If eligible, award the required grace marks without exceeding the maximum marks.
8. Recheck the subject's pass status after applying grace marks.
9. Calculate total marks, maximum total marks, and percentage.
10. Generate the final result:
    - PASS: All subjects passed after grace marks.
    - FAIL: One or more subjects remain failed.
11. Assign a classification based on the percentage if the student passes.
12. Display the subject-wise results, grace marks awarded, total, percentage, and final classification.
13. Stop.

                           #flowchar

                                     START
            |
            v
   Input student details
            |
            v
   Input number of subjects
            |
            v
   Enter marks and pass criteria
            |
            v
    Are the inputs valid?
        /         \
      No           Yes
      |             |
      v             v
 Display error   Check each subject
      |             |
      |             v
      |       Has student passed?
      |          /       \
      |        Yes        No
      |         |          |
      |         |          v
      |         |   Check grace eligibility
      |         |          |
      |         |          v
      |         |   Apply allowed grace marks
      |         |          |
      |         |          v
      |         |   Cap marks at maximum
      |         |          |
      |         +----------+
      |             |
      |             v
      |     Calculate total and percentage
      |             |
      |             v
      |     All subjects passed?
      |         /       \
      |       No         Yes
      |       |           |
      |       v           v
      |   Final FAIL   Assign classification
      |       |           |
      |       +-----+-----+
      |             |
      |             v
      |      Display final result
      |             |
      +-------------+
                    |
                    v
                   STOP


                   #code


                   
# Filename: examination_result_grace_mark_validation.py

print("EXAMINATION RESULT AND GRACE-MARK VALIDATION")
print("-" * 48)

student_name = input("Enter student name: ").strip()
number_of_subjects = int(input("Enter number of subjects: "))
grace_limit = int(input("Enter maximum grace marks allowed per subject: "))

if number_of_subjects <= 0 or grace_limit < 0:
    print("Invalid number of subjects or grace-mark limit.")
else:
    subjects = []
    total_marks = 0
    total_maximum = 0
    failed_subjects = 0

    for i in range(number_of_subjects):
        print(f"\nSubject {i + 1}")

        subject_name = input("Enter subject name: ").strip()
        maximum_marks = int(input("Enter maximum marks: "))
        pass_marks = int(input("Enter minimum passing marks: "))
        obtained_marks = int(input("Enter marks obtained: "))

        # Validate subject marks and pass criteria
        if (
            maximum_marks <= 0
            or pass_marks < 0
            or pass_marks > maximum_marks
            or obtained_marks < 0
            or obtained_marks > maximum_marks
        ):
            print("Invalid marks or passing criteria. Please restart.")
            subjects = []
            break

        grace_awarded = 0
        final_marks = obtained_marks

        # Apply grace marks only when needed to reach the pass mark
        if obtained_marks < pass_marks:
            required_grace = pass_marks - obtained_marks

            if required_grace <= grace_limit:
                grace_awarded = required_grace

                # Ensure final marks never exceed maximum marks
                final_marks = min(
                    obtained_marks + grace_awarded,
                    maximum_marks
                )

        passed = final_marks >= pass_marks

        if not passed:
            failed_subjects += 1

        subjects.append({
            "name": subject_name,
            "obtained": obtained_marks,
            "grace": grace_awarded,
            "final": final_marks,
            "maximum": maximum_marks,
            "status": "PASS" if passed else "FAIL"
        })

        total_marks += final_marks
        total_maximum += maximum_marks

    if subjects and len(subjects) == number_of_subjects:
        percentage = (total_marks / total_maximum) * 100
        final_result = "PASS" if failed_subjects == 0 else "FAIL"

        print("\n" + "=" * 68)
        print(f"Student Name: {student_name}")
        print("=" * 68)
        print(
            f"{'Subject':<18}{'Original':>10}{'Grace':>8}"
            f"{'Final':>10}{'Maximum':>10}{'Status':>10}"
        )
        print("-" * 68)

        for subject in subjects:
            print(
                f"{subject['name']:<18}"
                f"{subject['obtained']:>10}"
                f"{subject['grace']:>8}"
                f"{subject['final']:>10}"
                f"{subject['maximum']:>10}"
                f"{subject['status']:>10}"
            )

        print("-" * 68)
        print(f"Total Marks: {total_marks}/{total_maximum}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Final Result: {final_result}")

        if final_result == "PASS":
            if percentage >= 75:
                classification = "Distinction"
            elif percentage >= 60:
                classification = "First Class"
            elif percentage >= 50:
                classification = "Second Class"
            else:
                classification = "Pass Class"

            print(f"Classification: {classification}")
        else:
            print("Classification: Not applicable")
            print(f"Failed Subjects: {failed_subjects}")



                          #output

                          EXAMINATION RESULT AND GRACE-MARK VALIDATION
------------------------------------------------
Enter student name: Ravi
Enter number of subjects: 3
Enter maximum grace marks allowed per subject: 5

Subject 1
Enter subject name: Mathematics
Enter maximum marks: 100
Enter minimum passing marks: 40
Enter marks obtained: 38

Subject 2
Enter subject name: Physics
Enter maximum marks: 100
Enter minimum passing marks: 40
Enter marks obtained: 65

Subject 3
Enter subject name: Chemistry
Enter maximum marks: 100
Enter minimum passing marks: 40
Enter marks obtained: 75

====================================================================
Student Name: Ravi
====================================================================
Subject              Original   Grace     Final   Maximum    Status
--------------------------------------------------------------------
Mathematics                38       2        40       100      PASS
Physics                    65       0        65       100      PASS
Chemistry                  75       0        75       100      PASS
--------------------------------------------------------------------
Total Marks: 180/300
Percentage: 60.00%
Final Result: PASS
Classification: First Class
