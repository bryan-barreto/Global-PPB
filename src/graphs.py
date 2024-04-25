import matplotlib.pyplot as plt
from init import init
from growth import growth
import numpy as np



def daily_uploads_chart():
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
    fig.savefig('./images/daily_uploads.png', bbox_inches='tight')

def average_player_improvement():
    engine, dfs = init()
    player_id_list = dfs['player']['player_id'].values
    player_average_list = [growth(player) for player in player_id_list]
    return np.mean(player_average_list)
    
def total_players():
    engine, dfs = init()
    total_players = len(dfs['player'])
    print(total_players)
    pass

def favorite_stage_graph():
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
    fig.savefig('./images/favorite_stage.png', bbox_inches='tight')
    pass

def players_by_country():
    engine, dfs = init()
    player_countries = dfs['player']['country']
    player_countries_unique = player_countries.unique()
    player_countries = dfs['player'][['country']]
    player_countries_values = [len(player_countries[player_countries['country']==country]) for country in player_countries_unique]
    fig = plt.figure(figsize=(8,6))
    plt.pie(player_countries_values, labels=player_countries_unique)
    plt.show()
    pass

# daily_uploads_chart()
# average_player_improvement()
# total_players()
# favorite_stage_graph()
players_by_country()