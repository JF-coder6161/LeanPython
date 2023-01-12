import pygal_maps_world.maps as pygal

word_map = pygal.World()
word_map.title = 'North,Central,and South America'
word_map.add('North America',['ca', 'mx', 'us'])
word_map.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
word_map.add('South America',
             ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe'
                 , 'py', 'sr', 'uy', 've'])
word_map.render_to_file('americas.svg')
