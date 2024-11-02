import flet as ft
from flet_route import Params, Basket
from utils.style import *
from utils.Validation import Validation
import time


class SignupPage:
    validation = Validation()

    error_filed = ft.Text(' ', color='red')
    email_input = ft.Container(
        content=ft.TextField(label='Укажите Email',
                             bgcolor=secondaryBgColor,
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color=secondaryFontColor),
        border_radius=15
    )

    login_input = ft.Container(
        content=ft.TextField(label='Укажите логин',
                             bgcolor=secondaryBgColor,
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color=secondaryFontColor),
        border_radius=15
    )

    password_input = ft.Container(content=ft.TextField(label='Пароль', password=True, can_reveal_password=True,
                                                       bgcolor=secondaryBgColor, border=ft.InputBorder.NONE, filled=True,
                                                       color=secondaryFontColor), border_radius=15)

    Confpassword_input = ft.Container(content=ft.TextField(label='Подтвердите пароль', password=True, can_reveal_password=True,
                                                       bgcolor=secondaryBgColor, border=ft.InputBorder.NONE,
                                                       filled=True,
                                                       color=secondaryFontColor), border_radius=15)

    def view(self, page: ft.page, params: Params, basket: Basket):
        page.title = 'Регистрация'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.minimum_width = 800
        page.window.minimum_height = 400
        page.fonts = {"Metroplex Shadow": "fonts/Metroplex Shadow.ttf"}

        def signup(e):
            email_value = self.email_input.content.value
            login_value = self.login_input.content.value
            password_value = self.password_input.content.value
            confpassword_value = self.Confpassword_input.content.value
            if email_value and login_value and password_value and confpassword_value:
                if not self.validation.is_valid_email(email_value):
                    self.email_input.content.bgcolor=inputBgErrorColor
                    self.error_filed.value = 'Поле Email не соотвествует формату'
                    self.error_filed.size = 12
                    self.email_input.update()
                    self.error_filed.update()
                    time.sleep(1)
                    self.error_filed.size = 0
                    self.email_input.content.bgcolor= inputBgColor
                    self.error_filed.update()
                    self.email_input.update()
                elif not self.validation.is_valid_password(password_value):
                    self.error_filed.value = 'Пароль не соотвествует формату ( более 5 символов )'
                    self.error_filed.size = 12
                    self.error_filed.update()
                    time.sleep(1)
                    self.error_filed.size = 0
                    self.error_filed.update()
                elif password_value != confpassword_value:
                    self.error_filed.value = 'Пароли не совпадают'
                    self.error_filed.size = 12
                    self.error_filed.update()
                    time.sleep(1)
                    self.error_filed.size = 0
                    self.error_filed.update()
                else:
                    self.error_filed.value = 'Вы успешно зарегистрировались'
                    self.error_filed.size = 12
                    self.error_filed.color = ft.colors.GREEN
                    self.error_filed.update()
                    time.sleep(4)
                    page.go('/')
            else:
                self.error_filed.value = 'Заполните все поля'
                self.error_filed.size = 12
                self.error_filed.update()
                time.sleep(1)
                self.error_filed.size = 0
                self.error_filed.update()

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
                                    ft.Text('Добавить аккаунт',
                                            color=defaultFontColor,
                                            size=25,
                                            weight=ft.FontWeight.NORMAL,
                                            font_family='Metroplex Shadow'),
                                    self.error_filed,
                                    self.email_input,
                                    self.login_input,
                                    self.password_input,
                                    self.Confpassword_input,
                                    ft.Container(
                                        ft.Text('Зарегистрироваться', color=defaultFontColor),
                                        alignment=ft.alignment.center, height=40, bgcolor=hoverBgColor,
                                        on_click=lambda e: signup(e)
                                    ),

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
                                    ft.Icon(name=ft.icons.VERIFIED_USER_ROUNDED,
                                            color=hoverBgColor,
                                            size=140),
                                    ft.Text('Форма регистрации',
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