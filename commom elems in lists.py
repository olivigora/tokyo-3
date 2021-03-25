english_students = ["Michael", "Jane", "John", "Connor"]
german_students = ["Michael", "Connor", "John"]
both_classes = []
for item in english_students:
	if item in german_students:
		if item not in both_classes:
			both_classes.append(item)

print(both_classes)