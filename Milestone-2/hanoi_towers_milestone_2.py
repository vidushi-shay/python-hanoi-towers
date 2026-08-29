from graphics import *
from stack import Stack
import pickle
disk_lst=[]

def main():
    '''
    Purpose: Unify all graphic functions
    Parameters: None
    Returns: None
    '''    
    win = GraphWin('HanoiWindow', 800, 600)
    win.setBackground('light gray')
    create_graphics(win)
    disk_lst = []

    quit_btn, save, load, reset, move = create_buttons(win)
    error_text, middle_text = write_texts(win)
    entry1, entry2, entry3, entry4 = create_entries(win)
    num_disk, target= use_entries(entry1,entry2)
    source, destination= second_entries(entry3,entry4)
    
    tower1, tower2, tower3=create_towers(num_disk)
    towers=[tower1, tower2, tower3]

    draw_disks(win, towers)
    move_count = 0
    update_middle(middle_text, move_count, target, num_disk, towers, win)
    while True:
        pt = win.getMouse()
        error_text.setText("")
        if clicked(quit_btn, pt):
            win.close()
            return
        reset_clicked = clicked_reset(pt, reset, entry1, entry2, entry3, entry4,error_text, middle_text, move_count, win)
        if reset_clicked:
            towers, num_disk, target = reset_clicked
            move_count = 0
        if clicked(move, pt):
            source, destination = second_entries(entry3, entry4)
            moved = move_disk(towers, source, destination, error_text)
            if moved:
                move_count += 1
                draw_disks(win, towers)
                update_middle(middle_text, move_count, target, num_disk, towers, win)
        if clicked(save, pt):
            save_game(num_disk, target, towers, source, destination, win, error_text)
        loaded = clicked_load(load, pt, error_text, win, towers)
        if loaded:
            num_disk, source, towers, destination, target = loaded
            move_count = 0
            draw_disks(win, towers)
            update_middle(middle_text, move_count, target, num_disk, towers, win)

def create_buttons(win:GraphWin)->GraphWin:
    '''
    Purpose: Define the buttons
    Parameters: GraphWindow
    Returns: (quit, save, load, reset, move): GraphWin
    '''    
    quit = draw_button(win, 715, 50, 60, 30, 'Quit')
    save = draw_button(win, 715, 50, 100, 30, 'Save')
    load = draw_button(win, 715, 50, 140, 30, 'Load')
    reset = draw_button(win, 40, 50, 100, 30, 'Reset')  
    move = draw_button(win, 250, 65, 535, 25, 'Move Disk')
    return quit, save, load, reset, move

def create_towers(num_disk:int):
    '''
    Purpose: Create the tower stack.
    Parameters: num_disk:int
    Returns: (tower1, tower2, tower3):list
    '''
    global disk_lst
    tower1 = Stack()
    tower2 = Stack()
    tower3 = Stack()
 
    for i in range(num_disk, 0, -1):
        tower1.push(i)
    disk_lst = []
    return tower1, tower2, tower3

def clicked_reset(pt, reset, entry1, entry2, entry3, entry4, error_text, middle_text, move_count, win):
    '''
    Purpose: Utilize the reset button
    Parameters: (pt, reset):GraphWin, towers:list, num_disk:int, (entry1,2,3,4, error_text, win):GraphWin
    Returns: towers:int, num_disk:int, target:int, else:None
    '''     
    if clicked(reset, pt):
        num_disk, target = use_entries(entry1, entry2)

        tower1=Stack()
        tower2=Stack()
        tower3=Stack()
        for i in range(num_disk, 0, -1):
            tower1.push(i)
        towers = [tower1, tower2, tower3]

        entry3.setText('1')
        entry3.setFill('dark gray')
        entry4.setText('3')
        entry4.setFill('dark gray')
        
        global disk_lst
        for disk in disk_lst:
            disk.undraw()
        disk_lst = []
        draw_disks(win, towers)
        update_middle(middle_text, move_count, target, num_disk, towers, win)
        error_text.setText("Towers reset")

        return towers, num_disk, target
    return None

def clicked_load(load,pt,error_text,win,towers)->int:
    '''
    Purpose: Utilize the load button
    Parameters:(load, pt,error_text,win):GraphWin,towers:list)
    Returns: num_disk:int, source:int, destination:int, target:int
    '''    
    if clicked(load, pt):
        saved = load_game(win, error_text)
        if saved:
            num_disk, target,towers, source, destination = saved
            draw_disks(win, towers)
            return num_disk, source, towers, destination, target
    return
   
