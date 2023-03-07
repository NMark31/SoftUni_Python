class Email:
    def __init__(self, sender, receiver, content) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True
    
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
    

emails = []

while True:
    line = input()

    if line == "Stop":
        break

    sender, receiver, content = line.split()

    email = emails.append(Email(sender, receiver, content))

sent_mails = [int(i) for i in input().split(", ")]

for index, email in enumerate(emails):
    if index in sent_mails:
        email.send()

    print(email.get_info())

