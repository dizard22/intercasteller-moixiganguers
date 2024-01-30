import reflex as rx


def _get_players(players: list) -> str:
    html_players = ""
    for p in players:
        html_players += f"""
        <li> class="accordion-item">
            <img src="/jugadors/{p}.jpg">
             <div class="content">
                <span>
                    <h2>{p}</h2>
                </span>
            </div>
        </li>"""
    return html_players


def carousel(players: list) -> rx.Component:
    return rx.html(
        f"""<ul class="accordion">
        {_get_players(players)}
        </ul>"""
    )