def create_graphics(win:GraphWin)->None:
    '''
    Purpose: Create the window graphics
    Parameters: win:WinGraph
    Returns: None
    '''    
    #Bottom line
    line=Line(Point(50, 500), Point(750, 500))
    line.setFill('black')
    line.draw(win)    
   
    #Three rectangles
    rec1 = Rectangle(Point(200, 275), Point(205, 500))
    rec1.setFill('red')
    rec1.draw(win)
   
    rec2 = Rectangle(Point(400, 275), Point(405, 500))
    rec2.setFill('red')
    rec2.draw(win)  
   
    rec3 = Rectangle(Point(600, 275), Point(605, 500))
    rec3.setFill('red')
    rec3.draw(win)    
   
def write_texts(win:GraphWin)->GraphWin:
    '''
    Purpose: Create the texts for the window
    Parameters: win:WinGraph
    Returns: error_text:GraphWin, middle_text:GraphWin
    '''    
    disk_text = Text(Point(170,50), 'Number of Disks? (Enter a positive int: 3 by default)')
    disk_text.setTextColor('black')
    disk_text.setSize(12)
    disk_text.draw(win)  
    target_text = Text(Point(160,80), 'Target Tower? (Enter a positive int: 3 by default)')
    target_text.setTextColor('black')
    target_text.setSize(12)
    target_text.draw(win)
    middle_text = Text(Point(400,200),'' )
    middle_text.setTextColor('green')
    middle_text.setSize(20)
    middle_text.draw(win)
    source_text = Text(Point(85,550),'From tower?')
    source_text.setTextColor('black')
    source_text.setSize(12)
    source_text.draw(win)
    destination_text = Text(Point(180,550),'To tower?')
    destination_text.setTextColor('black')
    destination_text.setSize(12)
    destination_text.draw(win)
    error_text = Text(Point(400,525),'')
    error_text.setTextColor('red')
    error_text.setSize(12)
    error_text.draw(win)  
    return error_text, middle_text
   
def clicked(rect:GraphWin, click_point:GraphWin)->bool:
    '''
    Purpose: Obtain button click parameters
    Parameters: 
    Returns: True or False:bool
    '''    
    p1=rect.getP1()
    p2=rect.getP2()
    if p1.getX() <= click_point.getX() <= p2.getX() and p1.getY() <= click_point.getY() <=p2.getY():
            return True
    return False  
   
def draw_button(win, start_x, w, start_y, h, string)->GraphWin:
    '''
    Purpose: Set the area of the rectangles for the buttons.
    Parameters: (win, start_x, w, start_y, h, string):GraphWin
    Returns: rectangle:GraphWin
    '''    
    rectangle = Rectangle(Point(start_x, start_y), Point(start_x + w, start_y + h))
    rectangle.draw(win)
    x_mid = (start_x + start_x + w) // 2
    y_mid = (start_y + start_y + h) // 2
    text = Text(Point(x_mid, y_mid), string)
    text.setSize(12)
    text.draw(win)
    return rectangle
   
def create_entries(win:GraphWin)->GraphWin:
    '''
    Purpose: Create entry boxes for user input.
    Parameters: win:GraphWin
    Returns:
    '''    
    entry1= Entry(Point(325,50),2)
    entry1.setText('3')
    entry1.setTextColor('black')
    entry1.draw(win)
   
    entry2= Entry(Point(325,80),2)
    entry2.setText('3')
    entry2.setTextColor('black')
    entry2.draw(win)    
   
    entry3= Entry(Point(135,550),2)
    entry3.setText('1')
    entry3.setTextColor('black')
    entry3.draw(win)
   
    entry4= Entry(Point(220,550),2)
    entry4.setText('3')
    entry4.setTextColor('black')
    entry4.draw(win)    
   
    return entry1, entry2, entry3, entry4

def use_entries(entry1, entry2)->int:
    '''
    Purpose: Convert entries into integers for other functions to utilize.
    Parameters: (entry1,2): GraphWin
    Returns: num_disk:int, target:int
    '''    
    num_disk=entry1.getText()
    if num_disk.isdigit() and int(num_disk) in range(3,6):
        num_disk =int(num_disk)
        entry1.setFill('dark gray')
    else:
        entry1.setText('3')
        entry1.setFill('yellow')
        num_disk=3
           
    target=entry2.getText()
    if target.isdigit() and int(target) in range(1,4):
        target=int(target)
        entry2.setFill('dark gray')
    else:
        entry2.setText('3')
        entry2.setFill('yellow')
        target = 3
    return num_disk, target

def second_entries(entry3,entry4):
    '''
    Purpose: Convert entries into integers for other functions to utilize.
    Parameters: (entry3,4): GraphWin
    Returns: num_disk: source:int, destination:int
    '''       
     
    source=entry3.getText()
    if source.isdigit() and int(source) in range(1,4):
        source=int(source)
        entry3.setFill('dark gray')
    else:
        entry3.setText('1')
        entry3.setFill('yellow')
        source = 1
          
    destination=entry4.getText()
    if destination.isdigit() and int(destination) in range(1,4):
        destination=int(destination)
        entry4.setFill('dark gray')
    else:
        entry4.setText('3')
        entry4.setFill('yellow')
        destination = 3   
    return source, destination

