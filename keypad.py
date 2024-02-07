from machine import Pin
from time import sleep

__version__ = '1.0.3'
__author__ = 'Teeraphat Kullanankanjana'

class KeypadException(Exception):
    """
    Exception class for keypad-related errors.
    """
    pass

class Keypad:
    def __init__(self, row_pins, column_pins, keys):
        """
        Initialize the keypad object.

        Args:
            row_pins (list): List of row pins.
            column_pins (list): List of column pins.
            keys (list): 2D list representing the key layout.

        Raises:
            KeypadException: If pins or keys are not properly defined.
        """
        if not all(isinstance(pin, Pin) for pin in row_pins):
            raise KeypadException("Row pins must be instances of Pin.")
        
        if not all(isinstance(pin, Pin) for pin in column_pins):
            raise KeypadException("Column pins must be instances of Pin.")
        
        if not isinstance(keys, list) or not all(isinstance(row, list) for row in keys):
            raise KeypadException("Keys must be a 2D list.")

        self.row_pins = row_pins
        self.column_pins = column_pins
        self.keys = keys

        for pin in self.row_pins:
            pin.init(Pin.IN, Pin.PULL_UP)

        for pin in self.column_pins:
            pin.init(Pin.OUT)

        if len(self.row_pins) != len(self.keys) or len(self.column_pins) != len(self.keys[0]):
            raise KeypadException("Number of row/column pins does not match the key layout size.")

    def read_keypad(self):
        """
        Read the keypad and return the pressed key.

        Returns:
            str or None: Pressed key or None if no key is pressed.

        Raises:
            KeypadException: If pins or keys are not properly defined.
        """
        if not self.column_pins:
            raise KeypadException("No column pins defined.")
        
        if not self.row_pins:
            raise KeypadException("No row pins defined.")
        
        if not self.keys:
            raise KeypadException("No key layout defined.")

        for col_pin in self.column_pins:
            col_pin.value(0)  # Set column pin to LOW
            for i, row_pin in enumerate(self.row_pins):
                if not row_pin.value():  # If row pin reads LOW
                    key_pressed = self.keys[i][self.column_pins.index(col_pin)]
                    col_pin.value(1)  # Set column pin back to HIGH
                    return key_pressed
            col_pin.value(1)  # Set column pin back to HIGH
        return None  # Return None if no key is pressed
