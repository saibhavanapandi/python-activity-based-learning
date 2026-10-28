#Algorithm
1. Start the program.
2. Input the initial account balance and maximum withdrawal limit per transaction.
3. Validate the initial balance and withdrawal limit.
4. Input the number of transactions to process.
5. For each transaction:
   - Select the transaction type: deposit or withdrawal.
   - Input the transaction amount.
   - Reject zero or negative amounts.
   - For a deposit, add the amount to the account balance.
   - For a withdrawal, check the per-transaction limit and available balance.
   - Approve valid transactions and reject invalid ones.
6. Record each transaction's type, amount, status, and resulting balance.
7. Calculate the total deposited, total withdrawn, number of successful transactions, and number of rejected transactions.
8. Display the final account balance and transaction summary.
9. Stop.
                                

                        #flowchart

                                      START
                |
                v
       Input initial balance
       and withdrawal limit
                |
                v
        Validate input values
                |
                v
       Input number of transactions
                |
                v
       Is another transaction left?
           /             \
         Yes              No
          |                |
          v                v
   Select transaction   Generate summary
      type and amount        |
          |                  v
          v             Display final balance
     Valid amount?           |
       /       \             |
      No       Yes           |
      |          |           |
      v          v           |
   Reject     Deposit or     |
 transaction  withdrawal?    |
                /    \       |
          Deposit  Withdraw  |
             |        |      |
             v        v      |
        Add amount  Check balance
        to balance  and limit
             |        |
             |        v
             |    Valid withdrawal?
             |      /       \
             |    Yes        No
             |     |          |
             |     v          v
             |   Deduct     Reject
             |   amount   transaction
             |     |          |
             +-----+----------+
                    |
                    v
          Record transaction result
                    |
                    +----> Next transaction
                               |
                               v
                              STOP



                              #code

                              
# Filename: atm_transaction_sequence_simulation.py

print("ATM TRANSACTION SEQUENCE SIMULATION")
print("-" * 45)

balance = float(input("Enter initial account balance: "))
withdrawal_limit = float(
    input("Enter maximum withdrawal per transaction: ")
)

if balance < 0 or withdrawal_limit <= 0:
    print("Invalid initial balance or withdrawal limit.")

else:
    number_of_transactions = int(
        input("Enter number of transactions: ")
    )

    if number_of_transactions < 0:
        print("Number of transactions cannot be negative.")

    else:
        total_deposited = 0.0
        total_withdrawn = 0.0
        successful = 0
        rejected = 0
        transaction_history = []

        for i in range(number_of_transactions):
            print(f"\nTransaction {i + 1}")
            print("1. Deposit")
            print("2. Withdraw")

            choice = input("Select transaction type (1/2): ")
            amount = float(input("Enter transaction amount: "))

            status = ""
            transaction_type = ""

            if amount <= 0:
                status = "Rejected: Invalid amount"
                transaction_type = "Invalid"

            elif choice == "1":
                balance += amount
                total_deposited += amount
                successful += 1
                status = "Successful"
                transaction_type = "Deposit"

            elif choice == "2":
                transaction_type = "Withdrawal"

                if amount > withdrawal_limit:
                    status = "Rejected: Exceeds withdrawal limit"
                    rejected += 1

                elif amount > balance:
                    status = "Rejected: Insufficient balance"
                    rejected += 1

                else:
                    balance -= amount
                    total_withdrawn += amount
                    successful += 1
                    status = "Successful"

            else:
                status = "Rejected: Invalid transaction type"
                transaction_type = "Invalid"

            # Count all rejected transactions, including invalid amounts.
            if status.startswith("Rejected") and amount <= 0:
                rejected += 1
            elif status.startswith("Rejected") and amount > 0:
                if choice not in ("1", "2"):
                    rejected += 1

            transaction_history.append({
                "number": i + 1,
                "type": transaction_type,
                "amount": amount,
                "status": status,
                "balance": balance
            })

            print("Status:", status)
            print(f"Available balance: Rs. {balance:.2f}")

        print("\n" + "=" * 76)
        print("TRANSACTION SUMMARY")
        print("=" * 76)
        print(
            f"{'No.':<5}{'Type':<15}{'Amount (Rs.)':>15}"
            f"{'Status':<38}"
        )
        print("-" * 76)

        for transaction in transaction_history:
            print(
                f"{transaction['number']:<5}"
                f"{transaction['type']:<15}"
                f"{transaction['amount']:>15.2f}"
                f"{transaction['status']:<38}"
            )

        print("-" * 76)
        print(f"Total deposited: Rs. {total_deposited:.2f}")
        print(f"Total withdrawn: Rs. {total_withdrawn:.2f}")
        print(f"Successful transactions: {successful}")
        print(f"Rejected transactions: {rejected}")
        print(f"Final account balance: Rs. {balance:.2f}")
                           

                           #output

                           ATM TRANSACTION SEQUENCE SIMULATION
---------------------------------------------
Enter initial account balance: 5000
Enter maximum withdrawal per transaction: 2000
Enter number of transactions: 4

Transaction 1
1. Deposit
2. Withdraw
Select transaction type (1/2): 1
Enter transaction amount: 1000
Status: Successful
Available balance: Rs. 6000.00

Transaction 2
1. Deposit
2. Withdraw
Select transaction type (1/2): 2
Enter transaction amount: 1500
Status: Successful
Available balance: Rs. 4500.00

Transaction 3
1. Deposit
2. Withdraw
Select transaction type (1/2): 2
Enter transaction amount: 2500
Status: Rejected: Exceeds withdrawal limit
Available balance: Rs. 4500.00

Transaction 4
1. Deposit
2. Withdraw
Select transaction type (1/2): 2
Enter transaction amount: 5000
Status: Rejected: Exceeds withdrawal limit
Available balance: Rs. 4500.00

============================================================================
TRANSACTION SUMMARY
============================================================================
No.  Type            Amount (Rs.)Status
----------------------------------------------------------------------------
1    Deposit              1000.00Successful
2    Withdrawal           1500.00Successful
3    Withdrawal           2500.00Rejected: Exceeds withdrawal limit
4    Withdrawal           5000.00Rejected: Exceeds withdrawal limit
----------------------------------------------------------------------------
Total deposited: Rs. 1000.00
Total withdrawn: Rs. 1500.00
Successful transactions: 2
Rejected transactions: 2
Final account balance: Rs. 4500.00