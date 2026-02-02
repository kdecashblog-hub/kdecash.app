from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        layout.add_widget(Label(
            text="KdeCash",
            font_size=32
        ))

        layout.add_widget(Label(
            text="Controle financeiro simples",
            font_size=18
        ))

        btn = Button(text="Entrar", size_hint=(1, 0.2))
        btn.bind(on_press=self.ir_historico)

        layout.add_widget(btn)
        self.add_widget(layout)

    def ir_historico(self, *args):
        self.manager.current = "history"


class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20)

        layout.add_widget(Label(
            text="Histórico Financeiro",
            font_size=24
        ))

        layout.add_widget(Label(
            text="(Em breve lançamentos aqui)",
            font_size=16
        ))

        self.add_widget(layout)


class KdeCashApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(HistoryScreen(name="history"))
        return sm


if __name__ == "__main__":
    KdeCashApp().run()
