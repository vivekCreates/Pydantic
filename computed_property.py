from pydantic import BaseModel,computed_field,Field



class HotelBooking(BaseModel):
    user_id: int
    room_id: int
    members: int
    nights: int = Field(
        ...,
        ge=1
    )
    rate_per_nights: int 
    
    @computed_field
    @property
    def total_amount(self)-> float:
        return self.nights * self.rate_per_nights
    
    
hotel = HotelBooking(
    user_id=12,
    room_id=34,
    members=3,
    nights=3,
    rate_per_nights=500.0
    
    
)
    
print("Hotel: ",hotel.total_amount)