from car import Car

class Battery(Car):
    def needs_service(self):
        return super().needs_service()
