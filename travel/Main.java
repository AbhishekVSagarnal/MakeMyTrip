import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // Read N, K, Q
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());

        // Read skyscraper positions
        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            if (!st.hasMoreTokens()) {
                // Handle missing input
                A[i] = 0; // Default value or handle error
            } else {
                A[i] = Integer.parseInt(st.nextToken());
            }
        }

        // Read queries
        int[] queries = new int[Q];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < Q; i++) {
            if (!st.hasMoreTokens()) {
                // Handle missing input
                queries[i] = 0; // Default value or handle error
            } else {
                queries[i] = Integer.parseInt(st.nextToken());
            }
        }

        // Solve the problem
        int[] result = solve(N, K, Q, A, queries);

        // Output the results
        for (int i = 0; i < Q; i++) {
            bw.write(result[i] + (i == Q - 1 ? "" : " "));
        }
        bw.newLine();
        bw.flush();
    }

    public static int[] solve(int N, int K, int Q, int[] A, int[] queries) {
        TreeSet<Integer> positions = new TreeSet<>();
        TreeMap<Integer, Integer> lengthCounts = new TreeMap<>();

        // Initialize with the boundaries
        positions.add(0);
        positions.add(K);
        lengthCounts.put(K, 1);

        int[] maxAfter = new int[N];

        for (int i = 0; i < N; i++) {
            int x = A[i];
            Integer left = positions.floor(x);
            Integer right = positions.ceiling(x);
            if (left == null) left = 0;
            if (right == null) right = K;

            int originalLength = right - left;
            lengthCounts.put(originalLength, lengthCounts.getOrDefault(originalLength, 0) - 1);
            if (lengthCounts.get(originalLength) == 0) {
                lengthCounts.remove(originalLength);
            }

            int len1 = x - left;
            int len2 = right - x;
            lengthCounts.put(len1, lengthCounts.getOrDefault(len1, 0) + 1);
            lengthCounts.put(len2, lengthCounts.getOrDefault(len2, 0) + 1);

            positions.add(x);
            maxAfter[i] = lengthCounts.isEmpty() ? 0 : lengthCounts.lastKey();
        }

        int[] result = new int[Q];
        for (int i = 0; i < Q; i++) {
            int q = queries[i]; // Query value (1-based)
            if (q >= 1 && q <= N) { // Validate query value
                result[i] = maxAfter[q - 1]; // Convert to 0-based index
            } else {
                // Handle invalid query (e.g., q < 1 or q > N)
                result[i] = 0; // Default value or handle error
            }
        }
        return result;
    }
}