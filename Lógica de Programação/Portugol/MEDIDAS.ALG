Algoritmo "medidas"

Var

   a, b, c, areaQuadrado, areaTriangulo, areaTrapezio : real

Inicio

   escreva("Digite a medida A: ")
   leia(a)
   escreva("Digite a medida B: ")
   leia(b)
   escreva("Digite a medida C: ")
   leia(c)
   
   areaQuadrado <- a * a
   areaTriangulo <- (a * b) / 2
   areaTrapezio <- ((a + b) * c) / 2
   
   escreval("�rea do Quadrado = ", areaQuadrado:6:4)
   escreval("�rea do Tri�ngulo = ", areaTriangulo:6:4)
   escreval("�rea do Trap�zio = ", areaTrapezio:6:4)

Fimalgoritmo