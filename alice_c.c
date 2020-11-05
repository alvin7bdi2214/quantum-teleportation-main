#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#define N 8
int main(){
int i,n,m;
int target_bin_code;
int Alice_code[N]={1,1,0,1,0,1,1,1};
double x,y;
double a=1.0,b=0.0;
int count=0;

for(n=0;n<N;n++)printf("Alice code is %d ",Alice_code[n]);
printf("\n");
FILE* particle_3 =fopen("particle_3","w");
FILE* EPS_position =fopen("pos","w");


for(m=0;m<N;m++){
target_bin_code = Alice_code[m];

do{
n=rand()%4;
if(n==0){x=-b,y=a;}else if(n==1){x=-a,y=b;}else if(n==2){x=b,y=a;}else if(n==3){x=-a,y=-b;}
fprintf(particle_3,"%lf  %lf", x,y);
count ++;
}while(n != 3);  // EPR state is N=3
printf("%d\n",count);  // Save the position to find EPR states.
}

}