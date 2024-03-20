from core.booking import Booking


def test_create_booking_with_valid_data():
    booking = Booking(advertisement="4ec48510-2b1b-4a53-96b3-0e5b4bfc0f3c",
                      check_in_date="2024-03-10",
                      check_out_date="2024-03-13",
                      total_price=100,
                      guests_count=2)
    
    assert booking.guests_count == 2
    assert booking.total_price == 100