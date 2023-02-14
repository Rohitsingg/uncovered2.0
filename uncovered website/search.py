if __name__ == "__main__":
    movies_list = ["Mrits ","Mriet","Narshimareddy engineering college","Mrec","Mrecw","Mriet","Mrit","Mallareddy university"]
    user = input("Enter movie name:")
    search_list =[]
    index =0

    split_user = user.split(" ")

    for movies in movies_list:
        index += 1
        split_movieslist = movies.split(" ")
        for keyword1 in split_user:
            for keyword2 in split_movieslist:
                if keyword1.lower() == keyword2.lower():
                    search_list.append(index)

    print(len(search_list),"Results Found\n")                
    for index in search_list:
        print(movies_list[index-1]+"\n")



        
    width: 100%;
    background: linear-gradient(to top, rgba(0,0,0,0.5)50%,rgba(0,0,0,0.5)50%),url(images/hostelbg.jpg);
    background-position: center;
    background-size: cover;
    height: 115vh;


       width: 100%;
    height: 100vh;
    background: linear-gradient(to top, rgba(0,0,0,0.5)50%,rgba(0,0,0,0.5)50%),url(images/contactbg.jpg);
    display: flex;
    align-items: center;
    justify-content: center;


            <div class="uc__art">
          <img src="images/construction.png" alt="">

#main bg responsive style
              width: 100%;
    background: linear-gradient(to top, rgba(0,0,0,0.5)50%,rgba(0,0,0,0.5)50%),url(images/hostelbg.jpg);
    background-position: center;
    background-size: cover;
    height: 115vh;
