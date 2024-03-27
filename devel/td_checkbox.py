import ofjustpy as oj
from meltui_components.components import Checkbox
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

checkbox = Checkbox(key="acheckbox", label_text="Got Milk")


app = oj.load_app()

tlc = oj.PD.Container(childs=[#slider,
    checkbox
                                     
                        ],
                twsty_tags=[space/y/4, mr/x/auto]
                )
wp_endpoint = oj.create_endpoint(key="checkbox",
                                 childs = [ tlc                                          
                                     
                                           ],
                                 
                                 title="Checkbox"
                                 )
oj.add_jproute("/", wp_endpoint)
                
