# Name: Marc-Dwayne Santos

import textwrap

game_map = {
    # Rooms
    'room401': {
        'room_ID': 'room401',
        'room_name': 'Room 401',
        'room_description': "'My room's a mess... I wonder what's going on outside?'",
        'explored': 'true',
        'adjacent_rooms': {
            'south': ["hallwayA_4thFloor", None],
        }
    },
    'room402': {
        'room_ID': 'room402',
        'room_name': 'Room 402',
        'room_description': "The blast radius of the explosion was so large, it tore through room "
                            "402 and 404's walls.\n'Door's wide open.' ",
        'explored': 'false',
        'adjacent_rooms': {
            'north': ['hallwayA_4thFloor', None],
            'east': ['room404', None],
        },
        'available_items': ['Lighter']
    },
    'room403': {
        'room_ID': 'room403',
        'room_name': 'Room 403',
        'room_description': "Your eyes have adjusted to the darkness for so long, the light from the room completely blinded you as soon\n"
                            "as you opened the door. Inside looks as if nothing ever happened. It's surprisingly unsettling, considering what\n"
                            "you've experienced.",
        'explored': 'true',
        'adjacent_rooms': {
            'south': ["hallwayB_4thFloor", None],
        }
    },
    'room404': {
        'room_ID': 'room404',
        'room_name': 'Room 404',
        'room_description': "As you move your way to Room 404, you see that the rubble from the explosion piled up in "
                            "front of the door.\n'I can't get through the other side of the hole this way!'",
        'explored': 'false',
        'adjacent_rooms': {
            'west': ['room402', None],
            'below': ['room304', 'Bed Rope']
        },
        'available_items': ['Bed Rope']
    },
    'room304': {
        'room_ID': 'room304',
        'room_name': 'Room 304',
        'room_description': "Unfortunately, your poorly made knot caused you to fall mid-climb into the seemingly empty room.\n"
                            "'No way back up now...'\n"
                            "The room reeked of decaying flesh coming from the deceased resident who lies next to the door.",
        'explored': 'false',
        'adjacent_rooms': {
            'north': ['hallway_3rdFloor', 'Crowbar']
        },
        'available_items': ['Crowbar']
    },

    # Hallways
    'hallwayA_4thFloor': {
        'room_ID': 'hallwayA_4thFloor',
        'room_name': 'Fourth-Floor Hallway (West)',
        'room_description': "'A giant hole in the middle of the hallway?? How'd I sleep through all this?'",
        'explored': 'false',
        'adjacent_rooms': {
            'north': ['room401', None],
            'south': ['room402', None],
            'west': ['stairs_4thFloor', None],
            'east': ['hallwayB_4thFloor', 'Wooden Plank'],
        }
    },
    'hallwayB_4thFloor': {
        'room_ID': 'hallwayB_4thFloor',
        'room_name': 'Fourth-Floor Hallway (East)',
        'room_description': "Inching closer to room 403, you start to feel a unique sense of unease.",
        'explored': 'false',
        'adjacent_rooms': {
            'north': ['room403', "Room 403's Key Card"],
            'west': ['hallwayA_4thFloor', None],
            'east': ['elevator', 'Crowbar'],
        },
        'available_items': ['Pistol', 'Note']
    },
    'hallway_3rdFloor': {
        'room_ID': 'hallway_3rdFloor',
        'room_name': 'Third-Floor Hallway',
        'room_description': "The putrid stench grew stronger and started to flood your lungs as you enter the Third-Floor Hallway.\n"
                            "Even when you try to adapt to the smell, you notice multiple carcasses littered all over the hallway."
                            "\nIf the smell wasn't nauseating enough, the sight alone did the job. The elevator to the "
                            "east was\nbarricaded by heaps of furniture, most likely coming from room 304. There's no way "
                            "of calling it from here.",
        'explored': 'false',
        'adjacent_rooms': {
            'south': ['room304', 'Crowbar'],
            'west': ['stairs_3rdFloor', 'Crowbar']
        },
        'available_items': ['Wooden Plank']
    },

    # Stairs
    'stairs_4thFloor': {
        'room_ID': 'stairs_4thFloor',
        'room_name': 'Fourth-Floor Stairs',
        'room_description': "It’s so dark in here… I’m going to need some kind of light if I want to go down.",
        'explored': 'false',
        'adjacent_rooms': {
            'east': ["hallwayA_4thFloor", None],
            'below': ["stairs_3rdFloor", 'Lighter']
        }
    },
    'stairs_3rdFloor': {
        'room_ID': 'stairs_3rdFloor',
        'room_name': 'Third-Floor Stairs',
        'room_description': "As you reach the Third-Floor Stairs, you notice piles of furniture covering every step, "
                            "making it completely dangerous to go further down.",
        'explored': 'false',
        'adjacent_rooms': {
            'above': ['stairs_4thFloor', 'Lighter'],
            'east': ['hallway_3rdFloor', 'Crowbar'],
        },
        'available_items': ["Room 403's Key Card"]
    },

    # Elevator
    'elevator': {
        'room_ID': 'elevator',
        'room_name': 'Elevator',
        'room_description': "As the elevator doors close, you see the hallway give in to the existing damage.\n"
                            "The building is about to collapse; there's no turning back now!",
        'floor': 4,
        'explored': 'false',
        'adjacent_rooms': {},
        'available_items': ['Elevator Fob']
    }
}

