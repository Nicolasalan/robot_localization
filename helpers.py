def normalize(grid):
    """
    Dada uma grade de probabilidades não normalizadas, calcula o
    corresponde à versão normalizada dessa grade.
    """
    total = 0.0
    for row in grid:
        for cell in row:
            total += cell
    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            grid[i][j] = float(cell) / total
    return grid


def blur(grid, blurring):
    """
    Distribui a probabilidade em uma grade usando uma janela desfocada 3x3.
    O parâmetro de desfoque controla o quanto de uma crença se espalha
    em células adjacentes. Se o desfoque for 0, esta função terá
    nenhum efeito.
    """
    height = len(grid)
    width  = len(grid[0])

    center_prob = 1.0-blurring
    corner_prob = blurring / 12.0
    adjacent_prob = blurring / 6.0

    window = [
            [corner_prob,  adjacent_prob,  corner_prob],
            [adjacent_prob, center_prob,  adjacent_prob],
            [corner_prob,  adjacent_prob,  corner_prob]
        ]
    new = [[0.0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            grid_val = grid[i][j]
            for dx in range(-1,2):
                for dy in range(-1,2):
                    mult = window[dx+1][dy+1]
                    new_i = (i + dy) % height
                    new_j = (j + dx) % width
                    new[new_i][new_j] += mult * grid_val
    return normalize(new)

def is_robot_localized(beliefs, true_pos):
    """
    Retorna None se o robô não tiver uma "opinião forte" sobre
    sua crença. O robô tem uma opinião forte quando o
    o tamanho de sua melhor crença é maior que o dobro do tamanho de
    sua segunda melhor crença.

    Se TEM uma opinião forte, então esta função retorna
    Verdadeiro se essa opinião estiver correta e Falso se não estiver.
    """
    best_belief = 0.0
    best_pos = None
    second_best = 0.0
    for y, row in enumerate(beliefs):
        for x, belief in enumerate(row):
            if belief > best_belief:
                second_best = best_belief
                best_belief = belief
                best_pos = (y,x)
            elif belief > second_best:
                second_best = belief
    if second_best <= 0.00001 or best_belief / second_best > 2.0:
        # robô pensa que sabe onde está
        localized = best_pos == true_pos
        return localized, best_pos
    else:
        # Nenhuma crença forte e única
        return None, best_pos

def close_enough(g1, g2):
    if len(g1) != len(g2):
        return False
    if len(g1) == 0 or len(g1[0]) != len(g2[0]):
        return False
    for r1, r2 in zip(g1,g2):
        for v1, v2 in zip(r1, r2):
            if abs(v1 - v2) > 0.001:
                print(v1, v2)
                return False
    return True
