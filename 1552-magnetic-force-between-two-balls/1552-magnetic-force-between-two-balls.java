import java.util.Arrays;

class Solution {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);

        int left = 1;
        int right = position[position.length - 1] - position[0];

        while (left < right) {
            int mid = left + (right - left + 1) / 2;

            if (canPlace(position, m, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }

        return left;
    }

    private boolean canPlace(int[] position, int m, int dist) {
        int balls = 1;
        int lastPos = position[0];

        for (int i = 1; i < position.length; i++) {
            if (position[i] - lastPos >= dist) {
                balls++;
                lastPos = position[i];
            }
        }

        return balls >= m;
    }
}