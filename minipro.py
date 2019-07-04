fo=open("-------","r")
data=fo.read()

fr=open("---------","r")
rate=fr.read()

list_for_ratings=['movie_id','rating']
list_for_movies=['movie_id','movie_name','genre','year']


genre=set()
year=set()

'''for movie data'''
temporary_list2=[]
data_list=[]

temporary_list=data.split("\n")
for i in range(len(temporary_list)):
               temporary_list2.append(temporary_list[i].split(","))
for j in range(len(temporary_list2)):
               data_list.append(dict(zip(list_for_movies,temporary_list2[j])))
for i in range(len(temporary_list2)):
               data_list[i]["genre"]=temporary_list2[i][2].split("|")

'''for ratings data'''
rate_list=[]
temporary_list2.clear()
temporary_list=rate.split("\n")
for i in range(len(temporary_list)):
    temporary_list2.append(temporary_list[i].split(","))
for j in range(len(temporary_list2)):
    rate_list.append({list_for_ratings[i]:float(temporary_list2[j][i]) for i in range(len(list_for_ratings))})
fo.close()
fr.close()

'''set for genre'''
for i in range(len(data_list)):
        genre.update(x for x in data_list[i]["genre"])

'''set for year'''
for i in range(len(data_list)):
        year.update(x for x in [data_list[i]["year"]])



counter1_p=0
print("COUNT OF MOVIES OF ALL GENRES")
for each in genre:
    for i in range(len(data_list)):
        if each in data_list[i]["genre"]:
            counter1_p+=1       
    print(each,":",counter1_p )
    counter1_p=0



counter3_p=0
print("COUNT OF MOVIES OF ALL GENRE THAT WAS RELEASED AFTER 2000")
print("RATING GREATER THAN 3.5")
for each in genre:
    for i in range(len(data_list)):
        if int(data_list[i]["year"])>2000:
            if each in data_list[i]["genre"]:
                if rate_list[i]["rating"]>3.5:
                    counter3_p=counter3_p+1
    if counter3_p>0:
        print(each, ":",counter3_p)
        counter3_p=0    


great=0
print("TOP MOVIE RELEASED IN EACH YEAR \n")
for each in year:
    for i in range(len(data_list)):
        if each in str(data_list[i]['year']):
            if rate_list[i]["rating"]>great:
                great=rate_list[i]["rating"]
                names=data_list[i]["movie_name"]
    if great!=0:
        print("THE BEST MOVIE OF",each,"WAS",names)
        great=0
        names=0


counter2_p=0
print("COUNT MOVIES OF ALL GENRES WHERE RATINGS ARE GREATER THAN 4")
for each in genre:
    for i in range(len(data_list)):
        if each in data_list[i]["genre"]:
            if rate_list[i]["rating"]>4:
                counter2_p+=1
    if counter2_p!=0:
        print(each, ":", counter2_p)
        counter2_p=0



top=0
print("TOP MOVIE OF EACH GENRE \n")
for each in genre:
    for i in range(len(data_list)):
        if each in data_list[i]["genre"]:
            if rate_list[i]["rating"]>top:
                top=rate_list[i]["rating"]
                name=data_list[i]["movie_name"]
    if top!=0:
        print("THE BEST",each,"MOVIE IS",name)
        top=0
        name=0
