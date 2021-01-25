from datetime import date
today = date.today()

## Print out #### sections into new-file.
def rmd_creator(name: str, chapter: str, infile: str, outfile: str):
    f = open(infile, 'r')
    f_out = open(outfile, 'w')
    file_by_line = {}
    chunk_start = []
    chunks = {}
    libtxt = []
    libtxt.append('```{r}\n')

    chunks['setup'] = f'---\ntitle: \"Chapter {chapter} In Class\"\nauthor: \"{name}\"\ndate: \"{today.strftime("%m/%d/%y")}\"\noutput: word_document\n---\n\n'
    chunks['knitr'] = '```{r setup, incude+FALSE}\nknitr::opts_chunk$set(echo = TRUE)\n```\n\n'

    for cnt, line in enumerate(f):  # Loops over each line of the file and adds it to a dictionary.
        file_by_line[cnt] = line  # The key is the line number (starting at 0) and the value is a string of the line.
        if "####" in line:
            chunk_start.append(cnt)  # Adds the starting point of each chunk to a list.
        if line[0:7] == 'library':
            libtxt.append(line)
    libtxt.append('```\n')
    libtxt.append('\n')
    chunks['library'] = ''.join(libtxt)
    chunks['import_df'] = '``` {r}\n#Place import statements here.\n\n\n\n```\n\n'
    ##Compare two values in list and get the numbers between the two, looping through list
    chunk_size = []
    c = (len(chunk_start) * -1)
    while c < 0:  # get the first and second value in the list.
        chunk_size.append(range(chunk_start[c], chunk_start[(c + 1)]))
        c += 1

    ## Creates dictionary of each chunk.  Adds in the RMD syntax
    for n in chunk_size:
        # print('start of range')
        txt = []  # puts each string into this list, then joins the list together into a single string.
        txt.append('```{r}\n')
        for i in n:
            txt.append(file_by_line.get(i))
        txt.append('```\n')
        txt.append('\n')
        chunks[str(n)] = ''.join(txt)  # adds the chunk to the dict, with the key being the name of the range.
        # print('end of range')
    for v in chunks.values():  # This loop writes the values from each dictionary into a file
        f_out.write(v)

    # Close your files you animal.
    f.close()
    f_out.close()

    print("Output file created at:{}".format(outfile))


rmd_creator('Benjamin Pope', '5',
            'C:/Users/Benjamin/Documents/UWTacoma/MSBA/Winter 2021/BANLT 560/Chapter5/Ch5_0.r',
            'C:/Users/Benjamin/Documents/UWTacoma/MSBA/Winter 2021/BANLT 560/Chapter5/Ch5_BenPope_OUT.rmd')
