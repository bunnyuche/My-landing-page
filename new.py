def checkuser(dictionary):
    username = input(f'username: ')
    try:
        if username in dictionary:
            for i in range(2):
                password = input(f'password: ')
                tries = i+1
                if dictionary[username] == password:
                    return True
                else:
                    print(f'Incorrect password \nMax no of tries = 3')
                    print(F'TRIES = {tries}')
            return f'Invalid Password'
    except:
        return f'Invalid username'

names = {'kc': 1234,'bunny': 1243}
checkuser(names)