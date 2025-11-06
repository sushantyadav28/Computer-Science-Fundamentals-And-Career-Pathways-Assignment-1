# Mobile recharge system
# NAME :- Sushant
# Roll no. :- 2501350065
# course :- B.Tech cse FSD
# Subject :- Computer Science Fundamentals And Career Pathway.


mobile = input("Enter your 10-digit mobile number: ")     # Step 1: Input mobile number and validate


while len(mobile) != 10 or not mobile.isdigit():   # Show error if no. is incorrect
    print("❌ Invalid number! Please enter a valid 10-digit mobile number.")
    mobile = input("Enter your 10-digit mobile number: ")

                                                   # Step 2: Display recharge plans
print("\n📱 Available Recharge Plans:")
print("1. ₹199 - 1.5GB/day for 28 days")
print("2. ₹299 - 2GB/day for 28 days")
print("3. ₹599 - 1.5GB/day for 84 days")


choice = input("\nEnter your choice (1/2/3): ")           # Step 3: Take user choice


plans = {'1': 199, '2': 299, '3': 599}        # Step 4: Check selected plan

if choice in plans:
    amount = plans[choice]
    print(f"\nYou selected a plan of ₹{amount}.")
    confirm = input("Do you want to confirm recharge? (Y/N): ")

    
    if confirm.lower() == 'y':        # Step 5: Confirmation
        print("\nProcessing payment...")
        print("✅ Recharge Successful!")
        print(f"₹{amount} has been deducted from your account.")
    else:
        print("\nRecharge Cancelled ❌")

else:
    print("\nInvalid plan selection! Please restart the program.")
