#Zomato order
order_id=int(input("Enter a Order ID: "))
customer_name=str(input("Enter customer name: "))
customer_number=int(input("Enter mobile number: "))
beverages_name=input("Enter beverages name: ")
add_ons =list(input("Enter Items Ordered with quantity (format - item:qty, separated by commas): ").split(","))
price=int(input("Enter price: ₹"))
discount_percentage = float(input("Enter Discount Percentage: "))
coupons=int(input("Enter the number of coupons: "))
avilable_discount=int(input("Enter number of available discounts: "))
discount_details=(coupons,avilable_discount)
customer_location = input(" Enter deliver location: ")
delivery_time = set(input("How much time you want deliver: "))
payment=input("Payment will be Online or cash: ")
order_details={
    'Customer ordered' : beverages_name,
    'Customer add-ons' : add_ons,
    'Payment' : payment
}

#output
print('\nOutput:\n')

#Using Comma Separation (sep=',')
print("OrderID, Customer Name, customer_number: "+ str(order_id), customer_name, customer_number, sep=',')

#Using Percentage Formatting (% operator)
print("discount_Percentage: %.2f%%" % discount_percentage)

#using f-strings(f"")
print(f"Customer Name: {customer_name} \nCustomer number Contact No: {customer_number} \nPrice: ₹{price} \nDiscount Percentage: {discount_percentage}%")

#using.format()
print("Order Details: Customer ordered - {}, Customer add-ons -{},bill payment".format(order_details["Customer ordered"],order_details["Customer add-ons"],order_details["Payment"]))