from draw_image import draw_image


address_ll = "37.588392,55.734036"
size = '450,450'

map_params = {
    "ll": address_ll,
    "l": "map",
    "size": size,
    "z": 18
}
draw_image(map_params)
