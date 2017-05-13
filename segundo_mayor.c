/**
* @file segundo_mayor.c
* @brief En este programa se va a encargar de tomar el segundo elemento más grande de un arreglo.
* @author John Rosses
* @date 05/2015
* @version 1.0
*
* Este programa se va a encargar de recibir un arreglo cualquiera y tomar el segundo número más alto dentro de este. 
*El programa es capaz de solicitar al usuario el arreglo deseado e imprimir en pantalla el valor deseado.
* Se debe tomar en cuenta que el programa va a mostrar el segundo elemento con el valor más alto, es decir, si hay 2 elementos iguales que presentan el valor más alto, se va a imprimir este número en pantalla.  
* También se va a imprimir indicando el siguiente valor si se ignora la presencia del caso anterior.
*/



#include <stdio.h>
#include <math.h>
int main()
{
  int array[20]; ///< @param array Esta va a ser la variable obtenida através del usuario.
int n;///< @param n Esta va a ser la variable obtenida através del usuario del tamaño del array.
int c;///< @param c Esta va a ser la variable de la posición del primer puntero que recorre el array
int d;///< @param d Esta va a ser la variable de la posición del segundo puntero que recorre el array
int s;///< @param s Esta va a ser la variable utilizada para la memoria e intercambio de las variables en el array a la hora de ordenar


  printf("Digite el tamaño del arreglo\n"); ///< @brief pide al usuario el tamaño del array.
  scanf("%d", &n);
 
  printf("Digite los %d números del arreglo\n", n); ///<@brief pide al usuario los valores del arreglo.
 for (c = 0; c < n; c++) 
    scanf("%d", &array[c]);
/**
 * @brief Función búsqueda.
* Se va a encargar de ordenar los valores de manera descendiente en el array y así le será más fácil determinar cual es el segundo con el valor más alto
 */

  for (c = 0 ; c < ( n - 1 ); c++) 
  {
    for (d = 0 ; d < n - c - 1; d++) 
    {
      if (array[d] < array[d+1]) // @function buuble_sort verifica cual es mayor y lo intercambia si es necesario.
      {
        s = array[d];
        array[d]  = array[d+1];
        array[d+1] = s;
      }
    }
  }
 printf("El segundo Valor más alto es: %d \n", array[1]);

 
  for ( c = 1 ; c < n ; c++ ) 
     {
      if(array[0] > array[c])
      { 
       printf("El segundo Valor más alto sin tomar casos repetidos es: %d \n ", array[c]);
c = n;}
     else
    {}
}
  return 0;
}

