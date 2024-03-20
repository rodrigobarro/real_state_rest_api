import uuid
from datetime import datetime

class Booking:
    def __init__(self, advertisement, check_in_date, 
                 check_out_date, total_price, comment=None, 
                 guests_count=1):
        self.booking_id = str(uuid.uuid4())
        self.booking_code = str(uuid.uuid4())[:12]  
        self.advertisement = advertisement
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_price = total_price
        self.comment = comment
        self.guests_count = guests_count
        self.created_at = datetime.now()
        self.updated_at = datetime.now()