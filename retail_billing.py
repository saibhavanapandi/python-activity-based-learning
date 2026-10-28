#Algorithm
1. Start the program.
2. Input the number of products purchased.
3. For each product, enter the product name, category, unit price, and quantity.
4. Calculate the subtotal for each product using unit price × quantity.
5. Apply category-specific taxes:
   - Electronics: 18%
   - Clothing: 5%
   - Groceries: 0%
   - Other items: 12%
6. Calculate the total subtotal of all products.
7. Apply threshold discounts:
   - Bill amount of ₹1,000 or more: 5% discount.
   - Bill amount of ₹5,000 or more: 10% discount.
8. Limit the discount to a maximum concession of ₹1,000.
9. Calculate the final bill by adding taxes and subtracting the discount.
10. Display an itemized invoice containing product details, quantities, subtotals, taxes, discount, and final payable amount.
11. Stop the program.


                 #flowchart

                                  START
                   |
                   v
          Enter Number of Products
                   |
                   v
       Enter Product Name, Category,
            Price and Quantity
                   |
                   v
        Calculate Item Subtotal
          (Price x Quantity)
                   |
                   v
       Apply Category-Specific Tax
                   |
                   v
          More Products?
            /        \
          Yes         No
           |           |
           v           v
      Enter Next   Calculate Total
       Product      Subtotal
                       |
                       v
             Check Discount Threshold
                       |
                       v
              Calculate Discount
                       |
                       v
             Apply Maximum Discount
                  Limit (Rs. 1000)
                       |
                       v
            Calculate Final Bill
       (Subtotal + Tax - Discount)
                       |
                       v
             Generate Itemized Invoice
                       |
                       v
                      STOP




                      #code

                      
# Retail Billing with Multiple Discount Rules

TAX_RATES = {
    "electronics": 0.18,
    "clothing": 0.05,
    "groceries": 0.00,
    "other": 0.12
}

MAX_DISCOUNT = 1000.00


def calculate_discount(subtotal):
    if subtotal >= 5000:
        discount_rate = 0.10
    elif subtotal >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0.00

    discount = subtotal * discount_rate
    return min(discount, MAX_DISCOUNT)


def main():
    products = []
    n = int(input("Enter number of products: "))

    if n <= 0:
        print("Number of products must be positive.")
        return

    total_subtotal = 0.0
    total_tax = 0.0

    for i in range(n):
        print(f"\nProduct {i + 1}")

        name = input("Product name: ")
        category = input(
            "Category (electronics/clothing/groceries/other): "
        ).lower()

        if category not in TAX_RATES:
            print("Invalid category. Using 'other'.")
            category = "other"

        price = float(input("Unit price (Rs.): "))
        quantity = int(input("Quantity: "))

        if price < 0 or quantity <= 0:
            print("Invalid price or quantity. Try again.")
            continue

        subtotal = price * quantity
        tax = subtotal * TAX_RATES[category]

        products.append({
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "subtotal": subtotal,
            "tax_rate": TAX_RATES[category] * 100,
            "tax": tax
        })

        total_subtotal += subtotal
        total_tax += tax

    discount = calculate_discount(total_subtotal)
    final_bill = total_subtotal + total_tax - discount

    print("\n" + "=" * 78)
    print("                 RETAIL STORE INVOICE")
    print("=" * 78)

    print(
        f"{'Product':<16}{'Category':<14}{'Price':>9}"
        f"{'Qty':>5}{'Subtotal':>12}{'Tax':>10}"
    )
    print("-" * 78)

    for p in products:
        print(
            f"{p['name']:<16}{p['category']:<14}"
            f"{p['price']:>9.2f}{p['quantity']:>5}"
            f"{p['subtotal']:>12.2f}{p['tax']:>10.2f}"
        )

    print("-" * 78)
    print(f"Total subtotal:       Rs. {total_subtotal:.2f}")
    print(f"Total category tax:   Rs. {total_tax:.2f}")
    print(f"Discount:             Rs. {discount:.2f}")
    print(f"Maximum concession:   Rs. {MAX_DISCOUNT:.2f}")
    print("-" * 78)
    print(f"FINAL BILL:           Rs. {final_bill:.2f}")
    print("=" * 78)


if __name__ == "__main__":
    main()



                          #output


Enter number of products: 3

Product 1
Product name: Laptop
Category (electronics/clothing/groceries/other): electronics
Unit price (Rs.): 2000
Quantity: 2

Product 2
Product name: Shirt
Category (electronics/clothing/groceries/other): clothing
Unit price (Rs.): 1000
Quantity: 2

Product 3
Product name: Rice
Category (electronics/clothing/groceries/other): groceries
Unit price (Rs.): 100
Quantity: 5

==============================================================================
                 RETAIL STORE INVOICE
==============================================================================
Product         Category          Price  Qty    Subtotal       Tax
------------------------------------------------------------------------------
Laptop          electronics     2000.00    2     4000.00    720.00
Shirt           clothing        1000.00    2     2000.00    100.00
Rice            groceries        100.00    5      500.00      0.00
------------------------------------------------------------------------------
Total subtotal:       Rs. 6500.00
Total category tax:   Rs. 820.00
Discount:             Rs. 650.00
Maximum concession:   Rs. 1000.00
------------------------------------------------------------------------------
FINAL BILL:           Rs. 6670.00
==============================================================================
                