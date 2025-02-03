#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

// returns whether the number num is prime
// by returning 0 if no factors are found
// returns (halts at) 1 if a factor is found,
// aside from num and 1.  Starts looking at 2.
int has_factors(uint64_t num) {
  int num_factors = 0;

  if (num > 2) { 
  
    for (int i = 2; i <= sqrt((double)num); i++) {
      if (num % i == 0) return ++num_factors;
    }
  }
  return num_factors;
}

int main(int argc, char* argv[])
{
    uint64_t n = 0;
    
    //scanf("%ld", &n);
    n = strtoll(argv[1],NULL,10);

// find the largest prime factor of n   
/*    for (uint64_t i = n; i > 2; i--) {
        if(!has_factors(i)) {
            printf(" %ld", i);
            printf("\n");
            fflush(stdout);
            return 0;
        }
    }
*/
    int64_t int_sqrt = ((int64_t) sqrt((double)n));
    int64_t highestPrimeDivisor = 1;
    int64_t quotient = 0;
    for (int64_t divisor = int_sqrt; divisor > 2; divisor--) {
        if (n % divisor == 0) {
            quotient = (int64_t) (n/divisor);
            if (!has_factors(quotient)) {
            	printf(" %ld\n", quotient);
                fflush(stdout);
				return 0;
            }
            if (!has_factors(divisor)) {
                if (highestPrimeDivisor == 1) {
                    highestPrimeDivisor = divisor;
				}
            }
        }
    }
    if (highestPrimeDivisor == 1) { highestPrimeDivisor = n ; }
    printf(" %ld\n", highestPrimeDivisor );
    fflush(stdout);

    return 0;
}
