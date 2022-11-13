import random
from tkinter import Button
import settings

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #Append the object to the Cell.all list - all is a class attribute
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click_actions) #<Button-1> convention de Left click y 3 es Right click
        btn.bind('<Button-3>', self.right_click_actions) #<Button-1> convention de Left click y 3 es Right click
        self.cell_btn_object = btn
        
    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!")

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self) -> str:
        return f"Cell({self.x},{self.y})"