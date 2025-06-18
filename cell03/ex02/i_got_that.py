while True:
    user_input = input("Whatchu gotta say? : " if 'user_input' not in locals() else "I got that! Anything else? : ")
    if user_input.strip().upper() == "STOP":
        break