public class Answer {
    public static int answer(int[] l) {
        // Your code here
        int res = 0; int leftcount, rightcount;
        if (l.length < 3) return 0;
        for (int i = 1; i < l.length - 1; i++)
        {
            leftcount = 0; rightcount = 0;
            for (int j = 0; j < i; j++)
                if (l[i] % l[j] == 0)
                    leftcount++;
                    
            for (int k = i + 1; k < l.length; k++)
                if (l[k] % l[i] == 0)
                    rightcount++;
                    
            res += leftcount * rightcount;
        }
        return res;
    }
}