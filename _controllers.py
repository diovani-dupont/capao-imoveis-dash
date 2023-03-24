from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

list_of_locations = {
    "Todos": 0,
    "Centro": 1,
    "Zona Nova": 2,
    "Navegantes": 3,
    "Jardim Beira Mar": 4,
}

slider_size = [100, 500, 750, 1000, 1250]

controllers = dbc.Row(
    [
        html.Img(id="logo", src=app.get_asset_url("logo.png"), style={"width": "40%"}),
        html.H2(
            "Preço dos Imóveis em Capão da Canoa/RS",
            style={"margin-top": "30px", "margin-bottom": "20px"},
        ),
        html.P(
            """Utilize este dashboard para analisar os valores dos imóveis na cidade de Capão da Canoa"""
        ),
        html.H3(
            """Bairro""",
            style={"margin-top": "30px", "margin-bottom": "25px"},
        ),
        dcc.Dropdown(
            id="location-dropdown",
            options=[{"label": i, "value": j} for i, j in list_of_locations.items()],
            value=None,  # aqui estava 0
            placeholder="Selecione um Bairro"
        ),

        html.H4(
            """Área (m²)""",
            style={"margin-top": "30px", "margin-bottom": "10px"},
        ),
        dcc.Slider(min=0, max=4, id="slider-square-size",
                   marks={i: str(j) for i, j in enumerate(slider_size)}),
        html.H4(
            """Variáveis de Controle""",
            style={"margin-top": "30px", "margin-bottom": "10px"},
        ),
        dcc.Dropdown(
            options=[{"label": "QUARTOS", "value": "QUARTOS"},
                    {"label": "BANHEIROS", "value": "BANHEIROS"},
                    {"label": "VAGAS", "value": "VAGAS"},
                    {"label": "PRECO", "value": "PRECO"}],
            value="PRECO",
            id="dropdown-color")
    ],
    justify="center",
    align="center",
    style={"margin-top": "50px"},
)
