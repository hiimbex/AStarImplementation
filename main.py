# Here is where our A Star Implementation should live :)
input = [start,end]
# Priority queues Open and Closed begin empty.
open = []
closed = []
start = (0,0)
# Put S into Open with priority f(s) = g(s) + h(s)
open.append(input.pop(0))
# Is Open empty?
while open.length != 0:
    for x in range(start.x - 1, start.x + 1):
        for y in range(start.y - 1, start.y + 1):
            open.append((x,y))
    open.sort()
# Yes? No solution.
# No. Remove node with lowest f(n). Call it n.
# If n is a goal, stop and report success (for pathfinding, return the path)
# Otherwise, expand n. For each n’ in successors(n)
# Let f’ = g(n’) + h(n’) = g(n) + cost (n, n’) + h(n’)
# If n’ not seen before or n’ previously expanded with f(n’) > f’ or n’ currently in Open with f(n’) > f’
# Then place or promote n’ on Open with priority f’
# Else ignore n’
# Place record for n in Closed
