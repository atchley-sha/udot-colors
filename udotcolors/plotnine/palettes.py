from ..colors import get_color, get_palette
import matplotlib as mpl
import plotnine
import ColorKit as ck
import pprint
import warnings


def _palette_gen(
    palette="main",
    reverse=False,
    # backward=False,
):
    def f(n):
        if n > len(get_palette(palette)):
            warnings.warn("Not enough colors in this palette!")
        else:
            colors = get_palette(palette)
            # if backward:
            #     colors.reverse()
            pal = colors[:n]
            if reverse:
                pal.reverse()
            return pal

    return f
