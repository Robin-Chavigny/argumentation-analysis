import base64
import json
from typing import List, Dict

import dash
import visdcc
from dash import html, callback, Input, Output, State, ALL, dcc, ctx, Dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
import pandas as pd
import io
import os

from py_arg.abstract_argumentation_classes.abstract_argumentation_framework import AbstractArgumentationFramework
from py_arg.generators.abstract_argumentation_framework_generators.abstract_argumentation_framework_generator import \
    AbstractArgumentationFrameworkGenerator
from py_arg.import_export.argumentation_framework_from_aspartix_format_reader import \
    ArgumentationFrameworkFromASPARTIXFormatReader
from py_arg.import_export.argumentation_framework_from_iccma23_format_reader import \
    ArgumentationFrameworkFromICCMA23FormatReader
from py_arg.import_export.argumentation_framework_from_json_reader import ArgumentationFrameworkFromJsonReader
from py_arg.import_export.argumentation_framework_from_trivial_graph_format_reader import \
    ArgumentationFrameworkFromTrivialGraphFormatReader
from py_arg.import_export.argumentation_framework_to_aspartix_format_writer import \
    ArgumentationFrameworkToASPARTIXFormatWriter
from py_arg.import_export.argumentation_framework_to_iccma23_format_writer import \
    ArgumentationFrameworkToICCMA23FormatWriter
from py_arg.import_export.argumentation_framework_to_json_writer import ArgumentationFrameworkToJSONWriter
from py_arg.import_export.argumentation_framework_to_trivial_graph_format_writer import \
    ArgumentationFrameworkToTrivialGraphFormatWriter
from py_arg_visualisation.functions.explanations_functions.explanation_function_options import \
    EXPLANATION_FUNCTION_OPTIONS
from py_arg_visualisation.functions.explanations_functions.get_af_explanations import \
    get_argumentation_framework_explanations
from py_arg_visualisation.functions.extensions_functions.get_accepted_arguments import get_accepted_arguments
from py_arg_visualisation.functions.extensions_functions.get_af_extensions import get_argumentation_framework_extensions
from py_arg_visualisation.functions.graph_data_functions.get_af_graph_data import get_argumentation_framework_graph_data
from py_arg_visualisation.functions.import_functions.read_argumentation_framework_functions import \
    read_argumentation_framework
import chardet
import random

random.seed(42)

dash.register_page(__name__, name='Visualise BAF', title='Visualise BAF')


# Create layout elements and compose them into the layout for this page.

def get_bipolar_setting_specification_div():
    return html.Div(children=[
        dcc.Store(id='selected-argument-store-bipolar'),
        dbc.Col([
            dbc.Row([dbc.Col([dbc.DropdownMenu(
                                label="Choose a Topic",
                                children=[
                                    dbc.DropdownMenuItem("Racism", id="racism-bipolar"),
                                    dbc.DropdownMenuItem("Economy", id="economy-bipolar"),
                                    dbc.DropdownMenuItem("Climate Change", id="climate-change-bipolar"),
                                    dbc.DropdownMenuItem("Supreme Court", id="supreme-court-bipolar"),
                                    dbc.DropdownMenuItem("Minimum Wage", id="minimum-wage-bipolar"),
                                    dbc.DropdownMenuItem("COVID", id="covid-bipolar"),
                                    dbc.DropdownMenuItem("Healthcare", id="healthcare-bipolar"),
                                    dbc.DropdownMenuItem("National Security", id="national-security-bipolar"),
                                    dbc.DropdownMenuItem("Why They Should Be Elected", id="why-they-should-be-elected-bipolar"),
                                    dbc.DropdownMenuItem("Democracy", id="democracy-bipolar"),
                                    dbc.DropdownMenuItem("Integrity", id="integrity-bipolar"),
                                ],
                                id="dropdown-menu-bipolar",
                                className="mb-2"
                                ),
                                html.Div(id='output-dropdown-bipolar')
                            ], width=4),
                     dbc.Col([dbc.DropdownMenu(
                                label="Machine Learning",
                                children=[
                                    dbc.DropdownMenuItem("SVM", id="svm"),
                                    dbc.DropdownMenuItem("Random Forest", id="random-forest"),
                                    dbc.DropdownMenuItem("Decision Tree", id="decision-tree"),
                                ],
                                id="dropdown-ml-bipolar",
                                className="mb-2"
                                ),
                                html.Div(id='output-dropdown-ml-bipolar')
                            ], width=4),
                     dbc.Col([dcc.Upload(dbc.Button('Upload AF', className='w-100'), id='upload-af-bipolar'),
                                html.Div(id='output-upload-bipolar')
                            ]),
                     ], className='mt-2'),
            dbc.Row([
                dbc.Col(
                    html.Div([
                        html.P('Type of argument visible:'),
                        dbc.Button('All', id='toggle-button-bipolar', n_clicks=0, className="mb-2", style={"background-color": "gray", "color": "white"})
                    ], id='toggle-container-bipolar', style={'display': 'none'})
                )
            ], className='mt-2'),
            dbc.Row([dbc.Col(id='slider-container-bipolar', 
                             children=[dcc.Slider( id='slider-bipolar', 
                                                  min=1, 
                                                  max=100, 
                                                  step=1, 
                                                  value=50, 
                                                  marks={i: str(i) for i in range(1, 101, 99)}
                                                ),
                                        html.Div(id='output-container-bipolar', 
                                                 style={'margin-top': '20px'}
                                                )
                                    ],
                            style={'display': 'none', 'margin-top': '20px'}
                        )   
                     ], className='mt-2'),
            dbc.Row([
                dbc.Col(dbc.Checklist(
                    id='checkbox',
                    options=[
                        {'label': 'Attack', 'value': 'attack'},
                        {'label': 'Support', 'value': 'support'}
                    ],
                    value=['attack'],  # Default selected values
                    inline=True  # To display options in a single line
                ), width=6),
                dbc.Col(html.Div(id='output-checkbox'), width=6)
            ], className="mt-4"),
            dbc.Row([dbc.Col(dbc.Button('Display', id='generate-random-af-button-bipolar', n_clicks=0,
                                        className='w-100')),
                     dcc.Store(id='generation-results-bipolar'),
                     ], className='mt-2'),
            dbc.Row([
                dbc.Col([
                    html.B('Arguments'),
                    dbc.Textarea(id='bipolar-arguments',
                                 placeholder='Add one argument per line. For example:\n A\n B\n C',
                                 value='', style={'height': '0px'})
                ]),
                dbc.Col([
                    html.B('Attacks'),
                    dbc.Textarea(id='bipolar-attacks',
                                 placeholder='Add one attack per line. For example: \n (A,B) \n (A,C) \n (C,B)',
                                 value='', style={'height': '0px'}),
                ])
            ], className='mt-22'),
            dbc.Row([
                dbc.InputGroup([
                    dbc.InputGroupText('Filename'),
                    dbc.Input(value='edited_af', id='22-af-filename'),
                    dbc.InputGroupText('.'),
                    dbc.Select(options=[{'label': extension, 'value': extension}
                                        for extension in ['JSON', 'TGF', 'APX', 'ICCMA23']],
                               value='JSON', id='22-af-extension'),
                    dbc.Button('Download', id='22-af-download-button'),
                ], className='mt-2'),
                dcc.Download(id='22-af-download')
            ]),
            dbc.Row([
                dbc.Col([
                    html.H1(["Explanation "], style={'margin-top':'50px', 'text-decoration': 'underline'}),
                    html.Div(id='node-click-message-bipolar')
                ])
            ])
        ])
    ])


def get_bipolar_evaluation_div():
    return html.Div([
        dbc.Col([
            
                dbc.Row([
                    dbc.Col(html.B('Semantics')),
                    dbc.Col(dbc.Select(options=[
                        {'label': 'Completed', 'value': 'Completed'},
                        {'label': 'Grounded', 'value': 'Grounded'},
                        {'label': 'Restrainted', 'value': 'Restrainted'},
                    ], value='Completed', id='bipolar-evaluation-semantics')),
                ]),
                dbc.Row([
                    dbc.Col(html.B('Evaluation strategy')),
                    dbc.Col(dbc.Select(
                        options=[
                            {'label': 'Credulous', 'value': 'Credulous'},
                            {'label': 'Skeptical', 'value': 'Skeptical'}
                        ], value='Credulous', id='bipolar-evaluation-strategy')),
                ]),
                dbc.Row(id='bipolar-evaluation'),
                dcc.Store(id='evaluation-results-bipolar'),
                dbc.Row([dbc.Col(dbc.Button('Display', id='generate-accept-af-button-bipolar', n_clicks=0, className='w-100')),], className='mt-2'),
        ])
    ])


