def on_forever():
    if input.compass_heading() > 337.5 or input.compass_heading() < 22.5:
        basic.show_arrow(ArrowNames.NORTH)
    elif input.compass_heading() > 22.5 and input.compass_heading() <= 67.5:
        basic.show_arrow(ArrowNames.NORTH_EAST)
    elif input.compass_heading() > 67.5 and input.compass_heading() <= 112.5:
        basic.show_arrow(ArrowNames.EAST)
    elif input.compass_heading() > 112.5 and input.compass_heading() <= 157.5:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif input.compass_heading() > 112.5 and input.compass_heading() <= 157.5:
        basic.show_arrow(ArrowNames.SOUTH)
    elif input.compass_heading() > 157.5 and input.compass_heading() <= 202.5:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    elif input.compass_heading() > 202.5 and input.compass_heading() <= 247.5:
        basic.show_arrow(ArrowNames.WEST)
    elif input.compass_heading() > 292.5 and input.compass_heading() <= 337.5:
        basic.show_arrow(ArrowNames.NORTH_WEST)
    else:
        basic.show_string("Wrong")
basic.forever(on_forever)
