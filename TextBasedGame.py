# Name: Marc-Dwayne Santos
import sys
import textwrap
import time

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
        'room_description': "The blast radius of what looks to be the explosion was so large, it tore through room "
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
        },
        'sequence_triggered': 'false',
        'read_note': 'false'
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
        'room_description': "Unfortunately, your poorly-made knot caused you to fall mid-climb into the seemingly empty room.\n"
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
                            "east was\nblocked by heaps of furniture, most likely coming from room 304. There's no way "
                            "of calling it from here.\nThe stairs to the west was barricaded too...",
        'explored': 'false',
        'adjacent_rooms': {
            'south': ['room304', None],
            'west': ['stairs_3rdFloor', 'Crowbar']
        },
        'available_items': ['Wooden Plank']
    },

    # Stairs
    'stairs_4thFloor': {
        'room_ID': 'stairs_4thFloor',
        'room_name': 'Fourth-Floor Stairs',
        'room_description': "It’s so dark in here…",
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
        'available_items': ['Elevator Fob'],
        'is_generator_on': 'false'
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
             "\t\tIf you're reading this, it means it's too late for me. Past these doors will be me... Or at least what I used to be.\n"
             "\t\tI thought I could hold out for a little while longer, but there's nothing left for me to live for. Even then,\n"
             "\t\tI couldn't get myself to finish the deed. So to whoever's reading this, please finish it for me. Don't think to hesitate\n"
             "\t\teven for a second, otherwise you'll end up like the rest of us.\n\n"
             "\t\tP.S., Should you ever still want to keep living, turn on the generator that I hot-wired to my room. It'll switch power to the elevator.\n"
             "\t\tEscape through the 2nd floor. Ground's probably infested with them.\n\n"
             "\t\tGood luck. \n\n\t\t --David",
    'Elevator Fob': 'One-way ticket.'
}

valid_directions = ['north', 'south', 'east', 'west', 'up', 'down']

inventory = []
adjacent_rooms = {}
floor = None
command_count = 0

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

    global floor
    match floor:
        case 3:
            print(f"\t{ITALIC}You press the button for the third floor. Once you arrive, you remember that the elevator and the stairs\n"
                  "\tgoing down from this floor was already blocked by heaps of furniture, let alone the additional rubble\n"
                  "\tfrom the collapsed floor above. \n\n"
                  f"\tThe elevator goes dark. Much like the lifeless body next to you, you realize you're stuck there... forever.{END}\n")
        case 2:
            print(
                f"\t{ITALIC}You press the button for the second floor. You arrive to a seemingly empty hallway, with a\n"
                f"\tstraight shot to the 2nd-floor balcony.\n\n"
                f"\tThe elevator goes dark. You make a run towards the 2nd-floor balcony.{END}\n\n"
                
                f"{LIGHT_GREEN}THE END{END}\n\n"
                f"Congratulations on beating the game!\n"
                f"Number of commands entered: {LIGHT_CYAN}{command_count}{END}\n"
                f"Time spent to reach finish: {LIGHT_CYAN}{record_time_spent()}{END}")
            sys.exit()
        case 1:
            print(
                f"{ITALIC}You press the button for the first floor. Once you arrive, you're met with dozens more people like"
                f"\tthe man you saw in room 403. Going down here was a huge mistake, as they all start to race towards you with\n"
                f"\tintense hunger in their eyes.\n\n"
                f"\tThe elevator goes dark. There's nothing left to do than to become one of them.{END}\n")

    if get_game_over_response() == 'yes':
        floor = 4
        hallwayB_4thFloor = game_map['hallwayB_4thFloor']
        hallwayB_4thFloor['adjacent_rooms']['east'][1] = 'Crowbar'

        load_room('hallwayB_4thFloor')
        action = input(f"Your move (to see all actions, enter '{LIGHT_BLUE}Help{END}'): ")
        execute(action, current_room)
    else:
        sys.exit()

