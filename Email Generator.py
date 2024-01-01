import random
first = ('gary', 'david', 'chrispus', 'jared', "selicia", "luke", 'conley', 'caden', 'aiden', 'liam', 'emma', 'noah', 'olivia', 'oliver', 'william', 'ava', 'james', 'isabella', 
'sophia', 'benjamin', 'charlotte', 'elijah', 'mia', 'lucas', 'amelia', 'mason', 'harper', 'logan', 'evelyn')
last = ('watkins', 'mwampea', 'culver', 'bentley', 'bishop', 'Smith', 'johnson', 'williams', 'brown', 'jones', 'garcia', 'miller', 'davis', 'rodriguez', 'martinez', 'ernandez', 'lopez', 'gonzalez', 'wilson', 'anderson', 'thomas', 'taylor', 'moore', 'jackson', 'martin')
number1 = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50")
number2 = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50")
suffix = ("hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com", "state.gov", "mail.ru", "bk.ru", "list.ru", 'humbleisd.net', 'mid.ru')
first = random.choice(first)
last = random.choice(last)
number1 = random.choice(number1)
number2 = random.choice(number2)
suffix = random.choice(suffix)
class Email:
    

    def __init__(self, first, last, number1, number2, suffix):
        self.first = first
        self.last = last
        self.number1 = number1
        self.number2 = number2
        self.suffix = suffix

        print('New Email for Ayo: {}'.format(self.email))

    @property
    def email(self):
        return '{}{}{}{}@{}'.format(self.first, self.last, self.number1, self.number2, self.suffix)

emp_1 = Email(first, last, number1, number2, suffix)
