import random
def password_generation(number):  
  
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
      
    password = ""  
  
    for i in range(number):  
        password = password + random.choice(characters)  
      
  
    return password

if __name__ == "__main__":  
    number=int(input("Enter the desired length:"))
    password = password_generation(number)  
    print("The password randomly generated is:", password)