import pandas as pd
import plotly.graph_objects as go
from plotly.express import choropleth

covid = pd.read_excel (r'C:\Users\jiaji\PycharmProjects\pythonProject1\covidinasean.xlsx')

#choropleth map
df=covid.query("Week_Number==41")
df = df[['iso_code','location', 'Week_Number','total_cases','total_deaths','total_tests']]
chart1=choropleth(df, locations='iso_code',hover_name='location',hover_data=df.columns,color='total_cases',color_continuous_scale='rainbow',height=700,title='Total Covid Cases in ASEAN')
#chart1.show()

#line graph with drop down
df1 = covid[['location', 'Week_Number','total_cases']]
total_cases = df1.pivot_table('total_cases', 'Week_Number', 'location')
total_cases.fillna(0, inplace=True)
#plotly
chart2 = go.Figure()

# set up ONE trace
chart2.add_trace(go.Scatter(x=total_cases.index,
                         y=total_cases[total_cases.columns[0]],
                         visible=True)
             )

updatemenu = []
buttons = []

# button with one option for each dataframe
for col in total_cases.columns:
    buttons.append(dict(method='restyle',
                        label=col,
                        visible=True,
                        args=[{'y':[total_cases[col]],
                               'x':[total_cases.index],
                               'type':'scatter'}, [0]],
                        )
                  )

# some adjustments to the updatemenus
updatemenu = []
your_menu = dict()
updatemenu.append(your_menu)

updatemenu[0]['buttons'] = buttons
updatemenu[0]['direction'] = 'down'
updatemenu[0]['showactive'] = True

# add dropdown menus to the figure
chart2.update_layout(showlegend=False, updatemenus=updatemenu,title='ASEAN Confirmed Cases Weekly Trend')
#chart2.show()


#dashboard
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
graph1 = dcc.Graph(
        id='graph1',
        figure=chart1,
        className="six columns"
    )

graph2 = dcc.Graph(
        id='graph2',
        figure=chart2,
        className="six columns"
    )

header = html.H2(children="COVID Dataset Analysis")

row1 = html.Div(children=[graph1, graph2],)

#row2 = html.Div(children=[graph3, graph4])

layout = html.Div(children=[header, row1], style={"text-align": "center"})

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)