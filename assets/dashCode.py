from dash.html import Div, Button, Img
from dash.dcc import Tabs, Tab, Input, Upload


def getLayoutFormated():
    return Div(
        [
            Div(
                children=[
                    Div(
                        children=[
                            Div(
                                children=[
                                    Div(
                                        children=[
                                            Div(
                                                children=["ACG"],
                                                id="acg",
                                                className="acg",
                                            )
                                        ],
                                        id="website-title",
                                        className="website-title",
                                    ),
                                    Div(
                                        children=[
                                            Div(
                                                children=[
                                                    Img(
                                                        className="networkicon",
                                                        src="./assets/networkicon.png",
                                                    )
                                                ],
                                                id="neuralnetworkicon",
                                                className="neuralnetworkicon",
                                            ),
                                            Div(
                                                children=[],
                                                id="separator1",
                                                className="separator1",
                                            ),
                                            Div(
                                                children=[
                                                    Img(
                                                        className="regressoricon",
                                                        src="./assets/regressoricon.png",
                                                    )
                                                ],
                                                id="classifiericon",
                                                className="classifiericon",
                                            ),
                                            Div(
                                                children=[],
                                                id="separator2",
                                                className="separator2",
                                            ),
                                            Div(
                                                children=[
                                                    Img(
                                                        className="classifiericon2",
                                                        src="./assets/classifiericon2.png",
                                                    )
                                                ],
                                                id="regressionicon",
                                                className="regressionicon",
                                            ),
                                            Div(
                                                children=[],
                                                id="separator3",
                                                className="separator3",
                                            ),
                                            Div(
                                                children=[
                                                    Img(
                                                        className="settingsicon2",
                                                        src="./assets/settingsicon2.png",
                                                    )
                                                ],
                                                id="settingsicon",
                                                className="settingsicon",
                                            ),
                                            Div(
                                                children=[],
                                                id="separator4",
                                                className="separator4",
                                            ),
                                        ],
                                        id="navigation",
                                        className="navigation",
                                    ),
                                ],
                                id="leftmenu_upper_box",
                                className="leftmenu_upper_box",
                            ),
                            Div(children=[], id="footer", className="footer"),
                        ],
                        id="left-menu",
                        className="left-menu",
                    ),
                    Div(
                        children=[
                            Div(
                                children=[
                                    Div(
                                        children=[
                                            Div(
                                                children=[
                                                    Div(
                                                        children=[
                                                            Div(
                                                                children=["Argumentos"],
                                                                id="args_title_text",
                                                                className="args_title_text",
                                                            )
                                                        ],
                                                        id="args_title_box",
                                                        className="args_title_box",
                                                    ),
                                                    Div(
                                                        children=[
                                                            Div(
                                                                children=[
                                                                    Div(
                                                                        children=[
                                                                            Div(
                                                                                children=[
                                                                                    "Número de Épocas:"
                                                                                ],
                                                                                id="numepochs_text",
                                                                                className="numepochs_text",
                                                                            ),
                                                                            Div(
                                                                                children=[],
                                                                                id="numepochs_box",
                                                                                className="numepochs_box",
                                                                            ),
                                                                        ],
                                                                        id="arg6",
                                                                        className="arg6",
                                                                    ),
                                                                    Div(
                                                                        children=[
                                                                            Div(
                                                                                children=[
                                                                                    "Taxa de Aprendizagem:"
                                                                                ],
                                                                                id="learningrate_text",
                                                                                className="learningrate_text",
                                                                            ),
                                                                            Div(
                                                                                children=[],
                                                                                id="learningrate_box",
                                                                                className="learningrate_box",
                                                                            ),
                                                                        ],
                                                                        id="arg1",
                                                                        className="arg1",
                                                                    ),
                                                                ],
                                                                id="frame-9",
                                                                className="frame-9",
                                                            ),
                                                            Div(
                                                                children=[
                                                                    Div(
                                                                        children=[
                                                                            Div(
                                                                                children=[
                                                                                    "Funcão de Ativação:"
                                                                                ],
                                                                                id="activationfunction_text",
                                                                                className="activationfunction_text",
                                                                            ),
                                                                            Div(
                                                                                children=[],
                                                                                id="activationfunction_box",
                                                                                className="activationfunction_box",
                                                                            ),
                                                                        ],
                                                                        id="arg4",
                                                                        className="arg4",
                                                                    ),
                                                                    Div(
                                                                        children=[],
                                                                        id="arg5",
                                                                        className="arg5",
                                                                    ),
                                                                ],
                                                                id="frame-10",
                                                                className="frame-10",
                                                            ),
                                                            Div(
                                                                children=[
                                                                    Div(
                                                                        children=[],
                                                                        id="arg2",
                                                                        className="arg2",
                                                                    ),
                                                                    Div(
                                                                        children=[
                                                                            Button(
                                                                                children=[
                                                                                    Div(
                                                                                        children=[
                                                                                            "Executar"
                                                                                        ],
                                                                                        id="exec_button_text",
                                                                                        className="exec_button_text",
                                                                                    )
                                                                                ],
                                                                                id="exec_alg_button_dash_BUTTON",
                                                                                className="exec_alg_button_dash",
                                                                            )
                                                                        ],
                                                                        id="arg3",
                                                                        className="arg3",
                                                                    ),
                                                                ],
                                                                id="frame-11",
                                                                className="frame-11",
                                                            ),
                                                        ],
                                                        id="args_content",
                                                        className="args_content",
                                                    ),
                                                ],
                                                id="topleft",
                                                className="topleft",
                                            ),
                                            Div(
                                                children=[
                                                    Div(
                                                        children=[
                                                            Div(
                                                                children=[
                                                                    "Enviar Dados"
                                                                ],
                                                                id="senddata_title",
                                                                className="senddata_title",
                                                            )
                                                        ],
                                                        id="senddata_title_box",
                                                        className="senddata_title_box",
                                                    ),
                                                    Div(
                                                        children=[
                                                            Upload(
                                                                children=[
                                                                    Button(
                                                                        children=[
                                                                            Div(
                                                                                children=[
                                                                                    "Selecionar Tabela"
                                                                                ],
                                                                                id="select_table_text",
                                                                                className="select_table_text",
                                                                            )
                                                                        ],
                                                                        id="select_button_dash_BUTTON",
                                                                        className="select_button_dash",
                                                                    )
                                                                ],
                                                                id="upload_but_box_UPLOAD",
                                                                className="upload_but_box",
                                                            ),
                                                            Upload(
                                                                children=[
                                                                    Upload(
                                                                        children=[
                                                                            "tabela.csv",
                                                                            Div([]),
                                                                        ],
                                                                        id="datauploaded_name_UPLOAD",
                                                                        className="datauploaded_name",
                                                                    )
                                                                ],
                                                                id="datauploaded_name_box_UPLOAD",
                                                                className="datauploaded_name_box",
                                                            ),
                                                        ],
                                                        id="senddata_content",
                                                        className="senddata_content",
                                                    ),
                                                ],
                                                id="topright",
                                                className="topright",
                                            ),
                                        ],
                                        id="center-top",
                                        className="center-top",
                                    ),
                                    Div(
                                        children=[
                                            Div(
                                                children=["Visualização"],
                                                id="visualization_title",
                                                className="visualization_title",
                                            ),
                                            Div(
                                                children=[
                                                    Div(
                                                        children=[],
                                                        id="visualization_box_1",
                                                        className="visualization_box_1",
                                                    ),
                                                    Div(
                                                        children=[],
                                                        id="visualization_box_2",
                                                        className="visualization_box_2",
                                                    ),
                                                    Div(
                                                        children=[],
                                                        id="visualization_box_3",
                                                        className="visualization_box_3",
                                                    ),
                                                ],
                                                id="visualization",
                                                className="visualization",
                                            ),
                                        ],
                                        id="center-bottom",
                                        className="center-bottom",
                                    ),
                                ],
                                id="frame-12",
                                className="frame-12",
                            )
                        ],
                        id="bodydashboard",
                        className="bodydashboard",
                    ),
                ],
                id="free_dashboard",
                className="free_dashboard",
            )
        ]
    )
