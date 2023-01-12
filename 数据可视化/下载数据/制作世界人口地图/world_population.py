import json
from country_codes import get_country_code
import pygal_maps_world.maps as pygal
from pygal.style import RotateStyle, LightColorizedStyle

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    
    # 存储每个国家2010年的人口数量
    # 创建一个包含人口数量的字典
    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(pop_dict['Country Name'])
            if code:
                cc_populations[code] = population

#  根据人口数量将所有国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for code, population in cc_populations.items():
    if population < 10000000:
        cc_pops_1[code] = population
    elif population < 1000000000:
        cc_pops_2[code] = population
    else:
        cc_pops_3[code] = population

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

word_map_style = RotateStyle('#336699', base_style=LightColorizedStyle)
word_map = pygal.World(word_map_style=word_map_style)
word_map._title = 'World Population in 2010, by Country'
word_map.add('0-10m', cc_pops_1)
word_map.add('10m-1bn', cc_pops_2)
word_map.add('>1bn', cc_pops_3)

word_map.render_to_file('world_population.svg')
