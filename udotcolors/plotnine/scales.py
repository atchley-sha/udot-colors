import plotnine
from .palettes import _palette_gen, _palette_gen_seq

## Discrete scales ####


def scale_fill_udot(
    palette="main",
    reverse=False,
    # backward=False,
    **kwargs,
):
    scale = plotnine.scales.scale_discrete.scale_discrete(
        aesthetics="fill",
        palette=_palette_gen(
            palette=palette,
            reverse=reverse,
            # backward=backward,
        ),
        **kwargs,
    )
    return scale


def scale_color_udot(
    palette="main",
    reverse=False,
    # backward=False,
    **kwargs,
):
    scale = plotnine.scales.scale_discrete.scale_discrete(
        aesthetics="color",
        palette=_palette_gen(
            palette=palette,
            reverse=reverse,
            # backward=backward,
        ),
        **kwargs,
    )
    return scale


scale_colour_udot = scale_color_udot


## Sequential scales ####


def scale_fill_udot_seq(
    palette=None,
    colorlist=None,
    reverse=False,
    **kwargs,
):
    pal = _palette_gen_seq(palette=palette, colorlist=colorlist, reverse=reverse)
    scale = plotnine.scale_fill_gradientn(
        colors=pal()([x / 256 for x in range(257)]),
        **kwargs,
    )
    return scale


# def scale_color_udot_seq()

# scale_colour_udot_seq = scale_color_udot_seq


## Diverging scales

# def scale_fill_udot_div()
# def scale_color_udot_div()

# scale_colour_udot_div = scale_color_udot_div
