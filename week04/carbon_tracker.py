import datetime
import random


def show_welcome_message():
  print("==================================================")
  print("🌱 SUSTAINABILITY & CARBON FOOTPRINT TRACKER 🌱")
  print("==================================================")

  # Türkiye saat dilimi (UTC+3) manuel ve hatasız ayarlama
  tr_timezone = datetime.timezone(datetime.timedelta(hours=3))
  current_time = datetime.datetime.now(tr_timezone)
  formatted_date = current_time.strftime("%Y-%m-%d %H:%M")
  print(f"Analysis Date & Time: {formatted_date}\n")


def calculate_score():
  total_score = 0

  # Question 1: Transportation
  print("1. How do you usually commute daily?")
  print("1 - Public Transport / Walking / Bicycle")
  print("2 - Private Car (Gasoline / Diesel)")
  transport_choice = input("Your choice (1 or 2): ")

  if transport_choice == "1":
    total_score += 30
  elif transport_choice == "2":
    total_score += 10
  else:
    print("Invalid choice! No points added for this question.")

  # Question 2: Recycling
  print(
      "\n2. Do you separate waste (plastic, paper, glass) for recycling at"
      " home?"
  )
  print("1 - Definitely yes")
  print("2 - Sometimes / Rarely")
  print("3 - No")
  recycling_choice = input("Your choice (1, 2, or 3): ")

  if recycling_choice == "1":
    total_score += 30
  elif recycling_choice == "2":
    total_score += 15
  elif recycling_choice == "3":
    total_score += 5
  else:
    print("Invalid choice! No points added for this question.")

  return total_score


def get_random_tip():
  # random library usage
  tips = [
      (
          "Using a reusable water bottle instead of single-use plastic bottles"
          " makes a huge difference!"
      ),
      (
          "Turning off lights in empty rooms cuts energy consumption"
          " significantly."
      ),
      (
          "Choosing to walk for short distances lowers your overall carbon"
          " footprint."
      ),
      (
          "Unplugging electronics when not in use prevents phantom power"
          " drain."
      ),
  ]

  return random.choice(tips)


def main():
  show_welcome_message()

  user_name = input("What is your name? ")
  print(
      f"Awesome {user_name}, let's start with small steps for our planet!\n"
  )

  score = calculate_score()

  print("\n--------------------------------------------------")
  print(f"RESULTS - Sustainability Score: {score} / 60")

  if score >= 50:
    print("Congratulations! You are a true eco-friendly individual.")
  elif score >= 25:
    print("Not bad, but small changes can help our planet even more!")
  else:
    print("Time to pay a bit more attention to our daily habits!")

  print("--------------------------------------------------")

  # Daily tip using random selection
  print("Daily Sustainability Tip:")
  print(f"💡 {get_random_tip()}")
  print("==================================================")


# Program Entry Point
if __name__ == "__main__":
  main()