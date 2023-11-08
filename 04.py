def main():
    nodes = int(input("Enter the number of nodes: "))
    costmat = []
    rt = []
    
    for i in range(nodes):
        costmat_row = []
        for j in range(nodes):
          #if i != j:
            cost = int(input(f"Enter cost from node {i + 1} to node {j + 1}: "))
            costmat_row.append(cost)
        costmat.append(costmat_row)
    
    for i in range(nodes):
        rt_row = {'dist': [0] * nodes, 'from': [0] * nodes}
        for j in range(nodes):
            if i != j:
                rt_row['dist'][j] = costmat[i][j]
                rt_row['from'][j] = j
        rt.append(rt_row)
    
    while True:
        count = 0
        for i in range(nodes):
            for j in range(nodes):
                for k in range(nodes):
                    if rt[i]['dist'][j] > costmat[i][k] + rt[k]['dist'][j]:
                        rt[i]['dist'][j] = costmat[i][k] + rt[k]['dist'][j]
                        rt[i]['from'][j] = k
                        count += 1
        
        if count == 0:
            break

    for i in range(nodes):
        print(f"\nFor router {i + 1}:")
        for j in range(nodes):
            print(f"Node {j + 1} via {rt[i]['from'][j] + 1} Distance {rt[i]['dist'][j]}")
    
main()
