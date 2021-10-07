n = int(input("Enter a number : "))
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

    
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *




n = int(input("write a number  : "))

for i in range(n):
    print('*' * (n-i))
    
    
*****
****
***
**
*


n = int(input("Enter a number : "))
for i in range(n):
    print(' ' * (n-i-1) + '* ' * (i+1) )
    
           *
          * *
         * * *
        * * * *
       * * * * *
      * * * * * *
     * * * * * * *
    * * * * * * * *
   * * * * * * * * *
  * * * * * * * * * *
 * * * * * * * * * * *
* * * * * * * * * * * *

