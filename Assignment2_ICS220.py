from enum import Enum
class gender(Enum):
    Male = 1
    Female = 2
class Person:
    def __init__(self, firstName, lastName, phoneNo, age, gender):
        self.firstName = firstName
        self.lastName= lastName
        self.phoneNo = phoneNo
        self.age = age
        self.gender = gender

    def setFirstName(self, firstName):
        self.firstName = firstName
    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName):
        self.lastName= lastName
    def getLastName(self):
        return self.lastName

    def setPhoneNo(self, phoneNo):
        self.phoneNo = phoneNo
    def getPhoneNo(self):
        return self.phoneNo

    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

    def setGender(self, gender):
        self.gender =gender
    def getGender(self):
        return self.gender

    def __str__(self):
        return f"Name: {self.getFirstName()} {self.getLastName()}, Phone Number: {self.getPhoneNo()}, Age: {self.getAge()}, Gender: {self.getGender()}"

class ticketType(Enum):
    Adults = 1
    Children = 2
    Teacher = 3
    Student = 4
    Senior = 5
    Group = 6
    SpecialEvent = 7


class Visitor(Person):
    def __init__(self, firstName, lastName, phoneNo, age, gender, ticketType):
        Person.__init__(self, firstName, lastName, phoneNo, age, gender)
        self.ticketType = ticketType

    def setTicketType(self, ticketType):
        self.ticketType = ticketType
    def getTicketType(self):
        return self.ticketType
    def __str__(self):
        return Person.__str__(self)+ f"Ticket Type: {self.getTicketType()}"

class Ticket:
    def __init__(self, ticketID, timeDuration, location, tourDate, specialLocation, specialDuration):
        self.visitor = ""
        self.ticketID =ticketID
        self.timeDuration = timeDuration
        self.location = location
        self.tourDate = tourDate
        self.specialLocation = specialLocation
        self.specialDuration = specialDuration
        self.receipt = ""


    def addVisitor(self, firstName, lastName, phoneNo, age, gender, ticketType):
        v = Visitor(firstName, lastName, phoneNo, age, gender, ticketType)
        self.visitor = v

    def getVisitor(self):
        return self.visitor.firstName + self.visitor.lastName


    def setTicketID(self, ticketID):
        self.ticketID = ticketID
    def getTicketID(self):
        return self.ticketID

    def setTimeDuration(self, timeDuration):
        self.timeDuration = timeDuration
    def getTimeDuration(self):
        return self.timeDuration

    def setLocation(self, location):
        self.location = location
    def getLocation(self):
        return self.location

    def setTourDate(self, tourDate):
        self.tourDate = tourDate
    def getTourDate(self):
        return self.tourDate

    def setSpecialLocation(self, specialLocation):
        self.specialLocation = specialLocation
    def getSpecialLocation(self):
        return self.specialLocation

    def setSpecialDuration(self, specialDuration):
        self.specialDuration = specialDuration
    def getSpecialDuration(self):
        return self.specialDuration

    def __str__(self):
        return f"Visitor: {self.getVisitor()}, Ticket ID:{self.getTicketID()}, Time Duration: {self.getTimeDuration()}, Location:{self.getLocation()}, Tour Date: {self.getTourDate()}, Special Event Location: {self.getSpecialLocation()}, Special Event Duration: {self.getSpecialDuration()} "
class Receipt:
    def __init__(self, ticketType, ticketID):
        self.ticketType = ticketType
        self.ticketID = ticketID
        self.price = 0

    def setTicketType(self, ticketType):
        self.ticketType = ticketType
    def getTicketType(self):
        return self.ticketType

    def setTicketID(self, ticketID):
        self.ticketID = ticketID
    def getTicketID(self):
        return self.ticketID

    def calculatePrice(self):
        if self.ticketType.value == 1:
            self.price = 63 + 63*0.05

        if self.ticketType.value in range(2, 6):
            self.price = 0

        if self.ticketType.value == 6:
            self.price = 63 * 0.5

        if self.ticketType.value == 7:
            self.price = 63 + 63*0.05

    def getPrice(self):
        self.calculatePrice()
        return self.price

    def __str__(self):
        return f"Ticket Type: {self.getTicketType()}, Ticket ID: {self.getTicketID()}, Price: {self.getPrice()} "

class exhibitionLocation(Enum):
    permenantGallery = 1
    exhibitionHall= 2
    outdoorSpace = 3
class Artwork:
    def __init__(self, title, artist, createDate,history, exhibitionLocation ):
        self.title = title
        self.artist = artist
        self.createDate = createDate
        self.history = history
        self.exhibitionLocation = exhibitionLocation

    def setTitle(self, title):
        self.title = title
    def getTitle(self):
        return self.title

    def setArtist(self, artist):
        self.artist = artist
    def getArtist(self):
        return self.artist

    def setCreateDate(self, createDate):
        self.createDate = createDate
    def getCreateDate(self):
        return self.createDate

    def setHistory(self, history):
        self.history = history
    def getHistory(self):
        return self.history

    def setExhibitionLocation(self, exhibitionLocation):
        self.exhibitionLocation = exhibitionLocation
    def getExhibitionLocation(self):
        return self.exhibitionLocation

    def __str__(self):
        return f"Title: {self.getTitle()}, Artist: {self.getArtist()}, Creation Date: {self.getCreateDate()}, Historical Significance: {self.getHistory()}, Exhibition Location: {self.getExhibitionLocation()}"

class Exhibition:
    def __init__(self, location, timeDuration):
        self.location = location
        self.timeDuration = timeDuration
        self.artworks = []

    def setLocation(self, location):
        self.location = location
    def getLocation(self):
        return self.location

    def setTimeDuration(self, timeDuration):
        self.timeDuration = timeDuration
    def getTimeDuration(self):
        return self.timeDuration

    def __str__(self):
        return f" Location of Exhibition: {self.getLocation()}, Time Duration: {self.getTimeDuration()}"

#Test Cases
#Adding an artwork peice to a specific location in the exhibition
art1 = Artwork("Starry Night", "Vincent Van Gogh", 1889, "an oil-on-canvas painting by the Dutch Post-Impressionist painter", exhibitionLocation.permenantGallery)
#Displaying the information about the artwork
print(art1)
#Purchasing a ticket Case 1
ticket1 = Ticket("T01234", "12:30 - 2:30", "Main Gallery", "01/05/2024", "Exhibition Hall 1", "1:00 - 1:45" )
ticket1.addVisitor("Wadema", "Alremeithi", "0501234567", "19", gender.Female, ticketType.Student)
#Display Ticket information
print(ticket1)
#display the visitor's infromation
print(ticket1.visitor)
#Getting the receipt for the visitor
receipt1 =Receipt(ticketType.Student, "T01234")
print(receipt1)

#Purchasing a ticket Case 2
ticket2 = Ticket("T01236", "12:30 - 2:30", "Main Gallery", "01/05/2024", "Exhibition Hall 1", "1:00 - 1:45" )
ticket2.addVisitor("Mohamed", "Alremeithi", "0501234567", "22", gender.Male, ticketType.Adults)
#Display Ticket information
print(ticket2)
#display the visitor's infromation
print(ticket2.visitor)
#Getting the receipt for the visitor
receipt2 =Receipt(ticketType.Adults, "T01236")
print(receipt2)

