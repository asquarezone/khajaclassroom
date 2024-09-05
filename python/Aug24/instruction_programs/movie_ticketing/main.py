"""This module will have sampe usage code
"""
from ticketing.movie import User,Movie
from ticketing.theatre import Theatre,Screen,Seat
from ticketing.bookings import Screening,Booking,Payment

### Create a user

user_1 = User("xyz1", "xyz1@gmail.com")
user_2 = User("xyz2", "xyz2@gmail.com")


### Create a Theatre

gokul = Theatre("Gokul")

single_screen = Screen("single")
for row in "ABCDEFGHIJKLMN":
    for index in range(1,21):
        seat = Seat(row,index)
        single_screen.add_seat(seat)

gokul.add_screen(single_screen)

# Create a Movie
ironman = Movie(title='IronMan', language="English")



# Create a screening
screening = Screening(gokul, ironman)
screening.add_showtime(0,"11:15 AM")
screening.add_showtime(0,"2:15 PM")
screening.add_showtime(0, "6:15 PM")
screening.add_showtime(0, "9:15 PM")

# Create a booking

p = Payment()
p.payment_done(user_1, 200)
b = Booking()
b.book_ticket(user_1,screening,gokul.screens[0].seats[0],p)


