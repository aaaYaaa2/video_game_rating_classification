import load_lib
from load_dataset import LoadDataset
from visualize_dataset import VisualizeDataset
from apply_models import ApplyModel
import os 

class ClassifyVideoGameRating:
    def __init__(self):
        # load libraries 
        load_lib.LoadLibraries() 
        # load video game dataset 
        load_dataset = LoadDataset()
        print(os.getcwd())
        self.video_game_dataset = load_dataset.load_video_game_train()

    # visualize console distribution 
    def visualize_console(self):
        visualize_dataset = VisualizeDataset(self.video_game_dataset)
        return visualize_dataset.console_distribution()

    # visualize rating distribution 
    def visualize_rating(self):
        visualize_dataset = VisualizeDataset(self.video_game_dataset)
        return visualize_dataset.rating_distribution()

    # get cross validation map 
    def get_cross_validation_map(self):
        visualize_dataset = VisualizeDataset(self.video_game_dataset)
        return visualize_dataset.cross_validation()

    # get PCA graph 
    def get_target_pca(self):
        visualize_dataset = VisualizeDataset(self.video_game_dataset)
        return visualize_dataset.target_pca()

    # get training and testing dataset 
    def get_train_test_dataset(self, dataset):
        apply_model = ApplyModel()
        train_test_data = apply_model.get_train_and_test_dataset(dataset)
        return train_test_data

    def apply_model_by_name(self, name: str, dataset):
        train_test_dataset = self.get_train_test_dataset(dataset)
        X_train = train_test_dataset['X_train']
        X_test = train_test_dataset['X_test']
        y_train = train_test_dataset['y_train']
        y_test = train_test_dataset['y_test']

        apply_model = ApplyModel()
        
        return apply_model.apply_model(name, X_train, X_test, y_train, y_test)
