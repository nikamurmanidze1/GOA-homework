def name_lastaname(full_name):
    names = full_name.split()
    first_initial = names[0][0]
    last_initial = names[-1][0]
    print(f"{first_initial}{last_initial}")
name_lastaname("Nika Murmanidze")
