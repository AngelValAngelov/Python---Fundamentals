class Email:
    list_mail = list()

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def mail(self):
        Email.list_mail.append(list_message)
        return Email.list_mail

    def solve(self):
        num = list(numbers)
        for i in range(len(email.list_mail)):
            if str(i) in num:
                self.is_sent = True
                print(f"{email.list_mail[i][0]} says to {email.list_mail[i][1]}: "
                      f"{email.list_mail[i][2]}. Sent: {self.is_sent}")
            else:
                self.is_sent = False
                print(f"{email.list_mail[i][0]} says to {email.list_mail[i][1]}: "
                      f"{email.list_mail[i][2]}. Sent: {self.is_sent}")


email = Email

list_message = input()
while list_message != "Stop":
    list_message = list_message.split()
    email = Email(list_message[0], list_message[1], list_message[2])
    email.mail()
    list_message = input()
numbers = input()
email.solve()
