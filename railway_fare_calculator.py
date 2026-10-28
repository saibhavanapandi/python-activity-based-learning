#Algorithm
1. Start the program.
2. Input the journey distance in kilometres and the number of passengers.
3. For each passenger, enter their name, age, and travel class.
4. Calculate the base fare using distance slabs:
   - Up to 100 km: ₹1.00 per km
   - 101–300 km: ₹0.80 per km
   - Above 300 km: ₹0.60 per km
5. Apply the class multiplier:
   - Sleeper: 1.0
   - AC 3 Tier: 1.5
   - AC 2 Tier: 2.0
   - AC First Class: 3.0
6. Apply age-based concessions:
   - Children below 5 years: free.
   - Passengers aged 60 and above: 20% concession.
   - Other passengers: no concession.
7. Add a reservation fee of ₹40 per passenger, except for children travelling free.
8. Calculate the total fare for all passengers.
9. Ask whether the passenger wants to cancel the ticket.
10. If cancelled, calculate a cancellation penalty of 25% of the ticket fare before reservation fees.
11. Display each passenger's fare, concession, reservation fee, cancellation penalty, and final payable or refundable amount.
12. Stop the program.



                       #flowchart



                                        START
                   |
                   v
       Enter Journey Distance
                   |
                   v
        Enter Number of Passengers
                   |
                   v
       Enter Passenger Name, Age,
             and Travel Class
                   |
                   v
        Calculate Base Fare Using
             Distance Slabs
                   |
                   v
        Apply Class Multiplier
                   |
                   v
         Check Passenger Age
                   |
                   v
        Apply Age Concession
                   |
                   v
       Add Reservation Fee
                   |
                   v
        Calculate Ticket Fare
                   |
                   v
        Is Ticket Cancelled?
             /           \
           Yes            No
            |              |
            v              v
    Calculate Cancellation  Final Fare
          Penalty           Payable
            |                |
            v                |
    Calculate Refund         |
            |                |
            +-------+--------+
                    |
                    v
       Display Fare and Final Amount
                    |
                    v
       Are More Passengers Remaining?
              /           \
            Yes            No
             |              |
             v              v
      Enter Next Passenger  STOP




                   #code


                   
# Railway Fare and Reservation Calculator

CLASS_MULTIPLIERS = {
    "sleeper": 1.0,
    "ac3": 1.5,
    "ac2": 2.0,
    "first": 3.0
}

RESERVATION_FEE = 40.0
SENIOR_CONCESSION = 0.20
CANCELLATION_RATE = 0.25


def calculate_base_fare(distance):
    if distance <= 100:
        return distance * 1.00
    elif distance <= 300:
        return distance * 0.80
    else:
        return distance * 0.60


def main():
    distance = float(input("Enter journey distance (km): "))
    passengers = int(input("Enter number of passengers: "))

    if distance <= 0 or passengers <= 0:
        print("Distance and passenger count must be positive.")
        return

    total_fare = 0.0
    total_penalty = 0.0
    total_refund = 0.0

    for i in range(passengers):
        print(f"\nPassenger {i + 1}")

        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))

        print("Classes: sleeper, ac3, ac2, first")
        travel_class = input("Enter travel class: ").lower()

        if travel_class not in CLASS_MULTIPLIERS:
            print("Invalid class. Passenger skipped.")
            continue

        base = calculate_base_fare(distance)
        class_fare = base * CLASS_MULTIPLIERS[travel_class]

        if age < 5:
            concession = class_fare
            fare_after_concession = 0.0
            reservation = 0.0
        else:
            if age >= 60:
                concession = class_fare * SENIOR_CONCESSION
            else:
                concession = 0.0

            fare_after_concession = class_fare - concession
            reservation = RESERVATION_FEE

        ticket_fare = fare_after_concession + reservation

        cancel = input("Cancel ticket? (yes/no): ").lower()

        if cancel == "yes":
            # Penalty applies to fare after concession,
            # excluding the reservation fee.
            penalty = fare_after_concession * CANCELLATION_RATE
            refund = ticket_fare - penalty
            payable = 0.0

            total_penalty += penalty
            total_refund += refund
        else:
            penalty = 0.0
            refund = 0.0
            payable = ticket_fare
            total_fare += payable

        print("\n--- Passenger Fare Details ---")
        print("Name:", name)
        print("Distance:", distance, "km")
        print("Travel class:", travel_class)
        print(f"Base class fare: Rs. {class_fare:.2f}")
        print(f"Age concession: Rs. {concession:.2f}")
        print(f"Reservation fee: Rs. {reservation:.2f}")
        print(f"Ticket fare: Rs. {ticket_fare:.2f}")
        print(f"Cancellation penalty: Rs. {penalty:.2f}")
        print(f"Refund amount: Rs. {refund:.2f}")
        print(f"Amount payable: Rs. {payable:.2f}")

    print("\n===== JOURNEY SUMMARY =====")
    print(f"Total fare payable: Rs. {total_fare:.2f}")
    print(f"Total cancellation penalties: Rs. {total_penalty:.2f}")
    print(f"Total refunds: Rs. {total_refund:.2f}")


if __name__ == "__main__":
    main()


                  #output


                  Enter journey distance (km): 200
Enter number of passengers: 2

Passenger 1
Enter passenger name: Ravi
Enter age: 25
Classes: sleeper, ac3, ac2, first
Enter travel class: sleeper
Cancel ticket? (yes/no): no

--- Passenger Fare Details ---
Name: Ravi
Distance: 200.0 km
Travel class: sleeper
Base class fare: Rs. 160.00
Age concession: Rs. 0.00
Reservation fee: Rs. 40.00
Ticket fare: Rs. 200.00
Cancellation penalty: Rs. 0.00
Refund amount: Rs. 0.00
Amount payable: Rs. 200.00

Passenger 2
Enter passenger name: Meena
Enter age: 65
Classes: sleeper, ac3, ac2, first
Enter travel class: ac3
Cancel ticket? (yes/no): yes

--- Passenger Fare Details ---
Name: Meena
Distance: 200.0 km
Travel class: ac3
Base class fare: Rs. 240.00
Age concession: Rs. 48.00
Reservation fee: Rs. 40.00
Ticket fare: Rs. 232.00
Cancellation penalty: Rs. 48.00
Refund amount: Rs. 184.00
Amount payable: Rs. 0.00

===== JOURNEY SUMMARY =====
Total fare payable: Rs. 200.00
Total cancellation penalties: Rs. 48.00
Total refunds: Rs. 184.00