items_list = {
    'Lighter': 'I can use this to go through any dark places.',
    'Bed Rope': 'Looks like I can use this to climb my way down to the room below me. It’s not the best, but it’ll do.',
    'Crowbar': 'I can use this to tear those barricades down.',
    'Wooden Plank': 'I think I can use this to get to the other side of the hole! … But how can I get back up?',
    "Room 403's Key Card": "If 403's power is still on, it might make sense to keep this around.",
    'Pistol': 'Whatever’s inside, looks like he wants me to finish the job.',
    'Note': "It's the note that came with the pistol:\n\n" +
             "\t\tIf you're reading this, it means it's too late for me. Past these doors will be me... Or at least what used to be me.\n"
             "\t\tI thought I could hold out for a little while longer, but there's nothing left for me to live for. Even then,\n"
             "\t\tI couldn't get myself to finish the deed. So to whoever's reading this, please finish it for me. Do not even for a second\n"
             "\t\tthink to hesitate, otherwise you'll end up like the rest of us.\n\n\t\tP.S., Should you ever still want to keep living, turn on the generator\n"
             "\t\tthat I hot-wired to my room. It'll switch power to the elevator. Escape through the 2nd floor. Ground's probably infested with them.\n\n"
             "\t\tGood luck. \n\n\t\t --David",
    'Elevator Fob': 'One-way ticket.'
}

valid_directions = ['north', 'south', 'east', 'west', 'up', 'down']

inventory = []
adjacent_rooms = {}

ROOM_START = "room401"
TITLE = f"\n---ROOM 403: A TEXT ADVENTURE GAME---\n\n"
INTRO = textwrap.fill(
    "You wake up to find your apartment completely covered in debris. Curious, you leave your room to find that "
    "everything around you is in the same state. As you try to make out what's in front of you, you notice a "
    "huge hole separating you and the other half of the hallway. Everywhere is dark... except room 403 at the "
    "other side of the hole. Maybe whoever's inside 403 can tell you what's going on? Find and use any items you "
    "can find to get to the room, but be cautious! Who knows what could be inside...",100)
SEPARATOR = "----------------------\n"

# ANSI COLOR CODES https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
LIGHT_BLUE = "\033[1;34m"
LIGHT_GREEN = "\033[1;32m"
LIGHT_RED = "\033[1;31m"
LIGHT_CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
NEGATIVE = "\033[7m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
END = "\033[0m"

#--------------------------------------------------------------------------------------------------------------------#

def run_game():
    print(f"{BOLD}{TITLE}{END}"
          f"{ITALIC}{INTRO}{END}")
    current_room = load_room(ROOM_START)

    get_help()
    action = input(f"Your move (to see all actions, enter '{LIGHT_BLUE}Help{END}'): ")
    execute(action, current_room)

def execute(action, current_room):
    action = action.lower()
    floor = 4
    while action != 'exit':
        if action.startswith('look'):
            action = action.split()
            direction = action[1]
            look(direction)
        elif action.startswith('move'):
            action = action.split()
            direction = action[1]
            current_room = move(current_room, direction)

            room_name = current_room['room_name']
            if room_name == 'Elevator':
                floor = current_room['floor']
                break
        elif action.startswith('examine'):
            action = action.split()
            item = " ".join(action[1:len(action)])
            examine_item(item)
        else:
            match action:
                case 'inspect room' | 'inspect':
                    inspect_room(current_room)
                case 'rooms':
                    show_adjacent_rooms()
                case 'inventory' | 'inv':
                    print_inventory()
                case 'help':
                    get_help()
                case _:
                    print(f"\t{ITALIC}Invalid action: '{LIGHT_RED}{action}{END}'{ITALIC}. Try again.{END}\n")

        action = input(f"Your move (to see all actions, enter '{LIGHT_BLUE}Help{END}'): ").lower()

    # TODO: Final Results - Floors
    # TODO: Save-States



