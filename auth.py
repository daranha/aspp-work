det get_credentials():
    user = input('Type user name: ')
    password = input('Type password: ')
    password_verif = input('Type password again: ')
    return user, password_verif


get_credentials()
