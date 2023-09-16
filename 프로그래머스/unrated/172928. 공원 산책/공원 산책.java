import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] answer = {-1, -1};
        int R = park.length;
        int C = park[0].length();
        boolean[][] map = new boolean[R][C];
        
        for(int r=0; r<R; r++) {
            char[] str = park[r].toCharArray();
            for(int c=0; c<C; c++) {
                if (str[c]=='X') map[r][c] = false;
                else map[r][c] = true;
                if (str[c]=='S') answer = new int[] {r, c};
            }
        }
        
        HashMap<String, int[]> direction = new HashMap<>();
        direction.put("N", new int[] {-1, 0});
        direction.put("S", new int[] {1, 0});
        direction.put("W", new int[] {0, -1});
        direction.put("E", new int[] {0, 1});
        
        check: for(String route: routes) {
            String[] commend = route.split(" ");
            int amount = Integer.parseInt(commend[1]);
            int[] d = direction.get(commend[0]);
            int dr = answer[0] + d[0] * amount;
            int dc = answer[1] + d[1] * amount;
            
            if (dr < 0 || dr >= R || dc < 0 || dc >= C) continue;
            for (int i = 1; i <= amount; i++) {
                if (map[answer[0] + d[0] * i][answer[1] + d[1] * i]) continue;
                continue check;
            }
            answer = new int[] {dr, dc}; 
            System.out.println(answer[0] + " " + answer[1]);
        }
        
        return answer;
    }
}