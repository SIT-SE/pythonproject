import pandas as pd
import plotly
import plotly

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



df = pd.read_excel (r'C:\Users\mayma\Music\covid.xlsx')
#dfsum = df.loc[df['iso_code'] == 'IDN', 'new_cases'].sum()

# dfsum = df["total_cases"].sum()
# df_sum=pd.DataFrame(data=dfsum).T
# df_sum=df_sum.reindex(columns=df.columns)
# df_sum

# fig = px.bar(df, x = 'location', y = 'total_cases', title='Total new cases per week')
# fig.show()

app = dash.Dash(__name__)

dff = df.groupby('location', as_index=False)[['total_deaths','total_cases']].sum()
print (dff[:10])

app.layout = html.Div([
    html.Div([
        dash_table.DataTable(
            id='datatable_id',
            data=dff.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in dff.columns
            ],
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=False,
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 6,

            style_cell_conditional=[
                {'if': {'column_id': 'location'},
                 'width': '40%', 'textAlign': 'left'},
                {'if': {'column_id': 'total_deaths'},
                 'width': '30%', 'textAlign': 'left'},
                {'if': {'column_id': 'total_cases'},
                 'width': '30%', 'textAlign': 'left'},
            ],
        ),
    ],className='row'),

    html.Div([
        html.Div([
            dcc.Dropdown(id='linedropdown',
                options=[
                         {'label': 'Deaths', 'value': 'total_deaths'},
                         {'label': 'Cases', 'value': 'total_cases'}
                ],
                # value='total_deaths',
                multi=False,
                clearable=False
            ),
        ],className='six columns')



    ],className='row'),

    html.Div([

        html.Div([
            dcc.Graph(id='linechart'),
        ],className='six columns'),
        html.Div([
            dcc.Dropdown(id='piedropdown',
                         options=[
                             {'label': 'Deaths', 'value': 'total_deaths'},
                             {'label': 'Cases', 'value': 'total_cases'}
                         ],
                         # value='total_cases',
                         multi=False,
                         clearable=False
                         ),
        ], className='six columns'),
        html.Div([
            dcc.Graph(id='piechart'),
        ],className='six columns'),

    ],className='row'),


])


@app.callback(
    [Output('piechart', 'figure'),
     Output('linechart', 'figure')],
    [Input('datatable_id', 'selected_rows'),
     Input('piedropdown', 'value'),
     Input('linedropdown', 'value')]
)
def update_data(chosen_rows,piedropval,linedropval):
    if len(chosen_rows)==0:
        df_filterd = dff[dff['location'].isin(['Brunei','Cambodia','Indonesia','Malaysia', 'Laos', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Timor'])]
    else:
        print(chosen_rows)
        df_filterd = dff[dff.index.isin(chosen_rows)]

    pie_chart=px.pie(
            data_frame=df_filterd,
            names='location',
            values=piedropval,
            hole=.3,
            labels={'Countries':'location'}
            )



    list_chosen_countries=df_filterd['location'].tolist()
    df_line = df[df['location'].isin(list_chosen_countries)]

    line_chart = px.line(
            data_frame=df_line,
            x='Week_Number',
            y=linedropval,
            color='location',
            labels={'location':'location', 'dateRep':'date'},
            )
    line_chart.update_layout(uirevision='foo')

    return (pie_chart,line_chart)



if __name__ == '__main__':
    app.run_server(debug=True)
