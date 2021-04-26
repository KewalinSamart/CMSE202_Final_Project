import random

class oxygen_carbon_dioxide():
    
    def __init__ (self, dims, color = 'aqua'):
        
        '''
        Intializing the oxygen/carbon_dioxide object and it's coordinates on the board, as well as it's initial color.
        If the object is aqua, then it represents oxygen. If the object is orange, then it represents carbon dioxide. 
        '''
        
        self.coords = dims
        self.dims = random.sample(dims, 1)
        self.x = dims[0][0] #x coordinate
        self.y = dims[0][1] #y coordinate
        
        self.color = color #object's color 
            
    def draw(self):
        
        '''
        Draws the object on the board 
        '''
        
        plt.scatter(self.x, self.y, c=self.color) #plots object's coordinates on board 
        
    def movement_up(self):
        
        '''
        The movement_up method moves the object up two units on the board. 
        
        Oxygen molecules diffuse from the lungs and move freely towards organs through the arteries (blue path).
        Carbon dioxide molecules diffuse from the organs and move freely towards the lungs through the veins (purple path).
        '''
        
        o_dy = 2 #change in y is 2 units
        
        o_x = self.x 
        o_y = self.y - o_dy #the board is rotated 180 degrees
                            #2 must be subtracted from the y-coordinate to move up two units 
        
        self.x = o_x #object's coordinates update after it moves 
        self.y = o_y #object's coordinates update after it moves  

    def movement_down(self):
        
        '''
        The movement_down method moves the object down two units on the board. 
        
        Oxygen molecules diffuse from the lungs and move freely towards organs through the arteries (blue path).
        Carbon dioxide molecules diffuse from the organs and move freely towards the lungs through the veins (purple path).
        '''
        
        o_dy = 2 #change in y is 2 units
        
        o_x = self.x 
        o_y = self.y + o_dy #the board is rotated 180 degrees
                            #2 must be added to the y-coordinate to move down two units 
        
        self.x = o_x #object's coordinates update after it moves 
        self.y = o_y #object's coordinates update after it moves  

    def movement_right(self):
        
        '''
        The movement_right method moves the object right two units on the board. 
        
        Oxygen molecules diffuse from the lungs and move freely towards organs through the arteries (blue path).
        Carbon dioxide molecules diffuse from the organs and move freely towards the lungs through the veins (purple path).
        '''
        
        o_dx = 2 #change in x is 2 units
        
        o_x = self.x + o_dx #2 is added to the x-coordinate to move to the right two units
        o_y = self.y 
        
        self.x = o_x #object's coordinates update after it moves  
        self.y = o_y #object's coordinates update after it moves       
        
    def movement_left(self):
        
        '''
        The movement_left method moves the object left two units on the board. 
        
        Oxygen molecules diffuse from the lungs and move freely towards organs through the arteries (blue path).
        Carbon dioxide molecules diffuse from the organs and move freely towards the lungs through the veins (purple path).
        '''
        
        o_dx = 2 #change in x is 2 units
        
        o_x = self.x - o_dx #2 is subtracted from the x-coordinate to move to the left two units
        o_y = self.y 
        
        self.x = o_x #object's coordinates update after it moves  
        self.y = o_y #object's coordinates update after it moves   
        
    def transfer(self):
        
        '''
        The transfer method changes the color of the object, depending on its location. 

        Oxygen molecules (aqua) diffuse from the lungs and move freely towards organs through the arteries (blue path).
        Carbon dioxide molecules (orange) diffuse from organs and move freely towards the lungs through veins (purple path).
        '''
        
        if 70 < self.x < 135 and 5 < self.y < 40: #If object is within the arteries it will represent an oxygen molecule
            color = 'aqua' #oxygen molecules are represented by blue objects 
            self.color = color 
            
        elif 80 < self.x < 120 and ((140 < self.y < 160) or (170 < self.y < 190 ) or (200 < self.y < 220)): 
            #If object is within the veins it will represent a carbon dioxide molecule
            color = 'orange' #carbon dioxide molecules are represented by orange objects 
            self.color = color
            
    def board_location(self):
        
        '''
        Returns the object's current x and y coordinates on the board
        '''
        
        return self.x, self.y 
