from ofjustpy.Div_TF import gen_Div_type
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles
from ofjustpy_engine import HC_Div_type_mixins as TR

class SliderMixin:
    def __init__(self, **kwargs):
        """
        Initialize the MeltUI Slider mixin with the provided keyword arguments.

        Args:
            min (int): The minimum value of the slider. Defaults to 0.
            max (int): The maximum value of the slider. Defaults to 100.
            step (int): The amount to increment/decrement the value by when using the keyboard. Defaults to 1.
            orientation (str): The orientation of the slider. Either 'horizontal' or 'vertical'. Defaults to 'horizontal'.
            dir (str): The direction of the slider. Either 'ltr' or 'rtl'. Defaults to 'ltr'.
            disabled (bool): Whether or not the slider is disabled. Defaults to False.
            defaultValue (list): The default value of the slider. Pass in multiple values for multiple thumbs, creating a range slider. Defaults to an empty list.
            value (any): A writable store that can be used to update the slider value. Defaults to None.
            onValueChange (function): A callback that is called when the value of the slider changes. Defaults to None.
        """
        self.domDict.vue_type= "meltui_component"
        self.domDict.html_tag = "slider"
        for key in ['min', 'max', 'step', 'orientation', 'dir', 'disabled', 'defaultValue', 'value', 'onValueChange']:
            if key in kwargs:
                self.attrs[key] = kwargs[key]


Slider = gen_Div_type(
        HCType.passive,
        "Slider",
        SliderMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.meltui_slider,
        )                                

class AvatarMixin:
    def __init__(self, **kwargs):
        """
        Initialize the Avatar mixin with the provided keyword arguments.

        Args:
            src (str): The source of the image to display. Defaults to an empty string.
            delayMs (int): The amount of time in milliseconds to wait before displaying the image. Defaults to 0.
        """
        self.domDict.vue_type= "meltui_component"
        self.domDict.html_tag = "avatar"
        for key in ['src', 'delayMs', 'fallback_text']:
            if key in kwargs:
                self.attrs[key] =  kwargs.get(key),

        self.domDict.fallback_classes = "text-3xl font-medium text-magnum-700"
        self.domDict.root_classes = "flex h-16 w-16 items-center justify-center rounded-full bg-neutral-100"
        self.domDict.img_classes= "h-full w-full rounded-[inherit]"

    @property
    def fallback_classes(self):
        return self.domDict.get('fallback_classes', "text-3xl font-medium text-magnum-700")

    @fallback_classes.setter
    def fallback_classes(self, value):
        self.domDict['fallback_classes'] = value

    @property
    def root_classes(self):
        return self.domDict.get('root_classes', "flex h-16 w-16 items-center justify-center rounded-full bg-neutral-100")

    @root_classes.setter
    def root_classes(self, value):
        self.domDict['root_classes'] = value

    @property
    def img_classes(self):
        return self.domDict.get('img_classes', "h-full w-full rounded-[inherit]")

    @img_classes.setter
    def img_classes(self, value):
        self.domDict['img_classes'] = value
        
Avatar = gen_Div_type(
        HCType.passive,
        "Avatar",
        AvatarMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.meltui_avatar,
        )             

class CalendarMixin:
    def __init__(self, *args, **kwargs):
        self.domDict.vue_type= "meltui_component"
        self.domDict.html_tag = "calendar"

        
Calendar = gen_Div_type(
        HCType.passive,
        "Calendar",
        CalendarMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.meltui_calendar,
        )             


class CheckboxMixin:
    def __init__(self, **kwargs):
        """
        Initialize the CheckboxMixin with the provided keyword arguments.

        Args:
            disabled (bool): Whether or not the checkbox is disabled. Defaults to False.
            required (bool): Whether or not the checkbox is required. Defaults to False.
            name (str): The name of the checkbox. Defaults to None.
            value (str): The value given as data when submitted with a name. Defaults to None.
            defaultChecked (bool | str): The default checked state of the checkbox. 'indeterminate' is used to indicate that the checkbox is in an indeterminate state. Defaults to False.
            checked (bool | str): The controlled checked state store of the checkbox. Defaults to None.
            onCheckedChange (function): A callback called when the value of the checked store should be changed. Defaults to None.
        """
        self.domDict.vue_type= "meltui_component"
        self.domDict.html_tag = "checkbox"        
        for key in [
            'disabled', 'required', 'name', 'value', 'defaultChecked', 'checked', 'onCheckedChange'
        ]:
            if key in kwargs:
                self.attrs[key] = kwargs[key]


        self.domDict.label_text = kwargs.get('label_text')

        self.domDict.root_classes = "flex items-center justify-center"
        self.domDict.button_classes = "flex size-7 appearance-none items-center justify-center rounded-lg bg-white text-magnum-600 shadow hover:opacity-75"
        self.domDict.label_classes= "pl-4 font-medium text-magnum-900"
        
Checkbox = gen_Div_type(
        HCType.active,
        "Checkbox",
        CheckboxMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.meltui_checkbox,
        )                             
from ofjustpy.htmlcomponents_impl import assign_id
Checkbox = assign_id(Checkbox)
