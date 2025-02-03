#include <stdio.h>
#include <stdint.h>
#include <math.h>

int has_factors(uint64_t num) {
  int num_factors = 0;

  if (num > 2) { 
  
    for (int i = 2; i <= sqrt((double)num); i++) {
      if (num % i == 0) return ++num_factors;
    }
  }
  return num_factors;
}

int main()
{
    uint64_t n = 0;
    
    scanf("%ld", &n);
    
    for (uint64_t i = n; i > 2; i--) {
        if(has_factors(i) == 0) {
            printf(" %ld", i);
            printf("\n");
            fflush(stdout);
            return 0;
        }
    }
    printf("\n");
    fflush(stdout);

  return 0;
}
