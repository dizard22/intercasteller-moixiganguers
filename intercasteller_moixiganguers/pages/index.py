import reflex as rx

import intercasteller_moixiganguers.constants as const
import intercasteller_moixiganguers.styles.styles as styles
import intercasteller_moixiganguers.utils as utils
from intercasteller_moixiganguers.components.carousel import carousel
from intercasteller_moixiganguers.components.footer import footer
from intercasteller_moixiganguers.components.parallax import parallax
from intercasteller_moixiganguers.components.title import title
from intercasteller_moixiganguers.styles.styles import Size


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        # navbar(),
        parallax(),
        rx.box(
            rx.center(
                rx.vstack(
                    title("Porters"),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    padding=Size.MEDIUM.value
                )
            ),
            carousel(const.porters),
            rx.center(
                rx.vstack(
                    title("Defenses"),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    padding=Size.MEDIUM.value
                )
            ),
            carousel(const.defenses),
            rx.center(
                rx.vstack(
                    title("Migcampistes"),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    padding=Size.MEDIUM.value
                )
            ),
            carousel(const.migs),
            rx.center(
                rx.vstack(
                    title("Davanters"),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    padding=Size.MEDIUM.value
                )
            ),
            carousel(const.devanters),
            rx.center(
                rx.vstack(
                    title("Seleccionadors"),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    padding=Size.MEDIUM.value
                )
            ),
            carousel(const.seleccionadors),
            footer(),
            z_index="8"
        ),
        class_name="wrapper"
    )
