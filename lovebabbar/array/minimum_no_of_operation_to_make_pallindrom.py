# import java.util.Scanner;
# class sum
# {
#     public static void main(String[] args)
#     {
#         Scanner sr = new Scanner(System.in);
#         int n=sr.nextInt();
#         int a[]= new int[n];
#         for(int i=0;i<n;i++)
#         {
#             a[i]=sr.nextInt();
#         }
#         int ans = 0;
#   for (int i=0,j=n-1; i<=j;)
#   {
#     if(a[i]==a[j])
#     {
#       i++;
#       j--;
#     }
#     else if(a[i]>a[j])
#     {
#       j--;
#       a[j]+=a[j+1] ;
#       ans++;
#     }
#     else
#     {
#       i++;
#       a[i]+.
# =a[i-1];
#       ans++;
#     }
#   }
#   System.out.println(ans);
#     }
# }