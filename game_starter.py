import turtle
import math
import random
from Tile import Tile

t = turtle.Turtle()
scr = turtle.Screen()

def game_board():
    '''
        Function - game_board
            This function draws whole game of puzzle
        Parameter: None
        Returns - None
    '''
    t.hideturtle()
    t.speed(0)
    
    t.width(5)
    scr.setup(800, 800)
    t.penup()
    t.goto(-310, 325)
    t.pendown()
    t.forward(450)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(450)
    t.right(90)
    t.forward(500)

    t.color("blue")
    t.penup()
    t.goto(315, 325)
    t.left(90)
    t.pendown()
    t.forward(150)
    t.left(90)
    t.forward(500)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(500)
    t.penup()
    t.goto(175, 175)
    t.write("Leaders:", False, align="left", font=("Arial", 20))
    t.goto(185, 145)
    t.write("3: Ted", False, align="left", font=("Arial", 18))
    t.goto(185, 125)
    t.write("5: Yannis", False, align="left", font=("Arial", 18))
    t.goto(185, 105)
    t.write("2: Lex", False, align="left", font=("Arial", 18))
    t.penup()


    t.color("black")
    t.penup()
    t.goto(-310, -325)
    t.pendown()
    t.forward(85)
    t.right(90)
    t.forward(625)
    t.right(90)
    t.forward(85)
    t.right(90)
    t.forward(625)
    t.penup()
    t.width()

    t.right(180)

def create_button():
    '''
        Function - create_button
            this function creates reset, load,
            and quit button for the game
        Parameter: None
        Returns - None
    '''
    buttons = []
    reset_button = 'Resources/resetbutton.gif'
    load_button = 'Resources/loadbutton.gif'
    quit_button = 'Resources/quitbutton.gif'

    r = Tile(reset_button, 68, -282)
    r.load_piece()
    buttons.append(r)

    l = Tile(load_button, 168, -282)
    l.load_piece()
    buttons.append(l)

    q = Tile(quit_button, 262, -282)
    q.load_piece()
    buttons.append(q)

    return buttons
    

def thumbnail(meta_dict: dict, name='mario'):
    '''
        Function - thumbnail
            This function draw a thumbnail for
            current puzzle
        Parameters:
            meta_dict(dict): meta data dictionary that contains
            all information of puzzles from all .puz format file
            name(str): name of current playing puzzle
        Returns:
            tile object of thumbnail
    '''
    puzzle_info = meta_dict[name]
    
    thumbnail = Tile(puzzle_info[3][1], 270, 291)
    thumbnail.hide_turtle()
    thumbnail.load_piece()
    thumbnail.show_turtle()

    return thumbnail

def load_puzzle_ordered(meta_dict: dict, x, y, name='mario'):
    '''
        Function - load_puzzle_ordered
            This function make and returns tile
            object of current puzzle in order
        Parameters:
            meta_dict(dict): meta data dictionary that contains
            all information of puzzles from all .puz format file
            x(int): x coordinate of each tile
            y(int): y coordinate of each tile
            name(str): name of current playing puzzle
        Returns:
            a dictionary that contains tile object of current
            puzzle in order
    '''
    puzzle_info = meta_dict[name]

    # save starting x-cor for later use
    orig_x = x
    # save some puzzle info
    num_puz = int(puzzle_info[1][1])
    size = int(puzzle_info[2][1])
    puzzle_list = puzzle_info[4:]

    dict_of_puzzle = {}

    for i in range(1, num_puz+1):
        image = puzzle_list[i-1][1]
        key = puzzle_list[i-1][0]

        # when tile hit sqrt of total number
        # draw in a second row
        if i % math.sqrt(num_puz) == 0:
            dict_of_puzzle[key] = (Tile(image, x, y))
            dict_of_puzzle[key].hide_turtle()
            
            y = y - (size + 5)
            x = orig_x

        else:
            dict_of_puzzle[key] = (Tile(image, x, y))
            dict_of_puzzle[key].hide_turtle()
            x = x + (size+5)
        
    return dict_of_puzzle

