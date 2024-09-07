from flet import Page, SafeArea, Container, Column, Row, Text, TextField, AppView, app, MainAxisAlignment, CrossAxisAlignment


def main(page: Page) -> None:

    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.title = "Color change"

    color_text = Text("", color="")

    def on_color_change(e):
        color_text.value = e.control.value
        color_text.color = e.control.value
        page.update()

    InputField = TextField(hint_text="Enter color name", width=300, on_change=on_color_change)

    page.add(
        SafeArea(
            Column(
                controls=[
                    InputField,
                    color_text
                ],
                # alignment=MainAxisAlignment.CENTER
            )
        )
    )


if __name__ == "__main__":
    app(target=main, view=AppView.WEB_BROWSER, port=50724)
