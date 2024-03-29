from helpers import normalize, blur
import numpy as np
import pdb

def initialize_beliefs(grid):
    """
    retorna uma distribuicao de probalidade (crenca) inicial para um grid
    """
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs # precisa somar 1.0 total

def sense(color, grid, beliefs, p_hit, p_miss):
    """
    Atualiza as crencas do robo para cada celula do grid, baseado na cor da celula
    beliefs: crenca inicial
    p_hit: probabilidade de acerto
    p_miss: probabilidade de erro
    """
    new_beliefs = []

    height = len(grid)
    width = len(grid[0])

    for i in range(height):
        row = []
        for j in range(width):
            hit = (color == grid[i][j])
            row.append(beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss))
        new_beliefs.append(row)

    s = sum(map(sum, new_beliefs))

    # normaliza a distribuicao de probabilidade
    for i in range(height):
        for j in range(width):
            new_beliefs[i][j] = new_beliefs[i][j] / s

    return new_beliefs # distribuicao de probabilidade normalizada

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = int((i + dy) % height)
            new_j = int((j + dx) % width)
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