def execute(action, current_room):
    action = action.lower()
    while action != 'exit':
        if action.startswith('look') and len(action.split()) == 2:
            action = action.split()
            direction = action[1]
            look(direction)
        elif action.startswith('move') and len(action.split()) == 2:
            action = action.split()
            direction = action[1]
            current_room = move(current_room, direction)

            room_name = current_room['room_name']
            if room_name == 'Room 403' and game_map['room403']['read_note'] == 'true' and game_map['room403']['sequence_triggered'] == 'true' and game_map['elevator']['is_generator_on'] == 'false': # If note was read after already triggering the room 403 sequence, run generator
                turn_on_generator()
            if room_name == 'Elevator':
                increase_command_count()
                trigger_elevator_sequence()
                break
        elif action.startswith('examine'):
            action = action.split()
            item = " ".join(action[1:len(action)])
            examine_item(item)

            room_name = current_room['room_name']
            if (room_name == 'Room 403'
                    and game_map['room403']['read_note'] == 'true'
                    and game_map['room403']['sequence_triggered'] == 'true'
                    and game_map['elevator']['is_generator_on'] == 'false'): # If reading note in room 403 after already triggering the room 403 sequence, run generator
                current_room['room_description'] = (
                    "The lights in this room are now off. The generator must be running the elevator now.\n"
                    "'What just happened...?'")
                turn_on_generator()
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

        increase_command_count()
        action = input(f"Your move (to see all actions, enter '{LIGHT_BLUE}Help{END}'): ").lower()

    # TODO (OPTIONAL): Save-States


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
    print(
        "***Available Actions: ***\n"
        f"\t{LIGHT_BLUE}Inspect room{END} or {LIGHT_BLUE}Inspect{END}: "
        "Shows room description, available items, and interactable objects.\n"
          
        f"\t{LIGHT_BLUE}Rooms{END}: "
        "Shows all adjacent rooms (marked '???' if unexplored).\n"

        f"\t{LIGHT_BLUE}Look {LIGHT_GREEN}['North' / 'South' / 'East' / 'West' / 'Up' / 'Down']{END}: "
        "Hints an adjacent room in the provided direction.\n"
          
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
    if len(adjacent_rooms) > 0:
        for direction in adjacent_rooms:
            adjacent_room = game_map[adjacent_rooms[direction][0]]
            is_explored = adjacent_room['explored']
            room_ID = adjacent_room['room_name']
            if is_explored == 'true':
                print(f"\t{ITALIC}{direction.capitalize()}: {room_ID}{END}")
            else:
                print(f"\t{ITALIC}{direction.capitalize()}: ???{END}")
        print()
    else:
        print(f"\t{ITALIC}There's no where to go.{END}\n") # Unique to elevator

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
                current_room = load_room(adjacent_room_ID)
            else:
                if required_item in inventory:
                    current_room = move_with_required_item(adjacent_room_ID, current_room, required_item, direction)
                else:
                    print_reason_for_impasse(required_item)

            game_map.update(current_room)
        else:
            print("I can't go that way.\n")
    else:
        print(f"Invalid direction: {direction}.\n")

    return current_room

# Helper Method for look() and move()
def translate_vertical_direction(direction):
    if direction == 'up':
        direction = 'above'
    elif direction == 'down':
        direction = 'below'
    return direction

# Helper Method for move(), where specific item is required
def move_with_required_item(adjacent_room_ID, current_room, required_item, direction):
    room = game_map[adjacent_room_ID]
    print(f"\tLooks like I'll need a {YELLOW}{required_item}{END} to pass through.") \
        if required_item[0] not in ['a', 'e', 'i', 'o', 'u'] else (
        print(f"\tLooks like I'll need an {YELLOW}{required_item}{END} to pass through."))

    answer = input(f"Use {YELLOW}{required_item}{END}? Yes/No: ").lower()
    while answer not in ['yes', 'no']:
        print(f"\tInvalid action: '{LIGHT_RED}{answer}{END}'. Try again.\n")
        increase_command_count()
        answer = input(f"Use {YELLOW}{required_item}{END}? Yes/No: ").lower()
    else:
        increase_command_count()
        if answer == 'yes':
            print(f"\tUsed {YELLOW}{required_item}{END}.")
            use_item(required_item, direction)
            room['explored'] = 'true'
            game_map.update(room)
            current_room = load_room(adjacent_room_ID)
        else:
            print(f"\t{YELLOW}{required_item}{END} is required to pass through.\n")

    room_name = current_room['room_name']
    if room_name == 'Room 403' and current_room['sequence_triggered'] == 'false':
        current_room['sequence_triggered'] = 'true'
        trigger_403_sequence()

    return current_room

# Helper method for move() to print reason for impasse when item is required
def print_reason_for_impasse(required_item):
    match required_item:
        case 'Crowbar':
            print(f"\t'I think I can make my way through if I had something to {YELLOW}tear down{END} this barricade.'\n")
        case 'Lighter':
            print(f"\t'It's too dark for me to see where I'm going. I need to find {YELLOW}some kind of light{END}.'\n")
        case 'Bed Rope':
            print(f"\t'I think I can make something to {YELLOW}climb my way down{END} this hole.'\n")
        case "Room 403's Key Card":
            print(f"\t'Locked. I'll need to find the {YELLOW}key card to this door{END}.'\n")
        case 'Wooden Plank':
            print(f"\tI need to find {YELLOW}something sturdy{END} to bridge across this gap.")

def examine_item(item):
    item = "Room 403's Key Card" if item.lower() == "room 403's key card" else item.title()
    if item in inventory:
        if item == 'Note':
            game_map['room403']['read_note'] = 'true'
        print(f"\t{YELLOW}{item}{END}: {ITALIC}{items_list.get(item,'')}{END}\n")
    elif item not in inventory:
        if item not in items_list:
            print(f"\t{ITALIC}Invalid item '{LIGHT_RED}{item}{END}'.\n")
        else:
            print(f"\t{ITALIC}Item '{LIGHT_RED}{item}{END}'{ITALIC} is not in inventory.{END}\n")

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
                    f"'I'll need something to climb down.'\n\t"
                    f"Of all the things you could find, you decided to strip the bedsheets off the bed and roll\n\t"
                    f"it up into a {YELLOW}make-shift rope.{END}\n")
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
                      f"\t{ITALIC}tucked in one of its pockets.{END}\n")
        inventory.append(item)
        print(f"\t{ITALIC}Took {YELLOW}{item}{END}.\n")

    room.pop("available_items")
    game_map.update(room)

