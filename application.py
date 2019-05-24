from simulation import *
import time

def print_tree(node):
    if node.is_leaf():
        print "classe: " + str(node.value)
    else:
        print "node with attribute: " + str(node.value)
        for direction, child in node.childs.items():
            print "going to direction: " + str(direction)
            print_tree(child)

target = "classe"
positive_value = "4"        # 2 for benign, 4 for malignant

categoricals = []
numerics = ['clump_thickness',
            'uniformity_of_cell_size',
            'uniformity_of_cell_shape',
            'marginal_adhesion',
            'single_epithelial_cell_size',
            'bare_nuclei',
            'bland_chromatin',
            'nomal_nucleoli',
            'mitoses'
            ]

types = {"classe": str}
filedao = FileDAO()
filedao.load_dataframe("data/dataset1/preprocessed_dataset.csv", types)

start = time.time()

n_trees = [5]
ks = [5]

for k in ks:        # number of folds

    print "Starting process with K = " + str(k)
    start_k = time.time()       # started K

    for n_tree in n_trees:

        print "Starting process with n_tree = " + str(n_tree)
        start_ntree = time.time()

        parameters = (n_tree, target, positive_value, categoricals, numerics)
        simulation = Simulation(filedao.get_folds(k), parameters)    # criar uma simulacao
        simulation.run()

        end_ntree = time.time()
        ntree_time = end_ntree - start_ntree
        print "Time spent for ntree = " + str(n_tree) + ":" + str(ntree_time)

    end_k = time.time()         # ended k
    k_time = end_k - start_k
    print "Time spent for K = " + str(k) + ":" + str(k_time)
end = time.time()

print end - start
