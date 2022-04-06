with open("string.txt", "r",  encoding="utf-8") as read_file:
    with open("string1.txt", "w",  encoding="utf-8") as write_file:
        number_words_list = ["Один", "Два", "Три", "Четыре"]
        all_read_lines = read_file.readlines()
        for num, line in enumerate(all_read_lines):
            if len(line):
                words = line.split()
                print(f"{number_words_list[num]} {words[1]} {words[2]}", file=write_file)
        print("\tГотово\n")
