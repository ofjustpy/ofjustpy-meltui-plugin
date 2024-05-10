
class DialogMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "dialog"

    Trigger = gen_Div_type_by_tag("Trigger", prefix="Dialog_")
    Content = gen_Div_type_by_tag("Content", prefix="Dialog_")
    Header = gen_Div_type_by_tag("Header", prefix="Dialog_")
    Title = gen_Div_type_by_tag("Title", prefix="Dialog_")
    Description = gen_Div_type_by_tag("Description", prefix="Dialog_")

Dialog = gen_Div_type(
    HCType.passive,
    "Dialog",
    DialogMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_dialog,
)
