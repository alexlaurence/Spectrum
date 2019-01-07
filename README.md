# Spectrum-ASD-Tool
👩🏻‍⚕️ Cross-platform Autism screening using Keras API

## Introduction
An early diagnosis of neurodevelopmental disorders can improve treatment and significantly decrease associated healthcare costs. In this GUI-based tool, healthcare professionals and teachers can use supervised learning to diagnose Autistic Spectrum Disorder (ASD) based on behavioral features and individual characteristics. Spectrum uses a neural network from the Keras API which was built as a learning project for Pact's "Machine Learning for Healthcare Analytics Projects" book.

Through this tool, we were able to predict autism in patients with about 90% accuracy. I also learned how to deal with categorical data; a lot of health applications are going to have categorical data and one way to address this is by using one-hot encoded vectors. Furthermore, I learned how to reduce overfitting using dropout regularization.

<p align="center">
<img src="https://raw.githubusercontent.com/alexlaurence/Spectrum-ASD-Tool/master/Screenshots/gui1.png" data-canonical-src="https://raw.githubusercontent.com/alexlaurence/Spectrum-ASD-Tool/master/Screenshots/gui1.png" width="425" height="625"/>
<img src="https://raw.githubusercontent.com/alexlaurence/Spectrum-ASD-Tool/master/Screenshots/gui2.png" data-canonical-src="https://raw.githubusercontent.com/alexlaurence/Spectrum-ASD-Tool/master/Screenshots/gui2.png" width="425" height="625"/>
</p>

## Dependencies
* keras
* pandas
* tensorFlow
* sklearn

## Features
* 90% accuracy on supervised learning
* Screen individual on the spot for ASD
* Screen groups/cohort for ASD

## Trained Data
Data Set Name: Autistic Spectrum Disorder Screening Data for Children (n=293)

The dataset that we're going to be using for this chapter is the Autistic Spectrum Disorder Screening Data for Children Dataset provided by the UCI Machine Learning Repository, which can be found here: https://archive.ics.uci.edu/ml/datasets/Autistic+Spectrum+Disorder+Screening+Data+for+Children++. This dataset contains records of 292 patients or children that have been screened for autism. This contains details of their age, ethnicity, and familial history of autism. We will be using this dataset to predict whether these patients actually have autism.

Abstract: Autistic Spectrum Disorder (ASD) is a neurodevelopment  condition associated with significant healthcare costs, and early diagnosis can significantly reduce these. Unfortunately, waiting times for an ASD diagnosis are lengthy and procedures are not cost effective. The economic impact of autism and the increase in the number of ASD cases across the world reveals an urgent need for the development of easily implemented and effective screening methods. Therefore, a time-efficient and accessible ASD screening is imminent to help health professionals and inform individuals whether they should pursue formal clinical diagnosis.  The rapid growth in the number of ASD cases worldwide necessitates datasets related to behaviour traits. However, such datasets are rare making it difficult to perform thorough analyses to improve the efficiency, sensitivity, specificity and predictive accuracy of the ASD screening process. Presently, very limited autism datasets associated with clinical or screening are available and most of them are genetic in nature. Hence, we propose a new dataset related to autism screening of adults that contained 20 features to be utilised for further analysis especially in determining influential autistic traits and improving the classification of ASD cases. In this dataset, we record ten behavioural features (AQ-10-Child) plus ten individuals characteristics that have proved to be effective in detecting the ASD cases from controls in behaviour science. 

Source: Fadi Fayez Thabtah
Department of Digital Technology
Manukau Institute of Technology,
Auckland, New Zealand
fadi.fayez@manukau.ac.nz

## How To Use
Questions must be taken using the ASD Tests App (iOS/Android): http://www.asdtests.com/#about_asd. You can then collect demographic data as shown in the dataset descriptions .doc file. You can either collect data via Spectrum by appending each participant to the CSV file, and saving it. Or you can load a pre-existing CSV file and run the test (if you have collected this data by other means). Warning: pressing clear will clear all previous appends if not saved.

## Analysing the Data
In the predictions, 1 refers to predicted ASD, and 0 refers to predicted non-ASD. The order of each 1s and 0s refers to the order of the participant in the CSV file. For example, the first row (ignoring header) is the first participant. Therefore, 0 1 indicates that participant 1 is ASD, and participant 2 is non-ASD.

## Relevant Literature
1) Tabtah, F. (2017). Autism Spectrum Disorder Screening: Machine Learning Adaptation and DSM-5 Fulfillment. Proceedings of the 1st International Conference on Medical and Health Informatics 2017, pp.1-6. Taichung City, Taiwan, ACM. (http://fadifayez.com/wp-content/uploads/2017/11/Autism-Spectrum-Disorder-Screening-Machine-Learning-Adaptation-and-DSM-5-Fulfillment.pdf)
2) Thabtah, F. (2017). ASDTests. A mobile app for ASD screening. www.asdtests.com [accessed December  20th, 2017].
3) Thabtah, F. (2017). Machine Learning in Autistic Spectrum Disorder Behavioural Research: A Review. To Appear in Informatics for Health and Social Care Journal. December, 2017 (in press)

## Acknowledgement
* Fadi Fayez Thabtah - Data
* Eduonix Learning Solutions/Pact - 'Machine Learning for Healthcare Analytics Projects' Book
