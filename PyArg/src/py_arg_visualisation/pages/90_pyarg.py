import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path='/', title='Internship JAIST', name='Internship JAIST')


layout = dbc.Container([
    dbc.Row([
        html.H1('Welcome to my Internship at JAIST !', style={'text-align' : 'center', 'padding': '50px'}),
        dbc.Col([ html.A([html.Img(src='/assets/logo_isima.png', style={'width': '60%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://www.isima.fr/',target="_blank"),]),
        dbc.Col([ html.A([html.Img(src='/assets/logo_jaist.jpg', style={'width': '60%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://www.jaist.ac.jp/index.html',target="_blank"),]), 
        html.H2('1-Introduction'),
        html.P(['This intrnship take place from May 2024 to September 2024 at JAIST University. It is an integral part of my academic curriculum at ISIMA, designed to provide me with valuable international experience and to fulfill the requirements'
            ' for validating my second year of studies. The project I will be working on is titled "Multimodal Argument Mining Dataset for Political Debates with Audio and Transcripts." This research involves the development and analysis of a '
            'comprehensive dataset that integrates both audio and textual data from political debates. The goal is to advance the understanding and application of argument mining techniques by leveraging multimodal data sources.'
            'I am fortunate to be guided by two esteemed supervisors during this internship: Professor Teeradaj RACHARAK, who will be my supervisor at JAIST University, and, Alexandre GUITTON, my supervisor at ISIMA. ',
            'This opportunity not only allows me to contribute to a cutting-edge research project but also to gain exposure to different academic and cultural environments, enriching both my professional and personal development.']),
        html.H2('2-First research'),
        html.P(['During this internship, I had to conduct some additional research on various subjects to expand my knowledge and gain a better understanding of my studies. The first presentation took place on May 8th and was about '
            '"Argumentative Explanations for Pattern-based Text Classifiers." This presentation covers the work of Piyawat LERTVITTAYAKUMJORN and Francesca TONI. ',
            html.A('(Linke of the original document)', href='https://content.iospress.com/articles/argument-and-computation/aac220004#ref018',target="_blank")
        ]),
    ]),
        dbc.Row([
        html.A([html.Img(src='/assets/image_presentation/image1.png', style={'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://docs.google.com/presentation/d/1bYmTDVWkTl5dOfiMxNzFPucefAYxzk1jIGsowm4B1Y0/edit#slide=id.p',target="_blank")
    ]),
    dbc.Row([
        html.P('To resum, the document is a introduction of what is a pattern-based text classifiers and how it work. This document helped me before the start of my internship to visualize the subject that was totaly new for me. With this new knowledge '
            'my profesor gave me the first guidance to start working on the project of my internship.')
    ]),
    dbc.Row([
        html.H2('3-Start of the project'),
        html.P(['The second presentation took place on May 15th and dive into the main subject of this internship. The original document form the work of Rafael MESTRE, Razvan MILICIN, Stuart E. MIDDLETON, Matt RYAN, Jiatong ZHU and Timothy J. NORMAN. ',
        html.A('(Linke of the original document). ', href='https://aclanthology.org/2021.argmining-1.8.pdf',target="_blank"),
        ])
    ]),
    dbc.Row([
        html.A([html.Img(src='/assets/image_presentation/image2.png', style={'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://docs.google.com/presentation/d/1YlTziO5KjIpDY6pT3L0-MlkmVEYYRCfguoOWfUQWC5U/edit#slide=id.g708a6ee8a1_0_46',target="_blank")
    ]),
    dbc.Row([
        html.P(['In this document we found the dataset that we will use for our reshearch. As explain in the presentation the dataset is composed of audio enregistrements of the 2020 United State presidential debate. Each audio have been '
        'analyze with different method to extract the important data. This dataset represent all the different argument use by each speaker during each debat and the explanation for the relationship between those arguments. It also mention the different '
        'topic debated during the interview. I personaly used a Jupyter Notebook code to extract the data that I needed. Here is some result from the code. '
        ])
    ]),
    dbc.Row([html.Img(src='/assets/image_stat/image3.png', style={'width': '50%'}),
        html.Img(src='/assets/image_stat/image4.png', style={'width': '50%'})
    ]),
    dbc.Row([html.Img(src='/assets/image_stat/image5.png', style={'width': '50%'}),
        html.Img(src='/assets/image_stat/image6.png', style={'width': '50%'})
    ]),
    dbc.Row([html.Img(src='/assets/image_stat/image7.png', style={'width': '50%'}),
        html.Img(src='/assets/image_stat/image8.png', style={'width': '50%'})
    ]),
    dbc.Row([
        html.H2('4-Beginning of Machine Learning'),
        html.P('The next step in our project is the creation of differents machine learning models to extra new argument and see new'
               ' relation between them. Every ML model will be apply on Abstract Argumentation Framework (AA) and Bipolar Argumentation'
               ' Framework (BAF).'),
        html.P('The first model I added is the Support Vector Machine (SVM). This model use different kernel for its application like'
               ' linear, polynomial, radial basis function (rbf), sigmoidor kernel. To train our models we will divided our dataset'
               ' in two group. A training group that is composed of 80%_ of the original dataset, its use to train the model to '
               'reconized and learn how to found the correct output for a given data. The second group is the testing group with the'
               ' remaining 20%_ of the original dataset and it s use to testing the model and see how well it perform. For every '
               'models we used various k_fold to see its impact on the result output.'),
    ]),
    dbc.Row([
        html.A([html.Img(src='/assets/image_stat/ml/image11.png', style={'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})])
    ]),
    dbc.Row([
        html.P('We can see that the accuracy score of each kernel thos not depend of the type of AF. However we observe a slightly '
               'decrease for the sigmoid kernel compared to others. This observation will stand for the reste of our analysis. '),
    ]),
    dbc.Row([
        html.Img(src='/assets/image_stat/ml/image14.png', style={'width': '33%'}),
        html.Img(src='/assets/image_stat/ml/image13.png', style={'width': '33%'}),
        html.Img(src='/assets/image_stat/ml/image12.png', style={'width': '33%'}),
    ]),
    dbc.Row([
        html.P('To have a more global view of our models we had compared them with various primse. The Recall that is defined by the '
               'proportion of instanes correctly identify by the model, Recall = TP/(TP+FN), TP: True Positif; FN: Fals Negatif.'
               ' The Precision that is defined by the proportion of instances predict as Positif that are indeed positif, Precision='
               'TP/(TP+FP), FP: Fals Positif. And the F1 score which is defined by the harmonic mean of precision and recall, '
               'F1 = 2 x (Precision x Recall)/(Precision + Recall)'),
        html.P('The most notable result is for every models the recall score approximaly double in the AA type between the 5 and 10 '
               'K-folds. This as an direct impact on the F1 score as well.'),
        html.P('To extract the data from the original data set we choose to use the polynomial model with a 10 K-folds because it seems'
               ' to have the better overall performances.'),
    ]),
    dbc.Row([
        html.P('The second model I implemented is the Decision Tree model. This model divided recursively the dataset following certains '
               'conditions. The result is a graph with the shape of a tree,  Each node of the tree represents a decision point, '
               'it is an attributs that divide the upper dataset. It includes: An attributs are choose to maximise the measure of impurity/diversity,'
               ' here we use the gini index defined by : gini = 1-∑(i=1->n) (p_i)^2, where p_i is the proportion of samples of class i in the node.'
               ' If gini = 0 it is a perfect purity (all samples belong to a single class), and if gini = 0.5 it is the maximum'
               ' impurity (samples are evenly distributed among classes). It also contain the value or condition used to split the data.'
               ' We can find as well the number of samples reaching that node, and the class assigned to that node (based on the majority class).'),
    ]),
    dbc.Row([
        html.P('We divided the original dataset between 70% in the training groupe and 30% in the testing groupe.'),
    ]),
    dbc.Row([
        html.Img(src='/assets/image_stat/ml/image15.png', style={'width': '60%','display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
        html.Img(src='/assets/image_stat/ml/image16.png', style={'width': '33%','display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
    ]),
    dbc.Row([
        html.P('This is the representation of the decision tree for the AA model, 0 represent the Non-attack class and 1 the attack class.'
               ' For the BAF model we obtain this shematization with 2 representing the Support class and 0 the Neither one:'),
    ]),
    dbc.Row([
        html.Img(src='/assets/image_stat/ml/image18.png', style={'width': '33%','display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
        html.Img(src='/assets/image_stat/ml/image17.png', style={'width': '60%','display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
    ]),
    dbc.Row([
        html.P('The third model is the Random Forest. It creat a multitude of decision tree during its training and the resulted prediction'
               ' is the most represented class from each tree. For the repartition of the original dataset we use the same as the SVM'
               ' model, 80% training and 20% testing. We obtain for the AA model:'),
    ]),
    dbc.Row([
        html.Img(src='/assets/image_stat/ml/image20.png', style={'width': '45%', 'margin-left': 'auto', 'margin-right': 'auto'}),
        html.Img(src='/assets/image_stat/ml/image21.png', style={'width': '30%','heigth': '20%','margin-top': 'auto', 'margin-left': 'auto', 'margin-right': 'auto'}),
    ]),
    dbc.Row([
        html.Img(src='/assets/image_stat/ml/image19.png', style={'width': '80%','display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
    ]),
    dbc.Row([
        html.P('In comparaison the BAF model gave us this results:'),
    ]),
    dbc.Row([
        html.Img(src='/assets/image_stat/ml/image23.png', style={'width': '45%', 'margin-left': 'auto', 'margin-right': 'auto'}),
        html.Img(src='/assets/image_stat/ml/image22.png', style={'width': '30%','heigth': '20%','margin-top': 'auto', 'margin-left': 'auto', 'margin-right': 'auto'}),
    ]),
    dbc.Row([
        html.Img(src='/assets/image_stat/ml/image24.png', style={'width': '50%','display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
        html.Img(src='/assets/image_stat/ml/image25.png', style={'width': '50%','display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
    ]),


    dbc.Row([
        html.H2('5-Theoric aspect'),
        html.P(['On June 5th, I presented the "Artificial Intelligence on the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games", by Phan Minh DUNG. ',
        html.A('(Linke of the original document). ', href='https://pdf.sciencedirectassets.com/271585/1-s2.0-S0004370200X00100/1-s2.0-000437029400041X/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIDwt6edYHrGwHv73ScELrzLKj%2BekT3B64KW5L3rpA%2FfZAiEA%2FdMxYsMsOdQbF7ncj2OTefI%2FtgnGf4MtcR98JP8E2SAqswUIPxAFGgwwNTkwMDM1NDY4NjUiDK%2F%2BeI6BfgsahznljCqQBdoQfkFu0ZKiPnyXYCTee0Md6r%2BnRz4f1n6v6mUObUM2ygAQVGxZXyjCfZ2JVDHs0KzRbuCLni8HNeNjcu8HTXDv46fiFNWJlEbYPG%2F6lTwkVJnpwHELcZk2vdHCy4f7KO03jCvLpZlP5YaqRccKGn8Pj9%2FaDQFSew8jgNy6ormKjT8FPyG6mqgvIwXSNmNKclrOvsPVHoMt6ym13bkLxiZFO3ZvZG2azVUIWGzrP%2B6uTmU2pxJdUudgPMk6mrgth32lakZZXSMhj3nsl8E6F6At9kXaMQdSKabUmYaO25tZUv4mxtJJ3xbdiM3alP28mA1ER1KR9Dyd9DxPwIkp1O8FJLOfhNioRtJD9XOjwKrzuSuSA8r0hnUVwhFr9EqoNjN2sCO3OmnLECbOaHj0t8z6N9QZuGbdnrjJkPn4Cd9%2B2JfEtLteB8u67gU8sfRE6kA9TywxuybuL1ZsMk%2Bxsh%2BEHyoBh804O2gqlTQXeLeH4TELdaf%2B%2BnMJ%2FR3%2FO%2F9oFqgjHBiw7qD8ULz8r2SfpzvYP7FX4iuwIEaJh%2BYSMH8gn%2FRFN%2Bp5tpLmBO3msyuKvkn4bv9A0AvLjIU9T4ugXOZpJSdePT9TiaVDrbFIlhmCXMF5JIMcpNXNCgYtfmho%2B5hquXvrg2ovNdfoVHsigBWu2ualDaJr5lqshEY9mzsFYMMsKzSLob22naxUmImpidKc8dZvkBC893Gf4opBnuPU%2FSEIDKTrFPhkx9y3l5NVhE%2FuicjMd3CGXJbkNlLod2JjQXi4%2BMewXoeYQfX2Sy4N9iLbDtLp0zU9yyZ25MXaA2AuACUsCVD6qWzZU9kFzd6BQti3PXuhvEj6Qv7F8xsmCCWzMLC5rpBgsFTeNVreMPvJ5bIGOrEBDAHdFlmmdYEZH46U%2FmKYgjthtpx0dcCNjaHDbMM1JXbJvRMAXutV8LpmEIIe1ZJ4za4wgRzzX3etG4YESBZeb3IWLKk2ohkgfuGRg%2BZax6NmY3ug%2FquMLrMTEy0M1%2BZLM348nySBQ6cLQhsM%2F%2BjUEOelgqZj3AoCB4CnoLLAvvUE%2BNMUT%2FVIc53VEd4pFq6q0Z3z0%2FRW2eYTpqCAPDkryiajrt3IgO%2B1jEZZOuswW0hD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240531T070534Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYSWSRDPXT%2F20240531%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e52e971c9d024187c218a7f3baeec77cbf53b65e8d8e5f113348b5c725836c7d&hash=7682ca8d8fca403c6955bfafcf7aca3d967cb96a43136794a3a64714f44c5f4a&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=000437029400041X&tid=spdf-4d413a54-2a9e-468c-ad8d-f19d942893c1&sid=4d33db6e19d9b04e6a69dce17f0bb74cfeaegxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0e175e5901525e0b0d&rr=88c51dc2f813f593&cc=jp',target="_blank"),
        ])
    ]),
    dbc.Row([
        html.A([html.Img(src='/assets/image_presentation/image9.png', style={'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://docs.google.com/presentation/d/1Bl47jzgVVAB7U0b9fACJ9ni7j0aZLAITzIe2UH4sTtQ/edit#slide=id.g4dfce81f19_0_45',target="_blank")
    ]),
    dbc.Row([
        html.P('This prsentation explan the theory in nonmonotonic reasoning and human argumentation. '),
        html.P('I also do some reshearch about the System Usability Scale (SUS) and Systeme Usability and Learnability Scale (SULS) to learn more about the evaluation of an argumentation systeme. The allow me to realize the interactions between arguments. '),
        html.P(['This presentation took place on June 19th and is based on the articul "Misguided by research — The two dimensions of SUS" by George MELISSOURGOS. ',
        html.A('(Linke of the original document). ', href='https://medium.com/@geormelissourgos/leveraging-the-full-potential-of-the-sus-the-two-dimensions-b5846facec3',target="_blank"),
        ])
    ]),
    dbc.Row([
        html.A([html.Img(src='/assets/image_presentation/image10.png', style={'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://docs.google.com/presentation/d/1TXvdsbJ0PBYPrSSD9ZK097Q6sED7aENcUBrao41oy5Q/edit#slide=id.g206563da1c8_0_1',target="_blank")
    ]),
    dbc.Row([
        html.P(['This presentation took place on July 3rd and is based on the articul "Bipolar Argumentation Frameworks, Modal Logic and Semantic Paradoxes" by  Carlo PROIETTI, Davide GROSSI, Sonja SMETS, and Fernando VELAZQUEZ-QUESADA. ',
        html.A('(Linke of the original document). ', href='https://eprints.illc.uva.nl/id/eprint/1735/1/Bipolar_AF_and_modal_logic_preprint.pdf',target="_blank"),
        ])
    ]),
    dbc.Row([
        html.A([html.Img(src='/assets/image_presentation/image12.png', style={'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://docs.google.com/presentation/d/1Yy8gVmkdBUV6tLy71UBFpqinvXr4c-2oIyv6xPtp6yY/edit#slide=id.g25dfbb64097_0_0',target="_blank")
    ]),
    dbc.Row([
        html.P(['This presentation took place on July 3rd and is based on the articul "Doing Analogical Reasoning in Dynamic Assumption-based Argumentation Frameworks" by Teeradaj RACHARAK. ',
        html.A('(Linke of the original document). ', href='https://ieeexplore.ieee.org/document/10098089',target="_blank"),
        ])
    ]),
    dbc.Row([
        html.A([html.Img(src='/assets/image_presentation/image13.png', style={'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://docs.google.com/presentation/d/1bSwaIrm90EFR1jriAMNiQa0PQ5hGYC1zXHboal2hrts/edit#slide=id.g11f682941b8_0_111',target="_blank")
    ]),
    dbc.Row([
        html.P(['This presentation took place on July 11th and is based on the articul "LangChain AI Handbook" and more specificaly the chapter 5. ',
        html.A('(Linke of the original document). ', href='https://www.pinecone.io/learn/series/langchain/',target="_blank"),
        ])
    ]),
    dbc.Row([
        html.A([html.Img(src='/assets/image_presentation/image14.png', style={'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://docs.google.com/presentation/d/1iN-g7hHXjdHHdcNTG4upTttXPzb_Ck8W2-GQ8JYw_d8/edit#slide=id.p',target="_blank")
    ]),
], className='page')