def get_bipolar_explanation_div():
    return html.Div([
        dbc.Row([
            dbc.Col(html.B('Type')),
            dbc.Col(dbc.Select(options=[{'label': 'Acceptance', 'value': 'Acceptance'},
                                        {'label': 'Non-Acceptance', 'value': 'NonAcceptance'}],
                               value='Acceptance', id='bipolar-explanation-type'))]),
        dbc.Row([
            dbc.Col(html.B('Explanation function')),
            dbc.Col(dbc.Select(id='bipolar-explanation-function'))
        ]),
        dbc.Row(id='bipolar-explanation')
    ])


left_column = dbc.Col(
    dbc.Accordion([
        dbc.AccordionItem(get_bipolar_setting_specification_div(), title='Bipolar Argumentation Framework'),
        dbc.AccordionItem(get_bipolar_evaluation_div(), title='Evaluation', item_id='Evaluation'),
        
    ], id='bipolar-evaluation-accordion')
)
right_column = dbc.Col([
    dbc.Row([
        dbc.Card(visdcc.Network(data={'nodes': [], 'edges': []}, id='bipolar-argumentation-graph',
                                options={'height': '500px'}), body=True),
    ]),
    dbc.Row([
        html.Div(id='legend-colors-bipolar')
    ])
])
layout_abstract = dbc.Row([left_column, right_column])
layout = html.Div([html.H1(['Visualisation of Bipolar Argumentation Frameworks (BAF)'],style={'margin-top':'30px', 'margin-bottom':'30px', 'text-align': 'center', 'font-size': '45px'}), 
                html.A([html.P(['-> Abstract Argumentation Frameworks (AA)'],style={'margin-bottom':'15px'})], href='21-visualise-abstract', id='visualisation-link'),
                layout_abstract])



