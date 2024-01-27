def on_button_pressed_a():
    pins.digital_read_pin(DigitalPin.P0)
input.on_button_pressed(Button.A, on_button_pressed_a)
