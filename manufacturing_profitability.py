#Algorithm
1. Start the program.
2. Input the product name and number of units manufactured.
3. Enter the material cost per unit, labour cost per unit, machine cost per unit, and wastage percentage.
4. Calculate the total material cost.
5. Calculate the wastage cost based on the material cost.
6. Calculate the total labour cost and machine cost.
7. Add all costs to determine the total production cost.
8. Calculate the production cost per unit.
9. Input the selling price per unit and the required profit target percentage.
10. Calculate total revenue using selling price × number of units.
11. Calculate total profit using total revenue − total production cost.
12. Calculate profit percentage using profit divided by production cost × 100.
13. Compare the actual profit percentage with the specified profit target.
14. Display the cost breakdown, revenue, profit, and whether the production meets the target.
15. Stop the program.

                        #flowchart

                                         START
                   |
                   v
          Enter Product Details
                   |
                   v
       Enter Number of Units Produced
                   |
                   v
        Enter Material, Labour,
         Machine and Wastage Costs
                   |
                   v
        Calculate Material Cost
                   |
                   v
          Calculate Wastage Cost
                   |
                   v
       Calculate Labour and Machine Costs
                   |
                   v
        Calculate Total Production Cost
                   |
                   v
        Calculate Cost Per Unit
                   |
                   v
        Enter Selling Price Per Unit
          and Profit Target Percentage
                   |
                   v
         Calculate Total Revenue
                   |
                   v
           Calculate Total Profit
                   |
                   v
         Calculate Profit Percentage
                   |
                   v
       Profit Percentage >= Target?
              /            \
            Yes             No
             |               |
             v               v
       Target Achieved   Target Not Achieved
             |               |
             +-------+-------+
                     |
                     v
            Display Cost Analysis,
             Revenue and Profit
                     |
                     v
                    STOP


                    #code


                    
# Manufacturing Cost and Profitability Analysis

def main():
    print("MANUFACTURING COST AND PROFITABILITY ANALYSIS")

    product_name = input("Enter product name: ")
    units = int(input("Enter number of units produced: "))

    if units <= 0:
        print("Number of units must be positive.")
        return

    material_per_unit = float(
        input("Enter material cost per unit (Rs.): ")
    )
    labour_per_unit = float(
        input("Enter labour cost per unit (Rs.): ")
    )
    machine_per_unit = float(
        input("Enter machine cost per unit (Rs.): ")
    )
    wastage_rate = float(
        input("Enter wastage percentage: ")
    )
    selling_price = float(
        input("Enter selling price per unit (Rs.): ")
    )
    profit_target = float(
        input("Enter target profit percentage: ")
    )

    if min(material_per_unit, labour_per_unit,
           machine_per_unit, selling_price) < 0:
        print("Costs and selling price cannot be negative.")
        return

    if not 0 <= wastage_rate <= 100:
        print("Wastage percentage must be between 0 and 100.")
        return

    if profit_target < 0:
        print("Profit target cannot be negative.")
        return

    # Calculate production costs
    material_cost = material_per_unit * units
    wastage_cost = material_cost * wastage_rate / 100
    labour_cost = labour_per_unit * units
    machine_cost = machine_per_unit * units

    total_cost = (
        material_cost + wastage_cost
        + labour_cost + machine_cost
    )

    cost_per_unit = total_cost / units

    # Calculate revenue and profit
    revenue = selling_price * units
    profit = revenue - total_cost

    if total_cost > 0:
        profit_percentage = profit / total_cost * 100
    else:
        profit_percentage = 0.0

    meets_target = profit_percentage >= profit_target

    # Display report
    print("\n========== COST ANALYSIS REPORT ==========")
    print("Product:", product_name)
    print("Units produced:", units)
    print(f"Material cost: Rs. {material_cost:.2f}")
    print(f"Wastage cost: Rs. {wastage_cost:.2f}")
    print(f"Labour cost: Rs. {labour_cost:.2f}")
    print(f"Machine cost: Rs. {machine_cost:.2f}")
    print(f"Total production cost: Rs. {total_cost:.2f}")
    print(f"Production cost per unit: Rs. {cost_per_unit:.2f}")

    print("\n========== PROFITABILITY REPORT ==========")
    print(f"Selling price per unit: Rs. {selling_price:.2f}")
    print(f"Total revenue: Rs. {revenue:.2f}")
    print(f"Total profit: Rs. {profit:.2f}")
    print(f"Profit percentage: {profit_percentage:.2f}%")
    print(f"Required profit target: {profit_target:.2f}%")

    if meets_target:
        print("Result: PROFIT TARGET ACHIEVED")
    else:
        print("Result: PROFIT TARGET NOT ACHIEVED")

    print("==========================================")


if __name__ == "__main__":
    main()
                         

                         #output

                         MANUFACTURING COST AND PROFITABILITY ANALYSIS
Enter product name: Chair
Enter number of units produced: 100
Enter material cost per unit (Rs.): 500
Enter labour cost per unit (Rs.): 150
Enter machine cost per unit (Rs.): 100
Enter wastage percentage: 10
Enter selling price per unit (Rs.): 1000
Enter target profit percentage: 20

========== COST ANALYSIS REPORT ==========
Product: Chair
Units produced: 100
Material cost: Rs. 50000.00
Wastage cost: Rs. 5000.00
Labour cost: Rs. 15000.00
Machine cost: Rs. 10000.00
Total production cost: Rs. 80000.00
Production cost per unit: Rs. 800.00

========== PROFITABILITY REPORT ==========
Selling price per unit: Rs. 1000.00
Total revenue: Rs. 100000.00
Total profit: Rs. 20000.00
Profit percentage: 25.00%
Required profit target: 20.00%
Result: PROFIT TARGET ACHIEVED
==========================================