@callback(
    Output('output-dropdown-bipolar', 'children'),
    Output('output-dropdown-ml-bipolar', 'children'),
    Output('slider-container-bipolar', 'style'),
    [Input('racism-bipolar', 'n_clicks'),
     Input('economy-bipolar', 'n_clicks'),
     Input('climate-change-bipolar', 'n_clicks'),
     Input('supreme-court-bipolar', 'n_clicks'),
     Input('minimum-wage-bipolar', 'n_clicks'),
     Input('covid-bipolar', 'n_clicks'),
     Input('healthcare-bipolar', 'n_clicks'),
     Input('national-security-bipolar', 'n_clicks'),
     Input('why-they-should-be-elected-bipolar', 'n_clicks'),
     Input('democracy-bipolar', 'n_clicks'),
     Input('integrity-bipolar', 'n_clicks'),
     Input('svm', 'n_clicks'),
     Input('random-forest', 'n_clicks'),
     Input('decision-tree', 'n_clicks')],
    prevent_initial_call=True
)
def update_output_bipolar(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        return 'No topic selected', 'No ML selected'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    topic_dict = {
        "racism-bipolar": "Racism",
        "economy-bipolar": "Economy",
        "climate-change-bipolar": "Climate Change",
        "supreme-court-bipolar": "Supreme Court",
        "minimum-wage-bipolar": "Minimum Wage",
        "covid-bipolar": "COVID",
        "healthcare-bipolar": "Healthcare",
        "national-security-bipolar": "National Security",
        "why-they-should-be-elected-bipolar": "Why They Should Be Elected",
        "democracy-bipolar": "Democracy",
        "integrity-bipolar": "Integrity",
    }

    ml_dict = {
        "svm": "SVM",
        "random-forest": "Random Forest",
        "decision-tree": "Decision Tree",
    }

    if button_id in topic_dict:
        topic = topic_dict[button_id]
        ml = 'No ML selected'
        stl = {'display': 'none'}
    elif button_id in ml_dict:
        topic = 'No topic selected'
        ml = ml_dict[button_id]
        stl = {'display': 'block', 'margin-top': '20px'}
    else:
        topic = 'No topic selected'
        ml = 'No ML selected'
        stl = {'display': 'none'}

    return topic, ml, stl


@callback(
    Output('output-upload-bipolar', 'children'),
    Input('upload-af-bipolar', 'contents'),
    State('upload-af-bipolar', 'filename'),
    prevent_initial_call=True
)
def update_upload_bipolar(af_content: str, af_filename: str):
    if af_content is not None:
        return af_filename
    return 'No file selected'

@callback(
    Output('toggle-container-bipolar', 'style'),
    Input('output-dropdown-bipolar', 'children')
)
def display_toggle(topic:str):
    if topic=='No topic selected' or topic==None:
        return {'display': 'none'}
    return {'display': 'block'}

@callback(
    Output('toggle-button-bipolar', 'children'),
    Output('toggle-button-bipolar', 'style'),
    Input('toggle-button-bipolar', 'n_clicks')
)
def toggle_button(n_clicks):
    if n_clicks % 2 == 0:
        return 'All', {"background-color": "gray", "color": "white"}
    else:
        return 'Colored', {"background-color": "blue", "color": "white"}

# Définir le callback pour mettre à jour l'affichage de la valeur du slider
@callback(
    Output('output-container-bipolar', 'children'),
    [Input('slider-bipolar', 'value')]
)
def update_output_slider(value):
    return f'Vous avez sélectionné : {value}'

def replace_spaces(argument):
    return argument.replace(" ", "_").replace(",", ";")

prev_results = {'arguments':'','attacks':''}  

@callback(
    Output('generation-results-bipolar', 'data'),
    Output('generate-random-af-button-bipolar', 'n_clicks'),
    Output('upload-af-bipolar', 'contents'),
    Output('upload-af-bipolar', 'filename'),
    Input('generate-random-af-button-bipolar', 'n_clicks'),
    Input('upload-af-bipolar', 'contents'),
    State('upload-af-bipolar', 'filename'),
    State('output-dropdown-bipolar', 'children'),
    State('output-dropdown-ml-bipolar', 'children'),
    State('checkbox', 'value'),
    Input('slider-bipolar', 'value'),
    Input('toggle-button-bipolar', 'children'),
    prevent_initial_call=True
)
def generate_bipolar_argumentation_framework(_nr_of_clicks_random: int, af_content: str, af_filename: str, topic: str, ml: str, checkbox_values: list, value: int, toggle:str):
    """
    Generate a random AF after clicking the button and put the result in the text box.
    """
    global prev_results  # Utiliser la variable globale

    if _nr_of_clicks_random == 1:
        af_content=None
        af_filename=None
    if af_filename != None:
        if af_filename[-4:] == '.csv':
            if af_content.startswith("data:text/csv;base64,"):
                content_string = af_content[len("data:text/csv;base64,"):]
            decoded = base64.b64decode(content_string)
            encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary
            for encoding in encodings_to_try:
                try:
                    decoded_str = decoded.decode(encoding)
                    break  # Stop trying encodings once decoding succeeds
                except UnicodeDecodeError:
                    continue  # Try the next encoding if decoding fails

            # Handle if none of the encodings worked
            if 'decoded_str' not in locals():
                print("Unable to decode the data using any of the specified encodings.")
                decoded_str = None  # or handle the error appropriately
            lines = decoded_str.splitlines()
            data = [line.split('$,$') for line in lines]

            df = pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame(columns=data[0])

            l=[]
            h=[]
            for index, row in df.iterrows():
                sentence1 = row.iloc[4].replace(' ','_').replace(',',';')
                sentence2 = row.iloc[5].replace(' ','_').replace(',',';')

                if sentence1 not in l:
                    l.append(sentence1)
                if sentence2 not in l:
                    l.append(sentence2)
                
                if row.iloc[2] == 'Attack':
                    h.append(f'$A$({sentence1},{sentence2})')
                if row.iloc[2] == 'Support':
                    h.append(f'$S$({sentence1},{sentence2})')
            abstract_arguments_value = '$end$'.join((str(arg) for arg in l))
            abstract_attacks_value = '$end$'.join((str(defeat)for defeat in h) )

            results = {
                    'arguments': abstract_arguments_value,
                    'attacks': abstract_attacks_value
                }
            return results,0,af_content,af_filename

    elif dash.callback_context.triggered_id == 'slider-bipolar' or dash.callback_context.triggered_id == 'toggle-button-bipolar':
        return prev_results,0,af_content,af_filename


    elif dash.callback_context.triggered_id == 'generate-random-af-button-bipolar':
        _nr_of_clicks_random=0

        if topic != 'No topic selected':
            l=[]
            h=[]
            # Construire le chemin du fichier CSV de manière dynamique
            base_path = os.path.dirname(__file__)
            file_path = os.path.join(base_path, '..', 'data','us_debat', 'full_dataset_processing.csv')
            # Lire les données du fichier CSV en sautant la première ligne (l'entête)
            df = pd.read_csv(file_path, skiprows=0)

            for index, row in df.iterrows():
                if row.iloc[8]==topic:
                    # Extraire les éléments de la 5ème et 6ème colonne
                    argument_5 = row.iloc[4]
                    argument_6 = row.iloc[5]
                    # Remplacer les espaces par des tirets
                    argument_5 = replace_spaces(argument_5)
                    argument_6 = replace_spaces(argument_6)

                    # Vérifier si les éléments ne sont pas déjà présents dans la première liste de random_af
                    if toggle == 'All':
                        if argument_5 not in l:
                            l.append(argument_5)
                        if argument_6 not in l:
                            l.append(argument_6)
                    if toggle == 'Colored':
                        if row.iloc[2]=='Attack' and 'attack' in checkbox_values:
                            if argument_5 not in l:
                                l.append(argument_5)
                            if argument_6 not in l:
                                l.append(argument_6)
                        if row.iloc[2]=='Support' and 'support' in checkbox_values:
                            if argument_5 not in l:
                                l.append(argument_5)
                            if argument_6 not in l:
                                l.append(argument_6)
                    if row.iloc[2]=='Attack' and 'attack' in checkbox_values:
                        # Ajouter la relation entre les éléments à la deuxième liste de random_af
                        h.append(f'$A$({argument_5},{argument_6})')
                    if row.iloc[2]=='Support' and 'support' in checkbox_values:
                        # Ajouter la relation entre les éléments à la deuxième liste de random_af
                        h.append(f'$S$({argument_5},{argument_6})')

            # Suppose que random_af est un objet AbstractArgumentationFramework avec des attributs arguments et defeats
            abstract_arguments_value = '$end$'.join((str(arg) for arg in l))
            # Construction de la représentation des attaques en utilisant les éléments de defeats
            abstract_attacks_value = '$end$'.join((str(defeat)for defeat in h) )

            results = {
                'arguments': abstract_arguments_value,
                'attacks': abstract_attacks_value
            }
            prev_results = results
            return results,0,af_content,af_filename
        
        if ml == 'SVM':
            # Construire le chemin du fichier CSV de manière dynamique
            base_path = os.path.dirname(__file__)
            file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_svm_baf.csv')

            # Read the file content with multiple encodings
            encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

            for encoding in encodings_to_try:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        file_content = file.read()
                    break  # Stop trying encodings once reading succeeds
                except (UnicodeDecodeError, FileNotFoundError):
                    continue  # Try the next encoding if reading fails
                
            # Handle if none of the encodings worked or the file was not found
            if 'file_content' not in locals():
                print("Unable to read the data using any of the specified encodings or file not found.")
                file_content = None  # or handle the error appropriately

            if file_content:
                lines = file_content.splitlines()
                lines = lines[:value+1]
                data2 = [line.split('$,$') for line in lines]

                # Create a DataFrame
                df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
            else:
                print("Reading failed, DataFrame not created.")

            l=[]
            h=[]
            for index, row in df.iterrows():
                sentence1 = row.iloc[4].replace(' ','_').replace(',',';')
                sentence2 = row.iloc[5].replace(' ','_').replace(',',';')
                         
                if row.iloc[2] == 'Attack':
                    if 'attack' in checkbox_values:
                        h.append(f'$A$({sentence1},{sentence2})')
                        if sentence1 not in l:
                            l.append(sentence1)
                        if sentence2 not in l:
                            l.append(sentence2)
                if row.iloc[2] == 'Support':
                    if 'support' in checkbox_values:
                        h.append(f'$S$({sentence1},{sentence2})')
                        if sentence1 not in l:
                            l.append(sentence1)
                        if sentence2 not in l:
                            l.append(sentence2)
            abstract_arguments_value = '$end$'.join((str(arg) for arg in l))
            abstract_attacks_value = '$end$'.join((str(defeat)for defeat in h) )

            results = {
                    'arguments': abstract_arguments_value,
                    'attacks': abstract_attacks_value
                }
            prev_results = results
            return results,0,af_content,af_filename
        
        if ml == 'Random Forest':
            # Construire le chemin du fichier CSV de manière dynamique
            base_path = os.path.dirname(__file__)
            file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_forest_baf.csv')

            # Read the file content with multiple encodings
            encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

            for encoding in encodings_to_try:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        file_content = file.read()
                    break  # Stop trying encodings once reading succeeds
                except (UnicodeDecodeError, FileNotFoundError):
                    continue  # Try the next encoding if reading fails
                
            # Handle if none of the encodings worked or the file was not found
            if 'file_content' not in locals():
                print("Unable to read the data using any of the specified encodings or file not found.")
                file_content = None  # or handle the error appropriately

            if file_content:
                lines = file_content.splitlines()
                lines = lines[:value+1]
                data2 = [line.split('$,$') for line in lines]

                # Create a DataFrame
                df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
            else:
                print("Reading failed, DataFrame not created.")
            
            l=[]
            h=[]
            for index, row in df.iterrows():
                sentence1 = row.iloc[4].replace(' ','_').replace(',',';')
                sentence2 = row.iloc[5].replace(' ','_').replace(',',';')
                         
                if row.iloc[2] == 'Attack':
                    if 'attack' in checkbox_values:
                        h.append(f'$A$({sentence1},{sentence2})')
                        if sentence1 not in l:
                            l.append(sentence1)
                        if sentence2 not in l:
                            l.append(sentence2)
                if row.iloc[2] == 'Support':
                    if 'support' in checkbox_values:
                        h.append(f'$S$({sentence1},{sentence2})')
                        if sentence1 not in l:
                            l.append(sentence1)
                        if sentence2 not in l:
                            l.append(sentence2)
            abstract_arguments_value = '$end$'.join((str(arg) for arg in l))
            abstract_attacks_value = '$end$'.join((str(defeat)for defeat in h) )

            results = {
                    'arguments': abstract_arguments_value,
                    'attacks': abstract_attacks_value
                }
            prev_results = results
            return results,0,af_content,af_filename
                
        if ml == 'Decision Tree':
            # Construire le chemin du fichier CSV de manière dynamique
            base_path = os.path.dirname(__file__)
            file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_tree_baf.csv')

            # Read the file content with multiple encodings
            encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

            for encoding in encodings_to_try:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        file_content = file.read()
                    break  # Stop trying encodings once reading succeeds
                except (UnicodeDecodeError, FileNotFoundError):
                    continue  # Try the next encoding if reading fails
                
            # Handle if none of the encodings worked or the file was not found
            if 'file_content' not in locals():
                print("Unable to read the data using any of the specified encodings or file not found.")
                file_content = None  # or handle the error appropriately

            if file_content:
                lines = file_content.splitlines()
                lines = lines[:value+1]
                data2 = [line.split('$,$') for line in lines]

                # Create a DataFrame
                df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
            else:
                print("Reading failed, DataFrame not created.")

            l=[]
            h=[]
            for index, row in df.iterrows():
                sentence1 = row.iloc[4].replace(' ','_').replace(',',';')
                sentence2 = row.iloc[5].replace(' ','_').replace(',',';')
                         
                if row.iloc[2] == 'Attack':
                    if 'attack' in checkbox_values:
                        h.append(f'$A$({sentence1},{sentence2})')
                        if sentence1 not in l:
                            l.append(sentence1)
                        if sentence2 not in l:
                            l.append(sentence2)
                if row.iloc[2] == 'Support':
                    if 'support' in checkbox_values:
                        h.append(f'$S$({sentence1},{sentence2})')
                        if sentence1 not in l:
                            l.append(sentence1)
                        if sentence2 not in l:
                            l.append(sentence2)
            abstract_arguments_value = '$end$'.join((str(arg) for arg in l))
            abstract_attacks_value = '$end$'.join((str(defeat)for defeat in h) )

            results = {
                    'arguments': abstract_arguments_value,
                    'attacks': abstract_attacks_value
                }
            prev_results = results
            return results,0,af_content,af_filename

    return prev_results,0,af_content,af_filename


def replace_spaces2(argument):
    return argument.replace("_", " ").replace(";", ",")
def replace_fin(argument):
    return argument.replace("\n\n", "$end$")
def replace_mid(argument):
    return argument.replace(",", "$,$")
from py_arg.abstract_argumentation_classes.argument import Argument
from py_arg.abstract_argumentation_classes.defeat import Defeat

def generate_random_color(min_brightness=100):
    def is_bright(color):
        r, g, b = color
        # Calculer la luminosité
        brightness = (0.299 * r + 0.587 * g + 0.114 * b)
        return brightness >= min_brightness

    while True:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if is_bright(color):
            return "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
def add_different_color(colors):
    new_color = generate_random_color()
    while new_color in colors:
        new_color = generate_random_color()
    colors.append(new_color)
    return colors
def create_legend_colors(colors: list, speakers: list):
    elements = []
    for i in range(len(speakers)):
        elements.append(html.H3(speakers[i], style={'color': colors[i]}))
    return elements

@callback(
    Output('bipolar-argumentation-graph', 'data'),
    Output('legend-colors-bipolar', 'children'),
    Output('bipolar-arguments', 'value'),
    Output('bipolar-attacks', 'value'),

    Input('evaluation-results-bipolar', 'data'),
    Input('generation-results-bipolar', 'data'),
    Input('bipolar-arguments', 'value'),
    Input('bipolar-attacks', 'value'),
    Input('selected-argument-store-bipolar', 'data'),
    State('color-blind-mode', 'on'),
    State('output-dropdown-bipolar', 'children'),
    State('output-dropdown-ml-bipolar', 'children'),
    State('checkbox', 'value'),
    State('upload-af-bipolar', 'contents'),
    State('upload-af-bipolar', 'filename'),
    Input('slider-bipolar', 'value'),
    prevent_initial_call=True
)
def create_bipolar_argumentation_framework(evaluation_results, generation_results,
                                            arguments: str, attacks: str,
                                            selected_arguments: Dict[str, List[str]],
                                            color_blind_mode: bool, 
                                            topic: str, 
                                            ml: str,
                                            checkbox_values: list,
                                            af_content: str, af_filename: str,
                                            value: int):
    """
    Send the AF data to the graph for plotting.
    """
    
    trigger_id = ctx.triggered_id
        
    if trigger_id == 'evaluation-results-bipolar' and evaluation_results is not None:
        generation_results = None
        arguments = evaluation_results['arguments']
        attacks = evaluation_results['attacks']
    elif trigger_id == 'generation-results-bipolar' and generation_results is not None:
        evaluation_results = None
        arguments = generation_results['arguments']
        attacks = generation_results['attacks']
    
    if af_filename!=None:
        if af_content.startswith("data:text/csv;base64,"):
            content_string = af_content[len("data:text/csv;base64,"):]
        decoded = base64.b64decode(content_string)
        decoded_str = decoded.decode('utf-8')
        lines = decoded_str.splitlines()
        data = [line.split('$,$') for line in lines]

        df = pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame(columns=data[0])


        
    arguments=replace_fin(replace_spaces2(arguments))
    attacks=replace_fin(replace_spaces2(replace_mid(attacks)))

    try:
        arg_list = [Argument(arg) for arg in arguments.split("$end$")]
        defeat_list = []
        for attack in attacks.split('$end$'):
            att_list = attack.replace(')', '').replace('(', '').replace('$A$', '').replace('$S$', '').split("$,$")     
            if len(att_list) == 2 and att_list[0] != '' and att_list[1] != '':
                from_argument = Argument(att_list[0])
                to_argument = Argument(att_list[1])
                if from_argument not in arg_list or to_argument not in arg_list:
                    raise ValueError('Not a valid defeat, since one of the arguments does not exist.')
                defeat_list.append(Defeat(Argument(att_list[0]), Argument(att_list[1])))

        arg_framework = AbstractArgumentationFramework('AF', arg_list, defeat_list)
        #arg_framework = read_argumentation_framework(arguments, attacks)
    except ValueError:
        arg_framework = AbstractArgumentationFramework()

    if dash.callback_context.triggered_id != 'selected-argument-store-bipolar':
        selected_arguments = None
    
    data = get_argumentation_framework_graph_data(arg_framework, selected_arguments, color_blind_mode)

    colors=[]
    legend_elements=[]

    if af_filename!=None:
        l=[]
        for i in range(len(data['nodes'])):
            for index, row in df.iterrows():
                # Extraire les éléments de la 5ème et 6ème colonne
                argument_5 = row.iloc[4]
                argument_6 = row.iloc[5]

                argument_7 = row.iloc[6]
                argument_8 = row.iloc[7]
                    
                couleur1 = 'gray'  # default color if no match
                couleur2 = 'gray'  # default color if no match
                if argument_7 not in l:
                    colors = add_different_color(colors)
                    couleur1=colors[len(l)]
                    l.append(argument_7)
                else:
                    couleur1 = colors[l.index(argument_7)]

                if argument_8 not in l:
                    colors = add_different_color(colors)
                    couleur2=colors[len(l)]
                    l.append(argument_8)
                else:
                    couleur2 = colors[l.index(argument_8)]
                if data['nodes'][i]['id'] == argument_5:
                    data['nodes'][i]['color']=couleur1
                if data['nodes'][i]['id'] == argument_6:
                    data['nodes'][i]['color']=couleur2  
        legend_elements=create_legend_colors(colors,l)   
    
    elif topic!='No topic selected':
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, '..', 'data','us_debat', 'full_dataset_processing.csv')
        # Lire les données du fichier CSV en sautant la première ligne (l'entête)
        df = pd.read_csv(file_path, skiprows=0)
        l=[]
        for i in range(len(data['nodes'])):
            for index, row in df.iterrows():
                if row.iloc[8]==topic:
                    # Extraire les éléments de la 5ème et 6ème colonne
                    argument_5 = row.iloc[4]
                    argument_6 = row.iloc[5]

                    argument_7 = row.iloc[6]
                    argument_8 = row.iloc[7]
                        
                    couleur1 = 'gray'  # default color if no match
                    couleur2 = 'gray'  # default color if no match
                    if row.iloc[2] == 'Attack' and 'attack' in checkbox_values:
                        if argument_7 not in l:
                            colors = add_different_color(colors)
                            couleur1=colors[len(l)]
                            l.append(argument_7)
                        else:
                            couleur1 = colors[l.index(argument_7)]

                        if argument_8 not in l:
                            colors = add_different_color(colors)
                            couleur2=colors[len(l)]
                            l.append(argument_8)
                        else:
                            couleur2 = colors[l.index(argument_8)]
                        if data['nodes'][i]['id'] == argument_5:
                            data['nodes'][i]['color']=couleur1
                        if data['nodes'][i]['id'] == argument_6:
                            data['nodes'][i]['color']=couleur2 
                    if row.iloc[2] == 'Support' and 'support' in checkbox_values:
                        if argument_7 not in l:
                            colors = add_different_color(colors)
                            couleur1=colors[len(l)]
                            l.append(argument_7)
                        else:
                            couleur1 = colors[l.index(argument_7)]

                        if argument_8 not in l:
                            colors = add_different_color(colors)
                            couleur2=colors[len(l)]
                            l.append(argument_8)
                        else:
                            couleur2 = colors[l.index(argument_8)]
                        if data['nodes'][i]['id'] == argument_5:
                            data['nodes'][i]['color']=couleur1
                        if data['nodes'][i]['id'] == argument_6:
                            data['nodes'][i]['color']=couleur2         

        legend_elements=create_legend_colors(colors,l)

    elif ml == 'SVM':
        # Construire le chemin du fichier CSV de manière dynamique
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_svm_baf.csv')

        # Read the file content with multiple encodings
        encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

        for encoding in encodings_to_try:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    file_content = file.read()
                break  # Stop trying encodings once reading succeeds
            except (UnicodeDecodeError, FileNotFoundError):
                continue  # Try the next encoding if reading fails
                
        # Handle if none of the encodings worked or the file was not found
        if 'file_content' not in locals():
            print("Unable to read the data using any of the specified encodings or file not found.")
            file_content = None  # or handle the error appropriately

        if file_content:
            lines = file_content.splitlines()
            lines = lines[:value+1]
            data2 = [line.split('$,$') for line in lines]

            # Create a DataFrame
            df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
        else:
            print("Reading failed, DataFrame not created.")

        l=[]
        for i in range(len(data['nodes'])):
            for index, row in df.iterrows():
                # Extraire les éléments de la 5ème et 6ème colonne
                argument_5 = row.iloc[4]
                argument_6 = row.iloc[5]

                argument_7 = row.iloc[6]
                argument_8 = row.iloc[7]
                    
                couleur1 = 'gray'  # default color if no match
                couleur2 = 'gray'  # default color if no match
                if argument_7 not in l:
                    colors = add_different_color(colors)
                    couleur1=colors[len(l)]
                    l.append(argument_7)
                else:
                    couleur1 = colors[l.index(argument_7)]

                if argument_8 not in l:
                    colors = add_different_color(colors)
                    couleur2=colors[len(l)]
                    l.append(argument_8)
                else:
                    couleur2 = colors[l.index(argument_8)]
                if data['nodes'][i]['id'] == argument_5:
                    data['nodes'][i]['color']=couleur1
                if data['nodes'][i]['id'] == argument_6:
                    data['nodes'][i]['color']=couleur2  
        legend_elements=create_legend_colors(colors,l)   

    elif ml == 'Random Forest':
        # Construire le chemin du fichier CSV de manière dynamique
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_forest_baf.csv')

        # Read the file content with multiple encodings
        encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

        for encoding in encodings_to_try:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    file_content = file.read()
                break  # Stop trying encodings once reading succeeds
            except (UnicodeDecodeError, FileNotFoundError):
                continue  # Try the next encoding if reading fails
                
        # Handle if none of the encodings worked or the file was not found
        if 'file_content' not in locals():
            print("Unable to read the data using any of the specified encodings or file not found.")
            file_content = None  # or handle the error appropriately

        if file_content:
            lines = file_content.splitlines()
            lines = lines[:value+1]
            data2 = [line.split('$,$') for line in lines]

            # Create a DataFrame
            df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
        else:
            print("Reading failed, DataFrame not created.")

        l=[]
        for i in range(len(data['nodes'])):
            for index, row in df.iterrows():
                # Extraire les éléments de la 5ème et 6ème colonne
                argument_5 = row.iloc[4]
                argument_6 = row.iloc[5]

                argument_7 = row.iloc[6]
                argument_8 = row.iloc[7]
                    
                couleur1 = 'gray'  # default color if no match
                couleur2 = 'gray'  # default color if no match
                if argument_7 not in l:
                    colors = add_different_color(colors)
                    couleur1=colors[len(l)]
                    l.append(argument_7)
                else:
                    couleur1 = colors[l.index(argument_7)]

                if argument_8 not in l:
                    colors = add_different_color(colors)
                    couleur2=colors[len(l)]
                    l.append(argument_8)
                else:
                    couleur2 = colors[l.index(argument_8)]
                if data['nodes'][i]['id'] == argument_5:
                    data['nodes'][i]['color']=couleur1
                if data['nodes'][i]['id'] == argument_6:
                    data['nodes'][i]['color']=couleur2  
        legend_elements=create_legend_colors(colors,l)  

    elif ml == 'Decision Tree':
        # Construire le chemin du fichier CSV de manière dynamique
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_tree_baf.csv')

        # Read the file content with multiple encodings
        encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

        for encoding in encodings_to_try:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    file_content = file.read()
                break  # Stop trying encodings once reading succeeds
            except (UnicodeDecodeError, FileNotFoundError):
                continue  # Try the next encoding if reading fails
                
        # Handle if none of the encodings worked or the file was not found
        if 'file_content' not in locals():
            print("Unable to read the data using any of the specified encodings or file not found.")
            file_content = None  # or handle the error appropriately

        if file_content:
            lines = file_content.splitlines()
            lines = lines[:value+1]
            data2 = [line.split('$,$') for line in lines]

            # Create a DataFrame
            df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
        else:
            print("Reading failed, DataFrame not created.")

        l=[]
        for i in range(len(data['nodes'])):
            for index, row in df.iterrows():
                # Extraire les éléments de la 5ème et 6ème colonne
                argument_5 = row.iloc[4]
                argument_6 = row.iloc[5]

                argument_7 = row.iloc[6]
                argument_8 = row.iloc[7]
                    
                couleur1 = 'gray'  # default color if no match
                couleur2 = 'gray'  # default color if no match
                if argument_7 not in l:
                    colors = add_different_color(colors)
                    couleur1=colors[len(l)]
                    l.append(argument_7)
                else:
                    couleur1 = colors[l.index(argument_7)]

                if argument_8 not in l:
                    colors = add_different_color(colors)
                    couleur2=colors[len(l)]
                    l.append(argument_8)
                else:
                    couleur2 = colors[l.index(argument_8)]
                if data['nodes'][i]['id'] == argument_5:
                    data['nodes'][i]['color']=couleur1
                if data['nodes'][i]['id'] == argument_6:
                    data['nodes'][i]['color']=couleur2  
        legend_elements=create_legend_colors(colors,l)  

    for i in range(len(data['nodes'])):
        lab = ''
        if len(data['nodes'][i]['label']) != 61:
            for j in range(len(data['nodes'][i]['label'])):
                lab += data['nodes'][i]['label'][j]
                if j % 60 == 0 and j != 0:
                    if j + 1 < len(data['nodes'][i]['label']) and data['nodes'][i]['label'][j+1] != ' ' and data['nodes'][i]['label'][j] != ' ':
                        lab += '-'
                    lab += '\n'
            data['nodes'][i]['label'] = lab

    return data, legend_elements, arguments, attacks


