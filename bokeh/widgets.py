"""
An example of widgets not respecting the disabled state

Run using: bokeh serve widgets.py --host localhost:8888 --port 8888

then connect to http://localhost:8888 in a browser
"""

from bokeh.plotting import curdoc
import bokeh.models.widgets as widgets
from bokeh.layouts import widgetbox

# make some widgets
button = widgets.Button(label="button1")
dropdown = widgets.Dropdown(label="dropdown", menu=[("one","one"), ("two", "two"), ("three", "three")])
multi_select = widgets.MultiSelect(options=["one", "two", "three"])
radio_button_group = widgets.RadioButtonGroup(labels=["one", "two", "three"])
slider = widgets.Slider(start=1, end=3, value=1, step=1, title="slider")

# display them
widget_box1 = widgetbox(
    button,
    dropdown,
    multi_select,
    radio_button_group,
    slider
)

curdoc().add_root(widget_box1)


# make a toggle button to disable the other widgets
def on_disable(disabled):
    for child in widget_box1.children:
        child.disabled = disabled

toggle = widgets.Toggle(label="Disable")
toggle.on_click(on_disable)

widget_box2 = widgetbox(
    toggle
)

curdoc().add_root(widget_box2)