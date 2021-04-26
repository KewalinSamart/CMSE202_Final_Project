import random

class blood_cell():
    '''
    This is the blood cells class and it allows the blood cells to move around as well as absorb oxygen and carbon dioxide.
    '''
    
    def __init__(self, x_dims, y_dims, shape='round'): #We could change the shape attribute to an oxygen capacity attribute
        self.shape = shape
        #self.molecule = molecule
        self.x_dim = random.randint(x_dims[0], x_dims[1])
        self.y_dim = random.randint(y_dims[0], y_dims[1])
        
        if self.shape == 'round':
            oxygen_cap = 6
            carbon_cap = 5
        elif self.shape == 'sickle':
            oxygen_cap = 3
            carbon_cap = 2
        
        self.oxygen_cap = oxygen_cap
        self.carbon_cap = carbon_cap
        
    def transfer(self):
        # Determine if blood cell is in lungs using nearest neighbor, if it is then it picks up the maximum amount of oxygen and releases
        # CO2
      
        # Determine if blood cell is in an organ using nearest neighbor, if it is then it picks up the max amount of CO2 and releases
        # oxygen
        #neighbors = getNeighborValues(self.x_dim, self.y_dim, board)
        if 70 < self.x_dim < 135 and 5 < self.y_dim < 40:
            #ox_supply = self.oxygen_cap
            #carb_supply = 0
            color = 'red'
        elif 80 < self.x_dim < 120 and ((140 < self.y_dim < 160) or (170 < self.y_dim < 190 ) or (200 < self.y_dim < 220)):
            #ox_supply = 0
            #carb_supply = self.carbon_cap
            color = 'blue'
            
        self.color = color
        
    def draw(self, board):
        
        plt.figure(figsize=(20,10))
        plt.imshow(board) 
        plt.scatter(self.x_dim, self.y_dim, color=self.color)

    
    def move_left(self):
        # Subtract from the x coordinate, moving 1 unit left, y_coordinate can stay the same
        dx = -1
        new_xL = self.x_dim + dx
        new_yL = self.y_dim # or we could have a tiny range of back and forth y movement in a loop (new_yL = self.y_dim + (-1)^n_steps)
        
        self.x_dim = new_xL
        self.y_dim = new_yL
    
    def move_up(self):
        # Subtract from y coordinate, moving 1 unit up, x_coordinate can stay the same
        dy = -1
        new_xU = self.x_dim  # or we could have a tiny range of back and forth x movement in a loop (new_xU = self.x_dim + (-1)^n_steps)
        new_yU = self.y_dim + dy 
        
        self.x_dim = new_xU
        self.y_dim = new_yU
        
    def move_right(self):
        # Add to x coordinate, moving 1 unit right, y_coordinate can stay the same
        dx = 1
        new_xR = self.x_dim + dx
        new_yR = self.y_dim # or we could have a tiny range of back and forth y movement in a loop (new_yR = self.y_dim + (-1)^n_steps)
        
        self.x_dim = new_xR
        self.y_dim = new_yR
    
