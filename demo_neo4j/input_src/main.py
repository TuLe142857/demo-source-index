from animal import Dog, create_dog

def run_simulation():
    my_dog = create_dog("Buddy")
    sound = my_dog.speak()
    print(f"{my_dog.name} says {sound}")

if __name__ == "__main__":
    run_simulation()