@callback(
    Output('node-click-message-bipolar', 'children'),
    Input('bipolar-argumentation-graph', 'selection'),
    Input('upload-af-bipolar', 'contents'),
    State('upload-af-bipolar', 'filename'),
    State('output-dropdown-bipolar', 'children'),
    State('output-dropdown-ml-bipolar', 'children'),
    State('checkbox', 'value'),
    Input('slider-bipolar', 'value'),
)
def display_click_data(selection, af_content: str, af_filename: str, topic: str, ml:str, checkbox_values: list, value: int):
    if selection:
        node_id = selection['nodes'][0] if selection['nodes'] else None
        edge_id_list = selection['edges']
        if node_id is not None:
            if af_filename!=None:
                if af_content.startswith("data:text/csv;base64,"):
                    content_string = af_content[len("data:text/csv;base64,"):]
                decoded = base64.b64decode(content_string)
                decoded_str = decoded.decode('utf-8')
                lines = decoded_str.splitlines()
                data = [line.split('$,$') for line in lines]

                df = pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame(columns=data[0])
                elements = []
                att_list=[]
                att_by_list=[]
                sup_list=[]
                sup_by_list=[]
                for index, row in df.iterrows():
                    if row.iloc[2] == 'Attack':
                        if row.iloc[4] == node_id:
                            nn= f'{node_id}-{row.iloc[5]}'
                            if nn in edge_id_list:
                                att_list.append(row.iloc[3])
                        if row.iloc[5] == node_id:
                            nn= f'{row.iloc[4]}-{node_id}'
                            if nn in edge_id_list:
                                att_by_list.append(row.iloc[3])
                    if row.iloc[2] == 'Support':
                        if row.iloc[4] == node_id:
                            nn= f'{node_id}-{row.iloc[5]}'
                            if nn in edge_id_list:
                                sup_list.append(row.iloc[3])
                        if row.iloc[5] == node_id:
                            nn= f'{row.iloc[4]}-{node_id}'
                            if nn in edge_id_list:
                                sup_by_list.append(row.iloc[3])
                if att_list:
                    elements.append(html.H3("Attack : "))
                    for item in att_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if att_by_list:
                    elements.append(html.H3("Attacked by : "))
                    for item in att_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_list:
                    elements.append(html.H3("Support : "))
                    for item in sup_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_by_list:
                    elements.append(html.H3("Supported by : "))
                    for item in sup_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                return dbc.Row(elements)

            elif topic!='No topic selected':
                elements = []
                base_path = os.path.dirname(__file__)
                file_path = os.path.join(base_path, '..', 'data','us_debat', 'full_dataset_processing.csv')
                # Lire les données du fichier CSV en sautant la première ligne (l'entête)
                df = pd.read_csv(file_path, skiprows=0)
                att_list=[]
                att_by_list=[]
                sup_list=[]
                sup_by_list=[]
                for index, row in df.iterrows():
                    if row.iloc[8]==topic:
                        if row.iloc[2]=='Attack' and 'attack' in checkbox_values:
                            if row.iloc[4] == node_id:
                                nn= f'{node_id}-{row.iloc[5]}'
                                if nn in edge_id_list:
                                    att_list.append(row.iloc[3])
                            if row.iloc[5] == node_id:
                                nn= f'{row.iloc[4]}-{node_id}'
                                if nn in edge_id_list:
                                    att_by_list.append(row.iloc[3])
                        if row.iloc[2]=='Support' and 'support' in checkbox_values:
                            if row.iloc[4] == node_id:
                                nn= f'{node_id}-{row.iloc[5]}'
                                if nn in edge_id_list:
                                    sup_list.append(row.iloc[3])
                            if row.iloc[5] == node_id:
                                nn= f'{row.iloc[4]}-{node_id}'
                                if nn in edge_id_list:
                                    sup_by_list.append(row.iloc[3])
                if att_list:
                    elements.append(html.H3("Attack : "))
                    for item in att_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if att_by_list:
                    elements.append(html.H3("Attacked by : "))
                    for item in att_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_list:
                    elements.append(html.H3("Support : "))
                    for item in sup_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_by_list:
                    elements.append(html.H3("Supported by : "))
                    for item in sup_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                return dbc.Row(elements)

            elif ml == 'SVM':
                # Construire le chemin du fichier CSV de manière dynamique
                base_path = os.path.dirname(__file__)
                file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_svm_baf.csv')

                # Read the file content with multiple encodings
                encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

                for encoding in encodings_to_try:
                    try:
                        with open(file_path, 'r', encoding=encoding) as file:
                            file_content = file.read()
                        break  # Stop trying encodings once reading succeeds
                    except (UnicodeDecodeError, FileNotFoundError):
                        continue  # Try the next encoding if reading fails
                        
                # Handle if none of the encodings worked or the file was not found
                if 'file_content' not in locals():
                    print("Unable to read the data using any of the specified encodings or file not found.")
                    file_content = None  # or handle the error appropriately

                if file_content:
                    lines = file_content.splitlines()
                    lines = lines[:value+1]
                    data2 = [line.split('$,$') for line in lines]

                    # Create a DataFrame
                    df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
                else:
                    print("Reading failed, DataFrame not created.")

                elements = []
                att_list=[]
                att_by_list=[]
                sup_list=[]
                sup_by_list=[]
                for index, row in df.iterrows():
                    if row.iloc[2] == 'Attack':
                        if row.iloc[4] == node_id:
                            nn= f'{node_id}-{row.iloc[5]}'
                            if nn in edge_id_list:
                                att_list.append(row.iloc[3])
                        if row.iloc[5] == node_id:
                            nn= f'{row.iloc[4]}-{node_id}'
                            if nn in edge_id_list:
                                att_by_list.append(row.iloc[3])
                    if row.iloc[2] == 'Support':
                        if row.iloc[4] == node_id:
                            nn= f'{node_id}-{row.iloc[5]}'
                            if nn in edge_id_list:
                                sup_list.append(row.iloc[3])
                        if row.iloc[5] == node_id:
                            nn= f'{row.iloc[4]}-{node_id}'
                            if nn in edge_id_list:
                                sup_by_list.append(row.iloc[3])
                if att_list:
                    elements.append(html.H3("Attack : "))
                    for item in att_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if att_by_list:
                    elements.append(html.H3("Attacked by : "))
                    for item in att_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_list:
                    elements.append(html.H3("Support : "))
                    for item in sup_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_by_list:
                    elements.append(html.H3("Supported by : "))
                    for item in sup_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                return dbc.Row(elements)

            elif ml == 'Random Forest':
                # Construire le chemin du fichier CSV de manière dynamique
                base_path = os.path.dirname(__file__)
                file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_forest_baf.csv')

                # Read the file content with multiple encodings
                encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

                for encoding in encodings_to_try:
                    try:
                        with open(file_path, 'r', encoding=encoding) as file:
                            file_content = file.read()
                        break  # Stop trying encodings once reading succeeds
                    except (UnicodeDecodeError, FileNotFoundError):
                        continue  # Try the next encoding if reading fails
                        
                # Handle if none of the encodings worked or the file was not found
                if 'file_content' not in locals():
                    print("Unable to read the data using any of the specified encodings or file not found.")
                    file_content = None  # or handle the error appropriately

                if file_content:
                    lines = file_content.splitlines()
                    lines = lines[:value+1]
                    data2 = [line.split('$,$') for line in lines]

                    # Create a DataFrame
                    df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
                else:
                    print("Reading failed, DataFrame not created.")

                elements = []
                att_list=[]
                att_by_list=[]
                sup_list=[]
                sup_by_list=[]
                for index, row in df.iterrows():
                    if row.iloc[2] == 'Attack':
                        if row.iloc[4] == node_id:
                            nn= f'{node_id}-{row.iloc[5]}'
                            if nn in edge_id_list:
                                att_list.append(row.iloc[3])
                        if row.iloc[5] == node_id:
                            nn= f'{row.iloc[4]}-{node_id}'
                            if nn in edge_id_list:
                                att_by_list.append(row.iloc[3])
                    if row.iloc[2] == 'Support':
                        if row.iloc[4] == node_id:
                            nn= f'{node_id}-{row.iloc[5]}'
                            if nn in edge_id_list:
                                sup_list.append(row.iloc[3])
                        if row.iloc[5] == node_id:
                            nn= f'{row.iloc[4]}-{node_id}'
                            if nn in edge_id_list:
                                sup_by_list.append(row.iloc[3])
                if att_list:
                    elements.append(html.H3("Attack : "))
                    for item in att_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if att_by_list:
                    elements.append(html.H3("Attacked by : "))
                    for item in att_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_list:
                    elements.append(html.H3("Support : "))
                    for item in sup_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_by_list:
                    elements.append(html.H3("Supported by : "))
                    for item in sup_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                return dbc.Row(elements)

            elif ml == 'Decision Tree':
                # Construire le chemin du fichier CSV de manière dynamique
                base_path = os.path.dirname(__file__)
                file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_tree_baf.csv')

                # Read the file content with multiple encodings
                encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

                for encoding in encodings_to_try:
                    try:
                        with open(file_path, 'r', encoding=encoding) as file:
                            file_content = file.read()
                        break  # Stop trying encodings once reading succeeds
                    except (UnicodeDecodeError, FileNotFoundError):
                        continue  # Try the next encoding if reading fails
                        
                # Handle if none of the encodings worked or the file was not found
                if 'file_content' not in locals():
                    print("Unable to read the data using any of the specified encodings or file not found.")
                    file_content = None  # or handle the error appropriately

                if file_content:
                    lines = file_content.splitlines()
                    lines = lines[:value+1]
                    data2 = [line.split('$,$') for line in lines]

                    # Create a DataFrame
                    df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
                else:
                    print("Reading failed, DataFrame not created.")

                elements = []
                att_list=[]
                att_by_list=[]
                sup_list=[]
                sup_by_list=[]
                for index, row in df.iterrows():
                    if row.iloc[2] == 'Attack':
                        if row.iloc[4] == node_id:
                            nn= f'{node_id}-{row.iloc[5]}'
                            if nn in edge_id_list:
                                att_list.append(row.iloc[3])
                        if row.iloc[5] == node_id:
                            nn= f'{row.iloc[4]}-{node_id}'
                            if nn in edge_id_list:
                                att_by_list.append(row.iloc[3])
                    if row.iloc[2] == 'Support':
                        if row.iloc[4] == node_id:
                            nn= f'{node_id}-{row.iloc[5]}'
                            if nn in edge_id_list:
                                sup_list.append(row.iloc[3])
                        if row.iloc[5] == node_id:
                            nn= f'{row.iloc[4]}-{node_id}'
                            if nn in edge_id_list:
                                sup_by_list.append(row.iloc[3])
                if att_list:
                    elements.append(html.H3("Attack : "))
                    for item in att_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if att_by_list:
                    elements.append(html.H3("Attacked by : "))
                    for item in att_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_list:
                    elements.append(html.H3("Support : "))
                    for item in sup_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                if sup_by_list:
                    elements.append(html.H3("Supported by : "))
                    for item in sup_by_list:
                        elements.append(html.P(item))
                        elements.append(html.P("\n\n"))
                return dbc.Row(elements)

        edge_id = selection['edges'][0] if selection['edges'] else None
        if edge_id is not None:
            elements = []
            elements.append(html.H3("Relationship : "))
            if af_filename!=None:
                if af_content.startswith("data:text/csv;base64,"):
                    content_string = af_content[len("data:text/csv;base64,"):]
                decoded = base64.b64decode(content_string)
                decoded_str = decoded.decode('utf-8')
                lines = decoded_str.splitlines()
                data = [line.split('$,$') for line in lines]

                df = pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame(columns=data[0])
                
                for index, row in df.iterrows():
                        rela=row.iloc[4]+"-"+row.iloc[5]
                        if rela == edge_id :
                            elements.append(html.P(row.iloc[3]))
                            elements.append(html.P("\n\n"))
                return dbc.Row(elements)

            elif topic!='No topic selected':
                base_path = os.path.dirname(__file__)
                file_path = os.path.join(base_path, '..', 'data','us_debat', 'full_dataset_processing.csv')
                # Lire les données du fichier CSV en sautant la première ligne (l'entête)
                df = pd.read_csv(file_path, skiprows=0)
                for index, row in df.iterrows():
                    if row.iloc[8]==topic:
                        if row.iloc[2]=='Attack' and 'attack' in checkbox_values:
                            rela=row.iloc[4]+"-"+row.iloc[5]
                            if rela == edge_id :
                                elements.append(html.P(row.iloc[3]))
                                elements.append(html.P("\n\n"))
                        if row.iloc[2]=='Support' and 'support' in checkbox_values:
                            rela=row.iloc[4]+"-"+row.iloc[5]
                            if rela == edge_id :
                                elements.append(html.P(row.iloc[3]))
                                elements.append(html.P("\n\n"))
                return dbc.Row(elements)

            elif ml == 'SVM':
                # Construire le chemin du fichier CSV de manière dynamique
                base_path = os.path.dirname(__file__)
                file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_svm_baf.csv')

                # Read the file content with multiple encodings
                encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

                for encoding in encodings_to_try:
                    try:
                        with open(file_path, 'r', encoding=encoding) as file:
                            file_content = file.read()
                        break  # Stop trying encodings once reading succeeds
                    except (UnicodeDecodeError, FileNotFoundError):
                        continue  # Try the next encoding if reading fails
                        
                # Handle if none of the encodings worked or the file was not found
                if 'file_content' not in locals():
                    print("Unable to read the data using any of the specified encodings or file not found.")
                    file_content = None  # or handle the error appropriately

                if file_content:
                    lines = file_content.splitlines()
                    lines = lines[:value+1]
                    data2 = [line.split('$,$') for line in lines]

                    # Create a DataFrame
                    df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
                else:
                    print("Reading failed, DataFrame not created.")

                for index, row in df.iterrows():
                        rela=row.iloc[4]+"-"+row.iloc[5]
                        if rela == edge_id :
                            elements.append(html.P(row.iloc[3]))
                            elements.append(html.P("\n\n"))
                return dbc.Row(elements)
            
            elif ml == 'Random Forest':
                # Construire le chemin du fichier CSV de manière dynamique
                base_path = os.path.dirname(__file__)
                file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_forest_baf.csv')

                # Read the file content with multiple encodings
                encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

                for encoding in encodings_to_try:
                    try:
                        with open(file_path, 'r', encoding=encoding) as file:
                            file_content = file.read()
                        break  # Stop trying encodings once reading succeeds
                    except (UnicodeDecodeError, FileNotFoundError):
                        continue  # Try the next encoding if reading fails
                        
                # Handle if none of the encodings worked or the file was not found
                if 'file_content' not in locals():
                    print("Unable to read the data using any of the specified encodings or file not found.")
                    file_content = None  # or handle the error appropriately

                if file_content:
                    lines = file_content.splitlines()
                    lines = lines[:value+1]
                    data2 = [line.split('$,$') for line in lines]

                    # Create a DataFrame
                    df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
                else:
                    print("Reading failed, DataFrame not created.")

                for index, row in df.iterrows():
                        rela=row.iloc[4]+"-"+row.iloc[5]
                        if rela == edge_id :
                            elements.append(html.P(row.iloc[3]))
                            elements.append(html.P("\n\n"))
                return dbc.Row(elements)

            elif ml == 'Decision Tree':
                # Construire le chemin du fichier CSV de manière dynamique
                base_path = os.path.dirname(__file__)
                file_path = os.path.join(base_path, '..', 'data','ml_result', 'result_tree_baf.csv')

                # Read the file content with multiple encodings
                encodings_to_try = ['utf-8', 'latin-1', 'utf-16']  # Add more encodings as necessary

                for encoding in encodings_to_try:
                    try:
                        with open(file_path, 'r', encoding=encoding) as file:
                            file_content = file.read()
                        break  # Stop trying encodings once reading succeeds
                    except (UnicodeDecodeError, FileNotFoundError):
                        continue  # Try the next encoding if reading fails
                        
                # Handle if none of the encodings worked or the file was not found
                if 'file_content' not in locals():
                    print("Unable to read the data using any of the specified encodings or file not found.")
                    file_content = None  # or handle the error appropriately

                if file_content:
                    lines = file_content.splitlines()
                    lines = lines[:value+1]
                    data2 = [line.split('$,$') for line in lines]

                    # Create a DataFrame
                    df = pd.DataFrame(data2[1:], columns=data2[0]) if len(data2) > 1 else pd.DataFrame(columns=data2[0])
                else:
                    print("Reading failed, DataFrame not created.")

                for index, row in df.iterrows():
                        rela=row.iloc[4]+"-"+row.iloc[5]
                        if rela == edge_id :
                            elements.append(html.P(row.iloc[3]))
                            elements.append(html.P("\n\n"))
                return dbc.Row(elements)

    return 'Click on a node/edge to see the explanation.'



