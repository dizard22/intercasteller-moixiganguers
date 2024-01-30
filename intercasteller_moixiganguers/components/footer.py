import reflex as rx

import intercasteller_moixiganguers.constants as const
from intercasteller_moixiganguers.styles.colors import TextColor
from intercasteller_moixiganguers.styles.styles import Size


# from intercasteller_moixiganguers.components.ant_components import float_button


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/latevacolla_blanc.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotip de Moixiganguers.",
            margin_top=Size.SMALL.value,
            margin_bottom=Size.SMALL.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/location.svg",
                    height=Size.MEDIUM.value,
                    width=Size.MEDIUM.value
                ),
                rx.text(
                    "Les Cotxeres, plaça Catalunya núm. 1, Igualada"
                )
            ),
            href=const.MOIXIS_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/phone.svg",
                    height=Size.MEDIUM.value,
                    width=Size.MEDIUM.value
                ),
                rx.text(
                    "693 71 46 59"
                )
            ),
            href=const.MOIXIS_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/email.svg",
                    height=Size.MEDIUM.value,
                    width=Size.MEDIUM.value
                ),
                rx.text(
                    "moixiganguers@moixiganguers.cat",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.EMAIL,
            is_external=True
        ),
        # float_button(
        #     icon=rx.Image(src="/icons/donate.svg"),
        #     href=const.COFFEE_URL
        # ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.ZERO.value,
        color=TextColor.FOOTER.value
    )
