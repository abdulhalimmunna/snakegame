# Define the levels
LEVELS = [
    {'speed': 10, 'num_obstacles': 0},
    {'speed': 15, 'num_obstacles': 3},
    {'speed': 20, 'num_obstacles': 5}
]

# Define the Game class
class Game:
    def __init__(self):
        self.level = 0
        self.score = 0
        self.high_score = 0
        self.num_lives = 3
        self.snake = Snake()
        self.food = Food()
        self.obstacles = []
        self.speed = LEVELS[self.level]['speed']
        self.num_obstacles = LEVELS[self.level]['num_obstacles']

    def next_level(self):
        self.level += 1
        self.score += 100
        if self.level < len(LEVELS):
            self.speed = LEVELS[self.level]['speed']
            self.num_obstacles = LEVELS[self.level]['num_obstacles']
            self.snake.reset()
            self.food.reset()
            self.obstacles = []
            for i in range(self.num_obstacles):
                self.obstacles.append(Obstacle())
        else:
            self.game_over()

    def game_over(self):
        # Display the game over screen
        pass

    def update(self):
        # Update the game objects and check for collisions
        pass

    def draw(self):
        # Draw the game objects to the screen
        pass
# Define the Game class
class Game:
    def __init__(self):
        self.level = 0
        self.score = 0
        self.high_score = 0
        self.num_lives = 3
        self.snake = Snake()
        self.food = Food()
        self.speed = LEVELS[self.level]['speed']
        self.num_obstacles = LEVELS[self.level]['num_obstacles']
        self.load_high_score()

    def load_high_score(self):
        try:
            with open('high_score.txt', 'r') as f:
                self.high_score = int(f.read())
        except:
            pass

    def save_high_score(self):
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))

    def next_level(self):
        self.level += 1
        self.score += 100
        if self.level < len(LEVELS):
            self.speed = LEVELS[self.level]['speed']
            self.num_obstacles = LEVELS[self.level]['num_obstacles']
            self.snake.reset()
            self.food.reset()
            for i in range(self.num_obstacles):
                self.obstacles.append(Obstacle())
        else:
            self.game_over()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        # Display the game over screen

    def update(self):
        if self.snake.collide(self.food.position):
            self.score +=
