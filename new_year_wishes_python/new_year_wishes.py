import time

print("🎆 Welcome to New Year Wishes Generator 🎆")
time.sleep(1)

name = input("Enter your name: ")
time.sleep(1)

print("\nGenerating your New Year wish...")
time.sleep(2)

print(f"""
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
🎉 Happy New Year 2025, {name}! 🎉

May this year bring you:
🌟 Success
💖 Happiness
🚀 Growth
💻 New Skills

Keep shining and chasing your dreams!
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
""")
with open("new_year_wishes.txt", "a") as file:
    file.write(f"Happy New Year 2025, {name}!\n")

print("🎁 Your wish has been saved successfully!")
