#Here is where our A Star Implementation should live :)
# Priority queues Open and Closed begin empty. 
# Put S into Open with priority f(s) = g(s) + h(s)
# Is Open empty?
# Yes? No solution.
# No. Remove node with lowest f(n). Call it n.
# If n is a goal, stop and report success (for pathfinding, return the path)
# Otherwise, expand n. For each n’ in successors(n)
# Let f’ = g(n’) + h(n’) = g(n) + cost (n, n’) + h(n’)
# If n’ not seen before or n’ previously expanded with f(n’) > f’ or n’ currently in Open with f(n’) > f’
# Then place or promote n’ on Open with priority f’
# Else ignore n’
# Place record for n in Closed