def inspect_room(room):
    room_name = room['room_name']
    room_description = room['room_description']
    print(f"{SEPARATOR}{NEGATIVE} ~You are in: {BOLD}{room_name}~ {END}")
    print(f"{ITALIC}{room_description}{END}\n")
    if 'available_items' in room:
        take_item(room, room['available_items'])

def print_inventory():
    print(f'Inventory: {inventory}\n')

def get_help():
    print("***Available Actions: ***\n"
          f"\t{LIGHT_BLUE}Inspect room{END} or {LIGHT_BLUE}Inspect{END}: "
          "Shows room description, available items, and interactable objects.\n"

          f"\t{LIGHT_BLUE}Look {LIGHT_GREEN}['North' / 'South' / 'East' / 'West' / 'Up' / 'Down']{END}: "
          "Hints an adjacent room in the provided direction.\n"

          f"\t{LIGHT_BLUE}Rooms{END}: "
          "Shows all adjacent rooms (marked '???' if unexplored).\n"
          
          f"\t{LIGHT_BLUE}Move {LIGHT_GREEN}['North' / 'South' / 'East' / 'West' / 'Up' / 'Down']{END}: "
          "Move to the adjacent room in the provided direction.\n"

          f"\t{LIGHT_BLUE}Inventory{END} or {LIGHT_BLUE}Inv{END}: "
          "Shows all items and descriptions in your inventory.\n"

          f"\t{LIGHT_BLUE}Examine ['Item']{END}: "
          "Shows a brief description of the item.\n"

          f"\t{LIGHT_RED}Exit{END}: "
          f"Exits the game ({LIGHT_RED}WARNING: This will also reset the game!{END}).\n")

def load_room(room_ID):
    room = game_map[room_ID]
    global adjacent_rooms
    adjacent_rooms = room['adjacent_rooms']

    inspect_room(room)
    print_inventory()
    return room

def look(direction):
    direction = direction.lower()
    if direction in valid_directions:
        if direction == 'up' or direction == 'down':
            direction = translate_vertical_direction(direction)

        if direction in adjacent_rooms:
            adjacent_room_query = adjacent_rooms[direction]
            adjacent_room_ID = adjacent_room_query[0]
            adjacent_room = game_map[adjacent_room_ID]
            print(f"\t{ITALIC}{direction.capitalize()}: {adjacent_room['room_name']}{END}\n") if adjacent_room['explored'] == 'true' else print(f"\t{ITALIC}What's there?{END}\n")
        else:
            print(f"\t{ITALIC}There's nothing there.{END}\n")
    else:
        print(f"\t{ITALIC}Invalid direction.{END}\n")

def show_adjacent_rooms():
    for direction in adjacent_rooms:
        adjacent_room = game_map[adjacent_rooms[direction][0]]
        is_explored = adjacent_room['explored']
        room_ID = adjacent_room['room_name']
        if is_explored == 'true':
            print(f"\t{ITALIC}{direction.capitalize()}: {room_ID}{END}")
        else:
            print(f"\t{ITALIC}{direction.capitalize()}: ???{END}")
    print()

def move(current_room, direction):
    direction = direction.lower()
    if direction in valid_directions:
        if direction == 'up' or direction == 'down':
            direction = translate_vertical_direction(direction)

        if direction in adjacent_rooms:
            adjacent_room = adjacent_rooms[direction]
            adjacent_room_ID = adjacent_room[0]
            required_item = adjacent_room[1]

            room = game_map[adjacent_room_ID]
            if required_item is None:
                room['explored'] = 'true'
                game_map.update(room)
                current_room = load_room(adjacent_room_ID)
            else:
                if required_item in inventory:
                    current_room = move_with_required_item(adjacent_room_ID, current_room, required_item)
                else:
                    print_reason_for_impasse(required_item)
        else:
            print("I can't go that way.\n")
    else:
        print(f"Invalid direction: {direction}.\n")

    room_name = current_room['room_name']
    if room_name == 'room403':
        # TODO Room 403 Sequence
        pass
    if room_name == 'elevator':
        # TODO Elevator Sequence
        pass

    return current_room

# Helper Method for look() and move()
def translate_vertical_direction(direction):
    if direction == 'up':
        direction = 'above'
    elif direction == 'down':
        direction = 'below'
    return direction

