def shutdown():
    user_input = input("Do you want to shut down? (yes/no)").strip().lower()

    if user_input == "yes":
        print("Shutting down...")
    elif user_input == "no":
        print("Abort shut down")
    else:
        print("Sorry")

shutdown()        