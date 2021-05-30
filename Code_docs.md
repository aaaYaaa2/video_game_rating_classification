# Video Game Rating Code Docs

This file will breifly introduce the code documentation for this project. The project is divded into exploring the dataset, visualize the dataset and apply models. 

## index.py 
This is the entry point of the project, contains `ClassifyVideoGameRating` class. 

``` python3
    # initialize the class will load required dataset in the project 

    visualize_console() 
    # methods for visualize console distribution of the dataset 

    visulize_rating()
    # method for visualize esrb rating distribution in bar chart and pie chart 

    get_cross_validation_map()
    # method for plot cross validation map 

    get_target_pca() 
    # method for using PCA to visualize if the rating could be categorized 

    get_train_test_dataset()
    # method for split the dataset into training and testing 

    apply_model_by_name() 
    # method for getting the results of apply certain models 
```