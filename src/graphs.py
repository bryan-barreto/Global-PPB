import sys
import matplotlib.pyplot as plt
from init import init
from growth import growth
import numpy as np
from PIL import Image, ImageDraw, ImageFont 


def daily_uploads_chart(out_file = './images/daily_uploads_chart.png'):
    engine, dfs = init()
    dates = dfs['score'][['upload_date','stage']]
    dates_stage_r = dates[dates['stage'] == 'R']
    dates_stage_s = dates[dates['stage'] == 'S']
    dates_r = dates_stage_r['upload_date'].dt.date
    dates_s = dates_stage_s['upload_date'].dt.date
    dates_total = dates['upload_date'].dt.date
    date_count_r = dates_r.value_counts()
    date_count_s = dates_s.value_counts()
    dates_total_counts = dates_total.value_counts()
    date_count_r = date_count_r.sort_index()
    date_count_s = date_count_s.sort_index()
    dates_total_counts = dates_total_counts.sort_index()
    
    fig = plt.figure(figsize=(10, 6))  

    plt.plot(date_count_r.index, date_count_r, marker='o', linestyle='-', color='red')  
    plt.plot(date_count_s.index, date_count_s, marker='o', linestyle='-', color='blue')
    plt.plot(dates_total_counts.index, dates_total_counts, marker='o', linestyle='-', color='green')
    plt.legend(["Ruby", "Sapphire", "Total"])

    plt.title('Daily Uploads')  
    plt.xlabel('Date')  
    # plt.ylabel('Uploads')  
    plt.grid(True)  
    plt.xticks(rotation=45)  

    plt.tight_layout()  
    fig.savefig(out_file, bbox_inches='tight')
    print(out_file)
    print("Daily Uploads")

def average_player_improvement(out_file = './images/average_player_improvement.png'):
    engine, dfs = init()
    player_id_list = dfs['player']['player_id'].values
    player_average_list = [growth(player) for player in player_id_list]
    

    # Create an image object 
    image = Image.new("RGB", (400, 200), "white") 
    
    # Create a drawing object 
    draw = ImageDraw.Draw(image) 
    
    # Choose a font and size 
    font = ImageFont.truetype("arial.ttf", 72) 
    percentage = (np.mean(player_average_list)) * 100
    out_string = f"{percentage:.2f}%"
    # Draw the text on the image 
    draw.text((80, 60), out_string, font=font, fill="black") 
    
    # Save the image 
    image.save(out_file) 
    print(out_file) 
    print("Average Player Improvements")
     
    
def total_players(out_file = './images/total_players.png'):
    engine, dfs = init()
    total_players = len(dfs['player'])
    image = Image.new("RGB", (400, 200), "white") 
    
    # Create a drawing object 
    draw = ImageDraw.Draw(image) 
    
    # Choose a font and size 
    font = ImageFont.truetype("arial.ttf", 72) 
    out_string = f"{total_players}"
    # Draw the text on the image 
    draw.text((80, 60), out_string, font=font, fill="black") 
    
    # Save the image 
    image.save(out_file) 
    print(out_file) 
    print("Total Players")
    

def favorite_stage_graph(out_file = './images/favorite_stage_graph.png'):
    engine, dfs = init()
    players_stages = dfs['player'][['favorite_stage']]
    ruby_size = len(players_stages[players_stages['favorite_stage']=='R'])
    sapphire_size = len(players_stages[players_stages['favorite_stage']=='S'])
    # print(ruby_size)
    # print(sapphire_size)
    fig = plt.figure(figsize=(6,6))
    plt.bar(['Ruby', 'Sapphire'],[ruby_size,sapphire_size], color=['tab:red', 'tab:blue'])
    plt.title('Favorite Stages')
    # plt.show()
    fig.savefig(out_file, bbox_inches='tight')
    print(out_file) 
    print("Favorite Player Stage")

def players_by_country(out_file = './images/players_by_country.png'):
    engine, dfs = init()
    player_countries = dfs['player']['country']
    player_countries_unique = player_countries.unique()
    player_countries = dfs['player'][['country']]
    player_countries_values = [len(player_countries[player_countries['country']==country]) for country in player_countries_unique]
    fig = plt.figure(figsize=(8,6))
    plt.pie(player_countries_values, labels=player_countries_unique, autopct='%1.1f%%')
    # plt.show()
    fig.savefig(out_file, bbox_inches='tight')
    print(out_file) 
    print("Player Countries")


if __name__=='__main__':
    globals()[sys.argv[1]]()

# daily_uploads_chart()
# average_player_improvement()
# total_players()
# favorite_stage_graph()
# players_by_country()