@callback(
    Output('22-af-download', 'data'),
    Input('22-af-download-button', 'n_clicks'),
    State('bipolar-arguments', 'value'),
    State('bipolar-attacks', 'value'),
    State('22-af-filename', 'value'),
    State('22-af-extension', 'value'),
    prevent_initial_call=True,
)
def download_generated_bipolar_argumentation_framework(
        _nr_clicks: int, arguments_text: str, defeats_text: str, filename: str, extension: str):
    argumentation_framework = read_argumentation_framework(arguments_text, defeats_text)

    if extension == 'JSON':
        argumentation_framework_json = ArgumentationFrameworkToJSONWriter().to_dict(argumentation_framework)
        argumentation_framework_str = json.dumps(argumentation_framework_json)
    elif extension == 'TGF':
        argumentation_framework_str = \
            ArgumentationFrameworkToTrivialGraphFormatWriter.write_to_str(argumentation_framework)
    elif extension == 'APX':
        argumentation_framework_str = \
            ArgumentationFrameworkToASPARTIXFormatWriter.write_to_str(argumentation_framework)
    elif extension == 'ICCMA23':
        argumentation_framework_str = \
            ArgumentationFrameworkToICCMA23FormatWriter.write_to_str(argumentation_framework)
    else:
        raise NotImplementedError

    return {'content': argumentation_framework_str, 'filename': filename + '.' + extension}



