class Solution {
    public int solution(int a, int b) {
        if(Integer.parseInt(""+a+""+b)>(a*b*2)) {
	        	return Integer.parseInt(""+a+""+b);
	        }
	        return a*b*2;
    }
}