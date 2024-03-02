from simulate import Simulation
import simulate as sim
import helpers

def test_robot_works_in_rectangle_world():
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
    for i in range(1000):
        simulation = sim.Simulation(grid, blur, p_hit)
        simulation.run(1)

test_robot_works_in_rectangle_world()
