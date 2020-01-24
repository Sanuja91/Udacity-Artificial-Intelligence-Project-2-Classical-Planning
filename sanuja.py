from my_planning_graph import PlanningGraph
from air_cargo_problems import air_cargo_p1


problem = air_cargo_p1()
pg = PlanningGraph(problem, problem.initial).fill()
# In(C1, P2) and In(C2, P1) have inconsistent support when they first appear in
# the air cargo problem, 
score = pg.h_maxlevel()