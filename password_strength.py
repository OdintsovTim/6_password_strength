def check_lenth_password(password):
    if len(password) > 7:
        return True
    else:
        return False


def check_upper_case_in_password(password):
    return not password.islower()


def check_lower_case_in_password(password):
    return not password.isupper()


def check_digits_in_password(password):
    if password.isdigit():
        return False
    for letter in password:
        if letter in '123456789':
            return True
    return False


def check_symbols_in_password(password):
    for letter in password:
        if letter in '! " # $ % &  ( ) * + , - . / : ; < = > ? @ [ \ ] ^ ':
            return True
    return False


def get_password_strength(password):
    rating = 0
    if check_lenth_password(password):
        rating += 2
    if check_upper_case_in_password(password):
        rating += 2
    if check_lower_case_in_password(password):
        rating += 2
    if check_digits_in_password(password):
        rating += 2
    if check_symbols_in_password(password):
        rating += 2
    return rating


def main():
    password = input('Введите пароль для проверки его сложности: ')
    if len(password) < 4:
        print('Пароль слишком короткий')
        return
    rating = get_password_strength(password)
    print('Оценка сложности вашего пароля -', rating)

if __name__ == '__main__':
    main()
