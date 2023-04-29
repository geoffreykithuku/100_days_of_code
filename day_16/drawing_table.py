from prettytable import PrettyTable 
table = PrettyTable()
table.add_column("Name", ["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)