# Helper Method for move(), where specific item is required
def move_with_required_item(adjacent_room_ID, current_room, required_item):
    room = game_map[adjacent_room_ID]
    print(f"\tLooks like I'll need a {YELLOW}{required_item}{END} to pass through.") \
        if required_item[0] not in ['a', 'e', 'i', 'o', 'u'] else (
        print(f"\tLooks like I'll need an {YELLOW}{required_item}{END} to pass through."))

    answer = input(f"Use {YELLOW}{required_item}{END}? Yes/No: ").lower()
    while answer not in ['yes', 'no']:
        print(f"\tInvalid action: '{LIGHT_RED}{answer}{END}'. Try again.\n")
        answer = input(f"Use {YELLOW}{required_item}{END}? Yes/No: ").lower()
    else:
        if answer == 'yes':
            print(f"\tUsed {YELLOW}{required_item}{END}.")
            use_item(required_item)
            room['explored'] = 'true'
            game_map.update(room)
            return load_room(adjacent_room_ID)
        else:
            print(f"\t{YELLOW}{required_item}{END} is required to pass through.\n")
            return current_room

# Helper method for move() to print reason for impasse when item is required
# TODO: Cleanup - Move to items_list
def print_reason_for_impasse(required_item):
    match required_item:
        case 'Crowbar':
            print(f"\t'I think I can make my way through if I had something to {YELLOW}tear down{END} the barricade.'\n")
        case 'Lighter':
            print(f"\t'It's too dark for me to see where I'm going. I need to find {YELLOW}some kind of light{END}.'\n")
        case 'Bed Rope':
            print(f"\t'I think I can make something to {YELLOW}climb my way down{END} this hole.'\n")
        case "Room 403's Key Card":
            print(f"\t'Locked. I'll need to find the {YELLOW}key card to this door{END}.'\n")

def examine_item(item):
    item = "Room 403's Key Card" if item.lower() == "room 403's key card" else item.title()
    if item in inventory:
        print(f"\t{YELLOW}{item}{END}: {ITALIC}{items_list.get(item,'')}{END}\n")
    elif item not in inventory:
        if item not in items_list:
            print(f"\t{ITALIC}Invalid item '{LIGHT_RED}{item}{END}'.\n")
        else:
            print(f"\t{ITALIC}Item '{LIGHT_RED}{item}{END}'{ITALIC} is not in inventory.{END}\n")

# TODO: Cleanup - Move to items_list
def take_item(room, items):
    for item in items:
        match item:
            case 'Lighter':
                print(
                    f"\t{ITALIC}Seeing how there's barely any power anywhere, you searched for anything to provide light{END}\n\t"
                    f"{ITALIC}and found a {YELLOW}{item}{END} {ITALIC}in the room. The light is faint, but enough to help see where you're going.{END}\n")
            case "Room 403's Key Card":
                print(
                    f"\t{ITALIC}Something was glistening amidst the mess. It was {YELLOW}{item}{END}{ITALIC}, but why is it here?{END}\n")
            case 'Bed Rope':
                print(
                    f"\t{ITALIC}As you continue your search, you see another hole that leads straight to the room below.\n\t"
                    f"'I'll need something to climb down.' Of all the things you could find, you decided to strip\n\t"
                    f"the bedsheets off the bed and roll it up into a {YELLOW}make-shift rope.{END}\n")
            case 'Crowbar':
                print(
                    f"\t{ITALIC}You notice that the door is barricaded with wooden planks. There must be a reason why he prevented \n\t"
                    f"himself from ever going out. The thought of what's on the other side chilled you to the bone.\n\tOn the dead body's hand was the {YELLOW}{item}{END} "
                    f"{ITALIC}that was used to strip the wood off the room's drawer.{END}\n")
            case 'Wooden Plank':
                print(
                    f"\t{ITALIC}Looking up, you see the hallway that you were just in a while ago. A {YELLOW}large piece of the wooden flooring{END}\n"
                    f"\t{ITALIC}from the floor above flattened a good pile of the bodies in the hallway. Although heavy, it looks large\n"
                    f"\tand portable enough to bridge across the gap.\n"
                    f"\t'Next step... How do I get back up?'{END}\n")
            case 'Pistol':
                print(f"\t{ITALIC}Conveniently placed in front of room 403's door is a {YELLOW}{item}{END}.")
            case 'Note':
                print(f"\t{ITALIC}Underneath the {YELLOW}Pistol{END} {ITALIC}is a {YELLOW}{item}{END}. {ITALIC}(enter '{LIGHT_BLUE}Examine Note{END}' {ITALIC}to read the note)")
            case 'Elevator Fob':
                print(f"\t{ITALIC}You struggle to move anywhere as none of the floor buttons are working. 'Thankfully', there is a\n"
                      f"\tbody with you in the elevator. As you search through the body, you find the {YELLOW}{item}{END}\n"
                      f"\t{ITALIC}tucked in a pocket.{END}\n")
        inventory.append(item)
        print(f"\t{ITALIC}Took {YELLOW}{item}{END}.\n")

    room.pop("available_items")
    game_map.update(room)

def use_item(item):
    # TODO: Complete function
    pass

run_game()
