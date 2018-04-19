
###################################################### Use Custom Theme

html_theme = 'oods'
html_theme_path = [os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'themes')]


###################################################### Pygments Style
# https://stackoverflow.com/questions/48615629/how-to-include-pygments-styles-in-a-sphinx-project
"""
class OODSStyle(Style):
    background_color = "#fbfbfb"
    default_style = ""


def pygments_monkeypatch_style(mod_name, cls):
    import sys
    import pygments.styles
    cls_name = cls.__name__
    mod = type(__import__("os"))(mod_name)
    setattr(mod, cls_name, cls)
    setattr(pygments.styles, mod_name, mod)
    sys.modules["pygments.styles." + mod_name] = mod
    from pygments.styles import STYLE_MAP
    STYLE_MAP[mod_name] = mod_name + "::" + cls_name


pygments_monkeypatch_style("oods", OODSStyle)
pygments_style = "oods"
"""

