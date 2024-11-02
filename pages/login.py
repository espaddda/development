import flet as ft
from flet_route import Params, Basket
from utils.style import *


class LoginPage:

    email_input = ft.Container(
        content=ft.TextField(label='Укажите Email',
                              bgcolor=secondaryBgColor,
                              border=ft.InputBorder.NONE,
                              filled=True,
                              color=secondaryFontColor),
        border_radius=15
    )
    password_input = ft.Container(
        content=ft.TextField(label='Укажите пароль',
                             password=True, can_reveal_password=True,
                             bgcolor=secondaryBgColor,
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color=secondaryFontColor),
        border_radius=15
    )

    def view(self, page: ft.page, params: Params, basket: Basket):
        page.title = 'Espaddda'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.minimum_width = 800
        page.window.minimum_height = 400
        page.fonts = {"Metroplex Shadow": "fonts/Metroplex Shadow.ttf"}

        signup_link = ft.Container(ft.Text('Создать аккаунт', color=defaultFontColor),
                                   on_click=lambda e: page.go('/signup'))

        return ft.View(
            "/",
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=2,
                            padding=ft.padding.all(40),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text('Приветствую',
                                            color=defaultFontColor,
                                            size=25,
                                            weight=ft.FontWeight.NORMAL,
                                            font_family='Metroplex Shadow'),
                                    self.email_input,
                                    self.password_input,
                                    ft.Container(
                                        ft.Text('Авторизация', color=defaultFontColor),
                                        alignment=ft.alignment.center, height=40, bgcolor=hoverBgColor
                                    ),
                                    signup_link,

                                ]
                            )
                        ),
                        ft.Container(
                            expand=3,
                            image_src='images/1234.png',
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(name=ft.icons.LOCK_PERSON_ROUNDED,
                                            color=hoverBgColor,
                                            size=140),
                                    ft.Text('Авторизация',
                                            color=hoverBgColor,
                                            size=15,
                                            weight=ft.FontWeight.BOLD)
                                ]
                            )
                        )
                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )