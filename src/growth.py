from init import init
import numpy as np


def growth(player_id):
    engine, dfs = init()
    
    # players = dfs['player'][['player_id']] # Used to collect test player
    # pick_player = players.iat[2, 0] # Used to collect test player
    
    scores_by_player = dfs['score']

    scores_by_current_player = scores_by_player[scores_by_player['player_id'] == player_id]['score_value'].values
    
    average = moving_average(scores_by_current_player)
        
    return average

def moving_average(scores, k=5):
    moving_averages = []
    previous_highest = 0
    for i in range(len(scores)):
        if scores[i] > previous_highest:
            previous_highest = scores[i]
        if i < k - 1:
            moving_avg = (sum(scores[:i + 1]) / (i + 1)) / previous_highest
        else:
            moving_avg = (sum(scores[i - k + 1:i + 1]) / k) / previous_highest
        moving_averages.append(moving_avg)
    return np.average(moving_averages)




growth('f92a438a-79ad-4350-98dc-2a204eb939d3')