import flet as ft
#bf1r = battletfield 1 red
#bf2g = battletfield 2 green
bf1r = 0
bf2r = 0
bf3r = 0
bf1g = 0
bf2g = 0
bf3g = 0

rt = 6
gt = 6
turn = 0

def main(page: ft.Page):

    global bf1g
    global bf2g
    global bf3g
    global rt
    global gt
    def bf1click(e):
        global bf1g
        global gt
        global turn
        if(turn < 2):
            bf1g=bf1g+1
            gt=gt-1
            turn=turn+1
            bf1_text.value=str(bf1g)
            g_text.value=str(gt)
            page.update()
            print("Bf1 is now " + str(bf1g))
        else:
            print("You can only move 2 troops this turn")
        
    def bf2click(e):
        global bf2g
        global gt
        global turn
        if(turn < 2):
            bf2g=bf2g+1
            gt=gt-1
            turn=turn+1
            bf2_text.value=str(bf2g)
            g_text.value=str(gt)
            page.update()
            print("Bf2 is now " + str(bf2g))
        else:
            print("You can only move 2 troops this turn")
    def bf3click(e):
        global bf3g
        global gt
        global turn
        if(turn < 2):
            bf3g=bf3g+1
            gt=gt-1
            turn=turn+1
            bf3_text.value=str(bf3g)
            g_text.value=str(gt)
            page.update()
            print("Bf3 is now " + str(bf3g))
        else:
            print("You can only move 2 troops this turn")
    def end_turn(e):
        global turn
        turn = 0
        print("Turn ended")
        

    bf1_text = ft.Text(value=bf1g, size=25, color="#023020",weight=ft.FontWeight.BOLD)
    bf2_text = ft.Text(value=bf2g, size=25, color="#023020",weight=ft.FontWeight.BOLD)
    bf3_text = ft.Text(value=bf3g, size=25, color="#023020",weight=ft.FontWeight.BOLD)
    g_text = ft.Text(value=gt, size=25, color='black',text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)

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
                            bf1_text
                        ]),   
                    width=206,
                    height=285,
                    border_radius=20,
                    padding=ft.padding.all(20),
                    bgcolor=container_color,
                    ink=True,
                    on_click=bf1click,
                ),
                ft.Container(
                    content=
                        ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                            ft.Text("1", size=25, color="#8b0000",weight=ft.FontWeight.BOLD),
                            ft.Text("Battlefield 2",size=20,color='black'),
                            bf2_text
                        ]),   
                    width=206,
                    height=285,
                    border_radius=20,
                    padding=ft.padding.all(20),
                    bgcolor=container_color,
                    ink=True,
                    on_click=bf2click,
                ),
                ft.Container(
                    content=
                        ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                            ft.Text("0", size=25, color="#8b0000",weight=ft.FontWeight.BOLD),
                            ft.Text("Battlefield 3",size=20,color='black'),
                            bf3_text,
                        ]),   
                    width=206,
                    height=285,
                    border_radius=20,
                    padding=ft.padding.all(20),
                    bgcolor=container_color,
                    ink=True,
                    on_click=bf3click,
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
                    content=g_text,
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
                    on_click=end_turn,
                )
            ])
        ])
    )

ft.app(target=main)