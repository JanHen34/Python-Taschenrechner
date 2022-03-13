def addition():
    """Eine Funktion, die Addition von 2 Zahlen durchführt.

    Args: num1, num2 (float)
    
    Returns: result(float)
    """
    result = num1 + num2
    print(result)
    return result

def subtraction():
    """Eine Funktion, die Subtraktion von 2 Zahlen durchführt.

    Args: num1, num2 (float)
    
    Returns: result(float)
    """
    result = num1 - num2
    print(result)
    return result

def multiplication():
    """Eine Funktion, die Multiplikation von 2 Zahlen durchführt.

    Args: num1, num2 (float)
    
    Returns: result(float)
    """
    result = num1 * num2
    print(result)
    return result

def division():
    """Eine Funktion, die Division von 2 Zahlen durchführt.

    Args: num1, num2 (float)
    
    Returns: result(float)
    """
    result = num1 / num2
    print(result)
    return result

def potency():
    """Eine Fuktion, die Zwei Zahlen Potenziert

    Args: num1, num2 (float)

    Returns: result (float)
    """
    result = num1 ** num2
    print(result)
    return result

answer = "yes" 

while answer == "yes":
    num1 = float(input("Geben Sie die erste Zahl ein: "))           #Erste Zahl eingeben und in Float Konvertieren
    operator = input("Geben Sie den Operator ein: ")            #Operator eingeben und als String lassen
    num2 = float(input("Geben Sie die zweite Zahl ein: "))          #Zweite Zahl Eingeben und in Float konvertieren

    if operator == "+":
        addition()        
    elif operator == "-":
        subtraction()       
    elif operator == "*":
        multiplication()
    elif operator == "/":
        division()    
    elif operator == "**":
        potency()
    else:
        print("Syntaxfehler. Sie haben keinen gültigen Operator eingegeben.") 
    
    answer = input("Möchten Sie eine neue Rechnung durchführen?")

quit(input("Drücken Sie ENTER zum Beenden."))
    
    


    



  


    







