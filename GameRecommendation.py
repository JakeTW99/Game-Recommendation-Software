from linkedlist import LinkedList
from gamedata import *

# Inserting genres into a LinkedList
def insert_genres():
    genre_list = LinkedList()
    for genre in genres:
        genre_list.insert_beginning(genre)
    return genre_list

# Inserting platforms into a LinkedList
def insert_platforms():
    platform_list = LinkedList()
    for platform in platforms:
        platform_list.insert_beginning(platform)
    return platform_list

# Inserting games into a LinkedList

def insert_game_data():
    game_data_list = LinkedList()
    for genre in genres:
        genre_sublist = LinkedList()
        for platform in platforms:
            platform_sublist = LinkedList()
            for game in game_data:
                if game[1] == genre and game[3] == platform:
                    genre_sublist.insert_beginning(game)
                    platform_sublist.insert_beginning(game)
            game_data_list.insert_beginning(genre_sublist)
            game_data_list.insert_beginning(platform_sublist)
    return game_data_list
                    
my_genre_list = insert_genres()
my_platform_list = insert_platforms()
my_game_list = insert_game_data()

selected_genre = ""
selected_platform = ""

while len(selected_genre) == 0:
    user_input = str(input("\nType the beginning of a game genre and press enter to see if it's in our data."
                           "\nMake sure to narrow your search down to one specific genre: \n")).title()
    matching_genres = []
    genre_list_head = my_genre_list.get_head_node()
    while genre_list_head is not None:
        if str(genre_list_head.get_value()).startswith(user_input):
            matching_genres.append(genre_list_head.get_value())
        genre_list_head = genre_list_head.get_next_node()
        

    for genre in matching_genres:
        print("\n" + genre)
    
    if len(matching_genres) == 1:
        select_genre = str(input(
            "\nThe only genre that matches your input is " + matching_genres[0] + ".\nDo you want to look at " + 
            matching_genres[0] + " games? Enter Y for Yes and N for no\n")).upper()
        
        if select_genre == "Y":
            selected_genre = matching_genres[0]
            print("\nSelected Genre Type: " + selected_genre)
            print("\nNow you must pick which platform you are playing on.")
            while len(selected_platform) == 0:
                user_input_2 = str(input(
                "\nType the beginning of your chosen platform and press enter to see if it's in our data."
                "\nAgain, make sure to narrow your search down to one specific platform: \n")).upper()
                matching_platforms = []
                platform_list_head = my_platform_list.get_head_node()
                while platform_list_head is not None:
                    if str(platform_list_head.get_value()).startswith(user_input_2):
                        matching_platforms.append(platform_list_head.get_value())
                    platform_list_head = platform_list_head.get_next_node()
                
                for platform in matching_platforms:
                    print("\n" + platform)

                if len(matching_platforms) == 1:
                    select_platform = str(input(
                        "\nThe only platform that matches your input is " + matching_platforms[0] + ".\nDo you want to look at " +
                        selected_genre + " games on " + matching_platforms[0] + "? Enter Y for Yes and N for no\n")).upper()
                    if select_platform == "Y":
                        selected_platform = matching_platforms[0]
                        print("Selected Platform: " + selected_platform)


            game_list_head = my_game_list.get_head_node()
            while game_list_head.get_next_node() is not None:
                sublist_head = game_list_head.get_value().get_head_node()
                if sublist_head.get_value()[1] == selected_genre and selected_platform in sublist_head.get_value():
                    while sublist_head.get_next_node() is not None:
                        print("\nName: " + sublist_head.get_value()[0])
                        print("Genre: " + sublist_head.get_value()[1])
                        print("OpenCritic Score: " + sublist_head.get_value()[2] + "/100")
                        print("Platforms: " + sublist_head.get_value()[3] + "\n")
                        sublist_head = sublist_head.get_next_node()
                game_list_head = game_list_head.get_next_node()
            
                repeat_loop = str(input("Would you like to search for games in another genre or platform? Enter Y for Yes and N for No.\n")).upper()
                if repeat_loop == "Y":
                    selected_genre = ""