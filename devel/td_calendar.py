import ofjustpy as oj
from meltui_components.components import Calendar
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

calendar = Calendar()


app = oj.load_app()

tlc = oj.PD.Container(childs=[#slider,
    calendar
                                     
                        ],
                twsty_tags=[space/y/4, mr/x/auto]
                )
wp_endpoint = oj.create_endpoint(key="calendar",
                                 childs = [ tlc                                          
                                     
                                           ],
                                 
                                 title="Slider Demo"
                                 )
oj.add_jproute("/", wp_endpoint)
                
