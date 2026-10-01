class Solution {
    public boolean isValid(String s) {
        HashMap<Character , Character> pairs = new HashMap<>();
        Stack<Character> stack = new Stack<>();

        pairs.put(')','(');
        pairs.put('}','{');
        pairs.put(']','[');

        for (char ch :s.toCharArray()){
            if (ch =='(' || ch =='{' || ch=='['){
                stack.push(ch);
            }
            else{
                if(stack.isEmpty() || stack.peek()!= pairs.get(ch)){
                    return false;
                }
                stack.pop();
            }
        }
        return stack.size() == 0;
        
    }
}