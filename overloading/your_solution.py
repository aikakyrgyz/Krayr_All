#from goody import irange,type_as_str

class Date:

    def __init__(self,year,month,day):
        # your assert statements should have the same format
        # assert type(year) is int and year >= 0,   f'Date.__init__: year('{str(year)}') is not positive'
        pass

    def __getitem__(self,index):
        pass
        
    
    def __repr__(self):
        pass
    
    
    def __str__(self):
        pass


    def __len__(self):
        pass
    
    def __eq__(self,right):
        pass
    
    
    def __lt__(self,right):
        pass


    def __add__(self,right):
        pass
                        
                        
    def __radd__(self,left):
        pass
    
    
    def __sub__(self,right):
        pass
    
                    

if __name__ == '__main__':
    # Put in your own simple tests for Date before allowing driver to run

    print()
    import driver
    
    driver.default_file_name = 'tests.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()



        
        
        
        
        
