# Modules
import torch as nn
import numpy as np

# Function imported
from sklearn.model_selection import train_test_split

# Dataset preprocessing

def preprocessing(dataset):
 
 # Deletes rows containing nan or empty values
 dataset.replace('', np.nan, inplace=True)
 dataset.dropna(inplace=True)

 # Codify classes (Continua_sulla_traiettoria_corrente = 0, Rallenta_e_scendi_di_quota = 1 )
 dataset['Class_ID'] = dataset['Azione'].map({'Continua_sulla_traiettoria_corrente': 0, 'Rallenta_e_scendi_di_quota': 1 })

 # Split dataset based on classes
 continue_trajectory = dataset[dataset['Class_ID'] == 0]
 modify_trajectory = dataset[dataset['Class_ID'] == 1]

 # Get the input and the output (target)
 continue_trajectory_x = continue_trajectory[["Distanza_Target", "Angolo_Rispetto_Target", "Altezza", "Velocita_Vento"]].values
 modify_trajectory_x = modify_trajectory[["Distanza_Target", "Angolo_Rispetto_Target", "Altezza", "Velocita_Vento"]].values
 continue_trajectory_y = continue_trajectory[["Class_ID"]].values
 modify_trajectory_y = modify_trajectory[["Class_ID"]].values

 # Split data into training set and test set
 continue_trajectory_x_train, continue_trajectory_x_test, continue_trajectory_y_train, continue_trajectory_y_test = train_test_split(continue_trajectory_x, continue_trajectory_y, test_size=0.3, shuffle = False)
 modify_trajectory_x_train, modify_trajectory_x_test, modify_trajectory_y_train, modify_trajectory_y_test = train_test_split(modify_trajectory_x, modify_trajectory_y, test_size=0.3, shuffle = False)

 # Creation of the data training set
 x_train = np.concatenate([continue_trajectory_x_train, modify_trajectory_x_train])
 y_train = np.concatenate([continue_trajectory_y_train, modify_trajectory_y_train])
 x_train = nn.tensor(x_train).float()
 y_train = nn.tensor(y_train).float()

 # Creation of the data test set
 x_test = np.concatenate([continue_trajectory_x_test, modify_trajectory_x_test])
 y_test = np.concatenate([continue_trajectory_y_test, modify_trajectory_y_test])
 x_test = nn.tensor(x_test).float()
 y_test = nn.tensor(y_test).float()

 # Map both training and test set into binary matrix
 temp = nn.empty(y_train.shape[0], 2)
 temp[:,0] = y_train[:,0] == 0
 temp[:,1] = y_train[:,0] == 1
 y_train = temp
 temp = nn.empty(y_test.shape[0], 2)
 temp[:,0] = y_test[:,0] == 0
 temp[:,1] = y_test[:,0] == 1
 y_test = temp

 return x_train, y_train, x_test, y_test


