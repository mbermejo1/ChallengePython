print("Welcome!")
name = input("your name? ").capitalize()

print("Nice to see you", name)
print("This is a program that will count the times the letter you choose appears in your message.")
message = input("Write a message.")
letter = input("whitch letter would you like to count?")


print("The letter you chose appeared", message.count(letter), "times")