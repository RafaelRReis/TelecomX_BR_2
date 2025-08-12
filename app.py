import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
import pandas as pd
from math import ceil
import dash_bootstrap_components as dbc

# ========== Configuração Inicial ==========
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "TelecomX - Painel de Retenção de Clientes"

# ========== Paleta Corporativa Atualizada ==========
CORES = {
    'yes': '#B22234',  # Vermelho institucional
    'no': '#005F73' 
    
}
DETALHES = '#FFA000'   # Âmbar para destaques
FUNDO = '#FAFAFA'      # Cinza claro
TEXTO = '#263238'      # Azul petróleo
CARDS = '#ECEFF1'      # Cinza azulado claro

# Carregar dados
url = 'https://raw.githubusercontent.com/RafaelRReis/TelecomX_BR_2/main/Dados_tratados_desafio_Telecom_X.csv'
dados = pd.read_csv(url)

# ========== Componentes Reutilizáveis ==========
def criar_card(titulo, valor, icone, cor):
    return dbc.Card(
        dbc.CardBody([
            html.Div([
                html.H3(valor, className="card-title"),
                html.P(titulo, className="card-text")
            ], style={"textAlign": "center"}),
            html.Div(className=f"bi {icone}", style={
                "position": "absolute",
                "right": "20px",
                "top": "20px",
                "fontSize": "2rem",
                "color": cor
            })
        ]),
        className="mb-3 shadow-sm",
        style={"height": "100%", "position": "relative"}
    )

filtro_contrato = dcc.Dropdown(
    id='filtro-contrato',
    options=[{'label': 'Todos', 'value': 'all'}] + 
            [{'label': tipo, 'value': tipo} for tipo in dados['account_Contract'].unique()],
    value='all',
    clearable=False,
    className="mb-3"
)

filtro_servico = dcc.Dropdown(
    id='filtro-servico',
    options=[{'label': 'Todos', 'value': 'all'}] + 
            [{'label': servico, 'value': servico} for servico in dados['internet_InternetService'].unique()],
    value='all',
    clearable=False,
    className="mb-3"
)