def load_puzzle_mixed(meta_dict: dict, x, y, name='mario'):
    '''
        Function - load_puzzle_mixed
            This function make and returns tile
            object of current puzzle in mixed order
        Parameters:
            meta_dict(dict): meta data dictionary that contains
            all information of puzzles from all .puz format file
            x(int): x coordinate of each tile
            y(int): y coordinate of each tile
            name(str): name of current playing puzzle
        Returns:
            a dictionary that contains tile object of current
            puzzle in mixed order
    '''

    # do the same as ordered function above
    puzzle_info = meta_dict[name]

    orig_x = x
    num_puz = int(puzzle_info[1][1])
    size = int(puzzle_info[2][1])
    puzzle_list = puzzle_info[4:]
    
    # except shuffle the order so it's mixed
    random.shuffle(puzzle_list)

    dict_of_puzzle = {}

    for i in range(1, num_puz+1):
        image = puzzle_list[i-1][1]
        key = puzzle_list[i-1][0]
        
        if i % math.sqrt(num_puz) == 0:
            dict_of_puzzle[key] = (Tile(image, x, y))
            
            y = y - (size + 5)
            x = orig_x

        else:
            dict_of_puzzle[key] = (Tile(image, x, y))
            x = x + (size+5)


    for key, value in dict_of_puzzle.items():
        value.load_piece()

    return dict_of_puzzle


def game_plan(meta_dict, dict_of_puzzle,
              ordered, name='mario'):
    '''
        Function - game_plan
            This function takes information of puzzle and
            plays full game which would move tiles, announce
            win or lose
        Parameters:
            meta_dict(dict): meta data dictionary that contains
            all information of puzzles from all .puz format file
            dict_of_puzzle:(dict): a dictionary that contains
            mixed tile object of the current playing puzzle
            ordered(dict): a dictionary that contains ordered
            tile objec of the current playing puzzle
            name(str): name of current playing puzzle
        Returns - None
    '''
    
    puzzle_info = meta_dict[name]
    num_puz = puzzle_info[1][1]
    size = int(puzzle_info[2][1])
    blank_piece = dict_of_puzzle[num_puz]
    puz_range = 1.5 * size + 5
    

    def onclick_helper(x, y):
        '''
            Function - onclick_helper
                This function recognize the click and
                and moves tiles 
            Parameters:
                x - x coordinate of the click
                y - y cordinate of the click
            Returns - None
        '''

        # loop through the dictionary and find current tile
        for key, value in dict_of_puzzle.items():
            if x >= (value.get_x() - 50) and\
               x <= (value.get_x() + 50) and\
               y >= (value.get_y() -50) and\
               y <= (value.get_y() + 50):
                cur_click = value
                
                
                # when left and right pieces are clicked
                if value.get_x() >= (blank_piece.get_x() - puz_range) and\
                   value.get_x() <= (blank_piece.get_x() + puz_range) and\
                   value.get_y() == (blank_piece.get_y()):

                    new_x = blank_piece.get_x()
                    new_y = blank_piece.get_y()

                    # update x and y for blank and clicked
                    blank_piece.update_x(value.get_x())
                    blank_piece.update_y(value.get_y())
                    value.update_x(new_x)
                    value.update_y(new_y)

                    # load tiles again with new coordinate
                    value.load_piece()
                    blank_piece.load_piece()
                    # move_count += 1

                # when up and down pieces are clicekd   
                elif value.get_y() >= (blank_piece.get_y() - puz_range) and\
                     value.get_y() <= (blank_piece.get_y() + puz_range) and\
                     value.get_x() == (blank_piece.get_x()):
                    new_x = blank_piece.get_x()
                    new_y = blank_piece.get_y()

                    # update x and y for blank and clicked
                    blank_piece.update_x(value.get_x())
                    blank_piece.update_y(value.get_y())
                    value.update_x(new_x)
                    value.update_y(new_y)

                    # load tiles again with new coordinate
                    value.load_piece()
                    blank_piece.load_piece()
                    # move_count += 1

            '''
            counting moves here

            t.goto(-280, -290)
            print(move_count)
            t.write(f"Player Moves: {move_count}",
                    align="left", font=('style', 25, 'bold'))
            '''

        # winning cases
        identical = True

        # if x,y coordinate is not matched with
        # ordered puzzle then identical become false
        for key, value in dict_of_puzzle.items():
            if dict_of_puzzle[key].get_x() !=\
               ordered[key].get_x() or\
               dict_of_puzzle[key].get_y() !=\
               ordered[key].get_y():
                identical = False

        # when puzzle is ordered and clicked inside
        # of the gameboard show win msg
        if identical and x >= -310 and x <= 140 and\
           y >= -175 and y <= 325:
            print('game win')
            t.goto(0,0)
            t.showturtle()
            win = 'Resources/winner.gif'
            scr.register_shape(win)
            t.shape(win) 

    # pass onclick_helper function as object
    for key, value in dict_of_puzzle.items():
        value.access_onclick(onclick_helper)

    
    


