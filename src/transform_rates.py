# transform rsbe rating from character to numbers 

class TransformRates:
    # transform esrb rating to another mapping service 
    def transform_rates(self, dataset):
        video_game_rating_train = dataset 
        rating_mapping = {
            'E': 0,
            'ET': 1,
            'T': 2,
            'M': 3
        }
        video_game_rating_train['esrb_rating'] = video_game_rating_train['esrb_rating'].map(rating_mapping)
        return video_game_rating_train 

