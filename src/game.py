import pygame
from const import *
from board import Board

class Game:

    def __init__(self):
        self.board = Board()

    def show_board(self, surface):

        # color the surface
        for row in range (ROWS):
            for column in range (COLS):

                if (row + column) % 2 == 0:
                    color = (244, 164, 96)
                else:
                    color = (106, 74, 60) 
                
                # place rectangles
                rect = (column * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)
    
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece =  self.board.squares[row][col].piece
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)

