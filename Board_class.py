import numpy as np

class Board():
    def __init__(self):
        
        # attributes
        # initializing the board
        self.board = np.zeros(shape = (250,200))
        
        # left heart
        self.board[70:100,75:100] = 1
        self.left_heart = self.board[70:100,75:100]
        
        # right heart
        self.board[70:100,100:130] = 2
        self.right_heart = self.board[70:100,100:130]
        
        # lung
        self.board[5:40,70:135] = 3
        self.lung = self.board[5:40,70:135]
        
        # organ no.1
        self.board[140:160,80:120] = 4
        self.organ1 = self.board[140:160,80:120]
        
        # organ no.2
        self.board[170:190,80:120] = 5
        self.organ2 = self.board[170:190,80:120] 
        
        # organ no.3
        self.board[200:220,80:120] = 6
        self.organ3 = self.board[200:220,80:120]
        
        # vein connecting lung and left part of the heart
        self.board[40:70,80:90] = 1
        self.vein_lung_heart = self.board[40:70,80:90]
        
        # top vein connecting lung with organs
        self.board[80:90,25:75] = 1
        self.top_vein = self.board[80:90,25:75]
        
        # side vein connecting lung with organs
        self.board[90:215,25:35] = 1
        self.side_vein = self.board[90:215,25:35]
        
        # side vein organ no.1
        self.board[145:155,35:80] = 1
        self.side_vein_organ1 = self.board[145:155,35:80]
        
        # side vein organ no.2
        self.board[175:185,35:80] = 1
        self.side_vein_organ2 = self.board[175:185,35:80]
        
        # side vein organ no.3
        self.board[205:215,35:80] = 1
        self.side_vein_organ3 = self.board[205:215,35:80]
        
        # artery connecting lung and right part of the heart
        self.board[40:70,115:125] = 2
        self.art_lung_heart = self.board[40:70,115:125]
        
        # top artery connecting lung with organs
        self.board[80:90,130:180] = 2
        self.top_artery = self.board[80:90,130:180]
        
        # side artery connecting lung with organs
        self.board[90:215,170:180] = 2
        self.side_artery = self.board[90:215,170:180]
        
        # side artery organ no.1
        self.board[145:155,120:170] = 2
        self.side_art_organ1 = self.board[145:155,120:170]
        
        # side artery organ no.2
        self.board[175:185,120:170] = 2
        self.side_art_organ2 = self.board[175:185,120:170] 
        
        # side artery organ no.3
        self.board[205:215,120:170] = 2
        self.side_art_organ3 = self.board[205:215,120:170]
