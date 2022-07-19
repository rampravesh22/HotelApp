class Hotel(BaseModel):
    amenities = models.ManyToManyField(Amenities,related_name="Amenities")
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.FloatField()
    description = models.TextField()
    room_count = models.IntegerField(default=10)