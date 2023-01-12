import pygal_maps_world.maps as pygal

word_map = pygal.World()
word_map.title = 'Populations of Countries in North America'
word_map.add('North America',{'ca': 34126000, 'us': 309349000, 'mx': 113423000})
word_map.render_to_file('na_populations.svg')