import flet as ft

def main(page: ft.Page):

    container_color = "#bfbfbf"
    page.window_width=800
    page.window_height=600
    page.window_resizable = False
    page.window_title = "Blotto War"

    page.add(
        ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text("3", size=25, color='black',text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),
                border_radius=90,
                width=97,
                height=97,
                bgcolor=ft.colors.RED_200,
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                ft.Container(
                    content=
                        ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                            ft.Text("2", size=25, color="#8b0000",weight=ft.FontWeight.BOLD),
                            ft.Text("Battlefield 1",size=20,color='black'),
                            ft.Text("0", size=25, color="#023020",weight=ft.FontWeight.BOLD),
                        ]),   
                    width=206,
                    height=285,
                    border_radius=20,
                    padding=ft.padding.all(20),
                    bgcolor=container_color,
                    ink=True,
                    on_click=lambda e: print("Clickity 1"),
                ),
                ft.Container(
                    content=
                        ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                            ft.Text("1", size=25, color="#8b0000",weight=ft.FontWeight.BOLD),
                            ft.Text("Battlefield 2",size=20,color='black'),
                            ft.Text("1", size=25, color="#023020",weight=ft.FontWeight.BOLD),
                        ]),   
                    width=206,
                    height=285,
                    border_radius=20,
                    padding=ft.padding.all(20),
                    bgcolor=container_color,
                    ink=True,
                    on_click=lambda e: print("Clickity 2"),
                ),
                ft.Container(
                    content=
                        ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                            ft.Text("0", size=25, color="#8b0000",weight=ft.FontWeight.BOLD),
                            ft.Text("Battlefield 3",size=20,color='black'),
                            ft.Text("0", size=25, color="#023020",weight=ft.FontWeight.BOLD),
                        ]),   
                    width=206,
                    height=285,
                    border_radius=20,
                    padding=ft.padding.all(20),
                    bgcolor=container_color,
                    ink=True,
                    on_click=lambda e: print("Clickity 3"),
                )
            ]),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                ft.ElevatedButton(
                    content=ft.Text("Reset", size=20, color='black',text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),
                    style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.BLUE_200,
                            ft.MaterialState.HOVERED: ft.colors.RED_400,
                        },
                        padding=ft.padding.only(43,20,43,20),
                    )
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("5", size=25, color='black',text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),
                    border_radius=90,
                    width=97,
                    height=97,
                    bgcolor=ft.colors.GREEN_200,
                ),
                ft.ElevatedButton(
                    content=ft.Text("End turn", size=20, color='black',text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),
                    style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.BLUE_200,
                            ft.MaterialState.HOVERED: ft.colors.GREEN_500,
                        },
                        padding=ft.padding.only(30,20,30,20),
                    ),
                    on_click=lambda e: print("Clickity End turn"),
                )
            ])
        ])
    )

ft.app(target=main)