// 풀이4: C 구현
bool isPalindrome(char *s) {
	int bias_left = 0;
    int bias_right = 1;
    
    int str_len = strlen(s);
    for (int i = 0; i < str_len; i++) {
    	// 스킵 포인터 처리
        // 영문자, 숫자가 아니면 bias_left 값을 1 증가 시킴
        while (!isalnum(s[i + bias_left])) {
        	bias_left++;
            // 현재 바라보는 위치가 문자열의 끝 위치이면, 비교할 것이 없으므로 true 반환
            if (i + bias_left == str_len) {
            	return true;
            }
        // 문자열을 뒤에서 부터 조회하면서 영문자, 숫자가 아니면 bias_right 값을 1 증가 시킴
        while (!isalnum(s[str_len - i - bias_right])) {
        	bias_right++;
        }
        
        // 앞에서부터 조회해 온 현재 위치가 뒤에서부터 조회해 온 현재 위치에 비해 작지 않으면 더 이상 비교할 것이 없음
        if (i + bias_left >= str_len - i - bias_right)
        	break;
        // 팰린드롬 비교
        if (tolower(s[i + bias_left]) != tolower(s[str_len - i - bias_right]))
        	return false;
        }
        return true;
    }
}