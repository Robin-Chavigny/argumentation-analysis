import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path='/', title='Internship JAIST', name='Internship JAIST')



carousel_svm_conf_aa = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_linear_5.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_linear_8.png"},
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_poly_5.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_poly_8.png"},
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_rbf_5.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_rbf_8.png"},
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_sigmoid_5.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_sigmoid_8.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    className="carousel"
)

carousel_svm_conf_baf = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_linear_5_baf.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_linear_8_baf.png"},
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_poly_5_baf.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_poly_8_baf.png"},
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_rbf_5_baf.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_rbf_8_baf.png"},
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_sigmoid_5_baf.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/conf_sigmoid_8_baf.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    className="carousel"
)

carousel_svm_learn = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/learning_curv_5.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/learning_curv_8.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    className="carousel"
)

carousel_svm_learn_baf = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/learning_curv_5_baf.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/learning_curv_8_baf.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    className="carousel"
)

carousel_svm = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/accuracy.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/recall.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/precision.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/f1.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    className="carousel"
)

carousel_tree_conf_aa = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/conf_5.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/conf_8.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    className="carousel"
)

carousel_tree_conf_baf = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/conf_5_baf.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/conf_8_baf.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    className="carousel"
)

carousel_tree = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/accuracy.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/recall.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/precision.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/f1.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    style={'width': '50%'},
    className="carousel-tree"
)

carousel_forest_conf_aa = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/conf_5.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/conf_8.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    className="carousel"
)

carousel_forest_conf_baf = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/conf_5_baf.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/conf_8_baf.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    className="carousel"
)

carousel_svm_imp = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/imp_5.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/imp_8.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    style={'width': '80%'},
    className="carousel"
)
carousel_svm_imp_baf = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/imp_5_baf.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/imp_8_baf.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    style={'width': '80%'},
    className="carousel"
)

carousel_forest = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/accuracy.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/recall.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/precision.png"},
        {"key": "2", "src": "/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.4-Random Forest/f1.png"},
    ],
    controls=True,  # Affiche les flèches pour naviguer
    indicators=True,  # Affiche les indicateurs en bas du carrousel
    interval=False,  # Temps en millisecondes avant le passage à l'image suivante (2000 ms = 2 secondes)
    #ride="carousel",  # Permet de faire défiler automatiquement les images 
    style={'width': '50%'},
    className="carousel-tree"
)

