import logging

logFile = 'chess_logs.log'


# -----
def get_logger():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler and add it to the logger
    handler = logging.FileHandler(logFile)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Remove any existing handlers from the logger
    for existing_handler in logger.handlers:
        logger.removeHandler(existing_handler)

    # Add the new handler to the logger
    logger.addHandler(handler)

    return logger


# -----
def add_knight_Move():
    global knights_logger
    knights_logger += 1


# -----
def print_knight_Move():
    global knights_logger
    logger.info(f"Number of knight moves: {knights_logger}")


# -----
def end_game_data():
    logger.info("------- END GAME -------")
    logger.info("        GAME DATA:      ")


# -----
def start_game_data():
    logger.info("------- START GAME -------")
    logger.info("        GAME DATA:      ")


# -----
def update_counter_move():
    global rounds_with_full_team_white
    global rounds_with_full_team_Black
    global first_eaten_white
    global first_eaten_black

    if not first_eaten_white:
        rounds_with_full_team_white += 1
        print("white rounds", rounds_with_full_team_white)

    if not first_eaten_black:
        rounds_with_full_team_Black += 1
        print("black rounds", rounds_with_full_team_Black)


# -----
def update_eaten_pieces(team):
    global first_eaten_white
    global first_eaten_black

    if team:
        if not first_eaten_black:
            first_eaten_black = True
    else:
        if not first_eaten_white:
            first_eaten_white = True


# -----
def print_rounds_with_full_team():
    global rounds_with_full_team_white
    global rounds_with_full_team_Black
    logger.info(f"Rounds with full team white: {rounds_with_full_team_white}")
    logger.info(f"Rounds with full team black: {rounds_with_full_team_Black}")


# -----
logger = get_logger()
knights_logger = 0
rounds_with_full_team_white = 0
rounds_with_full_team_Black = 0
first_eaten_white = False
first_eaten_black = False

