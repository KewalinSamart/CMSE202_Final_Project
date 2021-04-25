import random
import matplotlib.pyplot as plt

class blood_cell():
    '''
    This is the blood cells class and it allows the blood cells to move around as well as absorb oxygen and carbon dioxide.
    '''
    
    def __init__(self, x_dims, y_dims, shape='round', color = 'red'): #We could change the shape attribute to an oxygen capacity attribute
        self.shape = shape
        #self.molecule = molecule
        self.x = x_dims
        self.y = y_dims
        
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
        
    def draw(self,color):
         
        plt.scatter(self.x, self.y, c=color)

    
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
    
    def distance (self, organ_locationx, organ_locationy): 
        
        '''
        Provides distance between oxygen object and inputed organ location
        '''
    
        distance = ((organ_locationx - self.x)**2) + ((organ_locationy - self.y)**2) 
        #distance formula, using organ and current oxygen molecule location 
        return distance
    
    def blood_cell_simulation(self):
        '''
        Blood Cell Object Movement
        '''
        b = blood_cell(120,40)

        fig, ax = plt.subplots(figsize=(10,5))
        color = 'red'
        for _ in range(10000):
    
            location = b.board_location()
    
            # change color when enter organs
            if location[0] == 100 and location[1] == 150:
                color = 'blue'
            if location[0] == 100 and location[1] == 180:
                color = 'blue'
            if location[0] == 100 and location[1] == 210:
                color = 'blue'
    
            # change color when enter lung
            if location[1] == 20:
                color = 'red' 
            
            # movement conditions based on coordinates
            if location[1] < 85 and location[0] > 150:
                b.movement_down()
                b.draw(color)
        
            elif location[0] >= 30 and location[0] < 85 and location[1] <= 85: 
                b.movement_right()
                b.draw(color)
        
            elif location[1] == 20 and location[0] == 85:
                b.movement_right()
                b.draw(color)
        
            elif location[1] == 20 and location[0] >= 85 and location[0] != 120:
                b.movement_right()
                b.draw(color)
        
            elif location[1] <= 40 and location[0] == 120:
                b.movement_down()
                b.draw(color)
        
            elif location[0] == 85 and location[1] <= 85:
                b.movement_up()
                b.draw(color)
   
            elif location[0] == 30:
                b.movement_up()
                b.draw(color)

            elif location[0] < 175 and location[1] == 85:
                b.movement_right()
                b.draw(color)
            
            elif location[0] == 175 and location[1] < 150: 
                b.movement_down()
                b.draw(color)
            
            elif location[0] == 175 and location[1] == 150: #Potentially enter organ 1
                prob = random.random()
                if prob > 0.33:
                    b.movement_down()
                    b.draw(color)
                else:
                    b.movement_left()
                    b.draw(color)
                
            elif location[0] == 30 and location[1] == 150:
                b.movement_up()
                b.draw(color)
            
            elif location[1] == 150:
                b.movement_left()
                b.draw(color)  
        
            elif location[1] < 180: #Potentially enter organ 2 
                b.movement_down()
                b.draw(color)
        
            elif location[0] == 175 and location[1] == 180:
                prob = random.random()
                if prob > 0.33:
                    b.movement_down()
                    b.draw(color)
                else:
                    b.movement_left()
                    b.draw(color)

            elif location[0] == 30 and location[1] == 180:
                b.movement_up()
                b.draw(color)

            elif location[1] == 180:
                b.movement_left()
                b.draw(color)  
    
            elif location[1] < 210: #Potentially enter organ 3 
                b.movement_down()
                b.draw(color)

            elif location[0] == 30 and location[1] == 210:
                b.movement_up()
                b.draw(color)

            elif location[1] == 210:
                b.movement_left()
                b.draw(color)  
    
    
            # Animaiton part (dosn't change)
            plt.imshow(board)
            clear_output(wait=True) # Clear output for dynamic display
            display(fig)            # Reset display
            fig.clear()             # Prevent overlapping and layered plots
            time.sleep(0.0001)      # Sleep for a fraction of a second to allow animation to catch up
            # Sleep for a fraction of a second to allow animation to catch up
    
