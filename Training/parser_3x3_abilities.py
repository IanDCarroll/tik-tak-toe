class Parser(object):

   def get_empty_square(self, options, look_up):
       lines = ((0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6))

       for line in lines:
           if lines.index(line) == look_up:
               return self.find_empty_spot(options, line)

   def find_empty_spot(self, options, spots):
       for spot in spots:
           if spot in options:
              return spot
