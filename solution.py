x = int(input("Enter the value of starting node  "))

TS1 = {2:10, 3:15, 4:20}
TS2 = {3:35, 4:25, 1:10}
TS3 = {4:30, 2:35, 1:15}
TS4 = {3:30, 2:25, 1:20}


#case1
if x == 1:
    min1 = min(TS1.get(2),TS1.get(3),TS1.get(4))
    for key, value in TS1.items():
        if value == min1:
            a1 = key
        
    if a1 == 2:
        min2 = min(TS2.get(3),TS2.get(4))
        for key, value in TS2.items():
            if value == min2:
                a2 = key
        if a2 == 3:
            min3 = TS3.get(4)
            Total = min2 + min1 + min3 + TS4.get(1)
            print("Path Taken" , ( x , a1 , a2 ,4))
        elif a2 == 4:
            min4 = TS4.get(3)
            Total = min2 + min1 + min4 + TS3.get(1)
            print("Path Taken" , ( x , a1 , a2 ,3))
        
    elif a1 == 3:   
        min3 = min(TS3.get(4),TS3.get(2))
        for key, value in TS3.items():
            if value == min3:
                a3 = key
                
        if a3 == 2:
            min2 = TS2.get(4)
            Total = min2 + min1 + min3 + TS4.get(1)
            print("Path Taken" , ( x , a1 , a3 ,4))
        elif a3 == 4:
            min4 = TS4.get(2)
            Total = min2 + min1 + min4 + TS2.get(1)
            print("Path Taken" , ( x , a1 , a3 ,2))
            
    elif a1 == 4:    
        min4 = min(TS4.get(3),TS4.get(2))
        for key, value in TS4.items():
            if value == min4:
                a4 = key
        if a4 == 3:
            min3 = TS3.get(2)
            Total = min2 + min1 + min3 + TS2.get(1)
            print("Path Taken" , ( x , a1 , a4 ,2))
        elif a4 == 2:
            min2 = TS2.get(3)
            Total = min2 + min1 + min4 + TS3.get(1)
            print("Path Taken" , ( x , a1 , a4 ,3))         
            
#case2            
elif x == 2:
    min2 = min(TS2.get(3),TS2.get(4),TS2.get(1))
    for key, value in TS2.items():
        if value == min2:
            a2 = key
    if a2 == 1:
        min1 = min(TS1.get(3),TS1.get(4))
        for key, value in TS1.items():
            if value == min1:
                a1 = key 
                
        if a1 == 3:
            min3 = TS3.get(4)
            Total = min2 + min1 + min3 + TS4.get(2)
            print("Path Taken" , ( x , a2 , a1 ,4))
        elif a1 == 4:
            min4 = TS4.get(3)
            Total = min2 + min1 + min4 + TS3.get(2)
            print("Path Taken" , ( x , a2 , a1 ,3))
            
            
    elif a2 == 3:
        min3 = min(TS3.get(4),TS3.get(1))
        for key, value in TS3.items():
            if value == min3:
                a3 = key
                
        if a3 == 1:
            min1 = TS1.get(4)
            Total = min2 + min1 + min3 + TS4.get(2) 
            print("Path Taken" , ( x , a2 , a3 ,4))
        elif a3 == 4:
            min4 = TS4.get(1)
            Total = min2 + min3 + min4 + TS1.get(2)
            print("Path Taken" , ( x , a2 , a3 , 1 ))
            
    elif a2 == 4:        
        min4 = min(TS4.get(3),TS4.get(1))
        for key, value in TS4.items():
            if value == min4:
                a4 = key
                
        if a4 == 3:
            min3 = TS3.get(1)
            Total = min2 + min1 + min3 + TS1.get(2) 
            print("Path Taken" , ( x , a2 , a4 ,1))
        elif a4 == 1:
            min4 = TS1.get(3)
            Total = min2 + min1 + min4 + TS3.get(2)
            print("Path Taken" , ( x , a2 , a4 ,3))

# case3            
elif x == 3:
    min3 = min(TS3.get(4),TS3.get(2),TS3.get(1))
    for key, value in TS3.items():
        if value == min3:
            a3 = key
    
    if a3 == 1:
        min1 = min(TS1.get(2),TS1.get(4))
        for key, value in TS1.items():
            if value == min1:
                a1 = key
                
        if a1 == 2:
            min2 = TS2.get(4)
            Total = min2 + min1 + min3 + TS4.get(3)
            print("Path Taken" , ( x , a3 , a1 ,4))
        elif a1 == 4:
            min4 = TS4.get(2)
            Total = min2 + min1 + min4 + TS2.get(3)
            print("Path Taken" , ( x , a3 , a1 ,2))
            
    
    elif a3 == 2:
        
        min2 = min(TS2.get(4),TS2.get(1))
        for key, value in TS2.items():
            if value == min2:
                a2 = key
        if a2 == 1:
            min1 = TS1.get(4)
            Total = min2 + min1 + min3 + TS4.get(3)
            print("Path Taken" , ( x , a3 , a2 ,4))
            
        elif a2 == 4:
            min4 = TS4.get(1)
            Total = min2 + min1 + min4 + TS1.get(3)
            print("Path Taken" , ( x , a3 , a2 ,1))     
    
    elif a3 == 4:        
        min4 = min(TS4.get(2),TS4.get(1))
        for key, value in TS4.items():
            if value == min4:
                a4 = key
                
        if a4 == 1:
            min1 = TS1.get(2)
            Total = min2 + min1 + min3 + TS1.get(3)
            print("Path Taken" , ( x , a3 , a4 ,2))
        elif a4 == 2:
            min2 = TS2.get(1)
            Total = min2 + min1 + min4 + TS1.get(3)
            print("Path Taken" , ( x , a3 , a4 ,1))        

#case4
elif x == 4:
    min4 = min(TS4.get(3),TS4.get(2),TS4.get(1))
    for key, value in TS4.items():
        if value == min4:
            a4 = key     
    
    if a4 == 1:
        min1 = min(TS1.get(2),TS1.get(3))
        for key, value in TS1.items():
            if value == min1:
                a1 = key
                
        if a1 == 3:
            min3 = TS3.get(2)
            Total = min2 + min1 + min3 + TS2.get(4)
            print("Path Taken" , ( x , a4 , a1 ,2))
        elif a1 == 2:
            min2 = TS2.get(3)
            Total = min2 + min1 + min4 + TS3.get(4)
            print("Path Taken" , ( x , a4 , a1 ,3))        
            
    elif a4 == 2:        
        min2 = min(TS2.get(3),TS2.get(1))
        for key, value in TS2.items():
            if value == min2:
                a2 = key
        if a2 == 3:
            min3 = TS3.get(1)
            Total = min2 + min1 + min3 + TS1.get(4) 
            print("Path Taken" , ( x , a4 , a2 ,1))
        elif a2 == 1:
            min4 = TS1.get(3)
            Total = min2 + min1 + min4 + TS3.get(4)
            print("Path Taken" , ( x , a4 , a2 ,3))        
                
    elif a4 == 3:
        min3 = min(TS3.get(2),TS3.get(1))
        for key, value in TS3.items():
            if value == min3:
                a3 = key

        if a3 == 1:
            min1 = TS1.get(2)
            Total = min2 + min1 + min3 + TS1.get(4)
            print("Path Taken" , ( x , a4 , a3 ,2))
        elif a3 == 2:
            min2 = TS2.get(1)
            Total = min2 + min1 + min4 + TS1.get(4)
            print("Path Taken" , ( x , a4 , a3 ,1))       
    
            
print("Total distance to return to starting node" , x , " = " , Total)           
