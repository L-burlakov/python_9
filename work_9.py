import string

from unittest import result


phone_book = {}

def save_new_rec(add_namenumber):
    global phone_book
    for_rec = add_namenumber.split(' ',1)
    phone_book [for_rec[0]] = for_rec[1]
    return 'Added'
    
def show_number(what_number):
    if what_number == 'all':
        for key,value in phone_book.items():
            a = print(key,':',value)
        return 'That`s all'  #' '.join(phone_book)
    else:
        for key,value in phone_book.items():
            if what_number == key:
                return value

def finish(some):
    print('Good Bye')
    return False

def start_the_bot(some):
    return 'How can I help U? '
    
    
    
operations = {'hello': start_the_bot, \
              'add': save_new_rec,\
              'change': save_new_rec,\
              'phone': show_number,\
              'show': show_number,\
              'good': finish,\
              'close': finish,\
              'exit': finish,\
              '.': finish}

def get_handler(words):
    return operations[words]
       
def parser_func(string_ask):
    some = 1
    ask_pars = string_ask.split(' ',1)
    handler = get_handler(ask_pars[0])
    if len(ask_pars) == 1:
        return handler(some)
    else:
        return handler(ask_pars[1])

    
def input_error(func):
    def inner():
        try:
            string_ask_dec = func()
            numb = string_ask_dec.split(' ',3)
            if len(numb)>2 and int(numb[2]) == False:
                raise Exception('Please, enter the digits')
            elif numb[0] not in operations:
                raise Exception('I don`t know this command')
            if numb[0] == 'add' and len(numb)<=2:
                raise Exception ('U haven`t wrote a number, try again')
            elif len(numb)>2 and len(numb[2]) != 10:
                raise Exception('This is not a number. It should be wth 10 digits')
        except Exception as e:
            print (e)

        else:
            return string_ask_dec
        # return string_ask_dec
    return inner

@input_error     
def main_func():
    string_ask_main = input('')
    string_ask_main = string_ask_main.lower()
    return string_ask_main
        

while True:    
    start_string = input('Start with hello \n')
    if start_string == 'hello' or start_string == 'Hello':
        print ('How can I help U? ')
        break
    else:
        print ('Please, be polite')
        continue
while True:
    string_ask = main_func()
    if string_ask == 'None' or string_ask == None or type(string_ask) == 'NoneType':
        continue
    d = parser_func(string_ask)
    if (type(d)) == bool:
        break
    else:
        print(d)
