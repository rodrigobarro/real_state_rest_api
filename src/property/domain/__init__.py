class Property:
    def __init__(self, property_id, max_guests, bathrooms_quantity, pets_allowed, 
                 cleaning_fee, activation_date, created_at, updated_at):
        self.property_id = property_id
        self.max_guests = max_guests
        self.bathrooms_quantity = bathrooms_quantity
        self.pets_allowed = pets_allowed
        self.cleaning_fee = cleaning_fee
        self.activation_date = activation_date
        self.created_at = created_at
        self.updated_at = updated_at