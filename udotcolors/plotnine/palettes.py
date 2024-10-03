from ..colors import get_color
from ..palettes import get_palette_qual, get_palette_seq, get_palette_div
import matplotlib.colors as mcolors
import plotnine
import ColorKit as ck
import pprint


def _palette_gen(
    palette="main",
    reverse=False,
    # backward=False,
):
    def f(n):
        if n > len(get_palette_qual(palette)):
            raise Exception(
                "Not enough colors in this palette!\n"
                + 'Number of colors in palette "'
                + palette
                + '": '
                + str(len(get_palette_qual(palette)))
                + "\n"
                + "Number of colors asked for: "
                + str(n)
            )

        colors = get_palette_qual(palette)
        # if backward:
        #     colors.reverse()
        pal = colors[:n]
        if reverse:
            pal.reverse()
        return pal

    return f


def _palette_gen_seq(palette=None, colorlist=None, reverse=False):

    map_name = palette if colorlist is None else "colorlist"

    if palette is not None and colorlist is not None:
        raise UserWarning(
            "Both `palette` and `colorlist` specified. Will use `colorlist`."
        )

    if colorlist is None:
        if palette is None:
            raise ValueError("Specify one of `palette` or `colorlist`")
        else:
            colorlist = get_palette_seq(palette)

    if reverse:
        colorlist.reverse()

    def f():
        pal = mcolors.LinearSegmentedColormap.from_list(map_name, colorlist)
        return pal

    return f
