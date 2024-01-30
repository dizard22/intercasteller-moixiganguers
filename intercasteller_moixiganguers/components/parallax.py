import reflex as rx


def parallax() -> rx.Component:
    return rx.html(
        f"""
      <div class="parallax__group hero-container">
        <div class="parallax__layer sky"></div>
        <div class="parallax__layer hero-text">
          <h2>Selecció Morada</h2>
          <ul>
            <li><a href="https://www.moixiganguers.cat/" target="_blank" class="btn">Moixiganguers</a></li>
          </ul>
        </div>
      </div>      
      <div class="info-container">
        <div class="text-container">
          <h2>Els jugadors seleccionats pel torneig de Berga 2024 son:</h2>
        </div>
      </div>
        """
    )