def reset_default(entry1, entry2, entry3, entry4, num_disk, towers) -> None:
    '''
    Purpose: Reset default entry parameters and towers
    Parameters: (entry1,2,3,4): GraphWin, num_disk:int, towers:list
    Returns: None
    '''    
    global disk_lst
    for disk in disk_lst:
        disk.undraw()
    disk_lst = []
    entry1.setText('3')
    entry1.setFill('dark gray')
    entry2.setText('3')
    entry2.setFill('dark gray')
    entry3.setText('1')
    entry3.setFill('dark gray')
    entry4.setText('3')
    entry4.setFill('dark gray')
    
    tower1, tower2, tower3 = towers
    tower1._stack_lst = []
    tower2._stack_lst = []
    tower3._stack_lst = []
    for i in range(num_disk, 0, -1):
        tower1.push(i)   
     

def draw_disks(win:GraphWin, towers:list)->None: 
    '''
    Purpose: Create the disks.
    Parameters: win:GraphWin, towers:list
    Returns: None
    '''
    global disk_lst
    for disk in disk_lst:
        disk.undraw()
    disk_lst= []
   
    base_y = 500
    disk_height = 20
    tower_x = [200, 400, 600]
       
    for i in range(3):
        stack_list = towers[i].get_lst()  
        level = 0
        while level < len(stack_list):
            size = stack_list[level]
            width = size * 40
            left = tower_x[i] - width // 2
            right = tower_x[i] + width // 2

            top_y = base_y - (level + 1) * disk_height
            bottom_y = top_y + disk_height

            disk = Rectangle(Point(left, top_y), Point(right, bottom_y))
            disk.setFill("blue")
            disk.setOutline("red")
            disk.draw(win)
           
            disk_lst.append(disk)
            level += 1        

def move_disk(towers:list, source:int, destination:int, error_text)->bool:
    '''
    Purpose: Pop and push disks from lists. 
    Parameters: towers:list, source:int, destination:int, error_text: GraphWin
    Returns: True or False:bool
    '''    
    s= source - 1
    d = destination -1
   
    tower_from = towers[s]
    tower_to = towers[d]
   
    if tower_from.is_empty():
        error_text.setText('ERROR : the source tower is empty. Please try again!')
        return False
    moving_disk = tower_from.top()
   
    if not tower_to.is_empty() and moving_disk > tower_to.top():
        error_text.setText("ERROR: Can't put bigger disk on a smaller one. Please try again! ")
        return False
   
    tower_from.pop()
    tower_to.push(moving_disk)
    return True

def game_finished(towers:list, num_disk:int)->bool:
    '''
    Purpose: Count total game movements to reach target tower.
    Parameters: towers:list, num_disks:int
    Return: boolean returns: True or False.
    '''    
    for tower in towers[1:]:
        lst = tower.get_lst()
        if len(lst) == num_disk and lst == sorted(lst, reverse= True):
            return True
    return False

def update_middle(middle_text,move_count,target, num_disk,towers,win)->GraphWin:
    '''
    Purpose: Update middle_text with game parameters or game completion.
    Parameters: middle_text:GraphWin,move_count:int,target:int, num_disk:int,towers:list,win:GraphWin
    Returns: middle_text:GraphWin
    '''    
    if game_finished(towers,num_disk) == True:
        middle_text.setText(f'Congratulations! All disks have been moved to tower {target} in {move_count} steps')
    else:
        middle_text.setText(f'Disks = {num_disk}. Target Tower = {target}')
    return middle_text
   
def save_game(num_disk:int, target:int, towers:list, source:int, destination:int,win,error_text)->list:
    '''
    Purpose: Save a game for later usage.
    Parameter: num_tower:int, target:int, towers:list, source:int, destination:int, (win, error_text):GraphWin
    Return: None
    '''    
    filename='game.p'
    try:
        f=open(filename,'wb')
        pickle.dump((num_disk, target,towers, source, destination),f)
        f.close()
        error_text.setText('Game saved.')
    except FileNotFoundError:
        error_text.setText("Can't load a saved game or no game has been saved.")        
def load_game(win,error_text)->list:
    '''
    Purpose: Load a saved game, or return an error message if no game is saved.
    Parameter: win:GraphWin, error_message:GraphWin
    Return: saved:list, None.
    '''    
    try:
        f=open('game.p','rb')
        saved=pickle.load(f)
        f.close()
        error_text.setText('Game loaded.')
        return saved
    except FileNotFoundError:
        error_text.setText("Can't load a saved game or no game has been saved.")      
        return None
