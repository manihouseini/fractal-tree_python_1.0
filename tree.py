import math
import pygame


def draw_tree(win, x, y, depth=3, length=10, offset=45, first=True, angle=0):
    if first:
        first = False
        x2 = x
        y2 = y - length
        pygame.draw.line(win, (255, 255, 255), (x, y), (x2, y2), 1)
        draw_tree(win, x2, y2, depth - 1, length * 0.8, offset, first, angle + offset)
    elif depth <= 0:
        return
    else:
        right_x = math.cos(math.radians(angle - 90)) * length + x
        right_y = math.sin(math.radians(angle - 90)) * length + y
        left_x = math.cos(math.radians(-angle - 90)) * length + x
        left_y = math.sin(math.radians(-angle - 90)) * length + y
        pygame.draw.line(win, (255, 255, 255), (x, y), (right_x, right_y), 1)
        pygame.draw.line(win, (255, 255, 255), (x, y), (left_x, left_y), 1)
        draw_tree(
            win,
            right_x,
            right_y,
            depth - 1,
            length * 0.8,
            offset,
            first,
            angle + offset,
        )
        draw_tree(
            win, left_x, left_y, depth - 1, length * 0.8, offset, first, angle + offset
        )