@callback(
    Output('evaluation-results-bipolar', 'data'),
    Output('bipolar-evaluation', 'children'),
    Input('generate-accept-af-button-bipolar', 'n_clicks'),
    State('bipolar-arguments', 'value'),
    State('bipolar-attacks', 'value'),
    State('bipolar-evaluation-accordion', 'active_item'),
    State('bipolar-evaluation-semantics', 'value'),
    State('bipolar-evaluation-strategy', 'value'),
    prevent_initial_call=True
)
def evaluate_bipolar_argumentation_framework(_nr_of_clicks_accept: int, arguments: str, attacks: str,
                                              active_item: str,
                                              semantics: str, strategy: str):
    if active_item != 'Evaluation':
        raise PreventUpdate

    if dash.callback_context.triggered_id == 'generate-accept-af-button-bipolar':
        arg_list = [Argument(arg) for arg in arguments.split("$end$")]
        defeat_list_att = []
        defeat_list_sup = []
        pri = 'Click on the extension/argument buttons to display the corresponding argument(s) in the graph.'
        for attack in attacks.split('$end$'):
            if attack[:3]=='$A$':
                att_list = attack.replace(')', '').replace('(', '').replace('$A$', '').split("$,$")   
                if len(att_list) == 2 and att_list[0] != '' and att_list[1] != '':
                    from_argument = Argument(att_list[0])
                    to_argument = Argument(att_list[1])
                    if from_argument not in arg_list or to_argument not in arg_list:
                        raise ValueError('Not a valid defeat, since one of the arguments does not exist.')
                    defeat_list_att.append(Defeat(Argument(att_list[0]), Argument(att_list[1])))
            if attack[:3]=='$S$':
                sup_list = attack.replace(')', '').replace('(', '').replace('$S$', '').split("$,$")   
                if len(sup_list) == 2 and sup_list[0] != '' and sup_list[1] != '':
                    from_argument = Argument(sup_list[0])
                    to_argument = Argument(sup_list[1])
                    if from_argument not in arg_list or to_argument not in arg_list:
                        raise ValueError('Not a valid defeat, since one of the arguments does not exist.')
                    defeat_list_sup.append(Defeat(Argument(sup_list[0]), Argument(sup_list[1])))


        new_arg_list = []

        if semantics == 'Grounded' or semantics == 'Completed':
            pri = 'The Grounded semantic is the least fixed point of the characteristic function.'
           
            fdeb = [arg_list]
            ffin = []
            
            while(fdeb != ffin):

                fdeb = []
                for arg in ffin:
                    fdeb.append(arg)


                if (fdeb == []):
                    for arg in arg_list:
                        t=0
                        for defeat in defeat_list_att:
                            if arg == defeat.to_argument:
                                t=1
                        if t == 0:
                            ffin.append(arg)
                else:
                    for arg in arg_list:
                        if arg not in fdeb:
                            t=0
                            for defeat in defeat_list_att:
                                if arg == defeat.to_argument:
                                    argatt = defeat.from_argument
                                    tt=1
                                    for argdef in fdeb:
                                        for defeat2 in defeat_list_att:
                                            if argatt == defeat2.to_argument and argdef == defeat2.from_argument:
                                                tt=0
                                        for defeat2 in defeat_list_sup:
                                            if arg == defeat2.to_argument and argdef == defeat2.from_argument:
                                                tt=0
                                    if tt == 1:
                                        t = 1
                            if t == 0:
                                ffin.append(arg)
                
            new_arg_list = ffin  

            if semantics == 'Completed':
                pri = 'The Completed semantic is the subset of all admissible argument with respect to an admissible extension (here the grounded semantic).'
                ground = ffin
                fdeb = []
                ffin = [ground]

                while (fdeb != ffin):
                    fdeb = []
                    for arg in ffin:
                        fdeb.append(arg)
                    ffin = []
                    for cur in fdeb:
                        v=0
                        for arg in arg_list:
                            if arg not in cur: 
                                t=0
                                for defeat in defeat_list_att:
                                    if arg == defeat.from_argument and defeat.to_argument in cur:
                                        t=1
                                    elif arg == defeat.to_argument:
                                        if defeat.from_argument in cur:
                                            t=1
                                        else:
                                            argatt = defeat.from_argument
                                            tt = 1
                                            for defeat2 in defeat_list_att:
                                                if defeat2.to_argument == argatt:
                                                    if defeat2.from_argument in cur or defeat2.from_argument == arg:
                                                        tt = 0
                                            for defeat2 in defeat_list_sup:
                                                if defeat2.to_argument == arg:
                                                    if defeat2.from_argument in cur or defeat2.from_argument == arg:
                                                        tt = 0
                                            if(tt == 1):
                                                t=1
                                if(t==0):
                                    v=1
                                    cur.append(arg)
                                    ffin.append(cur) 
                        if(v==0):
                            ffin.append(cur) 
                
                maxi = []
                for cur in ffin:
                    if len(maxi)<len(cur):
                        maxi =cur
                new_arg_list = maxi 
            
        elif semantics == 'Restrainted':
            pri = 'The Restrainted semantic is the subset of all admissible argument and the argument which are more defended than attacked.'
            def is_admissible_retrainted(arg):
                n=0
                for sup in defeat_list_sup:
                    if arg == sup.to_argument:
                        arg_sup = sup.from_argument
                        if is_admissible_retrainted(arg_sup)<1:
                            n = n-1
                for att in defeat_list_att:
                    if arg == att.to_argument:
                        arg_att = att.from_argument
                        if is_admissible_retrainted(arg_att)<1:
                            n = n+1
                return n
            for arg in arg_list:
                if is_admissible_retrainted(arg)<1:
                    new_arg_list.append(arg)


        defeat_list = []
        for arg in arg_list:
            n=0
            for i in range(len(defeat_list_att)):
                if arg == defeat_list_att[i].to_argument:
                    n=n-1
            for i in range(len(defeat_list_sup)):
                if arg == defeat_list_sup[i].to_argument:
                    n=n+1
            if n>=0:
                new_arg_list.append(arg)
                
        for arg in new_arg_list:   
            for i in range(len(defeat_list_att)):
                if arg == defeat_list_att[i].to_argument and defeat_list_att[i].from_argument in new_arg_list:
                    if defeat_list_att[i] not in defeat_list:
                        defeat_list.append(defeat_list_att[i])
                if arg == defeat_list_att[i].from_argument and defeat_list_att[i].to_argument in new_arg_list:
                    if defeat_list_att[i] not in defeat_list:
                        defeat_list.append(defeat_list_att[i])
            for i in range(len(defeat_list_sup)):
                if arg == defeat_list_sup[i].to_argument and defeat_list_sup[i].from_argument in new_arg_list:
                    if defeat_list_sup[i] not in defeat_list:
                        defeat_list.append(defeat_list_sup[i])
                if arg == defeat_list_sup[i].from_argument and defeat_list_sup[i].to_argument in new_arg_list:
                    if defeat_list_sup[i] not in defeat_list:
                        defeat_list.append(defeat_list_sup[i])


        new_defeat_list=[]
        att_list = attacks.split('$end$')

        for defeat in defeat_list:
            ndef=f'{defeat.from_argument}, {defeat.to_argument}'
            for att in att_list:
                natt= att[3:].replace('(','').replace(')','').replace('$,$',', ')
                if natt == ndef:
                    nn=str(defeat.from_argument)
                    nn2=str(defeat.to_argument)
                    new_defeat_list.append(f'{att[:3]}({nn.replace(' ','_').replace(',',';')},{nn2.replace(' ','_').replace(',',';')})')


        abstract_arguments_value = '$end$'.join((str(arg) for arg in new_arg_list))    

        abstract_attacks_value = '$end$'.join((defeat for defeat in new_defeat_list) )

        results = {
        'arguments': abstract_arguments_value,
        'attacks': abstract_attacks_value,
        }
        return results, html.Div([html.P(pri)])

    return {}, html.Div([html.P('Click on the extension/argument buttons to display the corresponding argument(s) in the graph.')])



