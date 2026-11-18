from fastapi import FastAPI
from nicegui import ui
from fix_json import FixJson

app = FastAPI()

database = FixJson('Database.json')

#create pie chart
pie_chart = {
    'color': ['#39FF14', '#334155'],
    'series': [{
        'type': 'pie', #type of chart
        'radius': ['65%', '85%'], #chart size(do not touch)
            
        'label':{
            'show': True,
            'position': 'center',
            'formatter': '40%',
            'fontSize': 28,
            'fontWeight': 'bold',
            'color': '#ffffff'
        },

        #chart placeholder values
        'data': [
            {'value:':10, 'name':'A'},
            {'value:':10, 'name':'B'}
        ]
    }]
}

# create point graph
point_graph = {
    'color': ['#39FF14', '#334155'],
    'yAxis' : {'type': 'value'},
    'xAxis' : {'type': 'category'},
    'series':[{
        'type':'line',
        'data':[],
    }]
}

# create points for 3d axis
three_axis = {
    'animation': False,
    'color': ['#39FF14', "#FFFFFF"],
    'xAxis3D':{
        'name': 'X',
                    'nameTextStyle': {'color': "#92149D"},
    "axisLabel": {"color": "#ffffff"},
    },
    'yAxis3D':{
        'name': 'Y',
        'nameTextStyle': {'color': "#2cb2b9" },
        "axisLabel": {"color": "#ffffff"}
    },
    'zAxis3D':{
        'name': 'Z',
                'nameTextStyle': {'color': "#099132"},
        "axisLabel": {"color": "#ffffff"}
    },
    'grid3D':{},
    'textStyle': {
            'color': '#ffffff' 
        },
    'series':[{
        'type':'line3D',
        'data':[[1,1,1],[2,2,2]],
    }]
}

@ui.page("/main")
async def main_page():

    ui.query('body').classes('bg-slate-800 text-white')
    with ui.row().classes('flex overflow-hidden'):
        with ui.card().classes('flex items-center justify-center bg-slate-800 border-4 border-[#335552]'):
            ui.label('LIFE SUPPORT SYSTEM').classes('text-2xl font-bold')
            with ui.column().classes('flex-1 w-60 h-auto overflow-hidden items-center justify-center'):
                ui.label('Oxygen').classes('text-xl font-bold')
                O2 = ui.echart(options=pie_chart).classes('h-65 -mt-6')
                ui.label('Water').classes('text-xl font-bold')
                water = ui.echart(options=pie_chart).classes('h-65 -mt-6')
                ui.label('Food').classes('text-xl font-bold')
                food = ui.echart(options=pie_chart).classes('h-65 -mt-6')
                
        with ui.column():
            with ui.card().classes('flex items-center justify-center bg-slate-800 border-4 border-[#335552]'):
                ui.label('Fuel').classes('text-2xl font-bold')
                with ui.column().classes('w-80 h-auto overflow-hidden items-center justify-center relative'):
                    point_graph_telemetry = ui.echart(options=point_graph).classes('w-80 h-75 -m-10')

            with ui.card().classes('flex items-center justify-center bg-slate-800 border-4 border-[#335552]'):
                ui.label('TRAJECTORY').classes('text-xl font-bold')
                with ui.column().classes('w-80 h-70 mb-8 items-center'):
                    three_axis_graph = ui.echart(options=three_axis).classes('w-85 h-100 -mt-2')

            with ui.card().classes('flex items-center justify-center bg-slate-800 border-4 border-[#335552]'):
                ui.label('SHIP ENVIRONMENT').classes('text-xl font-bold')
                with ui.column().classes('w-80 h-27 mb-8 items-start font-bold pl-5'):
                    light = ui.label(f"Light: waiting....")
                    humidity = ui.label(f"Humidity: waiting....")
                    temp = ui.label(f"Temperature: waiting....")
                    co2 = ui.label(f"Atmosphere: waiting....")

    def update_life_support(chart, key: str):
        try:
            value = database.open_data()[key]
            chart.options['series'][0]['data'] = [{'value': value}, {'value':100-value}]
            chart.options['series'][0]['label']['formatter'] = f"{value}"
            chart.update()
        except:
            pass

    def update_graph(graph, data):
        try:
            value = database.open_data()[data]
            graph.options['series'][0]['data'] = value
            graph.update()
        except:
            pass


    ui.timer(0.5, lambda: 
             (update_life_support(O2, 'O2'),
             update_life_support(water, "water"),
             update_life_support(food, "food"),
             update_graph(point_graph_telemetry, 'breeder_contents'),
             update_graph(three_axis_graph, 'accelarometer'),
             light.set_text(f"Light: {database.open_data()["light"]}"),
             humidity.set_text(f"Humidity: {database.open_data()["humidity"]}"),
             temp.set_text(f"Temperature: {database.open_data()["temperature"]}°C"),
             co2.set_text(f"Atmosphere: {database.open_data()["CO2"]} ppm")
             )
            )

ui.run_with(    
    app, storage_secret="3"
)