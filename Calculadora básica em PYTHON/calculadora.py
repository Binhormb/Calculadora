def calculadora():
    operacao = input ("Escolha uma operação: (+, -, *, /) ")
    
    if operacao == "+":
     num1 = float(input ("Digite o primeiro número:"))
     num2 = float(input ("Digite o segundo número:")) 
     resultado = num1 + num2 
     
    elif operacao == "-":
      num1 = float(input ("Digite o primeiro número:"))
      num2 = float(input ("Digite o segundo número:")) 
      resultado = num1 - num2  
      
    elif operacao == "*":
      num1 = float(input ("Digite o primeiro número:"))
      num2 = float(input ("Digite o segundo número:")) 
      resultado = num1 * num2  
      
    elif operacao == "/":
      num1 = float(input ("Digite o primeiro número:"))
      num2 = float(input ("Digite o segundo número:")) 
      resultado = num1 / num2  
      
    else:
      print("Operação inválida!!")
      return
    
    resultado = print("O Resultado é:", resultado)
    
calculadora()