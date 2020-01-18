from my_planning_graph import PlanningGraph
from air_cargo_problems import air_cargo_p1


ac_problem = air_cargo_p1()
ac_pg_serial = PlanningGraph(ac_problem, ac_problem.initial).fill()
# In(C1, P2) and In(C2, P1) have inconsistent support when they first appear in
# the air cargo problem, 
inconsistent_support_literals = [expr("In(C1, P2)"), expr("In(C2, P1)")]