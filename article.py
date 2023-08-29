class Article: 
    all = [] #initialise a empty list that will store all the article instances 
    # the article is initialised with an author as an Author object, a magazine as a Magazine object, and a title as a string
    def __init__(self, author, magazine, title):
        # make them the properties of this Article class
        #convert the properties to private to make them unchangeable when 'getting' them 
        self._author = author
        self._magazine = magazine
        self._title = title 
        #the .append method adds the 'self' instances to the all empty list and returns them 
        Article.all.append(self)
        
    # the Article class cannot change the name of the author, magazine or title name after it has been initialised
    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
    
    @property
    def title (self):
        return self._title
    
    # @classmethod
    # #when using the classmethod decorator we are making the function below it a class method 
    # def all_art (cls):
    #     return [articles for articles in Article.all]
    
    # #define a call method that gets the list of all article instances
    