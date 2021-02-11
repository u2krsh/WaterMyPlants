from kivymd.app import MDApp

from kivy.animation import Animation

md_shrine = MDShrine()
md_shrine.opacity = 0
instance.add_widget(md_shrine)


def add_screen_shrine(MDShrine):
    def remove_box(*args):
        instance.remove_widget(box)

def show_demo_shrine(interval):
    from kivy.animation import Animation
    from studies.shrine.shrine import MDShrine


anim = Animation(opacity=0, d=0.5)
anim.bind(on_complete=remove_box)
anim.start(box)
Animation(opacity=2, d=0.5).start(md_shrine)
self.theme_cls.primary_palette = "Red"

def show_demo_shrine(interval):
    from kivy.animation import Animation
    from studies.shrine.shrine import MDShrine

    anim = Animation(
        size_hint=(0.2, 0.2), pos_hint={"center_y": 0.7}, d=0.5
    )
    anim.bind(on_complete=lambda *x: add_screen_shrine(MDShrine))
    anim.start(box)

class App(MDApp):
    def build(self):
        return anim.start(box)



App().run()
