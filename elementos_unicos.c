/**
* @file elementos_unicos.c
* @brief En este programa se va a encargar de retornar la posición de los elementos únicos de un array.
* @author John Rosses
* @date 05/2015
* @version 1.0
*
* Este programa se va a encargar de recibir un arreglo cualquiera y escribe en un arreglo los índices del arreglo donde estan los números sin repetir
* El programa es capaz de solicitar al usuario el arreglo deseado e imprimir en pantalla los valores deseados.
*/
#include <stdio.h>
#include <math.h>


/**
 * @brief Función búsqueda.
* Se va a encargar de ordenar los valores de manera descendiente en el array y así le será más fácil determinar cual es el segundo con el valor más alto
 */
void elementos_unicos (int n, int c, int d, int s, int array[]) {
 printf("Los elementos únicos son: \n");
 for (c=0;c < n;c++) // primer puntero
 {
  s=0;
	  for (d=0;d < n;d++) // segundo puntero
	  {		
		   if(d == c) // esta condición evita que compare la casilla con si misma
		    {
		     d++;
		     }
	            else
                     {
                      }
            if(array[c]==array[d]) // compara para saber si son iguales
            {
             s=1;
            }
            else
            {}
           if(s==0) // condición para saber que no se ha repetido
            {
            if(d>=n-1) // pregunta a ver si ya terminó el recorrido
            {
       printf("%d ",array[c]);
            }
             else {}
             }
           else {}
          }
}
}

int main()
{
  int array[20]; ///< @param array Esta va a ser la variable obtenida através del usuario.
int array1[20]; ///< @param array Esta va a ser la variable mostrada al final del programa.
int n;///< @param n Esta va a ser la variable obtenida através del usuario del tamaño del array.
int c;///< @param c Esta va a ser la variable de la posición del primer puntero que recorre el array
int d;///< @param d Esta va a ser la variable de la posición del segundo puntero que recorre el array
int s;///< @param s Esta va a ser la variable utilizada para la memoria e intercambio de las variables en el array a la hora de ordenar
int e;///< @param e Esta va a ser la variable utilizada para la memoria  variables en el array a mostrar
int k;
e=0;
  printf("Digite el tamaño del arreglo, máximo 20\n"); ///< @brief pide al usuario el tamaño del array.
  scanf("%d", &n);
 
  printf("Digite los %d números del arreglo\n", n); ///<@brief pide al usuario los valores del arreglo.
 for (c = 0; c < n; c++) 
    scanf("%d", &array[c]);

  elementos_unicos (n, d, c, s, array);

  return 0;

}

