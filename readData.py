import glob

allFiles = sorted(glob.glob("./csvRunner/GVT-A33/*.txt"))
with open("./csvRunner/values/output.csv", "w") as output:
            pass

for file in allFiles:
    with open(file, "r") as dt:
        data = str(dt.read()).replace('\n', '=').split('=')
        # print(data)

    if file == allFiles[0]:
        with open("./csvRunner/values/output.csv", "a") as output:
            output.write(f"rckt_info,")
        for i in range(0, len(data) - 1, 2):
            with open("./csvRunner/values/output.csv", "a") as output:
                output.write(f"{data[i].strip()},")

        with open("./csvRunner/values/output.csv", "a") as output:
            output.write('\n')

    with open("./csvRunner/values/output.csv", "a") as output:
            output.write(f"{file.replace(',', '.')[:-4]},")

    for i in range(1, len(data) - 1, 2):
        with open("./csvRunner/values/output.csv", "a") as output:
            output.write(f"{data[i].strip()},")

    with open("./csvRunner/values/output.csv", "a") as output:
            output.write('\n')

# with open("./csvRunner/values/output.csv", "r") as output:
#             read = str(output.read())
# with open("./csvRunner/values/output.csv", "w") as output:
#             output.write(read.replace('.', ','))





