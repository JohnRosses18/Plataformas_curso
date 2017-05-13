/**
* @file buscador.c
* @brief En este programa se va a encargar de retornar la posición del elemento encontrado.
* @author John Rosses
* @date 05/2015
* @version 1.0
*
* Este programa se va a encargar de recibir un arreglo cualquiera y escribe en un arreglo los índices del arreglo donde estan los números sin repetir
* El programa es capaz de solicitar al usuario el arreglo deseado e imprimir en pantalla los valores deseados.
*/
 ///< @param array Esta va a ser la variable obtenida através del usuario.
///< @param n Esta va a ser la variable obtenida através del usuario del tamaño del array.
///< @param c Esta va a ser la variable de la posición del primer puntero que recorre el array
///< @param d Esta va a ser la variable de la posición del segundo puntero que recorre el array
///< @param s Esta va a ser la variable utilizada para la memoria e intercambio de las variables en el array a la hora de ordenar

#include <stdio.h>
#include <math.h>

int main()
{
  int array[20]; 
  int n;
  int c;
  int d;
  int s;

  printf("Digite el tamaño del arreglo, máximo 20\n"); ///< @brief pide al usuario el tamaño del array.
  scanf("%d", &n);
 
  printf("Digite los %d números del arreglo\n", n); ///<@brief pide al usuario los valores del arreglo.
 for (c = 0; c < n; c++) 
    scanf("%d", &array[c]);

printf("Digite el número a buscar: "); ///<@brief pide al usuario los valores del arreglo.
 scanf("%d", &d);

 printf("El elemento se encuentra en los índices: \n");
 
for (c=0;c < n;c++) // primer puntero
 {
  if (array[c]==d)
  {
   printf("%d \n",c);
 }
  else
{}
}
  return 0;
}

