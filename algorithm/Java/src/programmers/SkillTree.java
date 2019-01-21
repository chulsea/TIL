package programmers;

public class SkillTree {

    public int solution(String skill, String[] skillTrees) {
        int answer = 0;
        for (String skillTree : skillTrees){
            int idx = 0, i;
            int m = skillTree.length();
            for(i = 0; i < m; i++){
                int temp = skill.indexOf(skillTree.charAt(i) + "");
                if (temp == -1) continue;
                if (temp > idx) break;
                idx++;
            }
            if (i == m) answer++;
        }
        return answer;
    }

    public static void main(String[] args) {
        SkillTree test = new SkillTree();
        int answer = test.solution("CBD", new String[]{"BACDE", "CBADF", "AECB", "BDA"});
        System.out.println(answer);
    }
}
