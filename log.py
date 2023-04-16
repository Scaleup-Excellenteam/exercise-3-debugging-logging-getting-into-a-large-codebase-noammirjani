import logging
from enums import Player

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
def add_knight_Move(team):
    global knights_logger_white
    global knights_logger_black
    if team:
        knights_logger_white += 1
    else:
        knights_logger_black += 1


# -----
def print_knight_Move():
    global knights_logger_white
    global knights_logger_black
    logger.info(f"Number of knight moves white: {knights_logger_white}")
    logger.info(f"Number of knight moves black: {knights_logger_black}")


# -----
def end_game_data():
    logger.info("------- END GAME -------")
    logger.info("        GAME DATA:      ")


# -----
def start_game_data():
    logger.info("*" * 50)
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

    if not first_eaten_black:
        rounds_with_full_team_Black += 1


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


def print_board(game):
    logger.info("---------  BOARD ---------")
    logger.info("\n" + game)
    logger.info("-------  END BOARD -------")


# -----
def count_check(team):
    global count_white_check
    global count_black_check
    if team:
        count_white_check += 1
        print(f"White check: {count_white_check}")
    else:
        count_black_check += 1
        print(f"Black check: {count_black_check}")


# -----
def print_check_counters():
    global count_white_check
    global count_black_check
    logger.info(f"Number of checks white: {count_white_check}")
    logger.info(f"Number of checks black: {count_black_check}")


# -----
logger = get_logger()
knights_logger_white = 0
knights_logger_black = 0
rounds_with_full_team_white = 0
rounds_with_full_team_Black = 0
first_eaten_white = False
first_eaten_black = False
count_white_check = 0
count_black_check = 0
