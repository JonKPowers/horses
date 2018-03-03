def concatenate_text_fields(list_of_fields):
    """For consolidating text notes that are spread across several columns due to a
    255-byte length restriction"""
    all_text = ''
    for i in range(len(list_of_fields)):
        if list_of_fields[i]:
            all_text += str(list_of_fields[i])
    return all_text

def review_function(data=conditions, start=0, go=50):
    """For use in debugging the condition parser. Allows you to step through condition strings
    one at a time to confirm that the output and resulting restriction_dict is what you expect.
    returns a list of strings that you have marked as 'tricky' during review (for further testing
    and debugging outside of the parser review)."""
    data = data[start:start+go]
    tricky_strings = []
    i = start
    for item in data:
        print('\n\n\n#######################')
        print(f'#{i}')
        print('#######################')
        pull_race_restrictions(item)
        i += 1
        user_input = input('Enter (t)ricky_string or (q)uit').lower()
        if user_input == 't':
            tricky_strings.append(item)
        elif user_input == 'q':
            break
    return tricky_strings