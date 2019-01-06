import sys
import pandas as pd
import sklearn
import keras

# Childhood Autistic Spectrum Disorder Screening using Machine Learning
print('Python: {}'.format(sys.version))
print('Pandas: {}'.format(pd.__version__))
print('Sklearn: {}'.format(sklearn.__version__))
print('Keras: {}'.format(keras.__version__))

def run():
    '''
    import the data-set
    '''

    file = 'Autism-Child-Data.csv'

    # read the csv
    data = pd.read_table(file, sep = ',', index_col = None)

    # print the shape of the DataFrame, so we can see how many examples we have
    print('Shape of DataFrame: {}'.format(data.shape))
    print(data.loc[0])

    # print out multiple patients at the same time
    data.loc[:10]

    # print out a description of the dataframe
    data.describe()

    '''
    data pre-processing
    '''

    # drop unwanted columns
    data = data.drop(['result', 'age_desc'], axis=1)

    data.loc[:10]

    # create X and Y datasets for training
    x = data.drop(['class'], 1)
    y = data['class']

    x.loc[:10]

    # convert the data to categorical values - one-hot-encoded vectors
    X = pd.get_dummies(x)

    # print the new categorical column labels
    X.columns.values

    # print an example patient from the categorical data
    X.loc[1]

    # convert the class data to categorical values - one-hot-encoded vectors
    Y = pd.get_dummies(y)

    Y.iloc[:10]

    ''' 
    Split the Dataset into Training and Testing Datasets 
    '''

    from sklearn import model_selection
    # split the X and Y data into training and testing datasets
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size = 0.2)

    print(X_train.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_test.shape)

    # build a neural network using Keras
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.optimizers import Adam


    # define a function to build the keras model
    def create_model():
        # create model
        model = Sequential()
        model.add(Dense(8, input_dim=96, kernel_initializer='normal', activation='relu'))
        model.add(Dense(4, kernel_initializer='normal', activation='relu'))
        model.add(Dense(2, activation='sigmoid'))

        # compile model
        adam = Adam(lr=0.001)
        model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
        return model


    model = create_model()

    print(model.summary())

    '''
    Training the Network
    '''
    # fit the model to the training data
    model.fit(X_train, Y_train, epochs=50, batch_size=10, verbose = 1)

    '''
    Testing and Performance Metrics
    '''
    # generate classification report using predictions for categorical model
    from sklearn.metrics import classification_report, accuracy_score

    predictions = model.predict_classes(X_test)
    predictions

    print('Results for Categorical Model')
    print(accuracy_score(Y_test[['YES']], predictions))
    print(classification_report(Y_test[['YES']], predictions))