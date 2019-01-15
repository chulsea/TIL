package boj.graph;

import java.util.ArrayList;
import java.util.LinkedList;

public class BFSDFS {

    private static void bfs(int [][] adj, int start){
        boolean [] check = new boolean[adj.length];
        ArrayList<Integer> answer = new ArrayList<>();
        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(start);
        while (!queue.isEmpty()){
            int temp = queue.pop();
            check[temp - 1] = true;
            for (int i = 0; i < adj[temp - 1].length; i++){
                int temp2 = adj[temp - 1][i];
                if(!check[temp2 - 1]) queue.add(temp2);
            }
            answer.add(temp);
        }
        answer.stream().forEach(i -> System.out.print(i + " "));
    }

    private static void dfs(int [][] adj, int start){

    }

    public static void solution(int [][] adj, int start){
        bfs(adj, start);
    }

    public static void main(String[] args) {
        int [][] adj = new int[][]{
                {1, 2},
                {1, 3},
                {1, 4},
                {2, 4},
                {3, 4}
        };
        int start = 1;
        solution(adj, start);
    }
}
