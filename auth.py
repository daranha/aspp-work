def get_credentials():
    """Get credentials from user input"""
    user = input('Type user name: ')
    password = input('Type password: ')
    password_verif = input('Type password again: ')
    return user, password_verif

#def write_pwdd():

if __name__ == '__main__':
    get_credentials()
