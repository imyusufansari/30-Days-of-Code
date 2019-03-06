#include <iostream>
#include<math.h>
using namespace std;

int main()
{
  long long n;
  while(cin>>n)
  {
      int k;
      int i=0;
      if(n==0)
      cout<<n<<endl;
      while(n!=0)
      {
        if(n%2==1)
        {
        cout<<pow(2,i)<<"\n";
        break;
        }
        n=n/2;
         i++;
      }
  }
    return 0;
}