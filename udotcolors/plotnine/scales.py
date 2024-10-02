import plotnine
from .palettes import _palette_gen


def scale_color_udot(
    palette="main",
    reverse=False,
    # backward=False,
):
    scale = plotnine.scales.scale_discrete.scale_discrete(
        aesthetics="color",
        palette=_palette_gen(
            palette=palette,
            reverse=reverse,
            # backward=backward,
        ),
    )
    return scale


scale_colour_udot = scale_color_udot
