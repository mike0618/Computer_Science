class Temp_conv:
    # Calculations
    def ftoc(self, fahrenheit: float) -> float:
        """Fahrenheit to Celsius"""
        return (fahrenheit - 32) / 1.8

    def ftok(self, fahrenheit: float) -> float:
        """Fahrenheit to Kelvin"""
        return self.ftoc(fahrenheit) + 273.15
