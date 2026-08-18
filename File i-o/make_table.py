# generate multiplication tables from 2 to 20 and write it to the different files.

def generate_table(x):
    deel = ""
    for j in range(1, 11, 1):
        deel += f"{x} x {j} = {x*j}\n"
    with open(f"Tables/table_of_{x}.txt", "w") as t:
        t.write(deel)

for i in range(2, 21, 1):
    generate_table(i)