def use_item(item, direction):
    if item in ['Bed Rope', 'Wooden Plank']:
        # Remove item from inventory
        inventory.remove(item)

        # Remove adjacent room
        adjacent_rooms.pop(direction)
        print(f"\t{LIGHT_RED}Removed{END} {YELLOW}{item}{END} {LIGHT_RED}from your inventory.{END}")

    else:
        # Remove adjacent room item requirement
        adjacent_room_item_req = adjacent_rooms[direction]
        adjacent_room_item_req[1] = None

        # Remove room item requirement going back
        adjacent_room = game_map[adjacent_room_item_req[0]]
        if adjacent_room['room_name'] != 'Elevator':
            match direction:
                case 'north': direction = 'south'
                case 'south': direction = 'north'
                case 'east': direction = 'west'
                case 'west': direction = 'east'
                case 'above': direction = 'below'
                case 'below': direction = 'above'
            current_room_item_req = adjacent_room['adjacent_rooms'][direction]
            current_room_item_req[1] = None

def trigger_403_sequence():
    print(f"{ITALIC}However, you notice a smearing trail of blood leading to the back of the room. At the end of the trail looks to be\n"
          "an unconscious man sitting against the wall. He seems to be bleeding out.\n\n"
          "*OPTIONS*\n"
          f"\t{LIGHT_BLUE}Shoot him\n"
          f"\tCall out\n"
          f"\tApproach him{END}\n")

    action = input('Your move: ').lower()
    while action not in ['shoot him', 'call out', 'approach him', 'leave him be']:
        print(f"\t{ITALIC}Invalid action: '{LIGHT_RED}{action}{END}'{ITALIC}. Try again.{END}\n")
        increase_command_count()
        action = input('What will you do? ').lower()
    else:
        increase_command_count()
        match action:
            case 'shoot him':
                print(f"\t{ITALIC}Using your {YELLOW}Pistol{END}, {ITALIC}you decided to end the man's slow and painful suffering with one bullet.\n")

            case 'call out':
                print(
                    f"\t{ITALIC}'Hey, are you alright?'\n\n"
                    f"\tYou call out to the wounded man to take a closer look. As your voice echoes throughout the room, you notice\n"
                    f"\this arms start to twitch, almost seizure-like. Within seconds, he lunges, but thankfully there was a\n"
                    f"\tgood amount of distance before he could ever reach you. Despite his appearance, he starts to sprint\n"
                    f"\ttowards you in a rampant state!\n\n"
                    f"*OPTIONS*\n"
                    f"\t{LIGHT_BLUE}Shoot him{END}\n")

                shoot_villain_alt()

            case 'approach him':
                print(
                    f"\t{ITALIC}You slowly approach the wounded man to take a closer look. Halfway through the trail, you notice his arms\n"
                    f"\tstart to twitch...almost seizure-like.\n\n"
                    f"\tWithin seconds, he lunges towards you, knocking back the {YELLOW}Pistol{END} {ITALIC}you were holding as he pins you to the ground.\n"
                    f"\tAs his blood drips down on your body, you see him biting the air as he makes horrifying guttural noises. You\n"
                    f"\thold him back, trying not to let him bite you.\n\n"
                    f"*OPTIONS*\n"
                    f"\t{LIGHT_BLUE}Reach for pistol\n"
                    f"\tReach for crowbar{END} {ITALIC}next to you{END}\n")

                action = input('What will you do? ').lower()
                while action not in ['reach for pistol', 'reach for crowbar']:
                    print(f"\t{ITALIC}Invalid action: '{LIGHT_RED}{action}{END}'{ITALIC}. Try again.{END}\n")
                    increase_command_count()
                    action = input('What will you do? ').lower()
                else:
                    increase_command_count()
                    match action:
                        case 'reach for pistol':
                            print(f"\t{ITALIC}You try to reach for the pistol, but it's too far to grab! Doing so made you lose grip of the man trying to bite you.{END}\n\n")

                            if get_game_over_response() == 'yes':
                                trigger_403_sequence()
                            else:
                                sys.exit()
                        case 'reach for crowbar':
                            print(f"\t{ITALIC}You reach for the crowbar that was next to you. With the crowbar, you knock the man off.\n\n"
                                  f"\tWhile it's incapacitated from the blow, you rush toward the {YELLOW}Pistol{END}. {ITALIC}Now's your chance!\n\n"
                                  f"*OPTIONS*\n"
                                  f"\t{LIGHT_BLUE}Shoot him{END}\n")
                            shoot_villain_alt()

        print(f"{LIGHT_GREEN}THE END(?){END}\n\n"
              "Congratulations! You defeated the villain. While the game has finished, you still need to find a way out...\n"
              "Use what you have in your inventory to find a way out of your apartment!\n")

        game_map['room403']['room_description'] = "What just happened?"
        if game_map['room403']['read_note'] == 'true':
            turn_on_generator()

