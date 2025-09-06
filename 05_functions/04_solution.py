def print_kwargs(name, power):
    print("name: ", name , "power: ", power)

print_kwargs(power = "9000", name = "goku")

def print_kwargs2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_kwargs2(name = "vegeta", power = "8000", age = 48)