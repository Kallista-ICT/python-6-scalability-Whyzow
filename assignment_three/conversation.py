import greetings

def time(hour):
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    else:
        return "evening"

def main():
    name = input("What's your name? ")
    try:
        hour = int(input(f"{name}, what time is it now? My clock is not working. (0 ~ 23)  "))
        if hour < 0 or hour > 23:
            return ValueError

        period = time(hour)
        if period == "morning":
            print(greetings.good_morning(name))
        elif period == "afternoon":
            print(greetings.good_afternoon(name))
        else:
            print(greetings.good_evening(name))
    except ValueError:
        print("That's not a valid time. Please enter an hour between 0 and 23.")

if __name__ == "__main__":
    main()