def shoot_villain_alt():
    action = input('What will you do? ').lower()
    while action != 'shoot him':
        print(f"\t{ITALIC}Invalid action: '{LIGHT_RED}{action}{END}'{ITALIC}. Try again.{END}\n")
        increase_command_count()
        action = input('What will you do? ').lower()
    else:
        increase_command_count()
        print(
            f"\t{ITALIC}With no time to spare, You fire the {YELLOW}Pistol{END} {ITALIC}perfectly at his head. Great shot!\n\n"
            f"\tThe body plops down face-first just inches away from you. It's over. You take a moment to breathe,\n"
            f"\tcontemplating what in the world just happened.{END}\n")

def turn_on_generator():
    game_map['elevator']['is_generator_on'] = 'true'

    print(
        f"\t{ITALIC}You recall that the note mentioned 'turning on a generator'. You flip\n"
        f"\tthe switch located in corner of room 403, powering the elevator outside.\n")

def trigger_elevator_sequence():
    global floor
    if game_map['elevator']['is_generator_on'] == 'true':
        answer = int(input(f"This is it. What floor? "))
        while answer not in [4, 3, 2, 1]:
            print(f"\tInvalid action: '{LIGHT_RED}{answer}{END}'. Try again.\n")
            increase_command_count()
            answer = int(input(f"What floor? "))
        else:
            increase_command_count()
            floor =  answer
    else:
        print(f"\t{ITALIC}Even with the {YELLOW}Elevator Fob{END}, {ITALIC}you still can't get anywhere when there's no power."
              f"\tLike the lifeless body next to you, you realize you're truly trapped.\n")
        if get_game_over_response() == 'yes':
            hallwayB_4thFloor = game_map['hallwayB_4thFloor']
            # Reset Room Explored
            game_map['elevator']['explored'] = 'false'
            # Reset Available Item
            game_map['elevator']['available_items'].append('Elevator Fob')
            # Reset Item Requirement
            hallwayB_4thFloor['adjacent_rooms']['east'][1] = 'Crowbar'
            # Remove Elevator Fob From Inventory
            inventory.remove('Elevator Fob')

            current_room = load_room('hallwayB_4thFloor')
            action = input(f"Your move (to see all actions, enter '{LIGHT_BLUE}Help{END}'): ")
            execute(action, current_room)
        else:
            sys.exit()

def get_game_over_response():
    print(f"{LIGHT_RED}GAME OVER{END}")

    answer = input(f'Try again? ({LIGHT_BLUE}Yes{END} / {LIGHT_BLUE}No{END}) ').lower()
    while answer not in ['yes', 'no']:
        print(f"\t{ITALIC}Invalid action: '{LIGHT_RED}{answer}{END}'{ITALIC}. Try again.{END}\n")
        increase_command_count()
        answer = input(f'Try again? ({LIGHT_BLUE}Yes{END} / {LIGHT_BLUE}No{END}) ').lower()
    else:
        increase_command_count()
        return answer

def increase_command_count():
    global command_count
    command_count += 1

# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution?page=1&tab=scoredesc#tab-top
# https://www.w3schools.com/python/ref_func_round.asp
def record_time_spent():
    time_spent = round(time.time() - start_time, 0)
    if time_spent > 60:
        seconds_spent = int(time_spent % 60)
        minutes_spent = int(time_spent // 60)
        time_spent = f"{minutes_spent} minutes {seconds_spent} seconds"
    else:
        time_spent = f"{time_spent} seconds"
    return time_spent

start_time = time.time()
run_game()
