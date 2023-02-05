#You can access the dataset using this code at https://github.com/greeny00/Patika-Data_Science_Projects/tree/main via metadata.cvs file.

import pandas as pd
import time


df = pd.read_csv('metadata.csv') #csv file reading. The "read_..." command changes for different files. eg read_excel, read_json, read_html...
t=time.time()
print("File read time=",t) #This step not necessary. File reading takes time so I was wondering how long it took.

print("*************************************************************\nWhich category of information do you want to access?\n1-General information about data\n2-Column names\n3-First n row\n4-Specific columns information\n5-Specific columns and specific rows\n6-Specific or all columns unique informantions\n*************************************************************")


while(True):
    process=input("Please enter your process number as a number. Press the 'q' key to exit...:")
    if(process=="1"):#General information about data
        print(df.info())
        
        
    elif(process=="2"):#Column names
        print(df.columns)
        
        
    elif(process=="3"):#First n row
        n=int(input("Please enter the number of lines you want to see as numbers\n\033[5;31;40m REMINDER: The more rows you want to see, the longer the process takes:"))
        print(df.head(n))
        
        
    elif(process=="4"):#Specific columns information
        column_name=input("Please enter the column name you want to see exactly the same way:")
        print(df[column_name])
        
        
    elif(process=="5"):#Specific columns and specific rows
        col_info=input("Which columns do you want to display?Please enter the full columns name you want to see and separate with ','\nREMINDER: The more columns you want to see, the longer the process takes:")
        row_info=input("Enter the line spacing you want to see using ','(EXAMPLE:45,89) :")
        
        cols=col_info.split(",")
        rows=row_info.split(",")
        
        print(df[cols].iloc[int(rows[0]):int(rows[1])])
        
        
    elif(process=="6"):#Specific or all columns unique informantions
        info=input("How many columns do you want to display? If you want to access all of them, just type 'all'\n\033[5;31;40mREMINDER: The more columns you want to see, the longer the process takes:")
        
        if(info=="all"):
            print(df.nunique())
        else:
            columns=input("Please enter the full columns name you want to see and separate with ',':")
            col=columns.split(",")
            print(df[col].nunique())
            
        
    elif(process=="q"): #Exit
        print("Hope we could help, have a nice day...")
        break
    
        
    else:
        print("You entered something that is not understood by the program, please try again.")
        
    
