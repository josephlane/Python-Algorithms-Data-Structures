class Queue:
    
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Customer:

    def __init__(self, ticketNum, name):
        self.ticketNum = ticketNum
        self.name = name

    def getName(self):
        return self.name

    def getTicketNum(self):
        return self.ticketNum

class WaitingApp:

    def __init__(self):
        self.customer = ""
        self.customerQueue = Queue()

    def addCustomer(self, ticketNum, name):
        self.customer = Customer(ticketNum, name)
        self.customerQueue.enqueue(self.customer)
        
    def nextInLine(self):
        cust = self.customerQueue.dequeue()
        return "Now Server Ticket Num: " + cust.getTicketNum() + " - " + cust.getName()

    
