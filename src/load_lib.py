# class for importing necessary libraries 

class LoadLibraries:
    def __init__(self):
        import pandas as pd 
        import numpy as np 
        import matplotlib.pyplot as plt 
        import seaborn as sb
        from sklearn.preprocessing import StandardScaler 
        from sklearn.decomposition import PCA
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from mlxtend.feature_selection import SequentialFeatureSelector as sfs
        from sklearn.metrics import accuracy_score as acc
        from sklearn.tree import DecisionTreeClassifier 
        from sklearn.linear_model import PassiveAggressiveClassifier 
        from sklearn.linear_model import RidgeClassifier 
        from sklearn.neighbors import KNeighborsClassifier