def reset_button_clicker(buttons: list, dict_of_puzzle, ordered_puzzle):
    '''
        Function - rest_button_clicker
            this function operates reset button in the puzzle
        Parameter:
            buttons(list): it is a list that contains Tile
            object of reset, load, and quit buttons
        Returns - None
    '''
    
    r_button = buttons[0]
    reset_x = buttons[0].get_x()
    reset_y = buttons[0].get_y()
        
    def reset_clicker_helper(x, y):
        '''
            Function - reset_clicker_helper
                This function recognize the click and
                reset the puzzle tile in order 
            Parameters:
                x(int) - x coordinate of the click
                y(int) - y cordinate of the click
            Returns - None
        '''
        if x >= (reset_x - 50) and\
           x <= (reset_x + 50) and\
           y >= (reset_y -50) and\
           y <= (reset_y + 50):
            for key, value in dict_of_puzzle.items():
                x = ordered_puzzle[key].get_x()
                y = ordered_puzzle[key].get_y()
                
                value.update_x(x)
                value.update_y(y)
                value.load_piece()
                
    r_button.access_onclick(reset_clicker_helper)


def load_button_clicker(buttons: list, meta_dict,
                        mixed_puzzle, thumbnail_tile):
    '''
        Function - load_button_clicker
            this function operates load button in the puzzle
        Parameter:
            buttons(list): it is a list that contains Tile
            object of reset, load, and quit buttons
        Returns - None
    '''
    
    l_button = buttons[1]
    load_x = l_button.get_x()
    load_y = l_button.get_y()
    
    # list that would have all puzzle files
    puz_file_name = []

    load_message = "Enter the name of the puzzle you" +\
                   "wihs to load. Choices are:"
    # In order to show all puzzle file in .puz form
    # loop through and append in the list
    for key, value in meta_dict.items():
        file_name = key + ".puz"
        puz_file_name.append(file_name)

    # remove malformed puzzle
    puz_file_name.remove("malformed_mario.puz")

    for each in puz_file_name:
        load_message = load_message + "\n" + each
        
    def load_clicker_helper(x,y):
        '''
            Function - load_clicker_helper
                This function recognize the click and
                load different file of puzzle
            Parameters:
                x(int) - x coordinate of the click
                y(int) - y cordinate of the click
            Returns - None
        '''

        if x >= (load_x - 50) and\
           x <= (load_x + 50) and\
           y >= (load_y -50) and\
           y <= (load_y + 50):
            # opens a window for load puzzles with options
            puzzle_name = scr.textinput("Load Puzzle", load_message)

            # when user typed illegal cases of loading file
            if puzzle_name not in puz_file_name:
                print("working correctly")
                t.goto(0,0)
                scr.delay(700)
                scr.register_shape("Resources/file_error.gif")
                t.shape("Resources/file_error.gif")
                t.showturtle()
                scr.delay(0)
                t.hideturtle()
                
            # otherwise load the file
            else:
                puzzle_name = puzzle_name.strip(".puz")

                # hide all pieces of current puzzle 
                for key, value in mixed_puzzle.items():
                    value.hide_turtle()

                # after clear the board initiate the game
                # with new file and new puzzle
                new_ordered = load_puzzle_ordered(meta_dict, -246, 266, puzzle_name)
                new_puzzle = load_puzzle_mixed(meta_dict, -246, 266, puzzle_name)
                thumbnail_tile.hide_turtle()
                new_thumb = thumbnail(meta_dict, puzzle_name)
                game_plan(meta_dict, new_puzzle, new_ordered, puzzle_name)
                reset_button_clicker(buttons, new_puzzle, new_ordered)
                load_button_clicker(buttons, meta_dict, new_puzzle, new_thumb)

        

    # pass load_clicker_helper as parameter
    l_button.access_onclick(load_clicker_helper)
           

def quit_button_clicker(buttons: list):
    '''
        Function - quit_button_clicker
            this function operates quit button in the puzzle
        Parameter:
            buttons(list): it is a list that contains Tile
            object of reset, load, and quit buttons
        Returns - None
    '''
    # save x, y coordinate of quit button
    q_button = buttons[2]
    quit_x = q_button.get_x()
    quit_y = q_button.get_y()

    def quit_clicker_helper(x, y):
        '''
            Function - quit_clicker_helper
                This function recognize the click and
                quit the game when the the game clicks
                quit button
            Parameters:
                x(int) - x coordinate of the click
                y(int) - y cordinate of the click
            Returns - None
        '''
        if x >= (quit_x - 50) and\
           x <= (quit_x + 50) and\
           y >= (quit_y -50) and\
           y <= (quit_y + 50):
            
            quit_msg = 'Resources/quitmsg.gif'
            scr.delay(700)
            scr.register_shape(quit_msg)
            t.goto(0,0)
            t.shape(quit_msg)
            t.showturtle()
            scr.bye()

    q_button.access_onclick(quit_clicker_helper)

