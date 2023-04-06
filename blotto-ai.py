import flet as ft
from anytree import Node, RenderTree
#bf1r = battletfield 1 red
#bf2g = battletfield 2 green
bf1r = 0
bf2r = 0
bf3r = 0
bf1g = 0
bf2g = 0
bf3g = 0

rt = 12
gt = 12
turn = 0

def main(page: ft.Page):

    global bf1g, bf2g, bf3g, bf1r, bf2r, bf3r, rt, gt, turn
    
    def bf1click(e):
        global bf1g
        global gt
        global turn
        if(turn < 2):
            bf1g=bf1g+1
            gt=gt-1
            turn=turn+1
            bf1_text_g.value=str(bf1g)
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
            bf2_text_g.value=str(bf2g)
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
            bf3_text_g.value=str(bf3g)
            g_text.value=str(gt)
            page.update()
            print("Bf3 is now " + str(bf3g))
        else:
            print("You can only move 2 troops this turn")
    def end_turn(e):
        global turn
        if(turn!=2):
            print("Move 2 troops before ending turn")
            return 0
        check_win()
        turn = 0
        print("Turn ended")
        pc_turn()
    def check_win():
        if(((bf1g>bf1r and bf2g>bf2r) or (bf1g>bf1r and bf3g>bf3r) or (bf2g>bf2r and bf3g>bf3r))and rt+gt==0):
            print("Human wins")
        elif(((bf1g<bf1r and bf2g<bf2r) or (bf1g<bf1r and bf3g<bf3r) or (bf2g<bf2r and bf3g<bf3r))and rt+gt==0):
            print("AI wins")
        elif(rt+gt==0):
            print("Draw")
        
    
    def pc_turn():
        global bf1g, bf2g, bf3g, bf1r, bf2r, bf3r, rt, gt
        h = 0
        root = Node([bf1g,bf2g,bf3g,bf1r,bf2r,bf3r,rt,gt,h])
        nodes = []
        # nodes 0-5 1st level
        # nodes 6-41 2nd level
        # nodes 42-257 3rd level
        # nodes 258-1511 4th level

        def generate_next_level():
            i=0
            j=0
            b=0
            x=0
            y=0
            if(len(nodes)==6):
                print("lentgh is 6")
                b=5
                x=0
                y=2
            elif(len(nodes)==42):
                print("length is 42")
                j=6
                b=41
                x=2
                y=0
            elif(len(nodes)==258):
                print("length is 258")
                j=42
                b=257
                x=0
                y=2
            for n in nodes[j:]:
                nodes.append(Node([n.name[0]+2,n.name[1],n.name[2],n.name[3],n.name[4],n.name[5],n.name[6]-y,n.name[7]-x,h],parent=n))
                nodes.append(Node([n.name[0],n.name[1]+2,n.name[2],n.name[3],n.name[4],n.name[5],n.name[6]-y,n.name[7]-x,h],parent=n))
                nodes.append(Node([n.name[0],n.name[1],n.name[2]+2,n.name[3],n.name[4],n.name[5],n.name[6]-y,n.name[7]-x,h],parent=n))

                nodes.append(Node([n.name[0]+1,n.name[1]+1,n.name[2],n.name[3],n.name[4],n.name[5],n.name[6]-y,n.name[7]-x,h],parent=n))
                nodes.append(Node([n.name[0]+1,n.name[1],n.name[2]+1,n.name[3],n.name[4],n.name[5],n.name[6]-y,n.name[7]-x,h],parent=n))
                nodes.append(Node([n.name[0],n.name[1]+1,n.name[2]+1,n.name[3],n.name[4],n.name[5],n.name[6]-y,n.name[7]-x,h],parent=n))
                i=i+1
                if(i>b):
                    break
        
        def h_function():
            for n in nodes:
                h=0.00
                for i in range(3):
                    if(n.name[i]>n.name[i+3]):
                        h=h+1
                n.name[8]=h
            #for n in nodes[:6]:
            #    if n.children is not None:
            #        for n2 in n.children:
            #            n.name[8]=n.name[8]+n2.name[8]
            #            if n2.children is not None:
            #                for n3 in n2.children:
            #                    n.name[8]=n.name[8]+n3.name[8]
            #                    if n3.children is not None:
            #                        for n4 in n3.children:
            #                            n.name[8]=n.name[8]+n4.name[8]
        def best_move():
            best_move = nodes[0]
            for n in nodes[:6]:
                if n.name[8]>best_move.name[8]:
                    best_move = n
            return best_move
        def execute_move():
            global bf1r, bf2r, bf3r, rt
            bf1r = best_move().name[3]
            bf2r = best_move().name[4]
            bf3r = best_move().name[5]
            rt = rt-2
            bf1_text_r.value = str(bf1r)
            bf2_text_r.value = str(bf2r)
            bf3_text_r.value = str(bf3r)
            r_text.value = str(rt)
            page.update()
            check_win()
            print("AI moved troops")
        #bf1g = 0
        #bf2g = 1
        #bf3g = 2
        #bf1r = 3
        #bf2r = 4
        #bf3r = 5
        #rt = 6
        #gt = 7
        #h = 8
        # add 2 to one of the battlefields
        nodes.append(Node([bf1g,bf2g,bf3g,bf1r+2,bf2r,bf3r,rt-2,gt,h],parent=root))
        nodes.append(Node([bf1g,bf2g,bf3g,bf1r,bf2r+2,bf3r,rt-2,gt,h],parent=root))
        nodes.append(Node([bf1g,bf2g,bf3g,bf1r,bf2r,bf3r+2,rt-2,gt,h],parent=root))

        # add 1 to two of the battlefields
        nodes.append(Node([bf1g,bf2g,bf3g,bf1r+1,bf2r+1,bf3r,rt-2,gt,h],parent=root))
        nodes.append(Node([bf1g,bf2g,bf3g,bf1r+1,bf2r,bf3r+1,rt-2,gt,h],parent=root))
        nodes.append(Node([bf1g,bf2g,bf3g,bf1r,bf2r+1,bf3r+1,rt-2,gt,h],parent=root))
        if(rt-2+gt==0):
            #this is the last turn
            h_function()
            print("end reached")
            best_move()
            execute_move()
            return 0
        generate_next_level()
        if(rt-2+gt-2==0):
            h_function()
            print("end reached")
            best_move()
            execute_move()
            return 0
        print("First tree: \n")
        print(RenderTree(root))
        generate_next_level()
        if(rt-4+gt-2==0):
            print("end reached")
            h_function()
            best_move()
            execute_move()
            return 0
        print("\n")
        print("Second tree: \n")
        print(RenderTree(root))
        print("\n")
        generate_next_level()
        if(rt-4+gt-4==0):
            print("end reached")
            h_function()
            best_move()
            execute_move()
            return 0
        print("Third tree: \n")
        print(RenderTree(root))
        h_function()
        print(RenderTree(root))
        print(best_move().name)
        execute_move()

             

    bf1_text_g = ft.Text(value=bf1g, size=25, color="#023020",weight=ft.FontWeight.BOLD)
    bf2_text_g = ft.Text(value=bf2g, size=25, color="#023020",weight=ft.FontWeight.BOLD)
    bf3_text_g = ft.Text(value=bf3g, size=25, color="#023020",weight=ft.FontWeight.BOLD)
    g_text = ft.Text(value=gt, size=25, color='black',text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)
    r_text = ft.Text(value=rt, size=25, color='black',text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)

    bf1_text_r = ft.Text(value=bf1r, size=25, color="#8b0000",weight=ft.FontWeight.BOLD)
    bf2_text_r = ft.Text(value=bf2r, size=25, color="#8b0000",weight=ft.FontWeight.BOLD)
    bf3_text_r = ft.Text(value=bf3r, size=25, color="#8b0000",weight=ft.FontWeight.BOLD)

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
                content=r_text,
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
                            bf1_text_r,
                            ft.Text("Battlefield 1",size=20,color='black'),
                            bf1_text_g
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
                            bf2_text_r,
                            ft.Text("Battlefield 2",size=20,color='black'),
                            bf2_text_g
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
                            bf3_text_r,
                            ft.Text("Battlefield 3",size=20,color='black'),
                            bf3_text_g,
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