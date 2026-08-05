import pickle
from stack import Stack
towers=[]
   
def main():
    '''
    Purpose: Initialize game
    Parameter: None
    Return: None
    '''    
    print('WELCOME TO HANOI TOWERS GAME')
    choice=input('\nEnter 1 to Start a new game and 2 to Resume a saved game: ')
    while not choice.isdigit() or int(choice) not in range(1,3):
        choice=input('\nEnter 1 to Start a new game and 2 to Resume a saved game: ')
    if choice=='1':
        print('Starting a new game'+('.'*12))
        num_tower, num_disks, target = choice_one()
        towers=create_towers(num_tower,num_disks)
        menu(num_tower,num_disks,towers)
       
    if choice== '2':
        saved_game = choice_two()
        if saved_game == None:
            num_tower, num_disks, target = choice_one()
            towers=create_towers(num_tower, num_disks)
            menu(num_tower, num_disks, towers) 
            return
        
        num_tower, num_disks, towers = saved_game
        print(create_header(num_tower,num_disks))
        print_towers(towers,num_disks)
        menu(num_tower,num_disks,towers)   

def choice_one()->tuple:
    '''
    Purpose: User input to control game parameters
    Parameter: None
    Return: num_tower:str, num_disks:int, target:str
    '''        
    #print('Starting a new game'+('.'*12))
    num_tower=input('Number of towers [min=3,..,max=9]? ')
    while not num_tower.isdigit() or int(num_tower) > 9 or int(num_tower) < 3:
        num_tower=input('Number of towers [min=3,..,max=9]? ')
        
    num_disks=input('Number of disks [min=3,..,max=9]? ')
    while not num_disks.isdigit() or int(num_disks) > 9 or int(num_disks) < 3:
        num_disks=input('Number of disks [min=3,..,max=9]? ')
    num_disks=int(num_disks)
        
    target=input('Target Tower[min=2,..,max='+num_tower+']? ')
    while not target.isdigit() or int(target) > int(num_tower) or int(target) < 2:
        target=input('Target Tower[min=2,..,max='+num_tower+']? ')
    print('')
    return num_tower, num_disks, target

def choice_two()->list:
    '''
    Purpose: Load a saved game, or return an error message if no game is saved.
    Parameter: None
    Return: saved:list, None.
    '''
    filename=input('Enter file name e.g.: game.p): ')
    while not filename.replace('.','').isalpha() or '.' not in filename: 
            filename=input('Enter file name e.g.: game.p): ')    
    try:
        f=open(filename,'rb')
        saved=pickle.load(f)
        f.close()
        return saved
    except FileNotFoundError:
        print('file:',filename,'not found: Starting a new game '+ (16*'.'))
      #  choice_one()
        return None

def create_header(num_tower:str,num_disks:int)->str:
    '''
    Purpose: Create the tower headers
    Parameter: num_tower:str, num_disks:int
    Return: header:str
    '''    
    header=''
    for i in range(1,int(num_tower)+1):
        upper_layer=f"{num_disks*'='}{i}{num_disks*'='}"
        header += upper_layer+' '
    return header  

def create_towers(num_tower:str,num_disks:int)->list:    
    '''
    Purpose: Create the stack list, append the disks to first index
    Parameter: num_tower:str, num_disks:int
    Return: towers:list
    '''
    towers=[]
    for num in range(int(num_tower)):
        towers.append(Stack())
        if num == 0:
            for i in range(num_disks,0,-1):
                towers[0].push(i) 
    print(create_header(num_tower,num_disks))
    print_towers(towers,num_disks)
    return towers
 
def print_towers(towers:list, num_disks:int)->None:
    '''
    Purpose: Print towers for the rest of the functions to utilize.
    Parameter: towers:list, num_disks:int
    Return: None
    '''  
    #empty=[]
    #for t in towers:
        #empty.append(t.get_lst())
    i=0
   
    for row in range(num_disks):
        for column in range(len(towers)):
            t_index=towers[column].get_lst()
            if i < len(t_index):
                left = '*' * t_index[i]
                right = '*' * t_index[i]
                space=int(num_disks - t_index[i]) *' '
                stars=f'{space}{left}|{right}{space}'                
                print(stars,end=' ')
            else:
                spaces=int(num_disks) *' '
                print(f'{spaces}|{spaces}',end=' ')                    
        i+=1
        print()
 
