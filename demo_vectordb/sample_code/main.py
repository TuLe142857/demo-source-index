from helper import Speaker, say_hello, Cat, Dog

def local_utility():
    print("Doing some local utility work.")

def run_all():
    # Call to imported function
    say_hello("Antigravity")
    
    # Call to class constructor and method
    sp = Speaker()
    message = sp.speak()
    print(message)
    
    # Call to Cat and Dog speak methods
    my_cat = Cat()
    print(my_cat.speak())
    
    # Call to Dog speak method
    my_dog = Dog()
    print(my_dog.speak())
    
    # Call to local function
    local_utility()

if __name__ == "__main__":
    run_all()
