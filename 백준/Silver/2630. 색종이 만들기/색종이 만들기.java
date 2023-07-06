import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static int[] answer = new int[2];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N][N];

		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < N; c++) {
				arr[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		dc(0, 0, N, arr);
		System.out.println(answer[0] + "\n" + answer[1]);
	}

	private static int dc(int r, int c, int n, int[][] arr) {
		if (n == 1) {
			answer[arr[r][c]]++;
			return arr[r][c];
		}
		
		n /= 2;
		int b = 0, w = 0;
		
		for(int y=0; y<2; y++) {
			for(int x=0; x<2; x++) {
				int temp = dc(r+y*n, c+x*n, n, arr);
				switch(temp) {
				case 1: b++; break;
				case 0: w++; break;
				}
			}
		}
		if(b==4 || w==4) {
			answer[arr[r][c]] -= 3;
			return arr[r][c];
		}
		return -1;
	}
}