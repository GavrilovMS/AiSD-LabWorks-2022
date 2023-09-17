from Binary_tree import *
import pygame

def main():
    WIDTH = 1000
    HEIGHT = 800
    FPS = 30
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    tree = Binary_tree()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tree")
    clock = pygame.time.Clock()
    running = True

    input_box = pygame.Rect(15, 750, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    font = pygame.font.Font('freesansbold.ttf', 20)

    dif = WIDTH // 2

    def __traverse(Node, x, y, last_x, last_y, dif):
        if Node == None:
            return
        if Node != tree.root:
            pygame.draw.line(screen, WHITE, (x, y - 21), (last_x, last_y))
        pygame.draw.circle(screen, RED, (x, y), 20, 2)
        text1 = str(Node.data)
        text_obj = font.render(text1, True, WHITE)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_obj, text_rect)
        __traverse(Node.left, (x - dif), y + 100, x, y + 20, dif // 2)
        __traverse(Node.right, (x + dif), y + 100, x, y + 20, dif // 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        text = text.split()
                        if text[0] == 'new':
                            with open (text[1], 'r') as f:
                                new_str = f.read()
                                tree = Binary_tree(new_str)
                        elif text[0] == 'getbinarysearch':
                            tree.get_binary_search_tree()
                        elif text[0] == 'search':
                            tree.search(int(text[1]))
                        elif text[0] == 'balance':
                            tree.balance_tree()
                            tree.balance_tree()
                        elif text[0] == 'insert':
                            tree.insert(int(text[1]))
                        elif text[0] == 'delete':
                            tree.remove(int(text[1]))
                        elif text[0] == 'BFS':
                            tree.BFS()
                        elif text[0] == 'DFS':
                            if text[1] == 's':
                                tree.DFS_straight()
                            elif text[1] == 'c':
                                tree.DFS_centered()
                            elif text[1] == 'r':
                                tree.DFS_reverse()
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill((30, 30, 30))
        __traverse(tree.root, WIDTH // 2, 20, WIDTH // 2, 20, dif // 2)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
