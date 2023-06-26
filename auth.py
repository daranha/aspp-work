import json

def write_pwdb(user, password):
    pwdb = {}
    pwdb[user] = password
    fn = 'database.json'
    with open(fn, 'w') as f:
        json.dump(pwdb, f)



def get_credentials():
    """This is more and more useless"""
    user = input('Type user name: ')
    password = input('Type password: ')
    password_verif = input('Type password again: ')
    return user, password_verif

#def write_pwdd():

if __name__ == '__main__':
    user, password = get_credentials()
    write_pwdb(user, password)
