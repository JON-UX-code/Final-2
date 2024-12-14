class Calculator:
    def __init__(self, output_label, circle_button, lineEdit, label_2, square_button, lineEdit_2, label_3, rectangle_button, triangle_button, lineEdit_5,lineEdit_6,lineEdit_3,lineEdit_4,label_4,label_5,label_6,label_7):
        self.output_label = output_label
        self.circle_button = circle_button
        self.lineEdit = lineEdit
        self.label_2 = label_2
        self.square_button = square_button
        self.lineEdit_2 = lineEdit_2
        self.label_3 = label_3
        self.rectangle_button = rectangle_button
        self.triangle_button = triangle_button
        self.lineEdit_5=lineEdit_5
        self.lineEdit_6=lineEdit_6
        self.lineEdit_4=lineEdit_4
        self.lineEdit_3=lineEdit_3
        self.label_6 = label_6
        self.label_7 = label_7
        self.label_4 = label_4
        self.label_5 = label_5




        self.shape = None
        self.current_value = "0"

    def append_to_display(self, value):
        """Appends the value (button clicked) to the current display."""
        current_text = self.output_label.text()
        if current_text == "0":
            self.output_label.setText(value)
        else:
            self.output_label.setText(current_text + value)

    def clear_display(self):
        """Clears the display."""
        self.output_label.setText("0")

    def delete_last_char(self):
        """Deletes the last character from the display."""
        current_text = self.output_label.text()
        if len(current_text) > 1:
            self.output_label.setText(current_text[:-1])
        else:
            self.output_label.setText("0")

    def toggle_sign(self):
        """Toggles the sign of the current number."""
        current_text = self.output_label.text()
        if current_text.startswith("-"):
            self.output_label.setText(current_text[1:])
        else:
            self.output_label.setText("-" + current_text)

    def calculate_result(self):
        """Calculates the result of the current expression."""
        current_text = self.output_label.text()
        try:
            # Replace 'x' with '*' and '/' remains '/' for evaluation
            expression = current_text.replace('x', '*').replace('/', '/')
            result = str(eval(expression))
            self.output_label.setText(result)
        except Exception as e:
            self.output_label.setText("Error")

    def enable_resizing(self):
        """Enables resizing of the window when the Mode button is pressed and resizes it to 613x642."""
        self.output_label.window().resize(613, 642)  # Change size to 613x642
        self.output_label.window().setMinimumSize(363, 642)  # Optional: Set a minimum size
        self.output_label.window().show()

    def back_resizing(self):
        """Enables resizing of the window to its original size."""
        self.output_label.window().resize(363, 642)
        self.output_label.window().setMinimumSize(363, 642)  # Optional: Set a minimum size
        self.output_label.window().show()

    def circle_options(self):
        """Activate the circle area calculation mode."""
        self.shape = "circle"
        self.label_2.setText("Radius")
        self.circle_button.setText("Enter")
        self.lineEdit.clear()
        self.label_2.setVisible(True)
        self.lineEdit.setVisible(True)
        self.circle_button.setVisible(True)
        self.label_3.setVisible(False)  # Hide label_3 for the circle

    def square_options(self):
        """Activate the square area calculation mode."""
        self.shape = "square"
        self.label_3.setText("Side Length:")
        self.square_button.setText("Enter")
        self.lineEdit.clear()
        self.label_2.setVisible(True)
        self.lineEdit.setVisible(True)
        self.square_button.setVisible(True)
        self.label_3.setVisible(False)  # Hide label_3 for the square

    def rectangle_options(self):
        """Activate the rectangle area calculation mode."""
        self.shape = "rectangle"
        self.label_4.setText("Length:")
        self.label_5.setText("Width:")
        self.rectangle_button.setText("Enter")
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.lineEdit.setVisible(True)
        self.lineEdit_2.setVisible(True)
        self.rectangle_button.setVisible(True)

    def triangle_options(self):
        """Activate the triangle area calculation mode."""
        self.shape = "triangle"
        self.label_6.setText("Base:")
        self.label_7.setText("Height:")
        self.triangle_button.setText("Enter")
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.lineEdit.setVisible(True)
        self.lineEdit_2.setVisible(True)
        self.triangle_button.setVisible(True)

    def calculate_area(self, result=None):
        """Calculate the area based on the shape and input values."""
        if self.shape == "circle":
                radius = float(self.lineEdit.text())
                area = 3.1416 * (radius ** 2)  # Area of circle (πr²)
                self.output_label.setText(f"Area: {area:.2f}")

        elif self.shape == "square":
                side = float(self.lineEdit_2.text())
                area = side ** 2  # Area of square (side²)
                self.output_label.setText(f"Area: {area:.2f}")

        elif self.shape == "rectangle":
                length = float(self.lineEdit_3.text())
                width = float(self.lineEdit_4.text())
                area = length * width  # Area of rectangle (length × width)
                self.output_label.setText(f"Area: {area:.2f}")

        elif self.shape == "triangle":
            base = float(int(self.lineEdit_5.text()))
            height = float(int(self.lineEdit_6.text()))
            area = 0.5 * base * height  # Area of triangle (0.5 × base × height)
            self.output_label.setText(f"Area: {area:.2f}")








