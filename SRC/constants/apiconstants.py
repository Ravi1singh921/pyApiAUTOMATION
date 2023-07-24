# add your constants here


# adding the url constants, python-->functions
def base_url():
    return "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"

def URL_create_token():
    return "https://restful-booker.herokuapp.com/auth"

def urlL_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking" + booking_id