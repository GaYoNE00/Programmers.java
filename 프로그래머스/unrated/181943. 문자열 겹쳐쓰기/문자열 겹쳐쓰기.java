public class Solution {

	public String solution(String my_string, String overwrite_string, int s) {
		String answer = "";

		for (int i = 0; i < my_string.length(); i++) {
			if (i == s) {
				answer = answer + overwrite_string;
				if(i + overwrite_string.length() >=my_string.length()) {
					break;
				}else {
					i += overwrite_string.length();										
				}
			}
			answer = answer + my_string.charAt(i);
		}
		return answer;
	}
}