# In this file, users can modify the parameters used in training model.
# Users can also add a new dataset, by adding a new item to the dataset_parameters_dict. The form of items are {"dataset"_ name":parameters}

dataset_parameters_dict = {"pfur": {"features": ["BPB"],
                                   "neighbor_num": 160
                                   ,
                                   "embeddings": {'GraRep': {'dimensions':8, 'iteration': 40},
                                                  'Node2Vec': {'dimensions': 16},
                                                  'SocioDim': {'dimensions': 8}},
                                   "randomforest": {}}
                           }
