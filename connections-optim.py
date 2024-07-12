import itertools
import sys

cluster_number = int(sys.argv[1])
debugging = False

def combinlist(seq):
    return list(itertools.combinations(seq, 2))

def intersection(ll, la):
    res = []
    flat_res = []
    for l in ll:
        if list(set(l) & set(la)) == [] and list(set(flat_res) & set(l)) == []:
            res += [l]
            flat_res += [l[0], l[1]]

    debug("flat " + str(flat_res))
    return [la] + res

def equal(l, l2):
    return list(set(l) & set(l2)) != []

def print_pair(l):
    end = ""
    j = 0
    num = 0
    for d in l:
        if d[0] != j:
           print(num)
           num = 0
        if debugging:
           print(str(d[0]) + str(d[1]), end=" ")
        num += 1
        j = d[0]
    print(1)

def its(d):
    if cluster_number < 11:
       val = ("", "")
    elif cluster_number < 101:
       val = ("0", "")
    else:
       val = ("00", "0")
    
    if d < 10:
       return val[0] + str(d)
    elif d < 100:
       return val[1] + str(d)
    else:
       return str(d)

def print_res(l):
   for ds in l:
       for d in ds:
           print(its(d[0]) + "," + its(d[1]), end=" ")
       print()

def debug(p):
    if debugging:
       print(p)

def combi_optimization(connections_list):
    intersect = []
    res = []
    flat_res = []
    
    for conn in connections_list_cst:
        if conn in connections_list:
           intersect = intersection(connections_list, conn)
           for i in intersect:
               connections_list.remove(i)
               debug("remove " + str(i))
               debug("connections_list" + str(connections_list))
           res += [intersect]
           flat_res += intersect
        else:
           debug("skip " + str(conn))
    return (flat_res, res)



cluster_number_list = range(cluster_number)

connections_list = combinlist(cluster_number_list)
connections_list_cst = connections_list[:]

flat_res, res = combi_optimization(connections_list)

print_res(res)
print("number of steps:")
print(len(res))
print("number of paralel by step:")
for i in res:
   print(len(i), end=" ")
print("\ncheck number is the same:")
print(len(connections_list_cst))
print(len(flat_res))

print("check number is the n(n-1)/2:")
#print_pair(sorted(connections_list_fix))
#print_pair(sorted(flat_res))
