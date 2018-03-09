# qmail-spamlist-pycontrol

email_alias = ''

def get_email_alias(email_alias):
    print('Enter new Spam Alias (replace . with :):')
    email_alias = raw_input()
    return email_alias
#### todo: automaticly replace . with :

def get_choice(email_alias):
    while choice != 'invalid':
        print('How should we handle mails addressed to {}? 1/2/3'.format(email_alias))
        print('1 - delete')
        print('2 - forward')
        print('3 - bounce')
        print('0 - abort')
        choice_input = raw_input()
        if choice_input == '1':
            return 'deleted'
        elif choice_input == '2':
            return 'forwarded'
        elif choice_input == '3':
            return 'bounced'
        elif choice_input == '0':
            return 'abort'
        else:
            print('no vaild choice, try again ;-)')
####### todo: add more than one choice, e.g. forward and bounce

def write_qmail_file(email_alias, choice):
    if choice != 'abort':
        filename = '.qmail-{}'.format(email_alias)
        with open(filename, 'w') as f:
            if choice == 'deleted':
                print >>f,('# don\'t deliver mail to this alias, just delete it')
            elif choice == 'forwarded':
                print('Where should we forward mails addressed to {}? 1/2/3'.format(email_alias))
                email_forward = raw_input()
                print >>f,(email_forward)
            elif choice == 'bounced':
                print >>f,('|exit 100')
        print('Mails to {} will be {}'.format(email_alias, choice))
########todo: convert : back to .

add_another = True
email_alias = ''
choice = ''

print('Welcome to the qmail alias controller')
print
while add_another:
    email_alias = get_email_alias(email_alias)
### todo: check, if alias is allready known
    choice = get_choice(email_alias)
    if choice is not '':
        write_qmail_file(email_alias, choice)
    print('Add another alias? y/n')
    answer = raw_input()
    if answer == 'n':
        add_another = False
print('Bye.')
