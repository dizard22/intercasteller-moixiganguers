import reflex as rx
import intercasteller_moixiganguers.styles.styles as styles
from intercasteller_moixiganguers.routes import Route
from intercasteller_moixiganguers.styles.styles import Size
from intercasteller_moixiganguers.styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="/icons/moixiganguers.svg",
            alt="Moixiganguers",
            width=Size.INTERMEDIATE.value,
            height=Size.INTERMEDIATE.value
        ),
        rx.link(
            rx.box(
                rx.span("moixi", color=Color.PRIMARY.value),
                rx.span("ganguers", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )
