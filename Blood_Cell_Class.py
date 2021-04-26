import random
import matplotlib.pyplot as plt

class blood_cell():
    '''
    This is the blood cells class and it allows the blood cells to move around as well as absorb oxygen and carbon dioxide.
    '''
    
    def __init__(self, dims, shape='round', color = 'red'): #We could change the shape attribute to an oxygen capacity attribute
        self.shape = shape
        #self.molecule = molecule
        self.coords = dims 
        self.dims = random.sample(dims, 1)
        self.x = self.dims[0][0]
        self.y = self.dims[0][1]
        
        if self.shape == 'round':
            oxygen_cap = 6
            carbon_cap = 5
        elif self.shape == 'sickle':
            oxygen_cap = 3
            carbon_cap = 2
        
        self.oxygen_cap = oxygen_cap
        self.carbon_cap = carbon_cap
        
        self.color = color 
        
        b_x = self.x 
        b_y = self.y
        
    def transfer(self):
        # Determine if blood cell is in lungs using nearest neighbor, if it is then it picks up the maximum amount of oxygen and releases
        # CO2
      
        # Determine if blood cell is in an organ using nearest neighbor, if it is then it picks up the max amount of CO2 and releases
        # oxygen
        #neighbors = getNeighborValues(self.x_dim, self.y_dim, board)
        if 70 < self.x < 135 and 5 < self.y < 40:
            #ox_supply = self.oxygen_cap
            #carb_supply = 0
            color = 'red'
            self.color = color
            
        elif 80 < self.x < 120 and ((140 < self.y < 160) or (170 < self.y < 190 ) or (200 < self.y < 220)):
            #ox_supply = 0
            #carb_supply = self.carbon_cap
            color = 'blue'
            self.color = color
        
    def draw(self):
         
        plt.scatter(self.x, self.y, c=self.color)

    
    def movement_up(self):
        
        '''
        Oxygen moves through the arteries towards the heart and the lung
        This is shown through the oxygen object moving 1 unit upwards
        '''
        b_dy = 1
        
        b_x = self.x 
        b_y = self.y - b_dy 
        
        self.x = b_x #oxygen coordinates update after it moves 
        self.y = b_y   
        
    def movement_down(self):
        
        '''
        Oxygen moves through the arteries towards organs
        This is shown through the oxygen object moving 1 unit downwards
        '''
        b_dy = 1
        
        b_x = self.x 
        b_y = self.y + b_dy 
        
        self.x = b_x #oxygen coordinates update after it moves 
        self.y = b_y
        
    def movement_right(self):
        
        '''
        Oxygen moves through the arteries towards organs  
        This is shown through the oxygen object moving 1 unit to the right 
        '''
        
        b_dx = 1 
        
        b_x = self.x + b_dx
        b_y = self.y 
        
        self.x = b_x #oxygen coordinates update after it moves 
        self.y = b_y      
        
    def movement_left(self):
        
        '''
        Oxygen moves through the arteries towards organs 
        This is shown through the oxygen object moving 1 unit to the left 
        '''
        
        b_dx = 1
        
        b_x = self.x - b_dx
        b_y = self.y 
        
        self.x = b_x #oxygen coordinates update after it moves 
        self.y = b_y
        
    def board_location(self):
        
        '''
        Provides the current location of the oxygen object on the board
        '''
        
        return self.x, self.y
