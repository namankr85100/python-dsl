# int maxsubarraysum(vector<int> ar) {
#   int best = 0, sum = 0;
#   for (int i=0; i<ar.size(); i++) {
#     sum = max(ar[i], sum + ar[i]);
#     best = max(best, sum);
#   }
#   return best;
# }





# kadanae
# public int kadane(int[] arr){
# 	int max_so_far = 0, curr_max = Integer.MIN_VALUE;
#     for(int i: arr){
#     	max_so_far += i;
#         if(max_so_far<0) max_so_far = 0;
#         if(max_so_far>curr_max) curr_max = max_so_far;
#     }
#     return curr_max;
# }