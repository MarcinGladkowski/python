class Button:
    def __init__(self, label):
        self.label = label

        self.click_action = lambda: self.display_label(self)

    def display_label(self, button_bound):
        print(f"Button pressed: {button_bound.label}")

    def click(self):
        self.click_action()


buttonA = Button("Submit")
buttonB = Button("Cancel")

buttonA.click()
buttonB.click()