@callback(
    Output('selected-argument-store-bipolar', 'data'),
    Input({'type': 'extension-button-bipolar', 'index': ALL}, 'n_clicks'),
    Input({'type': 'argument-button-bipolar', 'index': ALL}, 'n_clicks'),
    State('selected-argument-store-bipolar', 'data'),
)
def mark_extension_or_argument_in_graph(_nr_of_clicks_extension_values, _nr_of_clicks_argument_values,
                                        old_selected_data: List[str]):
    button_clicked_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    if button_clicked_id == '':
        return old_selected_data
    button_clicked_id_content = json.loads(button_clicked_id)
    button_clicked_id_type = button_clicked_id_content['type']
    button_clicked_id_index = button_clicked_id_content['index']
    if button_clicked_id_type == 'extension-button-bipolar':
        in_part, undecided_part, out_part = button_clicked_id_index.split('|', 3)
        return {'green': in_part.split('+'), 'yellow': undecided_part.split('+'), 'red': out_part.split('+')}
    elif button_clicked_id_type == 'argument-button-bipolar':
        return {'blue': [button_clicked_id_index]}
    return []


@callback(
    Output('bipolar-explanation-function', 'options'),
    Output('bipolar-explanation-function', 'value'),
    [Input('bipolar-explanation-type', 'value')]
)
def setting_choice(choice: str):
    return EXPLANATION_FUNCTION_OPTIONS[choice], EXPLANATION_FUNCTION_OPTIONS[choice][0]['value']


