from thlr_automata import *

B=ENFA([0, 1, 2, 3], [0], [2], ["a", "b"], ((0, "a", 1), (0, "b", 2), (3, "a", 2), (2, "b", 2)))
B.export("B")
