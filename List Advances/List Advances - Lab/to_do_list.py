list_with_notes = []
while True:
    notes = input()
    if notes == 'End':
        break
    split_notes = notes.split('-')
    importance_note = int(split_notes[0])
    task = split_notes[1]
    list_with_notes.append((importance_note,task))
sorted_notes = [data[1] for data in sorted(list_with_notes)]
print(sorted_notes)
