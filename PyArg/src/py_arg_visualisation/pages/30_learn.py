import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

from py_arg_learning.identify_grounded_extension import IdentifyGroundedExtension
from py_arg_learning.list_complete_extensions import ListCompleteExtensions
from py_arg_learning.list_preferred_extensions import ListPreferredExtensions

dash.register_page(__name__, name='Contact', title='Contact')

# Get all exercises
exercise_dict = {
    'List all complete extensions': ListCompleteExtensions(),
    'List all preferred extensions': ListPreferredExtensions(),
    'Identify grounded extension': IdentifyGroundedExtension()
}

layout = dbc.Container([
            dbc.Row([
                html.H1('Get in Touch', style={'text-align' : 'center', 'padding': '50px','font-size': '70px'}),
                html.H1('Collaborate and Share Insights in Argumentation Analysis '),
                html.P("We appreciate your interest in our internship project, dedicated to advancing the field of argumentation analysis. Whether you have questions, feedback, or are interested in collaborating with us, we would love to hear from you. "
                       "I'm committed to fostering open communication and is eager to connect with fellow researchers, students, and professionals. Please don't hesitate to reach out through the contact form below or via the provided email "
                       "addresses. I look forward to engaging with you and exploring the exciting possibilities in this dynamic area of research.")
            ],className='page-text'),
            dbc.Row([
                html.H2('Main reshearcher:'),
                dbc.Col([
                    html.Img(src='/assets/robin2024.jpg', style={'width': '20%', 'display': 'block','margin-left': '30px'})
                ]),
                dbc.Col([
                    html.H4('Robin Chavigny',style={'margin-left': '-430px'}),
                    html.P(['- Resume: ',
                            html.A('Robin_Chavigny_CV_EN_2024', href='/assets/Robin_Chavigny_CV_EN_2024.pdf',target="_blank")
                    ],style={'margin-left': '-435px','margin-top': '0px'}),
                    html.P('- Email: robin.chavigny@etu.uca.fr ',style={'margin-left': '-435px','margin-top': '0px'}),
                    html.P(['- LinkedIn: ',
                            html.A('Robin Chavigny', href='https://www.linkedin.com/in/robin-chavigny-568556292/',target="_blank")
                    ],style={'margin-left': '-435px','margin-top': '0px'}),
                    html.P(['- GitHub of this project: ',
                            html.A('argumentation-analysis', href='https://github.com/Robin-Chavigny/argumentation-analysis',target="_blank")
                    ],style={'margin-left': '-435px','margin-top': '0px'}),
                ])
            ],className='page-text'),
            dbc.Row([
                html.H2('Tutors:',style={'margin-top': '10px'}),
                dbc.Col([
                    html.H3('From JAIST:',style={'margin-left': '30px'}),
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/racharak2024.png', style={'width': '42%', 'display': 'block','margin-left': '30px'})
                        ]),
                        dbc.Col([
                            html.H4('Teeradaj Racharak',style={'margin-left': '-130px'}),
                            html.P('- Office Phone: (+81)0761-51-1222',style={'margin-left': '-135px','margin-top': '0px'}),
                            html.P('- Email: racharak@jaist.ac.jp ',style={'margin-left': '-135px','margin-top': '0px'}),
                            html.P(['- Website: ',
                                    html.A('Teeradaj Racharak', href='https://sites.google.com/view/teeradaj',target="_blank")
                            ],style={'margin-left': '-135px','margin-top': '0px'}),
                        ])
                    ])
                ]),
                dbc.Col([
                    html.H3('From ISIMA:',style={'margin-left': '30px'}),
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/guitton2024.png', style={'width': '42%', 'display': 'block','margin-left': '30px'})
                        ]),
                        dbc.Col([
                            html.H4('Alexandre Guitton',style={'margin-left': '-130px'}),
                            html.P('- Office Phone: (+33)4 73 40 52 29',style={'margin-left': '-135px','margin-top': '0px'}),
                            html.P('- Email: alexandre.guitton@uca.fr ',style={'margin-left': '-135px','margin-top': '0px'}),
                            html.P(['- Website: ',
                                    html.A('limos.fr', href='https://limos.fr/detailperson/52',target="_blank")
                            ],style={'margin-left': '-135px','margin-top': '0px'}),
                        ])
                    ])
                ]),
            ],className='page-text'),
            dbc.Row([
                html.H2('University:',style={'margin-top': '10px'}),
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/logo_jaist.jpg', style={'width': '42%', 'display': 'block','margin-left': '30px'})
                        ]),
                        dbc.Col([
                            html.H4('Japan Advanced Institute of Science and Technology',style={'margin-left': '-150px'}),
                            html.P('- Office Phone: (+81)0761-51-1111',style={'margin-left': '-135px','margin-top': '0px'}),
                            html.P('- Adress: 1 Chome-1 Asahidai, Nomi, Ishikawa 923-1211',style={'margin-left': '-135px','margin-top': '0px'}),
                            html.P(['- Website: ',
                                    html.A('www.jaist.ac.jp', href='https://www.jaist.ac.jp/english/',target="_blank")
                            ],style={'margin-left': '-135px','margin-top': '0px'}),
                        ])
                    ])
                ]),
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            html.Img(src='/assets/logo_isima.png', style={'width': '42%', 'display': 'block','margin-left': '30px'})
                        ]),
                        dbc.Col([
                            html.H4("Institut Supérieur d'Informarique, de Modélisation et leurs Applications",style={'margin-left': '-150px'}),
                            html.P('- Office Phone: (+33)4 73 40 50 00',style={'margin-left': '-135px','margin-top': '0px'}),
                            html.P('- Email: secretariat@isima.fr ',style={'margin-left': '-135px','margin-top': '0px'}),
                            html.P('- Adress: 1 rue de la Chebarde, TSA 60026, 63178 Aubière CEDEX',style={'margin-left': '-135px','margin-top': '0px'}),
                            html.P(['- Website: ',
                                    html.A('isima.fr', href='https://www.isima.fr/',target="_blank")
                            ],style={'margin-left': '-135px','margin-top': '0px'}),
                        ])
                    ])
                ]),
            ],className='page-text'),
        ], className='page')


