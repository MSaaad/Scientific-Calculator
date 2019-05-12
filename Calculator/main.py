#import Combination
#import angle_converter
#import Cube
#import cube_root
#import factorial
#import length_converter
#import log
#import matrix
#import nth_power
#import nth_root
#import Percentage
#import reciprocal
#import simple
#import Square
#import Temp_converter
#import sine
#import cosine
#import tangent
#import Exponential
#import sinh
#import cosh
#import tanh
#import quadratic_eq
#import square_root



def calculator():
    print('\tWELOCME TO OUR SCIENTIFIC CALCULATOR......')
    print('\t==========================================')
    print('''
1. Addition                   2. Subtraction                        3. Multiplication
4. Division                   5. Square                             6. Cube
7. Square root                8. Cube root                          9. log
10. Antilog                   11. Nth Root                          12. Nth Power
13. Factorial                 14. Matrix(2x2)                       15. Matrix(3x3)
16. ln                        17. Reciprocal                        18. Percentage
19. Exponential               20. Quadratic Equation                21. Sin()
22. Cos()                     23. Tan()                             24. Sinh
25. Cosh                      26. Tanh
27. Length Conversion       28.Temperature Conversion         29. Angle Conversion
30. Permutation                 31. Combination ''')

#calculator()
    while True:    
        choice=int(input('Please choose from the following given options!'))
        if choice==1:
            import simple
            simple.add()
        elif choice==2:
            import simple
            simple.subtract()
        elif choice==3:
            import simple
            simple.multiply()
        elif choice==4:
            import simple
            simple.divide()
        elif choice==5:
            import Square
            Square.square()
        elif choice==6:
            import Cube
            Cube.cube()              
        elif choice==7:
            import square_root
            square_root.square_root()
        elif choice==8:
            import cube_root
            cube_root.cube_root()
        elif choice==9:
            import log
            log.log()
        elif choice==10:
            antilog.antilog()
        elif choice==11:
            import nth_root
            nth_root.nth_root()
        elif choice==12:
            import nth_power
            nth_power.nth_power()
        elif choice==13:
            import factorial
            factorial.factorial()
        elif choice==14:
            import matrix
            matrix.matrix()
        elif choice==15:
            matrix_3()
        elif choice==16:
            ln.ln()
        elif choice==17:
            import reciprocal
            reciprocal.reciprocal()
        elif choice==18:
            import Percentage
            Percentage.percentage()
        elif choice==19:
            import exponential
            exponential.exponential()
        elif choice==20:
            import quadratic_eq
            quadraric_eq.Quadratic()
        elif choice==21:
            import sine
            sine.sin()
        elif choice==22:
            import cosine
            cosine.cos()
        elif choice==23:
            import tangent
            tangent.tan()                                              
        elif choice==24:
            import sinh
            sinh.sinh()
        elif choice==25:
            import cosh
            cosh.cosh()
        elif choice==26:
            import tanh
            tanh.tanh()
        elif choice==27:
            import length_converter
            length_converter.length_converter()
        elif choice==28:
            import Temp_converter
            Temp_converter.temperature_converter()
        elif choice==29:
            import angle_converter
            angle_converter.rad()
            angle_converter.deg()
        elif choice==30:
            import Combination
            Combination.npr(x,y)
        elif choice==31:
            import Combination
            Combination.ncr(x,y)
        elif choice==32:
            import mod
            mod.mod()
#sec_num=int(input('Enter another number:'))
#calculator(sec_num)
