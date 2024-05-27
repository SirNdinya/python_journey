def calculate_discount(price, discount_percent):
    if discount_percent < 20:
         price
    else:
        discount_amount = price * (discount_percent / 100)
        final_price_ = price - discount_amount
        return final_price_


price_of_itme = float(input("Enter the original price of the item: "))
discount = float(input("Enter the percentage discount: "))
calculate_discount(price_of_itme, discount)
final_price = calculate_discount(price_of_itme, discount)

print(f"Final price after discount: {final_price}")