# ========== Layout Principal ==========
app.layout = dbc.Container([
    # Cabeçalho com KPI Cards
    dbc.Row([
        dbc.Col(html.H1("📊 Painel de Retenção de Clientes", className="text-center my-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col(criar_card("Total Clientes", len(dados), "bi-people-fill", DETALHES), md=3),
        dbc.Col(criar_card("Taxa de Churn", f"{dados['Churn'].value_counts(normalize=True)['yes']:.1%}", 
                          "bi-exclamation-triangle-fill", CORES['yes']), md=3),
        dbc.Col(criar_card("Clientes Retidos", f"{dados['Churn'].value_counts(normalize=True)['no']:.1%}", 
                          "bi-check-circle-fill", CORES['no']), md=3),
        dbc.Col(criar_card("Tempo Médio (meses)", f"{dados['customer_tenure'].mean():.1f}", 
                          "bi-clock-fill", TEXTO), md=3),
    ], className="mb-4"),
    
    # Filtros e Abas
    dbc.Row([
        dbc.Col([
            html.H5("🔍 Filtros", className="mb-3"),
            html.Label("Tipo de Contrato:", className="mb-1"),
            filtro_contrato,
            html.Label("Serviço de Internet:", className="mb-1"),
            filtro_servico,
            html.Button("Aplicar Filtros", id="aplicar-filtros", className="btn btn-primary w-100 mt-2")
        ], md=3),
        
        dbc.Col([
            dcc.Tabs(id="tabs-analise", value='tab-perfil', children=[
                dcc.Tab(label='👥 Perfil dos Clientes', value='tab-perfil', className="custom-tab"),
                dcc.Tab(label='🌐 Serviços Digitais', value='tab-servicos', className="custom-tab"),
                dcc.Tab(label='💳 Dados Financeiros', value='tab-financeiro', className="custom-tab"),
                dcc.Tab(label='📈 Insights Avançados', value='tab-insights', className="custom-tab"),
            ]),
            html.Div(id="conteudo-tabs", className="p-3 border rounded")
        ], md=9)
    ]),
    
    # Rodapé
    dbc.Row([
        dbc.Col(html.P("© 2023 TelecomX - Todos os direitos reservados | Painel atualizado diariamente", 
                      className="text-center text-muted small mt-4"), width=12)
    ])
], fluid=True, style={"backgroundColor": FUNDO})

# ========== Callbacks ==========
@app.callback(
    Output('conteudo-tabs', 'children'),
    [Input('tabs-analise', 'value'),
     Input('aplicar-filtros', 'n_clicks')],
    [State('filtro-contrato', 'value'),
     State('filtro-servico', 'value')]
)
def renderizar_conteudo(aba, n_clicks, contrato, servico):
    # Aplicar filtros
    dados_filtrados = dados.copy()
    if contrato != 'all':
        dados_filtrados = dados_filtrados[dados_filtrados['account_Contract'] == contrato]
    if servico != 'all':
        dados_filtrados = dados_filtrados[dados_filtrados['internet_InternetService'] == servico]
    
    if aba == 'tab-perfil':
        return dbc.Container([
            dbc.Row([
                dbc.Col(dcc.Graph(figure=gerar_grafico_churn(dados_filtrados)), md=6),
                dbc.Col(dcc.Graph(figure=gerar_grafico_demograficos(dados_filtrados)), md=6)
            ]),
            dbc.Row(dbc.Col(dcc.Graph(figure=gerar_heatmap_correlacao(dados_filtrados)), width=12))
        ])
    
    elif aba == 'tab-servicos':
        return dbc.Container([
            dbc.Row(dbc.Col(dcc.Graph(figure=gerar_grafico_servicos_internet(dados_filtrados)), width=12)),
            dbc.Row(dbc.Col(dcc.Graph(figure=gerar_grafico_telefonia(dados_filtrados)), width=12))
        ])
    
    elif aba == 'tab-financeiro':
        return dbc.Container([
            dbc.Row(dbc.Col(dcc.Graph(figure=gerar_grafico_contratos_pagamento(dados_filtrados)), width=12)),
            dbc.Row(dbc.Col(dcc.Graph(figure=gerar_grafico_metricas_financeiras(dados_filtrados)), width=12))
        ])
    
    elif aba == 'tab-insights':
        return dbc.Container([
            dbc.Row([
                dbc.Col(dcc.Graph(figure=gerar_grafico_risco_churn(dados_filtrados)), md=6),
                dbc.Col(dcc.Graph(figure=gerar_grafico_valor_vida_cliente(dados_filtrados)), md=6)
            ]),
            dbc.Row(dbc.Col(dash_table.DataTable(
                id='tabela-clientes-risco',
                columns=[{"name": i, "id": i} for i in dados_filtrados.columns],
                data=dados_filtrados.sort_values('account_Charges_Monthly', ascending=False).head(10).to_dict('records'),
                page_size=10,
                style_table={'overflowX': 'auto'},
                style_header={
                    'backgroundColor': CARDS,
                    'fontWeight': 'bold'
                },
                style_cell={
                    'textAlign': 'left',
                    'padding': '10px',
                    'border': '1px solid #eee'
                }
            ), width=12))
        ])

# Funções para gerar gráficos (implementação similar à original, mas com estilo atualizado)
def gerar_grafico_churn(dados):
    fig = px.pie(
        dados,
        names='Churn',
        title='Distribuição de Churn',
        color='Churn',
        color_discrete_map={'yes': CORES['yes'], 'no': CORES['no']}
    )
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(paper_bgcolor=FUNDO, font_color=TEXTO)
    return fig


def gerar_grafico_demograficos(dados):
    # Mapeia a coluna binária para texto (opcional, só para visual)
    dados['Senioridade'] = dados['customer_SeniorCitizen'].map({1: 'Sênior', 0: 'Não Sênior'})

    fig = px.histogram(
        dados,
        x='Senioridade',
        color='Churn',
        barmode='group',
        title='Churn por Faixa de Senioridade',
        color_discrete_map={'yes': CORES['yes'], 'no': CORES['no']}
    )

    fig.update_layout(
        xaxis_title='Cliente Sênior',
        yaxis_title='Número de Clientes',
        paper_bgcolor=FUNDO,
        font_color=TEXTO
    )

    return fig


def gerar_heatmap_correlacao(dados):
    corr = dados.select_dtypes(include='number').corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale='RdBu',
        title='Mapa de Correlação entre Variáveis Numéricas'
    )
    fig.update_layout(paper_bgcolor=FUNDO, font_color=TEXTO)
    return fig

def gerar_grafico_servicos_internet(dados):
    fig = px.histogram(
        dados,
        x='internet_InternetService',
        color='Churn',
        barmode='group',
        title='Tipo de Serviço de Internet por Churn',
        color_discrete_map={'yes': CORES['yes'], 'no': CORES['no']}
    )
    fig.update_layout(paper_bgcolor=FUNDO, font_color=TEXTO)
    return fig

def gerar_grafico_telefonia(dados):
    fig = px.histogram(
        dados,
        x='phone_MultipleLines',
        color='Churn',
        barmode='group',
        title='Uso de Linhas Telefônicas por Churn',
        color_discrete_map={'yes': CORES['yes'], 'no': CORES['no']}
    )
    fig.update_layout(paper_bgcolor=FUNDO, font_color=TEXTO)
    return fig

def gerar_grafico_contratos_pagamento(dados):
    fig = px.sunburst(
        dados,
        path=['account_Contract', 'account_PaymentMethod'],
        values='account_Charges_Monthly',
        color='Churn',
        title='Contratos e Métodos de Pagamento',
        color_discrete_map={'yes': CORES['yes'], 'no': CORES['no']}
    )
    fig.update_layout(paper_bgcolor=FUNDO, font_color=TEXTO)
    return fig

def gerar_grafico_metricas_financeiras(dados):
    fig = px.box(
        dados,
        x='Churn',
        y='account_Charges_Total',
        color='Churn',
        title='Distribuição de Cobrança Total por Churn',
        color_discrete_map={'yes': CORES['yes'], 'no': CORES['no']}
    )
    fig.update_layout(paper_bgcolor=FUNDO, font_color=TEXTO)
    return fig

def gerar_grafico_risco_churn(dados):
    media_tempo = dados.groupby('Churn')['customer_tenure'].mean().reset_index()
    fig = px.bar(
        media_tempo,
        x='Churn',
        y='customer_tenure',
        color='Churn',
        title='Tempo Médio de Permanência por Churn',
        color_discrete_map={'yes': CORES['yes'], 'no': CORES['no']}
    )
    fig.update_layout(paper_bgcolor=FUNDO, font_color=TEXTO)
    return fig


def gerar_grafico_valor_vida_cliente(dados):
    dados['CLV'] = dados['account_Charges_Monthly'] * dados['customer_tenure']
    fig = px.violin(
        dados,
        y='CLV',
        x='Churn',
        color='Churn',
        box=True,
        points='all',
        title='Valor do Cliente (CLV) por Churn',
        color_discrete_map={'yes': CORES['yes'], 'no': CORES['no']}
    )
    fig.update_layout(paper_bgcolor=FUNDO, font_color=TEXTO)
    return fig


# ... (outras funções de geração de gráficos)

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=10000, debug=True)

