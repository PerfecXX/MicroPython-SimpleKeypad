MicroPython Simple Keypad
=========================

|MicroPython| |License|

MicroPython library for interfacing with a keypad matrix

Feature
-------

-  Supports any keypad matrix configuration.
-  Easily customizable for different keypad layouts.
-  Provides exception handling for error management.

Example Usage
-------------

Example for 4x4 keypad metrix on MicroPython esp32.

.. code:: python

   from machine import Pin
   from keypad import Keypad
   from time import sleep

   # Define GPIO pins for rows
   row_pins = [Pin(25),Pin(26),Pin(27),Pin(14)]

   # Define GPIO pins for columns
   column_pins = [Pin(23),Pin(22),Pin(19),Pin(18)]

   # Define keypad layout
   keys = [
       ['1', '2', '3', 'A'],
       ['4', '5', '6', 'B'],
       ['7', '8', '9', 'C'],
       ['*', '0', '#', 'D']]

   keypad = Keypad(row_pins, column_pins, keys)

   while True:
       key_pressed = keypad.read_keypad()
       if key_pressed:
           print("Key pressed:", key_pressed)
       sleep(0.1)  # debounce and delay

.. |MicroPython| image:: https://img.shields.io/badge/MicroPython-Ready-brightgreen.svg
.. |License| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
