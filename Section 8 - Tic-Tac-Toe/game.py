import random
import tkinter as tk
from tkinter import messagebox, simpledialog
import pygame as pg



#1. Sound
#2. Mixer Initaliser
#3. Get the sound we want to play
pg.mixer.init()

#Load our sound file
soundtrack = pg.mixer.Sound("winner.mp3")



#tkinter - GUI Tools for use to able to visualise our code 
#pygame - Play our winning sound track when the player wins
#random - For generating our random confetti when a player wins

# #Create a window

# game_window = tk.Tk()
# game_window_label = tk.Label(text="Tic-Tac-Toe Game Window", fg="black", bg="white")

# #Push our changes to our window
# game_window_label.pack()
# game_window.mainloop()

#1. Create the Board
#[None] * 9

#1. When the game first starts
#2. When the game round ends and we starting a new round 
def create_game_board():
    return [None] * 9

#Create the board functionality
#Button = Tk Package

def create_game_buttons(root, board, player_info, update_state):
    game_buttons = [] # List - Collection Type that stores a list of values that are indexed
    
    #Range(9) = 0,1,2,3,4,5,6,7,8
    for b in range(9):
        #Command arg = Provide a function that is going called everytime a game button is interacted with
        # Lamada Function - Inline Function 
        game_button = tk.Button(root, text="", font=("normal", 45), width=5, height=2, command= lambda b=b: update_state(board, player_info, b, game_buttons)) #Update the state of our game)            

        #Create our grid structure - 3 x 3 grid
        #Columns = 0,1,2 = 3 Columns
        #Rows = 0,1,2 = 3 Row
        game_button.grid(column= b // 3, row=b % 3) #8 % 3 - Remainder is 2 (0, 1, 2) = 3 Row
        
        game_buttons.append(game_button)
        
    return game_buttons

#Updating the Game State
#1. Choose whether we have player 1 or player 2 making a play
#2 Check who the winner is 
#2b. Reset the board for a new round
#2c. Celebration and play our winning sound etc

def update_game_state(board, player_info, index, buttons):
    #board
    #buttons
    #player_info
    #index
    
    #1.Logic for our players
    player_option = 'O' if board.count('O') == board.count('X') else 'X'
    #Get info about our player who is either an O or X
    player_name = player_info[player_option]['name']
    
    if board[index] is None:
        #The player and fill the board index with their O or X
        board[index] = player_option
        #If this index on our board is filled? What happens to the tk.Button lodged in that box
        #We need to disable the button for the grid that has been filled
        buttons[index].config(text=player_option, state="disabled")
        
    #Updating the state of the game if there is a winner
    if check_game_winner(board):
        #1. Add one point to the winner of the round
        player_info[player_option]['score'] += 1 # += what ever the previous score value is, add 1
        
        #2. Play our winners soundtrack - pygame
        pg.mixer.Sound.play(soundtrack)
        #3. Confetti to appear on our game screen window
        #a. display_confetti
        display_confetti()
        #b. Display who won the round
        messagebox.showinfo("Tic-Tac-Toe", f"{player_name}: {player_option} has won this round!")
        #c. update the scores on our game window
        update_player_scores(player_info)
        #d. reset the game - reset the board and the buttons
        reset_game(board, buttons)
        #e. Keep logic here to check whether the entire game has been won - if all rounds are complete e.g 5 rounds and we have a winner
        #check_overall_win
        check_overall_win(player_info, number_of_game_rounds)
    elif None not in board:
       #4. If there is draw/tie
        #1. Tk Message box, message to say it's a draw
        messagebox.showinfo("Tic-Tac-Toe", "This game is a draw!")
        #2. reset the game 
        reset_game(board, buttons)  


def display_confetti():
    #1. Canvas (UI Canvas)
    canvas_height = 600
    canvas_width = 600
    confetti_canvas = tk.Canvas(root, height=canvas_height, width=canvas_width)
    #2. Canvas Grid Structure 
    confetti_canvas.grid(column=0, row=0, columnspan=3, rowspan=3)
    
    
    #Setup our confetti Styling
    #1. Colours
    confetti_colours_list = ["purple", "blue", "green", "yellow", "red", "orange"]
    #2. Number of Confetti Piece you want to be generated
    confetti_pieces = []
    
    #Soluton 2: Move the if block outside of the for loop to stop the recusion 
    #Generating our confetti pieces
    #200 Confetti Pieces
    
    for _ in range(200):
        #1 Confetti Dimensions and Co-ordinates 
        
        #2D Game - x-axis, y-axis
        #3D Game - x-axis, y-axis and z-axis
        
        #Starting Co-ordinate
        #x0, x1
        #y0, y1
        
        #Random - Randomisation 
        x_start = random.randint(0, 450) #x0
        y_start = random.randint(-200, 0) #y0, why -200 = Not be visible on screen 
        
    
        #Ending Co-ordinate
        x_end = x_start + random.randint(3, 15) #x1
        y_end = y_start + random.randint(3, 15) #y1
        
        #Use random.choice() to randomise the colour for each confetti piece
        single_confetti_piece = confetti_canvas.create_oval(x_start,y_start, x_end, y_end, fill=random.choice(confetti_colours_list))
        #Add our single confetti piece to our confetti pieces list
        confetti_pieces.append((single_confetti_piece, x_start, y_start)) # We need the x_starting point and y_starting point co-ordinates
        
        
    #Setup animation of are confetti falling to the ground 
    #inner function encapsulations
    def animate_confetti():
        for con_piece, x, y in confetti_pieces:
            
            #1. Movement of our confetti pieces - Confetti To Start from the top of the Game UI Window and then incremental move down to bottom of the windom
            confetti_canvas.move(con_piece, 0, 7) #xargs argument
            #move by pixels
            #y-axis - vertical axis
            
            #2. Update the state of the y co-ordinates of our confetti
            #[(confetti, x, y), (confetti, x, y), (confetti, x, y), (confetti, x, y)]
            confetti_pieces[confetti_pieces.index((con_piece, x, y))] = (con_piece, x, y + 7)
            
            
            #3. Determine whether the animation is finished 
            # work when the y for all of confetti piece is above the the length in pixels of the canvas
            
            #if and for 
        #Error 2: Indentation Error
        if all(y > canvas_height for _,_,y in confetti_pieces):
            # Remove the confetti display from the screen
            #1 sec = 1000 ms
            root.after(3000, confetti_canvas.destroy) #<---- Pass functions by reference only not by function call 
            #root.destroy() - Destroy all of the widgets in the main window - Trigger a shut down of the UI Window
            #root.quit() - Doesn't destroy any of the widgets in the window, remove any response to the UI
            #quit = it stops the mainloop() event loop 
        else:
            #If the y direction for the confetti piece are not all above the canvas height
            root.after(40, animate_confetti)   

        #Call our animate function this would allow us to begin animating the confetti we have generated
        #1. First time it runs would be via animate_confetti()
        #2.
    animate_confetti()
        
    
    
    
    





def check_overall_win(player_info, num_of_rounds):
    #1. Player Information
    #2. Number of Rounds (Max Number of Rounds decided at the start of the game)
    
    #a. If one player has more points that another player and the number of rounds are complete
    #b If one player has the same amount of points as the number of rounds and the other player has none
    if player_info['O']['score'] >= num_of_rounds or player_info['X']['score'] >= num_of_rounds:
        #Determine which player won by their Symbol
        overall_game_winner = 'O' if player_info['O']['score'] > player_info['X']['score'] else 'X'
        #Get the players name
        overall_game_winners_name = player_info[overall_game_winner]['name'] 
        
        #UI Logic - Messagebox, SimpleDialog 
        messagebox.showinfo("Tic-Tac-Toe", f"Congratulations {overall_game_winners_name} You have won the game!")
        
        #End the game window when we are finished
        root.quit() 
        
    
def update_player_scores(player_info):
    #Display of the player scores as the game is going on
    #1. Access our score text
    #1 - 0 
    game_score_text.set(f"{player_info['O']['name']} player O: {player_info['O']['score']} - {player_info['X']['name']} player X: {player_info['X']['score']}")
    #2. Change or set values to current state of the players scores
    

def reset_game(board, buttons):
    #1. Clear the board
    board[:] = create_game_board() 
    
    ##2. Take of the buttons for each sqaure in the board - Reset the buttons to be ready for usage again
    for button in buttons: 
        #For each button we want to reset the state of the button to normal and also remove any X's or O's
        button.config(text="", state="normal")
     
##Check who the winner is 
def check_game_winner(board):
    
    win_game_combinations = [
        [0,3,6], [1,4,7], [2,5,8], #Winning combinations for our columns (vertical wins)
        [0,1,2], [3,4,5], [6,7,8], #Winning combinations for our rows (horiziontal wins)
        [0,4,8], [2,4,6]   #Winning combinations for our diagonals 
    ]
    
    #Check if there is a winning combination
    for winning_combo in win_game_combinations:
        if board[winning_combo[0]] == board[winning_combo[1]] == board[winning_combo[2]] and board[winning_combo[0]] is not None:
                return True
    return False
            
        #If we do not check for board values that are not None then a player could win the game
        #based on empty squares

def get_player_info(player_number):
    
    #1. Trigger a Prompt
    player_name = simpledialog.askstring(f"Player {player_number}", f"Player {player_number}: Please Enter Player Name")
    if not player_name:
        messagebox.showwarning("No Input Error", f"Player {player_number} you must enter a name!")
        return None
    #Return our user data dictionary - e.g player_info['name']
    return {"name": player_name, "score": 0}

def main():
    #Global
    #1. Root
    #2. Game Score Text
    #3. Number of Game Rounds
    
    global root, game_score_text, number_of_game_rounds
    
    
    
    #2. Root
    root = tk.Tk()
    
    #Get the Main GUI Window to be invisble until it's time to start playing the game
    root.withdraw()
    
    #1. Score Text
    game_score_text = tk.StringVar()
    #1. Window of the game screen to be initalised
    #2. Prompts - Dialog box to ask what your name is (example)

     ######### Number of Rounds Information #########
    #a. Ask how many rounds the we want to have
    #input dialog box that receives user input (user data)
    number_of_game_rounds = simpledialog.askinteger("Tic-Tac-Toe Game Rounds", "How many game rounds would like to have e.g 5 for best of 5 rounds", minvalue=1)
    #What if the user gives us a bogus value
    #1. Not an integer
    #2. Less than 1 (min value)
    #3. If the user provide no response
    if not number_of_game_rounds:
        #close the game window
        root.destroy()
        return
        
        
    ######### Players Information #########
    player_one_info = get_player_info(1)
    if not player_one_info:
        root.destroy()
        return
        
    player_two_info = get_player_info(2)
    if not player_two_info:
        root.destroy()
        return
    
    #player info dictionary object
    player_info = {"O": player_one_info, "X": player_two_info}
    
    #UI/UX Enhancement
    root.deiconify()
    
    #Root Title
    root.title("Tic-Tac-Toe Game")
    
    #3. So we want the game to start - What the board to appear on the screen 
    game_score_label = tk.Label(root, textvariable=game_score_text, font=('normal', 12))
    ##row and columns zero indexed
    game_score_label.grid(row=3, column=0, columnspan=3)
    
    #Updating the score label
    update_player_scores(player_info)
    
    
    #Initalising the programmatic logic for the boards behaviour
    #1. Empty Board Initalisation
    board = create_game_board() # Programmatic initalised 9 squares of our grid
    #2. Initalise the buttons for the board
    create_game_buttons(root, board, player_info, update_game_state)
    
    
    
    #Things to do
    # 1. Fix the sizing of our board UI
    #2. Add the confetti to the celebration
    
    
    root.mainloop() # All our root window for our game to continuosly appear on the screen
    
    #4. We want the scores for each player to set and then appear on the screen 
    #5. Keep track of the state of our game
        




#3. Setup our dialogs
#a. What are their names
#b. How many rounds of the game do you want play?
       
if __name__ == "__main__":
    main()