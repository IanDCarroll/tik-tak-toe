class Parser(object):

   def get_empty_square(self, options, code):
       row_1 = [0, (0,1,2)]
       row_2 = [1, (3,4,5)]
       row_3 = [2, (6,7,8)]
       col_1 = [3, (0,3,6)]
       col_2 = [4, (1,4,7)]
       col_3 = [5, (2,5,8)]
       diag1 = [6, (0,4,8)]
       diag2 = [7, (2,4,6)]

       if code == row_1[0]:
           return self.find_empty_spot(options, row_1[1])
       elif code == row_2[0]:
           return self.find_empty_spot(options, row_2[1])
       elif code == row_3[0]:
           return self.find_empty_spot(options, row_3[1])
       elif code == col_1[0]:
           return self.find_empty_spot(options, col_1[1])
       elif code == col_2[0]:
           return self.find_empty_spot(options, col_2[1])
       elif code == col_3[0]:
           return self.find_empty_spot(options, col_3[1])
       elif code == diag1[0]:
           return self.find_empty_spot(options, diag1[1])
       elif code == diag2[0]:
           return self.find_empty_spot(options, diag2[1])

   def find_empty_spot(self, options, index_list):
       for spot in index_list:
           if spot in options:
              return spot
