import ofjustpy as oj
from meltui_components.components import Slider,Avatar
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

slider= Slider()

avatar = Avatar(src = 'https://avatars.githubusercontent.com/u/1162160?v=4')

app = oj.load_app()

tlc = oj.PD.Container(childs=[#slider,
    avatar
                                     
                        ],
                twsty_tags=[space/y/4, mr/x/auto]
                )
wp_endpoint = oj.create_endpoint(key="slider",
                                 childs = [ tlc                                          
                                     
                                           ],
                                 
                                 title="Slider Demo"
                                 )
oj.add_jproute("/", wp_endpoint)
                
