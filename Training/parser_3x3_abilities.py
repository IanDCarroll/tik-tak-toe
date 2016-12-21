class Parser(object):

   def get_empty_square(self, options, code):
       possibilities = ((0,1,2),(3,4,5),(6,7,8),
                        (0,3,6),(1,4,7),(2,5,8),
                        (0,4,8),(2,4,6))

       for possibility in possibilities:
           if possibilities.index(possibility) == code:
               return self.find_empty_spot(options, possibility)

   def find_empty_spot(self, options, index_list):
       for spot in index_list:
           if spot in options:
              return spot
