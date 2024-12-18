import pyxel

class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)
        pyxel.load("my_resource.pyxres")


        # Set the initial position of the square
        self.x = 75
        self.y = 55
        self.score = 0

        # Set the initial position and velocity of the sprite
        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 4
        self.sprite_dy = 4

        self.sprite2_x = 132
        self.sprite2_y = 95
        self.sprite2_dx = 3
        self.sprite2_dy = 3

        self.sprite3_x = 62
        self.sprite3_y = 25
        self.sprite3_dx = 1
        self.sprite3_dy = 1

        #self.sprite4_x = 22
        #self.sprite4_y = 75
        #self.sprite4_dx = 4
        #self.sprite4_dy = 4

        # Start the game loop
        pyxel.run(self.update, self.draw)

    
    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        if abs(self.x - self.sprite_x) <= 2 and abs(self.y - self.sprite_y) <= 2:
            self.score += 1
        if abs(self.x - self.sprite2_x) <= 2 and abs(self.y - self.sprite2_y) <= 2:
            self.score += 1
        if abs(self.x - self.sprite3_x) <= 2 and abs(self.y - self.sprite3_y) <= 2:
            self.score += 1
            self.score += 1

        
               #or self.sprite2_x or self.sprite3_x and self.y == self.sprite_y or self.sprite2_y or self.sprite3_y):
            

        # Simple interaction: Increase score when square reaches top-left corner
        

        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy

        self.sprite2_x += self.sprite2_dx
        self.sprite2_y += self.sprite2_dy

        self.sprite3_x += self.sprite3_dx
        self.sprite3_y += self.sprite3_dy

        #self.sprite4_x += self.sprite4_dx
        #self.sprite4_y += self.sprite4_dy

        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 160:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1

        if self.sprite2_x <= 0 or self.sprite2_x >= 160:
            self.sprite2_dx *=-1
        if self.sprite2_y <= 0 or self.sprite2_y >= 120:
            self.sprite2_dy *=-1

        if self.sprite3_x <= 0 or self.sprite3_x >= 160:
            self.sprite3_dx *=-1
        if self.sprite3_y <= 0 or self.sprite3_y >= 120:
            self.sprite3_dy *=-1

        #if self.sprite4_x <= 0 or self.sprite4_x >= 160:
            #self.sprite4_dx *=-1
        #if self.sprite4_y <= 0 or self.sprite4_y >= 120:
            #self.sprite4_dy *=-1

    

    

    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(0)

        # Draw a square (color 9)
        #pyxel.rect(self.x, self.y, 10, 10, 9)
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)

        # Draw the moving sprite (color 11)
        #pyxel.circ(self.sprite_x, self.sprite_y, 5, 11)
        pyxel.blt(self.sprite_x, self.sprite_y, 1, 0, 0, 16, 16, 0)
        pyxel.blt(self.sprite2_x, self.sprite2_y, 2, 0, 0, 16, 16, 0)
        pyxel.blt(self.sprite3_x, self.sprite3_y, 1, 0, 0, 16, 16, 0)
        #pyxel.blt(self.sprite4_x, self.sprite4_y, 2, 0, 0, 16, 16, 0)

        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        # Display a message when score is high
        if self.score >= 50:
            pyxel.text(50, 50, "merry christmas !", 8)

# Run the game
App()
