# Search methods

import search

ab = search.GPSProblem('N', 'L'
                       , search.romania)

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())
print("Busqueda A-B")
print("Ramificacion y acotación: ")
print(search.branch_and_bound_search(ab).path())
print("Ramificacion y acotacióncon subestimacion: ")
print(search.branch_and_bound_underestimation(ab).path())

tn = search.GPSProblem('T', 'N'
                       , search.romania)

print("Busqueda T-N")
print("Ramificacion y acotación: ")
print(search.branch_and_bound_search(tn).path())
print("Ramificacion y acotacióncon subestimacion: ")
print(search.branch_and_bound_underestimation(tn).path())

go = search.GPSProblem('G', 'O'
                       , search.romania)

print("Busqueda G-O")
print("Ramificacion y acotación: ")
print(search.branch_and_bound_search(go).path())
print("Ramificacion y acotacióncon subestimacion: ")
print(search.branch_and_bound_underestimation(go).path())
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