layout = dbc.Container([
    dbc.Row([
        html.H1('Welcome to my Internship at JAIST !', style={'text-align' : 'center', 'padding': '50px','font-size': '60px'}),
        dbc.Col([ html.A([html.Img(src='/assets/logo_isima.png', style={'width': '60%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://www.isima.fr/',target="_blank"),]),
        dbc.Col([ html.A([html.Img(src='/assets/logo_jaist.jpg', style={'width': '60%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})], href='https://www.jaist.ac.jp/index.html',target="_blank"),]), 
        
        



        
        html.H2('0-Introduction'),
        html.P(['This web site is the result of my intrnship taking place from May to September 2024 at JAIST University. It was an integral part of my academic curriculum at ISIMA, designed to provide me with valuable international experience and to '
                'fulfill the requirements for validating my second year of studies. The experience at JAIST was not only a significant academic milestone but also an invaluable opportunity for personal and professional development.']),
        html.P(['The primary focus of this internship was to investigate how argumentation is used in human communication and debate across various subjects. This involved a deep dive into the theoretical aspects of Argumentation Frameworks ',
                html.A('[1]', href='https://www.sciencedirect.com/science/article/pii/000437029400041X?ref=pdf_download&fr=RR-2&rr=8b4cc6494a9825fc',target="_blank"),
                ' to understand the diverse models that represent complex argumentative interactions. By examining these frameworks, I aimed to gain insights into the different ways in which argumentation can be structured and analyzed.']),
        html.P(['A key objective of my work was to develop an artificial intelligence system capable of identifying, analyzing, and elucidating arguments within debate transcripts',
                html.A('[2]', href='https://aclanthology.org/2021.argmining-1.8.pdf',target="_blank"),
                '. This system is presented in this  interactive web interface designed to present the results in a user-friendly manner in the "Visualisation section". To accomplish this, I engaged extensively with the theoretical underpinnings of '
                'argumentation frameworks and acquired new programming skills. Specifically, I learned to use Dash for web development, which was crucial for creating and deploying this web interface, and Heroku system for the web deployment.']),   
        html.P(['The dataset',
                html.A('[2]', href='https://aclanthology.org/2021.argmining-1.8.pdf',target="_blank"),
                ' for this project was composed of transcripts from U.S. presidential debates held during the 2020 election campaign. These transcripts were meticulously extracted from audio recordings of the debates, providing a rich source of data '
                'for the analysis. The processing and analysis of this data involved significant effort, including the development of machine learning models to classify and interpret the arguments.']),             
        html.P(['In addition to the technical aspects of the project, I was actively involved in presenting my research and findings. This included multiple presentations where I explored theoretical topics related to argumentation frameworks. These '
                'presentations were an essential part of the internship, allowing me to communicate my progress and insights to both my tutor and the broader research group at the laboratory. All presentations have been made available on this web '
                'interface, providing further insights into the theoretical underpinnings of the project.']),
        html.P(['This Presentation page offers a detailed overview of the various tasks I undertook during the internship, including the methodologies employed, the challenges encountered, and the solutions devised. It reflects on the learning outcomes of '
                'the internship, highlighting how the experience has contributed to my professional and academic growth. Through this page, I aim to provide a clear account of the significant achievements and developments that marked '
                'my time at JAIST, and how this experience has paved the way for future endeavors in the field of argumentation and artificial intelligence.']),
        html.P(['(github of the project : ',
                html.A('argumentation-analysis', href='https://github.com/Robin-Chavigny/argumentation-analysis',target="_blank"),
                ')']),
        
        




        html.H2('1-Start of the project'),
        html.P(['The internship began with Professor Racharack presenting a selection of subjects related to argumentation frameworks for the main project. Among these, I chose to base my research on the study titled “M-Arg: Multimodal Argument Mining '
                'Dataset for Political Debates with Audio and Transcripts”',
                html.A('[2]', href='https://aclanthology.org/2021.argmining-1.8.pdf',target="_blank"),
                '. This research addresses two pivotal questions in the field of argumentation mining: “How argumentative relations between units are annotated” and “How claims and/or premises are identified”. The original datasets produced by the M-Arg '
                'research serve as the foundation for all subsequent results in my project. To extract and analyze these datasets, I utilized the “data_extraction.ipynb” file ',
                html.A('(github : python/data_extraction.ipynb)', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/data_extraction.ipynb',target="_blank"),
                '. This Jupyter notebook contains the necessary code and procedures to process the data and generate the findings presented in this section.']),
        

        html.H4(['1.1-Original dataset overview']),
        html.P(['The M-Arg research [1] aimed to create a high-quality annotated dataset of political debates, complete with audio and time-stamped transcripts, specifically designed for multimodal argumentation mining. This comprehensive dataset serves '
                'multiple purposes within the research community. Primarily, it provides benchmark model results, allowing researchers to evaluate and compare their models performance against a standardized set of data. Furthermore, it offers a '
                'comparative analysis of the added value that multimodal models bring, as opposed to relying solely on text-only or audio-only models.']),
        html.P(['The original dataset is derived from five US 2020 presidential debates. These debates include three interactions solely between the two candidates, Donald Trump and Joe Biden, moderated by a single individual. In the remaining two '
                'debates, known as Town Hall events, the candidates engaged with the audience, adding a layer of complexity to the interactions. The lengths of the audio files from these debates range from approximately one hour to one hour and '
                'thirty-five minutes. These audio files have been meticulously transcribed into various text files, providing a rich resource for analysis, capturing the spoken words and time-stamped interactions.']),
        html.Ul([html.Li([html.A('github : python/us_election_2020_1st_presidential_debate.csv', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/us_election_2020_1st_presidential_debate.csv',target="_blank")]),
                 html.Li([html.A('github : python/us_election_2020_2nd_presidential_debate.csv', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/us_election_2020_2nd_presidential_debate.csv',target="_blank")]),
                 html.Li([html.A('github : python/us_election_2020_biden_town_hall.csv', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/us_election_2020_biden_town_hall.csv',target="_blank")]),
                 html.Li([html.A('github : python/us_election_2020_trump_town_hall.csv', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/us_election_2020_trump_town_hall.csv',target="_blank")]),
                 html.Li([html.A('github : python/us_election_2020_vice_presidential_debate.csv', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/us_election_2020_vice_presidential_debate.csv',target="_blank")])]),
        html.P(['These individual text files from all the debates are then compiled into a single comprehensive file. This compilation consolidates all the information, providing a unified resource that includes every debate s transcriptions and '
                'annotations. By compiling the texts files into one, researchers can easily access and analyze the complete dataset, facilitating a more streamlined and efficient workflow for argumentation mining and related tasks.']),
        html.Ul([html.Li([html.A('github : python/full_feature_extraction_dataset.csv', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/full_feature_extraction_dataset.csv',target="_blank")])]),
        html.P(['The debates were tokenized by sentences or utterances, resulting in a total of 6,527 segments. The segments were meticulously labeled to include the name of the speaker, the specific topic of their current conversation, and the precise '
                'time frame during which these segments appear in the audio file.']),
        html.Img(src='/assets/1-Start of the project/1.1-Original dataset overview/time_speak_per_speaker_for_every_debates.png'),
        html.P(['This graph represents the distribution of speaking time among various speakers. It clearly illustrates that the two presidential candidates were the most frequent speakers. Notably, Donald Trump had a significant advantage in speaking '
                'time due to his continuous speaking style. Additionally, the different moderators for each debate segment occupy a substantial portion of the speaking time, as their role is to pose questions to the candidates. These findings required '
                'meticulous analysis, as a high volume of speech does not necessarily correlate with the strength or quality of argumentation.']),
        html.Img(src='/assets/1-Start of the project/1.1-Original dataset overview/time_speak_per_intervention_per_speaker_for_every_debates.png'),
        html.P(['As depicted in this graphic, although Donald Trump spoke frequently, his contributions were often brief interjections. In contrast, Joe Biden s speeches were more extended when he spoke, reflecting a different speaking style. However, '
                'Kamala Harris had the longest speaking time per speech. This is noteworthy, as Joe Biden s running mate is well-known for her oratory skills, which likely contributed to her extended speaking durations. Her ability to articulate her '
                'points clearly and persuasively often resulted in her having the most prolonged speaking segments during the debates.']),
        html.P(['Throughout all the debates, the moderators introduced a variety of topics that addressed the primary concerns of the American people in 2020. These exchanges were organized around these topics, reflecting the most pressing issues of the '
                'time like the COVID pandemic or the economy of the country. Each topic must be understood within the context of 2020, highlighting why some were deemed far more significant than others.']),
        html.Img(src='/assets/1-Start of the project/1.1-Original dataset overview/number_of_exchanges_for_each_topic.png'),
        html.Img(src='/assets/1-Start of the project/1.1-Original dataset overview/number_of_exchanges_per_recurrence_for_each_topic.png'),
        html.P(['As anticipated, COVID-19 and racism emerged as the two predominant subjects in the United States in 2020. The global pandemic brought unprecedented health, economic, and social challenges, making COVID-19 a central focus of national '
                'discourse. The widespread impact of the virus affected nearly every aspect of daily ife, leading to discussions on public health measures, economic relief packages, and the overall response to the crisis.']),
        html.P(['Simultaneously, the resurgence and peak of the Black Lives Matter movement highlighted systemic racism and police brutality, bringing these critical issues to the forefront of public attention and debate. The death of George Floyd and '
                'subsequent protests across the nation intensified the call for racial justice and police reform. This movement not only emphasized the long-standing issues of racial inequality but also spurred widespread societal reflection and calls for '
                'change.']),
        html.P(['The confluence of these events underscored the urgency and gravity of addressing both the pandemic and racial injustice in the country. The debates reflected this urgency, dedicating significant time and focus to these topics, as they '
                'were central to the concerns and experiences of the American public in 2020. By discussing these issues extensively, the debates aimed to provide clarity on the candidates positions and proposed solutions to these critical challenges.']),
        html.P(['Political debates often encompass a broad spectrum of topics, each brimming with numerous arguments. This complexity can make it difficult to follow the discussion, potentially leading to the loss of critical information. To effectively '
                'manage and analyze this intricate web of discourse, employing an Argumentation Framework (AF) as an analytical tool is highly advantageous.']),
        html.P(['The Argumentation Framework allows for the systematic organization and evaluation of arguments, helping to clarify the relationships between different points of view. By mapping out how arguments support or contradict each other, AFs '
                'provide a structured way to navigate through the debate, ensuring that no significant argument is overlooked. This analytical approach not only enhances the clarity of the debate but also enables a deeper understanding of the underlying '
                'issues, making it easier to identify key points and assess the overall coherence of the discussion.']),

        
        html.H4(['1.2-Argument relationship']),
        html.P(['All these debates are characterized by intense argumentation, with each speaker vigorously defending their points and striving to convince or reassure their electorate. The debates are marked by a complex web of arguments, where each '
                'statement is interconnected with others, forming a dynamic dialogue. Rather than treating the identification of argumentative units and their relationships as separate tasks, the researchers opted to classify the relationship between '
                'sentence pairs directly as support, attack, or neither. The determination of these relationships was context-dependent, reflecting the nuances of the discussion.']),
        html.P(['To accurately classify the type of relationship between two sentences, the original researchers relied on human intelligence. The process began by randomly selecting a sentence from one of the audio transcripts. The second sentence was '
                'then chosen using a Gaussian function centered on the first sentence, ensuring that it was temporally close to the first. This method was designed to capture interactions that were likely to be contextually related, rather than isolated '
                'statements.']),
        html.P(['To assist the evaluators in making informed decisions, the researchers provided a context, i.e a group of sentences that included the two selected ones. This context was essential for understanding the broader discussion and the '
                'relationship between the sentences. The evaluators were then asked to determine the type of relationship between the sentences, whether one supported, attacked, or had no significant relationship to the other. In addition to classifying '
                'the relationship, the evaluators were required to explain their reasoning, offering insight into their thought process.']),
        html.P(['This meticulous process resulted in the creation of the first dataset, named “full_data.csv”',
                html.A('(github : python/full_dataset.csv)', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/full_dataset.csv',target="_blank"),
                ', which contains not only the classified relationships between sentence pairs but also the evaluators explanations and confidence levels. This dataset serves as a foundational resource for analyzing argumentative relationships within the '
                'context of the 2020 presidential debates.']),
        html.P(['The file “full_data.csv” primarily consists of several key components that are critical for understanding the relationships between argumentative sentences. Among these are:']),
        html.Ul([html.Li([html.Strong('Confidence Level (confidence) : '),
                          'This represents the evaluators self-assessed certainty in their judgment about the relationship between the sentences. It is rated on a scale from 1 to 5, with higher scores indicating greater confidence.']),
                 html.Li([html.Strong('Relation (relation) : '),
                          'This is the type of relationship suggested by the evaluator between the two selected sentences, classified as either support, attack, or neither.']),
                 html.Li([html.Strong('Context (context) : '),
                          'This includes the group of sentences provided to the evaluator, containing the two key sentences being analyzed. The context is crucial for understanding the broader discussion and helps the evaluator make an informed judgment.']),
                 html.Li([html.Strong('Relation Gold (relation_gold ) : '),
                          'This represents the true relationship between the sentences as determined by a consensus or a more rigorous evaluation process. It serves as the ground truth against which the evaluators suggestions are compared.']),
                 html.Li([html.Strong('Relation Gold Reason (relation gold reason) : '),
                          'This is the rationale behind the designation of the true relationship type, explaining why the “relation_gold” was determined as such. It provides insight into the logic used to establish the ground truth.'])]),
        html.P(['In the process of determining the true type of relationship between sentence pairs, all the answers from different evaluators are taken into account. The evaluators confidence scores play a pivotal role in this process. If an evaluator '
                'frequently and correctly identifies the true relationship type with high confidence, their trust score improves. This trust score reflects the evaluator s reliability and expertise in making accurate judgments.']),
        html.P(['An evaluator with a high trust score will have a greater influence on subsequent evaluations, meaning their suggestions are weighted more heavily in determining the true relationship type. This dynamic process ensures that the most '
                'reliable evaluators contribute significantly to the final dataset, improving the overall accuracy of the classifications.']),
        html.P(['This methodology leads to the creation of the second dataset, named “full_data_processing.csv”',
                html.A('(github : python/full_dataset_processing.csv)', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/full_dataset_processing.csv',target="_blank"),
                '. This file is particularly valuable for our project as it contains the refined results after considering the evaluators trust scores. The dataset offers a more accurate and reliable representation of argumentative relationships, making '
                'it one of the most utilized resources in our analysis.']),
        html.P(['Here s an overall view of the “full_data_processing.csv” dataset, which includes:']),
        html.Img(src='/assets/1-Start of the project/1.2-Argument relationship/distribution_of_relation_type_in_full_datset.png',style={'width': '40%', 'height' : '40%'}),
        html.Img(src='/assets/1-Start of the project/1.2-Argument relationship/number_of_relation_per_type_for_each_topic.png'),
        html.P(['This dataset serves as a cornerstone for our project, providing a reliable basis for analyzing argumentative structures and relationships within the debates. It is instrumental in understanding how different statements relate to one '
                'another, especially in the context of a high-stakes environment like political debates.']),
        html.P(['In the context of analyzing argumentative relationships within debates, it is common to observe that the “neither” relationship is predominant. This phenomenon can be attributed to the nature of debates, where the majority of sentences '
                'do not exhibit direct argumentative connections with one another.']),
        html.P(['During a debate, participants typically present a wide range of statements, arguments, and counterarguments. However, not all of these elements are directly interconnected in terms of argumentative structure.']),
        html.Img(src='/assets/1-Start of the project/1.2-Argument relationship/example_of_arguments_not_interacting_with_every_other.png',style={'width': '30%', 'margin-bottom': '15px'}),
        html.P(['Many sentences serve different purposes. They might provide background information, elaborate on a particular point, clarify previous statements, or introduce entirely new ideas. These sentences contribute to the overall flow and '
                'coherence of the debate but do not necessarily engage in direct argumentative interaction with other sentences.']),
        html.P(['As a result, when analyzing the relationships between sentences, a significant proportion will fall into the “neither” category. This means that these sentences neither support nor attack other sentences within the context of the debate. '
                'For instance, a candidate might state factual information or offer an opinion that doesn t directly counter or bolster another speaker s argument, leading to a “neither” classification.']),
        html.P(['The prevalence of “neither” relationships underscores the complexity and diversity of discourse in debates. Debates are not merely a series of direct confrontations between opposing arguments. They also involve a considerable amount of '
                'dialogue that is supplementary or tangential to the core argumentative exchanges. This diversity in discourse reflects the multifaceted nature of debates, where not every statement is explicitly tied to others in an argumentative manner.']),
        html.P(['Understanding the predominance of “neither” relationships is crucial for our analysis. It highlights the importance of considering the broader context and the different functions that statements serve within a debate. By recognizing that '
                'not every sentence will have a clear argumentative connection to another, we can develop a more nuanced and accurate analysis of the debate s overall structure and the interactions between participants.']),


        



        html.H2('2-Various type of Argumentation Framework (AF)'),
        html.P(['The theory of argumentation frameworks is a broad and evolving subject that has developed significantly since its initial formalization by researchers such as P. M. Dung in 1995, as detailed in his seminal research “On the acceptability '
                'of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games”. Dung s framework laid the foundation for understanding how arguments can be constructed, evaluated, and accepted within a formal '
                'system, providing a basis for subsequent developments in the field of argumentation theory.']),
        html.P(['Dung’s abstract argumentation framework introduced a formal model where arguments are represented as nodes in a graph, with directed edges indicating attacks between arguments. This model allowed for the systematic study of argument '
                'acceptability, defining various semantics such as grounded, preferred, and stable extensions, which describe different sets of collectively acceptable arguments. The significance of Dung s work lies in its ability to generalize and unify '
                'different approaches to nonmonotonic reasoning, logic programming, and game theory, making it a pivotal reference point for further research in argumentation theory.']),
        html.P(['To gain a comprehensive understanding of the concept and its evolution, I also presented the paper “Argumentative explanations for pattern-based text classifiers” by P. Lertvittayakumjorn ',
                html.A('[3]. ', href='https://content.iospress.com/articles/argument-and-computation/aac220004#ref018',target="_blank"),
                'This research delves into the application of argumentation frameworks for providing explanations in the context of machine learning, particularly for text classification tasks. The paper addresses a key challenge in the field of '
                'artificial intelligence: the need for interpretable and transparent models.']),
        

        html.H4(['2.1-What is an AF?']),
        html.P(['The Argumentation Framework (AF) s theory seeks to explore and understand the fundamental mechanisms that humans use in argumentation and to implement these mechanisms on computers. This field of study delves into how people construct, '
                'present, and evaluate arguments, and it aims to replicate these processes in computational models. The ultimate goal is to enable machines to engage in argumentation, mimicking the human ability to reason, debate, and reach conclusions '
                'through structured dialogue.']),
        html.P(['One of the core principles guiding this theory is encapsulated in the adage “The one who has the last word laughs best”. This phrase highlights a key aspect of argumentation: the strength of an argument often lies not just in its initial '
                'presentation, but in its ability to withstand challenges and counterarguments. In essence, the most convincing argument is one that remains standing after all opposing arguments have been addressed or refuted. This principle underscores '
                'the importance of resilience and persistence in argumentative discourse.']),
        html.P(['Argumentational reasoning, which is at the heart of this theory, is based on the concept of “external stability” of accepted arguments. External stability refers to the idea that a statement or argument is considered credible and '
                'acceptable if it can be successfully defended against any attacking arguments. In other words, an argument is deemed believable if it can be maintained in the face of opposition, or more generally, if there is no convincing evidence to '
                'contradict it. This notion emphasizes the dynamic nature of argumentation, where the strength of an argument is constantly tested against potential objections.']),
        html.Img(src='/assets/2-Various type of Argumentation Framework (AF)/2.1-What is an AF/visual_representation_of_a_general_AF.png',style={'width': '20%','margin-bottom': '15px'}),
        html.P(['This framework provides a mathematical and logical foundation for understanding how arguments can be constructed, related, and evaluated, especially when they oppose or support each other. We generaly define AF = (AR, →) where :']),
        html.Ul([html.Li(['AR : is a set of arguments containing all the individual arguments that are part of the discussion or analysis. Each element in the set represents a distinct argument, which can be a statement, claim, or proposition that someone '
                          'might put forward in the debate.']),
                 html.Li([' → : is a binary relation on AR in the form → ⊆ AR × AR. This means that → is a set of ordered pairs (A, B), where each pair indicates that argument A is in conflict with or attacks argument B. The notion of “attack” in this '
                          'context refers to a situation where one argument challenges, contradicts, or undermines another argument.'])]),
        html.P(['Formally, A→ B defines the relationship “A represents an attack against B”. This relationship is crucial in the study of argumentation because it allows us to model how different arguments interact, particularly when they are in '
                'opposition. In other words, if A→ B holds, it indicates that argument A is presented as a counter to argument B, attempting to weaken or refute B.']),
        html.P(['This structure allows us to formally analyze the dynamics of argumentation, including identifying which arguments are “defensible” in the face of attacks, which arguments are mutually reinforcing, and how overall agreement or consensus '
                'can be reached in a contentious environment.']),

        
        html.H4(['2.2-Various type of AF']),
        html.P(['There exist a multitude of type of AF. In our project, we focus on two key types of argumentation frameworks: Abstract Argumentation Framework (AA)',
                html.A('[2] ', href='https://aclanthology.org/2021.argmining-1.8.pdf',target="_blank"),
                'and Bipolar Argumentation Framework (BAF)',
                html.A('[4]. ', href='https://eprints.illc.uva.nl/id/eprint/1735/1/Bipolar_AF_and_modal_logic_preprint.pdf',target="_blank"),
                'Each of these models provides a different perspective on how argumentative relationships are structured and classified, which in turn affects how we analyze and interpret the interactions between arguments.']),

        html.H5(['2.2.1-Abstract Argumentation Framework (AA)']),
        html.P(['The Abstract Argumentation Framework is a foundational model in the field of argumentation theory. It simplifies the analysis by considering only a single type of relationship between arguments: the attack relation. In the AA model, '
                'arguments can either attack or be attacked by other arguments, and this interaction forms the basis for determining which arguments are considered acceptable (or defensible).']),

        html.H5(['2.2.2-Bipolar Argumentation Framework (BAF)']),
        html.P(['The Bipolar Argumentation Framework extends the basic structure of the AA model by introducing an additional type of relationship known as Support. This inclusion recognizes that arguments can not only attack one another but can also '
                'provide support, thereby strengthening the position of another argument. Classification in the BAF model is therefore more nuanced, as it distinguishes between three types of relationships:']),
        html.Ul([html.Li([html.Strong(['Attack : ']),
                          'As in the AA model, this category includes relationships where one argument challenges another.']),
                 html.Li([html.Strong(['Support : ']),
                          'This category captures relationships where one argument bolsters or strengthens another, providing a positive link between the two.']),
                 html.Li([html.Strong(['Neither : ']),
                          'This category includes relationships where there is no direct interaction in terms of attack or support. These relationships are neutral, indicating that the arguments in question do not directly influence each other in the '
                          'context of the discussion.'])]),
        html.P(['We mainly model this type of AF by: BAF = (AR, →, ⇒) with (AR, →) representing a basic AF, and ⇒ is a binary relation on AR in the form ⇒⊆ AR × AR, where for any (A, B) ∈ AR × AR, A ⇒ B means that argument A supports argument B.']),
        html.Img(src='/assets/2-Various type of Argumentation Framework (AF)/2.2-Various type of AF/visual_representation_of_a_general_BAF.jpg',style={'width': '15%','padding':'15px'}),
        html.P(['To further solidify my understanding of BAF, I also presented the work titled “Bipolar Argumentation Frameworks, Modal Logic and Semantic Paradoxes”',
                html.A('[4]. ', href='https://eprints.illc.uva.nl/id/eprint/1735/1/Bipolar_AF_and_modal_logic_preprint.pdf',target="_blank"),
                'This work delves into the theoretical underpinnings of BAF, exploring how bipolar relationships can be modeled using modal logic and addressing the complex semantic paradoxes that can arise in such frameworks.']),

        html.H5(['2.2.3-Importance of Distinction in Representation']),
        html.P(['Understanding and distinguishing between these two frameworks—AA and BAF—is crucial for our project. Each framework offers unique insights into the nature of argumentative interactions, and by incorporating results from both, we can '
                'achieve a more comprehensive and accurate analysis of the relationships between arguments.']),
        html.P(['In the continuation of this project, the distinction between the AA and BAF models will play a vital role in our analysis. By acknowledging the specific characteristics of each framework, we can ensure that our classification of '
                'argumentative relationships is precise and reflective of the underlying structure of the debates we are studying.']),
        html.P(['This dual approach, utilizing both AA and BAF models, allows us to capture the full spectrum of argumentative interactions, from direct opposition to supportive connections, thereby enabling a more thorough and nuanced analysis of the '
                'debates.']),


        html.H4(['2.3-Acceptability of arguments']),
        html.P(['An important part of the AF theory is the acceptability of the argument. We begin by introducing some foundational concepts that are critical to the framework’s structure and function. One of the key concepts is conflict-freeness.']),
        html.P(['A set of arguments S is considered conflict-free if no arguments within S attack each other. In other words, for any two arguments A and B in S, argument A does not attack argument B. This concept is fundamental because it ensures that '
                'the set S represents a coherent group of arguments that do not contradict or undermine one another within the framework.']),
        html.P(['Building on the idea of conflict-freeness, we introduce the notion of an acceptable argument. An argument A within the set of all arguments AR is deemed acceptable with respect to a set S of arguments if it can be defended against all '
                'attacks from arguments outside S. Specifically, for every argument B in AR that attacks A, there must exist an argument in S that attacks B for the AA model or in addition an acceptable argument in S that supports A for the BAF model. '
                'This condition ensures that A is protected by the set S from any external attacks, making it an argument that can be reasonably upheld within the context of the argumentation framework.']),
        html.P(['From the concepts of conflict-freeness and acceptability, we can derive extensions, which are sets of arguments that satisfy certain criteria based on different semantics. These extensions provide a systematic way to evaluate the '
                'acceptability of arguments within the framework. The most common types of semantics used to define these extensions include:']),
        html.Ul([html.Li([html.Strong(['Grounded Extension']),
                          html.A('[2]', href='https://aclanthology.org/2021.argmining-1.8.pdf',target="_blank"),
                          ' : A grounded extension is the smallest (with respect to set inclusion) conflictfree set of arguments that defends itself. It is unique and is often considered the most conservative extension because it only includes arguments '
                          'that can be indisputably defended against all attacks. It’s important in situations where minimality and caution in accepting arguments are prioritized. The Grounded extension can be created easily with the following algorithm:',
                          html.Img(src='/assets/2-Various type of Argumentation Framework (AF)/2.3-Acceptability of arguments/grounded_extension_algorithm.png',style={'margin-bottom': '15px'}),
                          'The notion of acceptable with respect to (w.r.t) an set of argument is variable depending of the type of AF we study. For the AA model we say that a is acceptable w.r.t S if ∀x ∈ A, [(x, a) ∈ R =⇒ ∃s ∈ S, (s, x) ∈ R]. For the '
                          'BAF=(A,att,sup) model we add a other condition, a is acceptable w.r.t S if ∀x ∈ A, [(x, a) ∈ att =⇒ ∃s ∈ S, (s, x) ∈ att or (s, a) ∈ sup].']),
                 html.Li([html.Strong(['Complete Extension']),
                          html.A('[2]', href='https://aclanthology.org/2021.argmining-1.8.pdf',target="_blank"),
                          ' : Complete extensions include all arguments that are acceptable with respect to themselves. This means that every argument in the extension is defended by other arguments within the same extension. It provides a balanced '
                          'approach, capturing both the arguments that can be defended and those that play a role in defending others. We formaly define it by the following settlements : S is a complete extension if ∀x ∈ A, x is acceptable w.r.t S ⇔ x ∈ '
                          'S.']),
                 html.Li([html.Strong(['Restrained Extension : ']),
                          'Restrained extensions aim to strike a balance by including defensible arguments while avoiding overly aggressive stances that could destabilize the argumentation framework. This type of extension is particularly useful in '
                          'scenarios where moderation and stability are desired, allowing for a comprehensive yet controlled evaluation of the argument set. To achieve this, the notion of w.r.t is reviewed. For the AA model, a is acceptable w.r.t S if '
                          '|{s ∈ S, ∀x ∈ {x ∈ A, (x, a) ∈ R}, (s, x) ∈ R}| ≥ |{x ∈ A, (x, a) ∈ R}|. For the BAF model, a is acceptable w.r.t S if ∀x ∈ A, [(x, a) ∈ att =⇒ ∃s ∈ S, (s, x) ∈ att or |{s ∈ S, (s, a) ∈ sup}| ≥ |{x, (x, a) ∈ att}|].'])
                        ]),
        html.P(['These extensions are critical for understanding the dynamics of argumentative interactions. By analyzing which arguments belong to which extensions under different semantics, we can systematically evaluate the acceptability and '
                'defensibility of various positions within a debate or discussion. This structured approach allows us to resolve complex argumentative interactions by identifying which arguments can be upheld, which are disputed, and how these relationships'
                 ' influence the overall discourse.']),
        html.P(['Each type of extension offers a different lens through which to view the argumentation, and depending on the context or the goals of the analysis, different extensions might be more appropriate.']),






        html.H2(['3-Beginning of the Machine learning']),
        html.H4(['3.1-Set up']),
        html.P(['The next phase of the internship focuses on the development of an artificial intelligence (AI) system designed to analyze and extract arguments from the original dataset. This phase is critical for advancing the understanding and '
                'representation of debate’s content by uncovering new arguments and identifying relationships between them. The primary objective is to enhance the depth and accuracy of argumentation analysis, particularly in the context of Abstract '
                'Argumentation (AA) and Bipolar Argumentation Framework (BAF) representations.']),
        html.P(['To achieve this goal, I employed a range of machine learning (ML) models, carefully selecting and evaluating each to determine the most efficient one for the task. The models included various supervised learning algorithms, with a '
                'particular focus on:']),
        html.Ul([html.Li([html.Strong(['Support Vector Machines (SVM) : ']),
                          'It’s well-suited for classification tasks, making them a strong candidate for identifying argument types and relationships. Their ability to handle high-dimensional spaces and define optimal hyperplanes for separation was '
                          'leveraged to classify arguments into categories such as Attack, Support, and Neither.']),
                 html.Li([html.Strong(['Decision Trees : ']),
                          'With their straightforward approach to classification, they were used to map out the decision paths leading to different argument types. Their interpretability made them a valuable tool for understanding the decision-making '
                          'process in argument classification.']),
                 html.Li([html.Strong(['Random Forests : ']),
                          'This ensemble learning method was tested for its robustness and flexibility in dealing with complex datasets. By constructing multiple decision trees and averaging their results, Random Forests provided insights into the '
                          'reliability and variability of argument classification, offering a balanced approach between accuracy and computational efficiency.'])]),
        html.P(['A significant challenge in this phase was ensuring that the chosen machine learning models could effectively handle the nuances of both Abstract Argumentation (AA) and Bipolar Argumentation Framework (BAF) representations. This required '
                'the models to not only detect individual arguments but also map out the intricate network of relationships between them. For AA model, it focused primarily on identifying attack relationships. The models needed to differentiate between '
                'Attack and Non-attack relationships, where Non-attack included both Neither and Support categories. For BAF model, it introduced an additional complexity by including Support relationships alongside Attack and Neither. The models were ' 
                'trained to recognize and classify these relationships, accounting for the additional layer of relational dynamics in BAF.']),
        html.P(['The culmination of this phase was the development of a robust AI system capable of providing insightful analyses and visualizations of debate arguments. Using the trained models, the system could autonomously extract arguments from new '
                'datasets, identifying the key components of debates. Moreover the AI system could accurately classify the relationships between arguments, distinguishing between Attack, Support, and Neither categories, depending on the representation '
                '(AA or BAF).']),

       html.H5(['3.1.1-Pre-processing']),
       html.P(['Before applying any models, we first need to pre-process the data. The raw data consists of a multitude of characters, which cannot be directly analyzed by our machine learning models. Therefore, it is necessary to convert this data into a '
               'format that our AI can effectively utilize.']),
        html.P(['The preprocessing begins by dividing the data into input features and target labels. In our case, the target labels are the “relation gold” values for each instance. For the Abstract Argumentation (AA) models, we define two classes that '
                'we want to distinguish: 0 for non-attack and 1 for attack. These two classes are a recast of the original dataset labels, with the non-attack class regrouping the neither and support labels. For the Bipolar Argumentation Framework (BAF) '
                'models, we define three classes from the three original label: 0 for neither, 1 for attack, and 2 for support.']),
        html.P(['The original dataset we use in this part is “full_datset.csv”. As illustrated in the following graph, the dataset is significantly imbalanced, with a disproportionate number of relationships labeled as “Neither”.']),
        html.Img(src='/assets/1-Start of the project/1.2-Argument relationship/distribution_of_relation_type_in_full_datset.png',style={'width': '40%'}),
        html.P(['To address the issue of class imbalance in the dataset, we applied undersampling to the majority classes. In the context of the Abstract Argumentation (AA) framework, the minority class was “Non-attack”, while in the Bipolar Argumentation '
                'Framework (BAF), the minority classes were “Neither” and “Support”.']),
        html.P(['To achieve this, we selected samples from these overrepresented classes by selecting random existing relation form the majority classes. This effectively decreasing their presence in the dataset. After selecting these new samples, we '
                'shuffled the entire dataset to ensure that the different classes were well-mixed. This shuffling step was crucial to prevent the model from learning patterns based solely on the order of the data, which could lead to biased predictions.']),
        html.P(['By undersampling the majority classes and ensuring a randomized distribution, we aimed to provide the models with a more balanced dataset. This approach helps in improving the model’s ability to correctly identify and classify relationships'
                ' across all classes, leading to more accurate and reliable predictions.']),
        html.P(['Once the classes are defined, the next step is to convert the textual data into a format that the AI can process. For this, we use Term Frequency-Inverse Document Frequency (TF-IDF) vectorization. TF-IDF is a statistical measure used to '
                'evaluate the importance of a word in a document relative to a collection of documents (corpus). The TF-IDF vectorizer transforms our text data into numerical values by creating a matrix where each row represents a document and each column '
                'represents a word in the vocabulary, with values indicating the importance of each word']),
        html.P(['The TF-IDF process involves the following steps, first, the data is tokenized by breaking it down into individual words or tokens. Next, the Term Frequency (TF) for each document is calculated, representing how often a word appears in a '
                'document. The Inverse Document Frequency (IDF) is then determined, measuring how important a word is by considering how common or rare it is across all documents in the corpus. Words that appear in many documents have a lower IDF value. '
                'Finally, the TF and IDF values are multiplied for each word, resulting in a TF-IDF score that reflects the importance of a word in a document relative to the entire corpus']),
        html.P(['To enhance the efficiency of the TF-IDF vectorization process, we introduced additional parameters. Specifically, we set the max df parameter to 0.95. This parameter helps to filter out terms that appear in more than 95% of the different '
                'relations. By excluding these frequently occurring terms, which are often less informative, we can improve the relevance and quality of the feature set used for training the machine learning models.']),
        html.P(['The result of TF-IDF vectorization is a sparse matrix where each row corresponds to a document and each column corresponds to a term from the vocabulary, with the cell values representing the TF-IDF score for each term-document pair. By '
                'converting the textual data into this mathematical matrix, we enable our machine learning models to process and analyze the data effectively. This transformation is crucial for training the models to identify and classify the argumentation '
                'relations accurately.']),
        html.P(['To train the various machine learning models and ensure the robustness and reliability of the results, I employed the cross-validation technique. This method involves dividing the original dataset into k equally sized subsets, known as '
                'k-folds. Each fold serves as a validation set while the remaining k-1 folds are combined to form the training set. This training set allow the model to learn and discern patterns and relationships within the data, thereby enabling it to '
                'predict the correct output for given inputs. After training, the model is evaluated on the held-out fold. This testing set is used to evaluate the performance of the trained model, providing insights into how well it generalizes to new, '
                'unseen data. This process is repeated k times, with each fold serving as the validation set once. The model’s performance is assessed for each fold, and the results are averaged to provide an overall performance metric. This average score '
                'reflects the model’s effectiveness across all subsets of the data. By using cross-validation, we ensure that every data point is used for both training and validation. This technique helps to reduce the variance of the evaluation, '
                'providing a more robust estimate of the model’s performance and mitigating issues related to overfitting or underfitting. Overall, cross-validation allows for a comprehensive assessment of the model’s performance by utilizing the entire '
                'dataset for both training and testing, thus providing a reliable measure of its generalization capability.']),

        html.H5(['3.1.2-SVM']),
        html.P(['The first model incorporated into this project is the Support Vector Machine (SVM). SVM is a versatile supervised learning algorithm that can be utilized for both classification and regression tasks. In this project, SVM was employed '
                'specifically for classification purposes. The SVM model operates by using different kernels to transform the input data into a form suitable for the learning algorithm, enabling it to handle non-linear relationships effectively. The '
                'kernels employed in this study include the linear kernel, polynomial kernel, radial basis function (RBF) kernel, and sigmoid kernel. Each kernel was evaluated separately by training and testing the SVM model with that specific kernel.']),
        html.P(['By applying different kernels and employing k-fold cross-validation, a comprehensive evaluation of each kernel’s impact on the model’s performance was achieved. This thorough evaluation process was instrumental in selecting the most '
                'effective kernel for our specific application, ensuring that the SVM model could accurately identify and classify arguments within the debate transcripts.']),
    ],className='page-text'),
    dbc.Row([
        dbc.Col([carousel_svm_conf_aa]),
        dbc.Col([carousel_svm_conf_baf]),
    ],className='page-text'),
    dbc.Row([
        dbc.Col([carousel_svm_learn]),
        dbc.Col([carousel_svm_learn_baf]),
    ],className='page-text'),
    dbc.Row([
        carousel_svm
    ],className='page-text'),
    dbc.Row([
        html.P(['The accuracy scores for each kernel do not exhibit significant dependence on the type of Argumentation Framework (AF). However, a slight decrease in performance is observed for the sigmoid kernel compared to the other kernels. This '
                'trend will be considered in all subsequent analyses.']),
        html.P(['To obtain a more comprehensive view of our models, we compared them using several performance metrics. These metrics include Recall, Precision, and the F1 score:']),
        html.Ul([html.Li([html.Strong(['Recall : ']),
                          'This metric is defined as the proportion of instances correctly identified by the model. It is calculated using the formula:',
                          html.Img(src='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/recall_formula.png', style={'width': '20%'}),
                          'where TP denotes True Positives and FN denotes False Negatives. Recall measures the model’s ability to identify all relevant instances within the data.']),
                 html.Li([html.Strong(['Precision : ']),
                          'This metric represents the proportion of instances predicted as positive that are indeed positive. It is computed using the formula:',
                          html.Img(src='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/precision_formula.png', style={'width': '21%'}),
                          'where FP denotes False Positives. Precision evaluates the accuracy of the positive predictions made by the model.']),
                 html.Li([html.Strong(['F1 Score : ']),
                          'The F1 score is defined as the harmonic mean of Precision and Recall. It provides a single metric that balances the trade-off between Precision and Recall. The F1 score is calculated using the formula:',
                          html.Img(src='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/f1_formula.png', style={'width': '22%'}),
                          'The F1 score is useful when we need to balance Precision and Recall, especially in situations where one metric is more critical than the other.']),
                ]),
        html.P(['By evaluating our models using these metrics, we gain a clearer understanding of their performance and effectiveness in identifying and classifying arguments.']),
        html.P(['Given the greater number of classes in the BAF model, its performance is slightly less effective compared to models with fewer classes. The increased complexity from additional classes can impact the model’s ability to accurately classify '
                'and differentiate between argument relationships, leading to somewhat reduced performance metrics.']),
        html.P(['With these observations, we opted to use the polynomial kernel with a 8-fold cross-validation for extracting data from the original dataset. This choice was made based on the polynomial model’s superior overall performance across the '
                'various metrics. The 8-fold cross-validation allows for a more comprehensive evaluation by training and testing the model on multiple subsets of the data, providing a robust estimate of the model’s performance.']),
        html.P(['By selecting the polynomial model with 8-fold cross-validation, we aim to leverage its enhanced performance in terms of Recall and F1 score to achieve more accurate and reliable results in identifying and analyzing arguments within the '
                'dataset.']),

        html.H5(['3.1.3-Decision Tree']),
        html.P(['The second model implemented in this project is the Decision Tree model. This model recursively partitions the dataset based on certain conditions to form a tree-like structure. Each node in the tree represents a decision point where the '
                'data is split according to specific attributes. The goal of the Decision Tree algorithm is to divide the dataset in a way that maximizes the homogeneity of the resulting subsets.']),
        html.P(['The Decision Tree model utilizes criteria to select attributes that best split the dataset. In this project, the Gini index is used as the measure of impurity or diversity. The Gini index is defined as:']),
        html.Img(src='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.2-SVM/gini.png', style={'width': '20%'}),
        html.P(['where pi represents the proportion of samples belonging to class i in the node. A Gini index of 0 indicates perfect purity, where all samples in the node belong to a single class. Conversely, a Gini index of 0.5 represents maximum '
                'impurity, where the samples are evenly distributed across different classes.']),
        html.P(['Each node in the Decision Tree contains the attribute or condition used to split the data, the number of samples reaching that node, and the class assigned to that node, which is determined based on the majority class of the samples in '
                'that node.'])

    ],className='page-text'),
    dbc.Row([
        dbc.Col([carousel_tree_conf_aa]),
        dbc.Col([carousel_tree_conf_baf]),
    ],className='page-text'),
    dbc.Row([
        dbc.Col([
            html.A([html.Img(src='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/tree_5.png')], href='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/tree_5.pdf',target="_blank"),
            html.A([html.Img(src='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/tree_5_baf.png')], href='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/tree_5_baf.pdf',target="_blank"),
            ]),
        dbc.Col([
            html.A([html.Img(src='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/tree_8.png')], href='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/tree_8.pdf',target="_blank"),
            html.A([html.Img(src='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/tree_8_baf.png')], href='/assets/3-Beginning of the Machine learning/3.1-Set up/3.1.3-Decision Tree/tree_8_baf.pdf',target="_blank"),
        ]),
        html.P(['Here is some comparison between the various model of decision tree:'])
    ],className='page-text'),
    dbc.Row([
        carousel_tree
    ],className='page-text'),
    dbc.Row([
        html.H5(['Random Forest']),
        html.P(['The third model implemented is the Random Forest. This model is an ensemble learning technique that constructs a multitude of decision trees during the training phase. Each decision tree is built using a different subset of the data and '
                'features, allowing the Random Forest to capture various aspects of the data’s structure. During prediction, the class that is most frequently represented among the individual trees is chosen as the final prediction.']),
        html.P(['The Random Forest’s approach of aggregating predictions from multiple decision trees helps in reducing overfitting and improving generalization. By averaging the predictions from a diverse set of trees, the model aims to achieve a more '
                'robust and reliable classification performance for the AA model.']),
        html.P(['In the context of the Abstract Argumentation (AA) model, the Random Forest provides the following results:'])
    ],className='page-text'),
    dbc.Row([
        dbc.Col([carousel_forest_conf_aa]),
        dbc.Col([carousel_forest_conf_baf]),
    ],className='page-text'),
    dbc.Row([
        carousel_svm_imp
    ],className='page-text'),
    dbc.Row([
        carousel_svm_imp_baf
    ],className='page-text'),
    dbc.Row([
        carousel_forest
    ],className='page-text'),
    dbc.Row([
        html.P(['The Random Forest’s performance for the BAF model is assessed using the same metrics as for the Abstract Argumentation (AA) model. The results reveal how well the Random Forest model classifies instances into the different BAF classes, '
                'such as Support and Neither.']),
        html.P(['By evaluating these results, we can compare the effectiveness of the Random Forest model across different Argumentation Frameworks. This comparison helps in understanding how the model’s performance varies with different types of '
                'argumentation relationships and contributes to selecting the most suitable model for the specific application.']),
        

        html.H4(['3.2-Extraction and visualisation']),
        html.P(['After training and evaluating various machine learning models, the next step in the project involves the systematic extraction of relevant data from the original dataset. This extraction process is implemented using a Jupyter notebook '
                'program and follows a detailed, multi-step procedure designed to ensure accuracy and relevance in analyzing the relationships between arguments.']),
        html.P(['The first step is the random argument selection. The program initiates the process by selecting a random argument from the original dataset. Before proceeding with the selected argument, the program checks if the topic associated with '
                'this argument is present in the dataset. If the topic is absent or if the argument is deemed trivial or irrelevant (e.g., statements related to general politeness, filler content, or off-topic remarks) and labeled with “Neither”, the '
                'argument is disregarded. This filtering step ensures that only meaningful and contextually significant arguments are considered for further analysis.']),
        html.P(['After identifying a relevant argument, the next step involves selecting a context of 32 other arguments (like in the M-Arg research) surrounding the chosen argument. This context provides a snapshot of the discussion, capturing the flow '
                'and dynamics of the debate. The context is carefully selected to include arguments that precede and follow the chosen argument. This balanced approach ensures that the context provides a comprehensive view, reflecting both the buildup '
                'to and the aftermath of the argument. The 32-argument context is an optimal size, large enough to capture a significant portion of the debate while remaining manageable for analysis.']),
        html.P(['Within the selected context, the program randomly selects a second argument, it will be opposed to the first one selected earlier. This second argument is critical for the next phase of the process, as it serves as the counterpart to the '
                'first argument, representing the potential relationship between the two. The selection of the second argument is not entirely random; it is influenced by the relevance and positioning of the argument within the context. This ensures that '
                'the relationship between the two arguments is likely to be meaningful and reflective of the actual dynamics of the debate.']),
        html.P(['Once the two arguments are selected, the trained machine learning model is applied to predict the relationship between them. This step leverages the capabilities of the previously trained and evaluated models to classify the relationship '
                'accurately. The model uses all the knowledge it learned in its training to predict the nature of the relationship. Depending on the argumentation framework (AA or BAF), the relationship could be classified as an Attack, Support, or '
                'Neither.']),
        html.P(['The results of the relationship predictions are compiled into a comprehensive file. This file consolidates all relevant data, including the original arguments, the context, and the predicted relationships. The compiled file serves as a '
                'detailed record of the analysis, providing a clear and organized view of the argument relationships within the dataset. This file can be used for further analysis, visualization, and presentation of the results.']),
        html.P(['This systematic extraction process ensures that the analysis is thorough, relevant, and reflective of the actual dynamics within the dataset. By carefully selecting arguments, context, and relationships, the process leverages the '
                'strengths of the trained machine learning models to provide valuable insights into the structure and flow of the debates.']),
        html.P(['The extraction and analysis process marks a significant advancement in the project, enabling a deeper understanding of the argumentation within the dataset. The resulting data file serves as a robust resource for further exploration and '
                'contributes to the broader field of argumentation mining.']),
        html.P(['This phase of the internship marked a significant step forward in the field of argumentation mining, combining advanced machine learning techniques with the theoretical foundations of argumentation frameworks. The AI system developed '
                'during this phase not only contributes to the academic understanding of debate analysis but also provides practical tools for researchers and practitioners in the field.']),






        html.H2(['4-Start of the GPT explanation']),
        html.P(['n the previous section, the focus was on identifying the type of relationship between two arguments. However, we encountered a significant challenge: all the lines in Figure 25 were marked with the same default “relation gold reason”. '
                'This issue arose because ML model cannot create original made text to explain its prediction. To address this challenge, we developed a new program named “explanation.py”',
                html.A(' (github : python/explanation.py) ', href='https://github.com/Robin-Chavigny/argumentation-analysis/blob/main/python/explanation.py',target="_blank"),
                ', which leverages the capabilities of the GPT-4 model. This program was specifically designed to provide detailed explanations for the identified relationships between arguments, thereby enhancing the model’s ability to handle complex '
                'tasks and improving the accuracy of predictions.']),
        

        html.H4(['4.1-How it work/ definition']),
        html.P(['GPT-4 is a state-of-the-art language model developed by OpenAI, renowned for its ability to understand and generate human-like text based on the input it receives. Trained on a vast and diverse dataset that includes text from books, '
                'articles, websites, and various other sources, GPT-4 has not only learned grammar and factual information but has also developed advanced reasoning abilities and contextual understanding.']),
        html.P(['It employs a transformer architecture characterized by multiple layers of attention mechanisms and feedforward neural networks. This architecture enables the model to process input text in parallel, making it highly efficient in '
                'understanding long-range dependencies within the text. By processing tokens in context, GPT-4 considers surrounding text to grasp the meaning and intent behind each token. This deep contextual comprehension allows the model to generate '
                'responses that are coherent, contextually relevant, and aligned with human-like reasoning.']),
        html.P(['When generating text, GPT-4 predicts the next token in a sequence based on the patterns and knowledge it has acquired during training. This iterative prediction process enables the model to produce complete sentences, paragraphs, or '
                'even more extended pieces of text, making it suitable for a wide range of applications.']),
        html.P(['In our project, GPT-4 was employed to enhance the analysis of argument relationships by providing detailed explanations for the relationships identified by the ML models. The first step involved importing the dataset previously processed '
                'by the machine learning models, ensuring that GPT-4 would have the necessary information for generating explanations.']),
        html.P(['After importing the dataset, we carefully selected various arguments from the existing data and fed them into the GPT-4 model. To guide GPT-4 effectively, a prompt was crafted to clearly outline the task and the context in which it was '
                'to operate. The prompt used is: ”You will be given two arguments, the context in which these arguments are taking place, and the relation they are in. Your goal is to explain the type of relation.”']),
        html.P(['This prompt was designed to ensure GPT-4 understood the context and the relationships between arguments, enabling it to generate explanations that are both accurate and contextually relevant.']),
        html.P(['By instructing GPT-4 to explain the relationship types based on the provided context, the model was able to overcome some of the limitations encountered with previous machine learning models. The explanations generated by GPT-4 offered '
                'richer insights and more nuanced interpretations of the argument relationships, adding depth to the analysis.']),
        html.P(['This approach not only improved the accuracy of the relationship analysis but also provided a clearer understanding of how and why certain relationships were classified in a specific way. The use of GPT-4 in this context allowed for a '
                'more comprehensive interpretation of the data, ultimately enhancing the quality of the overall analysis.']),

        html.H4(['4.2-Results']),
        html.P(['Once GPT-4 generates the desired output, the results, initially in the form of tokens, are converted back into human-readable text. This conversion ensures that the output is suitable for various applications, such as chatbots, content '
                'generation, and language translation. The generated explanations are then compiled into a new file that preserves all previously included information while optimizing space usage by removing unnecessary context.']),
        html.P(['The newly created file, enriched with detailed explanations of argument relationships, is then uploaded to the web interface for visualization. This integration enhances the clarity and depth of the displayed data, allowing users to '
                'interact with and better understand the argument relationships. By providing more comprehensive and intelligible information, this added layer of detail significantly improves the overall user experience.']),
        html.P(['The use of GPT-4 in “explanation.py” addresses the issue of uniform relationship labeling by providing more precise and varied explanations. This improvement leads to a more accurate representation of the relationships between arguments. '
                'The detailed explanations generated by GPT-4 offer richer insights into the nature of argument relationships, helping users to better understand the dynamics of the debates. The integration of these explanations into the web interface '
                'provides users with a more interactive and engaging experience, as they can now explore the relationships between arguments with greater clarity and depth.']),
        html.P(['The development and integration of “explanation.py” represent a significant advancement in our project. By leveraging GPT-4’s advanced capabilities, we have addressed the limitations of previous models, providing more accurate, detailed, '
                'and contextually relevant explanations of argument relationships. This enhancement not only improves the accuracy of our analysis but also enriches the user experience, making the web interface a more powerful tool for exploring and '
                'understanding argumentation frameworks.']),






        html.H2(['5-Start of the web interface']),
        html.P(['To provide a clearer visualization of my work, I was tasked with developing a web interface to showcase all my achievements during the internship. Simultaneously, I was assigned to present on “Demonstrating PyArg 2.0”',
                html.A('[5]', href='https://ceur-ws.org/Vol-3546/paper14.pdf',target="_blank"),
                '[5]. The PyArg 2.0 demonstration website offers an excellent representation of argumentation frameworks, which I decided to use as the foundation for my own web interface.']),
        html.P(['This website is structured into three main sections:']),
        html.Ul([html.Li([html.Strong(['Presentation section : ']),
                          'his section give an overview of the internship. It provides a comprehensive summary of the goals, methodologies, and overall experience during my internship. It serves as an introduction to the broader context of my work. It '
                          'also contain theoretical and graphical results. This includes detailed explanations, graphical representations, and analysis of various argumentation models and datasets I worked with. Moreover this page contain all the '
                          'PowerPoint presentations I delivered during the internship, covering both bi-weekly updates and broader research topics. These presentations provide additional context and support for the findings and methodologies discussed '
                          'in the other parts of the website.']),
                 html.Li([html.Strong(['Visualization section : ']),
                          'This section is designed to allow users to engage directly with the data and models I developed. Users can explore different argumentation frameworks, test various scenarios, and visualize the results in real-time. The ' 
                          'interactive nature of this section makes it a key component of the website, demonstrating the practical applications of my research. Leveraging the foundation provided by the PyArg 2.0 website, I implemented similar tools and '
                          'interfaces that allow users to interact with']),
                 html.Li([html.Strong(['Contact section : ']),
                          'The final section of the website includes my contact details, providing a way for visitors to reach out for further information, collaboration, or discussion. This section personalizes the website and connects the digital '
                          'presentation of my work with the human element behind it.'])]),
        

        html.H4(['5.1-First functionality']),
        html.P(['The Visualization page is designed with a user-friendly interface, divided into two main sections. On the left side of the window, users will find a dropdown menu for selecting various Argumentation Frameworks (AFs) they wish to explore, '
                'accompanied by explanatory text, based on the previous GPT-4 file, and several interactive functionalities. On the right side, the display window allows users to visualize the results in a dynamic and detailed manner.']),
        html.P(['The first results I aimed to display on the website were those derived from the audio transcripts of the debates. To achieve this, I strategically divided the “full data processing.csv” file by topic, offering a clearer and more structured '
                'view of the different arguments presented during the debates.']),

        html.H5(['5.1.1-Visualization Spaces for Argumentation Models']),
        html.P(['I created two distinct visualization spaces corresponding to the two argumentation models we used: Abstract Argumentation Framework (AA) and Bipolar Argumentation Framework (BAF).']),
        html.Ul([html.Li([html.Strong(['Choose a Topic : ']),
                          html.P(['For both models, a dropdown menu is provided for users to select a specific topic. Once a topic is selected, it is displayed below the menu for easy reference. Additionally, a toggle button appears, offering users the '
                                  'option to view either “All” the arguments in the model or only the “Colored” arguments, which represent those involved in relationships. Arguments not in any relationship are displayed in gray, while arguments in '
                                  'relationships are color-coded, with each speaker assigned a unique color. In the AA model, Non-attack relationships are not explicitly shown, as their absence implicitly represents them. Similarly, in the BAF model, '
                                  'Neither relationships are not displayed, simplifying the visualization']),
                         html.P(['In the BAF model, checkboxes are also available, allowing users to choose whether they want to display Attack relationships, Support relationships, or both simultaneously, providing flexibility in how the data is '
                                 'visualized.'])]),
                 html.Li([html.P(['Machine Learning : ']),
                          html.P(['he dataset, created by the various ML model, contains 100 different relationships between arguments for each file. To enhance user experience and clarity, we have implemented a modifiable scale that allows users to '
                                  'adjust the number of relationships displayed on the screen.']),
                         html.P(['By allowing users to control the number of displayed relationships, the interface improves the clarity and manageability of the data. This feature helps users focus on specific subsets of relationships without being '
                                 'overwhelmed by the full dataset. Users can choose the number of relationships they wish to view at any given time. This option is provided through a scalable interface, which can be adjusted according to user preferences. '
                                 'The web interface facilitates easy navigation and interaction with the data, enabling users to explore and analyze the argument relationships more effectively. Overall, this approach ensures that users can access and '
                                 'review the argument relationships in a flexible and user-friendly manner, enhancing the overall usability of the web interface.'])]),
                 html.Li([html.Strong(['Generating and Displaying Argumentation Frameworks : ']),
                          'o facilitate the visualization of argumentation frameworks, we developed a function named “generate abstract argumentation framework”, (example function from the AA page). This function reads the selected topic’s data file and '
                          'converts it into an argumentation framework, consisting of arguments and their relationships. On the display window, relationships between arguments are visualized as arrows, where an arrow from argument A to argument B indicates '
                          'that A attacks (or supports) B. Arguments are color-coded to represent their respective speakers, and the names of the speakers are displayed below the window in corresponding colors. When users click on an argument within the '
                          'visualization, an explanation section appears on the Explanation part on the left side. This section details all the relationships involving that argument, including explanations from the dataset, thanks to the “display click '
                          'data”. Users can also click on specific relationships to view explanations related to that particular interaction.']),
                 html.Li([html.Strong(['Additional Functionalities : ']),
                          html.P(['To enhance user experience and functionality, we added two additional features to the visualization page:']),
                          html.Ul([html.Li([html.Strong(['Download Functionality : ']),
                                            'Users can download the currently displayed argumentation framework as a file. This feature allows for easy sharing and further analysis outside the web interface.']),
                                 html.Li([html.Strong(['Upload Functionality : ']),
                                          'Users also have the option to upload their own argumentation framework files from their computer. This functionality supports the exploration of custom frameworks, making the tool versatile for different use '
                                          'cases.'])])
                        ])
        ]),
        html.P(['These functionalities ensure that the website is not just a static display of results but a dynamic and interactive tool for exploring and analyzing argumentation frameworks in a detailed and user-friendly manner.']),


        html.H4(['Evaluation part']),
        html.P(['The second part of the website is the Evaluation section. This section is crucial for analyzing and determining the admissibility of arguments within the current argumentation framework, based on various semantics. The primary goal here '
                'is to identify and select the arguments that are considered “admissible“ according to specific criteria. An argument is considered admissible if it meets the criteria set by a particular semantic. In this context, the Evaluation section '
                'explores three main semantics: Grounded, Completed, and Restrained semantic. Users can choose the desired semantic for evaluation using a dropdown menu. Once selected, the system will analyze the argumentation framework based on the '
                'chosen semantic criteria. The system will then display only the arguments that are considered admissible according to the selected semantic. This process allows users to visually identify the admissible arguments within the framework. '
                'Similar to the Visualization section, users can interact with the arguments by clicking on them to view detailed explanations and relationships. This interaction is particularly useful in understanding why certain arguments are '
                'deemed admissible or inadmissible under the chosen semantic.']),
        html.P(['The Evaluation section, with its focus on admissibility and semantics, provides a powerful mechanism for analyzing argumentation frameworks. It allows users to delve into the intricacies of argument evaluation, offering both predefined '
                'and customizable options for a comprehensive analysis.']),






        html.H2(['6-Heroku']),
        html.P((['The final objective of our project was to deploy the web interface online, and we chose Heroku as the platform to achieve this. Heroku is a cloud computing platform designed to simplify the deployment, management, and scaling of web '
                 'and backend applications. As a Platform as a Service (PaaS) solution, Heroku provides a comprehensive environment for developing, running, and managing applications without the need to directly manage underlying infrastructure such as '
                 'servers, storage, and networks.'])),
         html.P(['Heroku’s key advantage is its streamlined deployment process, making it an ideal choice for projects like ours. It offers a user-friendly environment where developers can focus on coding and application logic, while Heroku handles the '
                 'complexities of infrastructure management. This allows for efficient and hassle-free deployment, especially for teams that want to deploy and scale applications quickly.']),
        html.P(['Heroku is fully compatible with Git, which is essential for streamlined deployment workflows. To deploy the application, we use simple Git commands, such as “git push heroku main”. This command pushes the latest version of the code to '
                'Heroku, triggering an automatic build and deployment process. Once the code is pushed to Heroku, the platform automatically detects the necessary environment (e.g., Python, Node.js, Ruby) and sets up the appropriate environment for the '
                'application.']),
        html.P(['After the code is pushed, Heroku’s build system compiles the application and installs dependencies as specified in the “requirements.txt” file (for Python applications). Heroku then deploys the application, making it accessible via a '
                'unique URL. This process ensures that the application is up and running with minimal manual intervention.']),
        html.P(['Heroku provides integrated tools for managing and monitoring the application. For example, “heroku logs” is a command that allows developers to view real-time logs, helping them monitor the application’s performance, identify errors, and '
                'troubleshoot issues. Heroku’s dashboard also offers visual insights into application performance, including memory usage, response times, and the number of active connections. These tools are crucial for maintaining the application’s '
                'health and ensuring a smooth user experience.']),
        html.P(['Heroku supports CI/CD pipelines, which automate the testing and deployment process. This ensures that every change made to the code is tested and deployed automatically, reducing the risk of errors and making the development process more '
                'efficient. By integrating with popular CI/CD tools like GitHub Actions, CircleCI, or Jenkins, Heroku allows developers to maintain a consistent and reliable deployment process, ensuring that new features and updates are rolled out '
                'seamlessly.']),
        html.P(['Security is a critical aspect of any web application, and Heroku implements robust security measures to safeguard applications and data. Heroku complies with industry-standard security certifications and regulations, such as the General '
                'Data Protection Regulation (GDPR). This ensures that the data processed and stored within the application is protected against unauthorized access and breaches. Heroku also offers automated backups, SSL encryption, and other security '
                'features that provide additional layers of protection for the application.']),
        html.P(['By leveraging Heroku’s platform, we were able to deploy our web interface efficiently and effectively. Heroku’s compatibility with Git, combined with its automated build and deployment process, allowed us to focus on developing the '
                'application without worrying about the complexities of infrastructure management. The integrated management and monitoring tools provided valuable insights into the application’s performance, while the CI/CD support ensured a smooth '
                'and consistent deployment workflow.']),
        html.P(['Heroku’s robust security measures further reinforced our decision, as they provided peace of mind that the application and its data were well-protected. Overall, Heroku proved to be a reliable and powerful platform for deploying and '
                'managing our web interface, making it an excellent choice for our project’s needs.']),






        html.H2(['7-Oher work/ presentation']),
        html.P(['Throughout the duration of my internship, I was tasked with researching various topics relevant to my main project. These presentations were organized into two distinct groups. The first group consisted of bi-weekly presentations with '
                'my tutor. Every two weeks, usually on Wednesdays, I was required to present theoretical research on subjects that would later be implemented in the main project, as well as to report on the progress made since the previous meeting.']),
        html.P(['The second group involved presenting broader topics to the entire research group within the laboratory. These presentations provided an overview of more general fields of study and facilitated knowledge sharing among the researchers.']),
        html.A([html.Img(src='/assets/7-Other work/sus.png', style={'margin-bottom' : '15px'})], href='https://docs.google.com/presentation/d/1TXvdsbJ0PBYPrSSD9ZK097Q6sED7aENcUBrao41oy5Q/edit#slide=id.g206563da1c8_0_1',target="_blank"),
        html.P(['On June 19th, I presented the article titled “Misguided by research — The two dimensions of SUS” by George MELISSOURGOS ',
                html.A('[6]', href='https://medium.com/@geormelissourgos/leveraging-the-full-potential-of-the-sus-the-two-dimensions-b5846facec3',target="_blank"),
                '. The presentation focused on the System Usability Scale (SUS) and its upgraded version, the System Usability and Learnability Scale (SULS). These scales are used for evaluating argumentation systems by providing measures of usability '
                'and learnability.']),
        html.P(['The SUS is a widely used ten-item Likert scale that captures users’ subjective assessments of the usability of a system. It provides a global view of how users perceive the ease of use and overall effectiveness of the system. In '
                'contrast, the SULS extends this evaluation by incorporating learnability, addressing both the usability and the ease with which users can learn to use the system effectively.',
                html.Img(src='/assets/7-Other work/sus_ex.png',style={'width':'40%'})]),
        html.P(['Usability can be measured through various aspects such as effectiveness, which assesses whether users can successfully achieve their objectives; efficiency, which evaluates the effort and resources expended to achieve those objectives; '
                'and satisfaction, which gauges the overall user experience. The System Usability and Learnability Scale (SULS) builds on the System Usability Scale (SUS) by dividing the ten questions into two categories: usability and learnability. '
                'Specifically, the 4th and 10th questions of the SUS are designated as learnability questions in the SULS. This division allows for a more nuanced benchmark of system performance, providing deeper insights into both usability and the ease '
                'of learning, thereby helping to identify and address user struggles more effectively in future system designs.']),
        html.A([html.Img(src='/assets/7-Other work/analogical.png')], href='https://docs.google.com/presentation/d/1bSwaIrm90EFR1jriAMNiQa0PQ5hGYC1zXHboal2hrts/edit#slide=id.g11f682941b8_0_111',target="_blank"),
        html.P(['On July 3rd, I presented the article titled “Doing Analogical Reasoning in Dynamic Assumption-based Argumentation Frameworks”',
                html.A('[7]', href='https://ieeexplore.ieee.org/document/10098089',target="_blank"),
                '. Analogical reasoning involves drawing conclusions by comparing two states of affairs: the source and the '
                'target. While analogical arguments are not deductively valid, they can provide highly probable conclusions, which can be especially useful for understanding new or unclear situations. This process involves transferring knowledge from a '
                'familiar case (the source) to an unfamiliar one (the target). To justify the validity of an analogical argument, it is crucial to demonstrate the similarity between the known and unknown cases. This similarity can be assessed through '
                'the presence of specific homomorphisms between the structures of the two cases. By quantifying this similarity, we can apply the conclusions drawn from the known case to infer conclusions about the unknown case, thereby facilitating the '
                'understanding and resolution of novel situations.']),
        html.A([html.Img(src='/assets/7-Other work/lang.png')], href='https://docs.google.com/presentation/d/1iN-g7hHXjdHHdcNTG4upTttXPzb_Ck8W2-GQ8JYw_d8/edit#slide=id.p',target="_blank"),
        html.P(['On July 11th, I participated in a multi-speaker presentation on the “LangChain AI Handbook” by James Briggs and Francisco Ingham. My focus was on Chapter 5, which covers “Retrieval Augmentation”',
                html.A('[8]', href='https://www.pinecone.io/learn/series/langchain/',target="_blank"),
                '. Retrieval Augmentation addresses a significant limitation of Large Language Models (LLMs): their data freshness problem. LLMs are constrained by the static nature of their training data, which means they lack knowledge about recent '
                'events and developments. Retrieval Augmentation mitigates this issue by enabling the retrieval of relevant information from an external knowledge base, which is then provided to the LLM. To build an effective knowledge base, the chapter '
                'utilizes a subset of Wikipedia.']),
        html.P(['To store the data, we process text chunks by encoding each one into vector embeddings. This process translates human-readable text into a format that is readable by AI, allowing for more dynamic and up-to-date responses from the LLM.',
                html.Img(src='/assets/7-Other work/embedding.png')]),
        html.P(['The embeddings created from the text chunks are then stored in a vector database. This database enables us to find text chunks with similar meanings by calculating the distance between embeddings in vector space. The distance measurement '
                'allows us to identify and retrieve text chunks that are semantically similar, even if they are expressed in different words or formats. This approach enhances the LLM’s ability to access relevant and contextually appropriate information '
                'from the external knowledge base, improving the overall accuracy and relevance of its responses.',
                html.Img(src='/assets/7-Other work/vector_kb.png')]),
        html.P(['The vector database serves as a scalable knowledge base that enables efficient searching of similar embeddings across billions of records. It facilitates the management of our knowledge base by allowing us to add, update, or remove '
                'records as needed. Additionally, the database supports various functionalities such as filtering, which enhances the precision of information retrieval.']),
        html.P(['To further improve trust in the answers provided by the system, incorporating citations into the responses is an effective strategy. Citations enable users to trace the origin of the information, providing transparency and allowing '
                'users to verify the sources from which the data is derived. This practice enhances the credibility and reliability of the responses generated by the system.']),
        html.A([html.Img(src='/assets/7-Other work/proba.png'),], href='https://docs.google.com/presentation/d/1NqHu-qsfMojsFL_kgPZOY0p688W46p5F5Z0QbkhRUEo/edit#slide=id.g124c66b833e_2_32',target="_blank"),
        html.P(['On August 8th, I presented the article titled “Towards (Probabilistic) Argumentation for Jury-based Dispute Resolution”',
                html.A('[9]', href='http://cs.ait.ac.th/~dung/Site/Publications_files/ProbabilisticArg.pdf',target="_blank"),
                '. This paper explores the application of argumentation frameworks in the context of jury-based dispute resolution, focusing on the integration of probabilistic reasoning.']),
        html.P(['The article investigates how argumentation can be used to model and analyze the decision-making process in jury-based systems. The focus is on developing a formal framework that allows for the representation and evaluation of '
                'conflicting arguments, incorporating probabilistic elements to account for uncertainty in evidence and argument strength.']),
        html.P(['The key contribution of the article is the introduction of a probabilistic dimension to traditional argumentation frameworks. This enhancement allows for a more nuanced analysis of arguments, reflecting the varying degrees of '
                'confidence that jurors may have in different pieces of evidence or argument chains.']),
        html.P(['The concepts presented in this article are relevant to the broader research on argumentation frameworks, particularly in how they can be applied to real-world scenarios like legal decision-making. The probabilistic approach aligns with '
                'the need to handle uncertainty and variability in complex argumentative contexts, similar to the challenges addressed in our project.']),






        html.H2(['8-Conclusion']),
        html.P(['My internship at the Japan Advanced Institute of Science and Technology (JAIST) was an incredibly enriching experience, providing me with deep insights into the fields of artificial intelligence (AI) and argumentation frameworks. Over '
                'the course of several months, I engaged in various tasks that not only expanded my technical knowledge but also contributed significantly to the development and deployment of an advanced AI system aimed at analyzing and explaining '
                'argumentation within debate transcripts.']),
        html.P(['The initial phase of my internship focused on the implementation and evaluation of several machine learning models tailored to different argumentation frameworks. I explored a range of algorithms, including Support Vector Machines '
                '(SVM), Decision Trees, and Random Forests, each chosen for its potential to handle the complexities of argumentation data. Through meticulous data preprocessing and model training, I gained a thorough understanding of how each model '
                'performed under different conditions.']),
        html.P(['Performance evaluation was a critical aspect of this phase. By employing techniques such as k-fold crossvalidation, I was able to rigorously test the models and identify the most effective ones for our objectives. This process not only '
                'highlighted the strengths and limitations of each approach but also provided insights into selecting the most appropriate kernels and parameters for optimal performance. The knowledge gained here was instrumental in building a robust '
                'AI system capable of accurately identifying and classifying arguments within debate transcripts.']),
        html.P(['A key component of the project was the integration of the GPT-4 model to enhance the system’s ability to generate explanations for the identified argument relationships. This involved taking the outputs of the machine learning models and '
                'transforming them into comprehensible text that could be easily understood by users. The implementation of GPT-4 allowed us to bridge the gap between complex AI-generated data and user-friendly explanations, significantly improving the '
                'clarity and usability of the system.']),
        html.P(['The integration of these explanations into the web interface was a major milestone. By enabling users to interact with the data and gain deeper insights into the argument relationships, we created a more engaging and informative user '
                'experience. This enhancement not only added value to the AI system but also made it more accessible to a broader audience, including those without a deep technical background.']),
        html.P(['The successful deployment of our web interface on Heroku marked another significant achievement of the internship. Heroku, with its robust platform, facilitated the seamless deployment and management of the application, allowing us to '
                'make the AI system accessible online. The platform’s integration with Git and support for continuous integration ensured a smooth and efficient deployment process, while its comprehensive security measures provided confidence that the '
                'application was well-protected.']),
        html.P(['The ability to deploy the system online meant that it could reach a wider audience, furthering its impact and usefulness. Heroku’s tools for monitoring and managing the application also allowed us to maintain high performance and '
                'reliability, ensuring that users could depend on the system for accurate and timely analysis.']),
        html.P(['Throughout the internship, I also engaged in research on relevant topics, including system usability scales and analogical reasoning within argumentation frameworks. These research efforts culminated in presentations that not only '
                'broadened my understanding but also contributed to the ongoing discussions within the research group. Presenting my findings allowed me to refine my communication skills and ensured that my work had a tangible impact on the team’s '
                'collective knowledge and progress.']),
        html.P(['In conclusion, this internship at JAIST has been an invaluable experience that has significantly deepened my understanding of AI, machine learning, and argumentation frameworks. It provided me with hands-on experience in model '
                'development, data processing, explanation generation, and system deployment. The skills and knowledge I acquired during this period have prepared me for future challenges and opportunities in the dynamic field of AI and beyond. I am '
                'confident that the experience and insights gained will serve as a strong foundation for my continued growth and success in this area.']),






        html.H2(['9-References']),
        html.P(['[1] P. M. Dung, "On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games", Artificial Intelligence, vol. 77, issue. 2, pp. 321–357, 1995, ',
                html.A('link.', href='https://pdf.sciencedirectassets.com/271585/1-s2.0-S0004370200X00100/1-s2.0-000437029400041X/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCqVmF3t%2FQ5g1VtYU2i9iVyVPhLVUZ4GwIsZDyrCLIXMgIgL6l68ZpAW61pjGCFw9gvgSCgDBW3WQKClxiJPqHCqMsqswUIHhAFGgwwNTkwMDM1NDY4NjUiDJnZOxjhVA79n2xlhCqQBRaL%2B3LWT9J7ptziYkrCkOp4P3yCQIuH8UyfT9ielATYjYwXqAfSm52uIglvhJqEOrnjEAT%2BFK6kQY69yswEieaYonRsDtRhP6xsVuyRmy4I0puBa3MyGSdW%2BSRHKsmo2GYO%2BiZeKuESrF9RrXLzP1pXUQiKxVLH4SPxxwhMLbDbsKOQBitDtnWhM%2BvByW6c5t5NADv7tX8Gtk3jYhSkzxfj%2FFK7R45BQ%2FZZGfW7kyTMFodhfsGIDV92nq8tYwLHimadVuB%2FPyqKQ%2FR9K3m5RJllkB%2BM0kwThDm4ZscEfl5bpJL%2F5kaVhrV17USYLKCaAi%2BwjZn%2FG8N6AjUqZpfRaBk5XeSmZQPOu8ObJKiNCdBVCXna152xb3KNNhH30uOX%2FMv34NNCmSglftTiOz76hzwDGqaIuHkV58lDPKGUuMrWwnxGrofVhW8jIGpJfzNfeCg2lrI2s6SOrJAqRUZW1CUyrNSbNSbzdNz6hthrS1PyjwLk7JPYyutHwhcs4oU3IB4aA4mMxrhde8wmZBUxEuUXIlSTfeyNEcYLtZjGcm6zUrj8FO05lIC7hizM9%2FV%2FReAVozzLipIp6TL%2Bvn0eIyZkw0bxww%2FhKdrqOQWC9Pc5xBtk%2F7w3JWEEyMwLMN8%2BZpPPcVDvsB2C%2B8fCBdgrjyHPInEhU6Y%2BFr5hQLpZbODmJ9x%2BpCf2nbxW9Xi1EeK71whgMdeI8%2BiDc1j%2Fiz%2BukuCc7m0beF78858TEfm1wZzXGwX%2Fgd2BV3S32%2BVexrJewOy%2FTHDuOL9T3zfIATlO7x93qpNpO6WKL2zZo6VHBBlVAhO2vjjf4cgM8%2FciDnsGF9zvfEWDdhvJyVsJjeqiFW8sIyI%2BjMU%2FZ9hFrTaw812EMLjAqbIGOrEBzYwKICAqiKrYpIA2wZhVIXyB9KINeDsxQPsRsSYLYMxXC2dmP9o2TGa43eSHiIbRVvbvP2L1cs8ur%2Fe5ev0NVgR1MiFk5j3pwmtPDtDS%2BdzwmoCjY6L22PASBqzrF9SpFindqUrBqYClBg3eiVIt7TkTnd8CdxbzGdZ2lN0ZOVRXH0rqY5MRIFDzRGy9qJZ0wXiBZEUG6gr7aAqWrPTTRkwSLn99aFFPgJL2S4z%2BilTw&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240519T211700Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY4QAJFMTT%2F20240519%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c0df67d844a0d0c046a960a6d3f2f8649c95eeeb40d1667fb1e85a4df79474cb&hash=a87607d56da2498c5ba797f1b6e8adda28029dafb4f0ad06a2ef3050de06c1e2&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=000437029400041X&tid=spdf-dbfb7159-3038-4bd8-85f7-69fd0dfd1242&sid=f5e835488af4354e196bed865e0db1c0e4dcgxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=04175d5658595102&rr=88671c7bfcaef6fa&cc=jp',target="_blank"),]),
        html.A([html.Img(src='/assets/9-References/dung.png'),], href='https://docs.google.com/presentation/d/1Gd4-CV5WjKMs4-XBuxJ5M0ZLoEVgVk_G/edit#slide=id.p1',target="_blank"),
        html.P(['[2] R. Mestre, R. Milicin, S.E. Middleton, M. Ryan, J. Zhu and T.J. Norman, "M-Arg: Multimodal Argument Mining Dataset for Political Debates with Audio and Transcripts", Proceedings of The 8th Workshop on Argument Mining, pp. 78–88, '
                'November 2021, ',
                html.A('https://aclanthology.org/2021.argmining-1.8.pdf.', href='https://aclanthology.org/2021.argmining-1.8.pdf',target="_blank"),
                ]),
        html.A([html.Img(src='/assets/9-References/marg.png'),], href='https://docs.google.com/presentation/d/1YlTziO5KjIpDY6pT3L0-MlkmVEYYRCfguoOWfUQWC5U/edit#slide=id.g708a6ee8a1_0_46',target="_blank"),
        html.P(['[3] P. Lertvittayakumjorn and F. Toni, "Argumentative Explanations for Pattern-based Text Classifier", Argument & Computation, vol. 14, no. 2, pp. 163–234, June 2023, doi: 10.3233/AAC-220004, ',
                html.A('https://content.iospress.com/articles/argument-and-computation/aac220004#ref018.', href='https://content.iospress.com/articles/argument-and-computation/aac220004#ref018',target="_blank")
                ]),
        html.A([html.Img(src='/assets/9-References/lev.png'),], href='https://docs.google.com/presentation/d/1bYmTDVWkTl5dOfiMxNzFPucefAYxzk1jIGsowm4B1Y0/edit#slide=id.p',target="_blank"),
        html.P(['[4] D. Odekerken, A. Borg and M. Berthold, "Demonstrating PyArg 2.", 7th Workshop on Advances in Argumentation in Artificial Intelligence, CEUR-WS.org, vol. 3546, paper. 14, November 2023, ',
                html.A('https://ceur-ws.org/Vol-3546/paper14.pdf.', href='https://ceur-ws.org/Vol-3546/paper14.pdf',target="_blank"),]),
        html.A([html.Img(src='/assets/9-References/pyarg.png'),], href='https://docs.google.com/presentation/d/1YlTziO5KjIpDY6pT3L0-MlkmVEYYRCfguoOWfUQWC5U/edit#slide=id.g2dbf2ba131f_0_299',target="_blank"),

        html.H2(['10-Internship presentation']),
        html.P(['Mi-Internship presentation :']),
        html.A([html.Img(src='/assets/10-Internship presentation/mi_internship.png'),], href='https://docs.google.com/presentation/d/1cQm1JuWbem_N-vhwT5iKUOw-8mH06PcQdPNcWaebytE/edit#slide=id.g2ba7dc93f75_0_0',target="_blank"),
        html.P(['Defense presentationb :']),
        html.A([html.Img(src='/assets/10-Internship presentation/defense.png'),], href='https://docs.google.com/presentation/d/1GrqavDwTV5Ro6hysghjavcROHwaxTSSnvn1lMcHYB0I/edit#slide=id.p',target="_blank"),
        
    ],className='page-text'),

], fluid=True,className='page')



