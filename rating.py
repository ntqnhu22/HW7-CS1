import sys
def process_row_format(lines):
    result={}
    for i in range (1, len(lines)):#skip the first line
        each_line=lines[i]
        title=each_line[0]#get the title only
        movie=each_line[1:]#get the number only
        total=0
        for rating in movie:
            total +=int(rating)
        if len(movie)>0:
            average=total/ len(movie)
            result[title]=average
    return result

def process_column_format(lines):
    total={}
    movie_count={}
    result={}
    for i in range (1, len(lines)):
        each_line=lines[i]
        title=each_line[0]#get the title only
        value=each_line[1]
#count the number of the appearance of the movie:
        if title in movie_count:
            movie_count[title] +=1
        else:
            movie_count[title] =1
    
#calculate the total:
        if title in total:
            total[title] += int(value)
        else:
            total[title]=int(value)

#calculate the average:
        for title in movie_count.keys() and total.keys():
            result[title]=total.get(title)/movie_count.get(title)
    return result

if __name__=="__main__":
    lines=[]
    input_file=sys.argv[1]
    output_file=sys.argv[2]
    with open(input_file, 'r') as f:
        for line in f.readlines():
            line=line.strip()
            lines.append(line.split(' '))
    with open(output_file,'w') as f:
        if lines[0][0]=='#Format:Row':
            data=process_row_format(lines)
            f.write(str(data))
        elif lines[0][0]=='#Format:Column':
            data=process_column_format(lines)
            f.write(str(data))
