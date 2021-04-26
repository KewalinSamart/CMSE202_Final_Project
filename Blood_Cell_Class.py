import random
import matplotlib.pyplot as plt

class blood_cell():
    '''
    This is the blood cells class and it allows the blood cells to move around as well as absorb oxygen and carbon dioxide.
    '''
    
    def __init__(self, dims, color = 'blue'): #We could change the shape attribute to an oxygen capacity attribute
        '''
        The __init__ function takes a single x and y coordinate in the form of a list containing two integer elements as 
        an input. It also takes in the color of the blood cell as a string. The function then indexes the list and assigns 
        the integer elements to two variables.
        '''
   
        self.x = dims[0]
        self.y = dims[1]
        
        self.color = color 
        
        
    def transfer(self):
        '''
        The transfer function does not require any inputs and it changes the color of the blood cell depending on its 
        location on the board (in an organ or in lungs).
        '''
        
        if 70 < self.x < 135 and 5 < self.y < 40:
            
            color = 'blue'
            self.color = color
            
        elif 80 < self.x < 120 and ((140 < self.y < 160) or (170 < self.y < 190 ) or (200 < self.y < 220)):
            
            color = 'red'
            self.color = color
        
    def draw(self):
        '''
        The draw function doesn't require any inputs and plots the blood cell on the board using its current color 
        and coordinates.
        '''
         
        plt.scatter(self.x, self.y, c=self.color)

    
    def movement_up(self):
        
        '''
        Blood cell moves through the arteries towards the heart and the lung
        This is shown through the oxygen object moving 1 unit upwards
        '''
        b_dy = 2
        
        b_x = self.x 
        b_y = self.y - b_dy 
        
        self.x = b_x #blood cell coordinates update after it moves 
        self.y = b_y   
        
    def movement_down(self):
        
        '''
        Blood cell moves through the arteries towards organs
        This is shown through the oxygen object moving 1 unit downwards
        '''
        b_dy = 2
        
        b_x = self.x 
        b_y = self.y + b_dy 
        
        self.x = b_x #blood cell coordinates update after it moves 
        self.y = b_y
        
    def movement_right(self):
        
        '''
        Blood cell moves through the arteries towards organs  
        This is shown through the blood cell object moving 1 unit to the right 
        '''
        
        b_dx = 2
        
        b_x = self.x + b_dx
        b_y = self.y 
        
        self.x = b_x #blood cell coordinates update after it moves  
        self.y = b_y      
        
    def movement_left(self):
        
        '''
        Blood cell moves through the arteries towards organs 
        This is shown through the blood cell object moving 1 unit to the left 
        '''
        
        b_dx = 2
        
        b_x = self.x - b_dx
        b_y = self.y 
        
        self.x = b_x #blood cell coordinates update after it moves 
        self.y = b_y
        
    def board_location(self):
        
        '''
        Provides the current location of the blood cell object on the board
        '''
        
        return self.x, self.y
