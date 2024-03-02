import simulate as sim
import helpers
import localizer

R = 'r'
G = 'g'

grid = [
    [R,G,G,G,R,R,R],
    [G,G,R,G,R,G,R],
    [G,R,G,G,G,G,R],
    [R,R,G,R,G,G,G],
]

blur = 0.001
p_hit = 100.0
simulation = sim.Simulation(grid, blur, p_hit)

simulation.run(1)
simulation.show_beliefs()

for i in range (0,20):
    simulation.run(1)

simulation.show_beliefs()
