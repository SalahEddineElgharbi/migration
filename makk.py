from django.http import Http404
class ppost():
    posts =[
       {'id' : 1,'titel' : 'firs','bodey':'this bbb '},
       {'id' : 2,'titel' : 'secondde','bodey':'this cc '},
       {'id' : 3, 'titel' : 'third', 'bodey' : ' this dd '},
    ]
    @classmethod
    def all(cls):
        return cls.posts
    @classmethod  
    def find(cls, id):
        try: 
           return cls.posts[int(id)-1]
        except:
      	   raise Http404('SORRY !!! errer 404')  
