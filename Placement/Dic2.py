#qus 1
def Movies(movies):
    nm = input('Enter movie name: ')
    for items in movies:
        if items['name'] == nm:
            if items['imdb'] >= 5.5:
                print("True")
        else:
            print("Movie name not present")
            break


#Ques 2
def Movies_sublist(movies):
    lst = []
    for items in movies:
        if items['imdb'] >= 5.5:
            lst.append(items['name'])
    print(lst)


#Ques 3

def Movies_categories(movies):
    lst1 = []
    cat = input('Enter the category of the movie')
    for items in movies:
        if items['category'] == cat:
            lst1.append(items['name'])
    print(lst1)


#Ques 4
def Movies_Avg(movies):
    a = int(input("Enter the number of movies"))
    i = 1
    b = 0
    while (i <= a):
        names = input("Enter the movie names \n")
        for items in movies:
            if items['name'] == names:
                b = b + items['imdb']
        i = i+1
    print(b/a)


#Ques 5
def Movies_categoriesAvg(movies):
    x = 0
    count = 0
    cat = input('Enter the category of the movie')
    for items in movies:
        if items['category'] == cat:
            count += 1
            x = x + items['imdb']
    y = x/count        
    print(y)



movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
Movies_Avg(movies)

        