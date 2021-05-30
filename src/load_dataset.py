# load the original dataset 
import pandas as pd 
import os
class LoadDataset:
    # load the dataset 
    def load_video_game_train(self):
        print(os.getcwd())
        video_game_rating_train = pd.read_csv('/Users/xcpeng/video_game_rating/data/Video_games_esrb_rating.csv')
        return video_game_rating_train 