@callback(
    Output('bipolar-explanation', 'children'),
    Input('bipolar-evaluation-accordion', 'active_item'),
    State('bipolar-arguments', 'value'),
    State('bipolar-attacks', 'value'),
    State('bipolar-evaluation-semantics', 'value'),
    Input('bipolar-explanation-function', 'value'),
    Input('bipolar-explanation-type', 'value'),
    State('bipolar-evaluation-strategy', 'value'),
    prevent_initial_call=True
)
def derive_explanations_abstract_argumentation_framework(active_item,
                                                         arguments: str, attacks: str,
                                                         semantics: str, explanation_function: str,
                                                         explanation_type: str, explanation_strategy: str):
    if active_item != 'Explanation':
        raise PreventUpdate

    # Compute the explanations based on the input.
    arg_framework = read_argumentation_framework(arguments, attacks)
    frozen_extensions = get_argumentation_framework_extensions(arg_framework, semantics)
    extensions = [set(frozen_extension) for frozen_extension in frozen_extensions]
    accepted_arguments = get_accepted_arguments(extensions, explanation_strategy)
    explanations = get_argumentation_framework_explanations(arg_framework, extensions, accepted_arguments,
                                                            explanation_function, explanation_type)

    # Print the explanations for each of the arguments.
    return html.Div([html.Div(html.B('Explanation(s) by argument:'))] +
                    [html.Div([
                        html.B(explanation_key),
                        html.Ul([html.Li(str(explanation_value).replace('set()', '{}'))
                                 for explanation_value in explanation_values])])
                     for explanation_key, explanation_values in explanations.items()])