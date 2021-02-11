![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/buttons.gif)

## Example of using MDButtons:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.theming import ThemeManager

Builder.load_string("""
<ExampleButtons@BoxLayout>:
    orientation: 'vertical'

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        background_palette: 'Primary'
        elevation: 10
        left_action_items: [['dots-vertical', lambda x: None]]

    ScrollView:
        size_hint_x: None
        width: box.width
        pos_hint: {'center_x': .5}
        bar_width: 0

        BoxLayout:
            id: box
            padding: dp(10)
            size_hint: None, None
            size: self.minimum_size
            spacing: dp(10)
            orientation: 'vertical'
            pos_hint: {'center_x': .5}

            BoxLayout:
                size_hint: None, None
                width: self.minimum_width
                height: dp(56)
                spacing: '10dp'



                MDFillRoundFlatButton:
                   text: "atButton"
                   pos_hint: {'center_x': .5}MDFillRoundFl




""")


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = "Example Buttons"
    main_widget = None

    def build(self):
        return Factory.ExampleButtons()


if __name__ == "__main__":
    Example().run()
```