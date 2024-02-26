print("Determine if a person is eligible for a discount on a movie ticket")
print("----------------------------------------------------")

age = int(input("Enter your age:"))
std = input("Are you a student? (yes/no):")

if age <= 12:
    print("Congrats! You are eligible for a discount on movie ticket. ")

elif 13 <= age <= 18 and std == "yes":
    print("Congrats! You are eligible for a discount on movie ticket.")

else:
    print("Sorry! You are not eligible for a discount on movie ticket.")
