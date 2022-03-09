class Calcul(object):
    
    
    def Cal(self, calc):
     
        return self.Cal_Valid(calc=calc)

    def Cal_Valid(self, calc):
      

        try:
            result = eval(calc)

            return self.__format_result(result=result)
        except (NameError, ZeroDivisionError, SyntaxError, ValueError):
            return 'Err' 

    def __format_result(self, result):
     

        result = str(result)
        if len(result) > 15:
            result = '{:5.5E}'.format(float(result))
            
        return result
