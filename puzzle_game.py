'''
    Tae Hyeon Lee
    CS 5001
    Final project
    This program plays slide puzzle with user
'''
import turtle
import os
from game_starter import *


t = turtle.Turtle()

def scan_puz_file():
    '''
    Function - scan_puz_file
        this function scan the .puz file and return
        them in a list
    Parameter: None
    Return: a list that contains all .puz file name
    '''
    puz_file = []
    for folder, sub_folder, files in os.walk(os.getcwd()):
        for each in files:
            name = each.split(".")
            if name[1] == "puz":
                puz_file.append(each)
    return puz_file


def create_dict(puz_file_list: list):
    '''
    Function - create_dict
        This function takes a list of file names
        and create a meta data in dictionary form
    Parameter:
        puz_file_list(list): a list that contains
        names of all .puz file
    '''
    try:
        meta_dict = {}
        for file in puz_file_list:
            name = file.strip(".puz")
            meta_dict[name] = []
            with open(file, mode='r') as puzzle:
                for each in puzzle:
                    each_line = each.split()
                    each_line[0] = each_line[0].strip(":")
                    meta_dict[name].append(each_line)


        return meta_dict

    except OSError:
        print("File not found!")
        
def main():
    '''
    Function - main
        This function runs and play the game
    Parameter: None
    Returns: None
    '''

    # show the splash screen before the game
    scr = turtle.Screen()
    starting_pic = 'Resources/splash_screen.gif'
    scr.delay(1000)
    scr.register_shape(starting_pic)
    t.shape(starting_pic)
    scr.delay(10)
    t.hideturtle()

    # show name an move window for user
    move_message = "Enter the number of moves (chances) you want (5-200)"
    name = scr.textinput("CS 5001 Puzzle Slide", "Your Name:")
    moves = scr.textinput("5001 Puzzle Slide - Moves", move_message)

    game_board()
    buttons = create_button()

    # go through the folder and read only .puz file
    filename = scan_puz_file()
    # create meta data from all .puz file
    meta_dict = create_dict(filename)

    # run and save both mixed and ordered puzzle
    mixed = load_puzzle_mixed(meta_dict, -246, 266)
    ordered = load_puzzle_ordered(meta_dict, -246, 266)
    
    thumbnail_tile = thumbnail(meta_dict)
    reset_button_clicker(buttons, mixed, ordered)
    quit_button_clicker(buttons)
    load_button_clicker(buttons, meta_dict,
                        mixed, thumbnail_tile)

    game_plan(meta_dict, mixed, ordered)
    


    
    




    
                     
    
    

if __name__ == "__main__":
    main()




'''

def load_piece(num_pieces, ):
    
    for i in range(

    
    
    num_puz = int(meta_dict['number'])
    size = int(meta_dict['size'])
    multiplier = 0
    addition = multiplier * size

    for i in range(1, num_puz+1):


def load_puzzle(puz_info: dict):
    x = -246
    y = 266
    
    puzzle_piece = puz_info["number"]
    puzzle_size = int(puz_info["size"])

    for i in range(1, int(puzzle_piece)+1):
        multiplier = 0
        addition = multiplier * puzzle_size
        
        key = str(i)
        each_piece = puz_info[key]
        
        ti = turtle.Turtle()
        ti.goto(x + addition, y)
        ti.register_shape(each_piece)
        ti.addshape(each_piece)

        multiplier += 1


        if i % math.sqrt(int(puzzle_piece)) == 0:
            y = y - puzzle_size
            
            ti.goto(x, y)

            ti = turtle.Turtle()
            ti.goto(x + addition, y)
            ti.register_shape(each_piece)
            ti.addshape(each_piece)


            multiplier = 0

def test(x, y):
    test = []
    
    multiplier = 0
    
    for i in range(1, 17):
        addition = multiplier * 98
        test.append([x + addition, y])
        multiplier =+ 1

        if i % 4 == 0:
            print("move y", "this is i", i)
            print(i % 4)
            multiplier =+ 1
            addition = multiplier * 98
            test.append([x + addition, y])
            y = y - 98
            multiplier = 0

    return test
'''
