# 56.Static method to convert units (like km to miles).

class UnitConverter:
    KM_TO_MILES = 0.621371
    MILES_TO_KM = 1.60934

    @staticmethod
    def km_to_miles(km: float) -> float:
        return km * UnitConverter.KM_TO_MILES

    @staticmethod
    def miles_to_km(miles: float) -> float:
        return miles * UnitConverter.MILES_TO_KM

# Example usage:
print(UnitConverter.km_to_miles(10))    # Output: 6.21371
print(UnitConverter.miles_to_km(6.2))   # Output: 9.978308
