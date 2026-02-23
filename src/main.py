def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False
def has_uppercase(password):
    for char in password: # using loop to check if any letter has capital letter in it 
        if char.isupper(): # checks if the character is uppercase
            return True
    else:
        return False
def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    else:
        return False
def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    else:
        return False

def has_special_character(password):
    for char in password:
        if char in "!@#$%^&*":
            return True
    else:
        return False


COMMON_PASSWORDS =     ["password", "123456", "qwerty"
]
def is_common_password(password):
    for common in COMMON_PASSWORDS:
        if password.lower() == common.lower():
            return True
    else:
        return False

def calculate_score(password):
    score = 0
    if check_length(password):
        score += 1
    if has_uppercase(password):
        score +=1
    if has_lowercase(password):
        score += 1
    if has_digit(password):
        score +=1
    if has_special_character(password):
        score += 1
    if len(password) > 12:
        score += 1
    if is_common_password(password):
        score = max(score - 1, 0)
    return score

def get_strength_rating(score):
    if score >= 0 and score <= 2:
        return "Weak"
    elif score >= 3 and score <= 4:
        return "Moderate"
    else:
        return "Strong"

def main():
    password = input("Enter a password: ")


    length_ok = check_length(password)
    has_upper = has_uppercase(password)
    has_lower = has_lowercase(password)
    has_number = has_digit(password)
    special_char = has_special_character(password)
    has_common = is_common_password(password)
    score = calculate_score(password)
    rate_strength = get_strength_rating(score)

    
    print("\nPassword check results:")
    print("Lenght check:", length_ok)
    print("Has uppercase:", has_upper)
    print("Haslowercase:", has_lower)
    print("Has a digit:", has_number)
    print("Has special character:",special_char)
    print("Is common password:",has_common)
    print("Score: ", score)
    print("Rating:",rate_strength)
if __name__ == "__main__":
    main()

