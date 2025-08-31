#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Rect, Surface
from code.Const import WIN_WIDTH, COLOR_WHITE, COLOR_LIGHT_BLUE, MENU_OPTIONS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load('./asset/menu.mp3')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(
                self.surf,
                self.rect
            )

            self.menu_text(
                text_size=50,
                text="Mountain",
                text_color=COLOR_WHITE,
                text_center_pos=(WIN_WIDTH / 2, 70)
            )
            self.menu_text(
                text_size=50,
                text="Shooter",
                text_color=COLOR_LIGHT_BLUE,
                text_center_pos=(WIN_WIDTH / 2, 120)
            )

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(
                    text_size=20,
                    text=MENU_OPTIONS[i],
                    text_color=COLOR_WHITE,
                    text_center_pos=(WIN_WIDTH / 2, 400 + 30 * i),
                )
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(
            self,
            text_size: int,
            text: str,
            text_color: tuple,
            text_center_pos: tuple
    ):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
