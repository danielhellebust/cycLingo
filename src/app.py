import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from transformers import MarianMTModel, MarianTokenizer

import spacy

nlp = spacy.load("./cycLingoNER")
nlp.add_pipe('sentencizer')
colors = {"cycLingo": "#F67DE3"}
options = {"colors": colors}

# create a dash app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Load NMT model

tokenizer = MarianTokenizer.from_pretrained('DanielHellebust/cyclingo')
model = MarianMTModel.from_pretrained("DanielHellebust/cyclingo")

# create app layout
app.layout = html.Div([
    dbc.Row([
        dbc.Col(
            dbc.Row(
                [
                    html.Div([html.H1('cycLingo Translator',
                                      style={'text-align': 'center', 'color': 'white', 'padding': '30px',
                                             'background-color': 'black'})]),
                    html.H3('English:', style={'padding': '10px', 'text-align': 'left', 'color': 'black'}),



                    dbc.Textarea(id='textarea-input',
                                 value='',
                                 placeholder='Enter text to translate',
                                 style={'width': '100%', 'height': 200}),
                    dbc.Button('Translate', id='translation-button', color='secondary', className='md-2',
                               n_clicks=0),
                    html.H3('Detected cycLingo entities', style={'padding-top': '30px','padding-bottom':'30px', 'text-align': 'left', 'color': 'black'}),
                    dcc.Markdown(id='output-ner',dangerously_allow_html=True, children='', style={'border': '1px dark grey', 'padding': '10px', 'height': 200}),
                    html.Br(),
                    html.H3('Norwegian Translation:',
                            style={'padding': '10px', 'text-align': 'left', 'color': 'black'}),
                    html.Br(),
                    dbc.Textarea(id='textarea-output',
                                 value='',
                                 style={'width': '100%', 'height': 200}),
                ]), md=12,
            style={'padding-left': '50px', 'padding-right': '50px', 'padding-top': '50px', 'padding-bottom': '50px'}),
    ]),
], style={'width': '100%', 'background-color': 'white'})

# add callback for text input
@app.callback(
    [Output('textarea-output', 'value'),Output('output-ner', 'children')],
    Input('translation-button', 'n_clicks'),
    State('textarea-input', 'value')
)


# update text area
def update_output(n_clicks, value):
    if n_clicks > 0:
        translated = model.generate(**tokenizer(value, return_tensors="pt", padding=True))
        result = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
        doc = nlp(value)
        result_ner = spacy.displacy.render(doc, style="ent", options=options, jupyter=False)

        return result, str(result_ner)
    else:
        return dash.no_update, dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