def game_rules(source:int, destination:int, towers:list)->bool:
    '''
    Purpose: Validate the moves of the disks to keep push/pops moves legal
    Parameter: source:int, destination:int, towers:list
    Return: boolean returns: True or False
    ''' 
    source_tower = towers[source - 1]
    dest_tower = towers[destination - 1]
    if source_tower.is_empty():
        print('Invalid move. The source tower is empty. Please try again!')
        print('')
        return False 
   
    if dest_tower.is_empty():
        return True
    
    top_source = source_tower.get_lst()[-1]      
    top_destination = dest_tower.get_lst()[-1]          

    if top_source > top_destination:
        print ("Invalid move. Can't put bigger disk on a smaller one. Please try again!")
        print('')
        return False
    return True    

def move_disk(source:int, destination:int, towers:list, move_count:int,num_disks:int)->int:
    '''
    Purpose: Perform the push and pop stack methods to move the disks.
    Parameter: source:int, destination:int, towers:list, move_count:int, num_disks:int 
    Return: move_count:int
    '''  
    disk=towers[source].pop()
    towers[destination].push(disk)
 
    return move_count

def game_finished(towers:list, num_disks:int)->bool:
    '''
    Purpose: Count total game movements to reach target tower.
    Parameter: towers:list, num_disks:int
    Return: boolean returns: True or False.
    '''    
    for tower in towers[1:]:
        lst = tower.get_lst()
        if len(lst) == num_disks and lst == sorted(lst, reverse= True):
            return True
    return False
   
def menu(num_tower:str,num_disks:int,towers:list)->None:
    '''
    Purpose: Perform user input commands to control the game.
    Parameter: num_tower:str, num_disks:int, towers:list
    Return: None.
    '''
    move_count = 0
    while True:
        
        print('\n\t1 - Move a disk\n\t2 - Save and End\n\t3 - End without Saving')
        new_choice=input('\nEnter 1 or 2 or 3: ')
        while not new_choice.isdigit() or int(new_choice) not in range(1,4):
            print('\n\t1 - Move a disk\n\t2 - Save and End\n\t3 - End without Saving')
            print('')
            new_choice=input('Enter 1 or 2 or 3: ')
            
        move_count += 1
        if new_choice=='1':
            control=control_disks(num_tower, num_disks, towers, move_count)
            if control == True:
                return 
            
        elif new_choice == '2':
            save_game(num_tower,num_disks,towers)
            break
            
        elif new_choice == '3':
            end_game()
            break
            
def control_disks(num_tower:str, num_disks:int, towers:list, move_count:int)->bool: 
    '''
    Purpose: Perform user input commands to move disks between towers.
    Parameter: num_tower:str, num_disks:int, towers:list, move_count:int
    Return: None.
    '''    
    source_tower=input('Source Tower? ')
    while not source_tower.isdigit() or int(source_tower) not in range(1,int(num_tower)+1):
        source_tower=input('Source Tower? ')
       
    dest_tower=input('Destination Tower? ')
    while not dest_tower.isdigit() or int(dest_tower) not in range(1,int(num_tower)+1):
        dest_tower=input('Destination Tower? ')
       
    source = int(source_tower)
    destination = int(dest_tower)
    if game_rules(source, destination, towers) == True:
        # -1 because list index starts at 0
        source -= 1
        destination -= 1 
        
        move_count = move_disk(source, destination, towers, move_count,num_disks)
        print('')
 
        if game_finished(towers, num_disks) == True :
            print(create_header(num_tower,num_disks))
            print_towers(towers,num_disks)             
            print(f'Good Job! Transfer acheived in {move_count} steps')
                       
            return True
        
    print(create_header(num_tower,num_disks))
    print_towers(towers,num_disks)
    
def save_game(num_tower:str,num_disks:int,towers:list)->list:
    '''
    Purpose: Save a game for later usage. 
    Parameter: num_tower:str, num_disks:int, towers:list
    Return: None.
    '''    
    filename=input('Enter file name e.g.: game.p): ')
    while not filename.replace('.','').isalpha() or '.' not in filename: 
            filename=input('Enter file name e.g.: game.p): ')
    try:
        f=open(filename,'wb')
        pickle.dump((num_tower,num_disks,towers),f)
        print("Game Saved ......")
        print("See you later ......!")  
        f.close()
        return
    except FileNotFoundError:
        
        print('File could not be saved')
        return None

def end_game()->None:
    '''
    Purpose: End the game without saving to a file.
    Parameter: None
    Return: None
    '''    
    print('Ending Game'+('.'*6))
    print('Goodbye!')
