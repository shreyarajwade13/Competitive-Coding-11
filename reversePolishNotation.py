class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # base case
        if tokens is None or len(tokens) == 0: return 0

        # logic
        # ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        stack = []

        # 2 1 3
        for token in tokens:
            if token not in '+-*/':
                # stack = [17,5]
                stack.append(int(token))
                continue

            # num2 = 3
            # num2 = -11
            # num2 = -132
            # num2 = 0
            # num2 = 17
            # num2 = 5
            num2 = stack.pop()

            # num1 = 9
            # num1 = 12
            # num1 = 6
            # num1 = 10
            # num1 = 0
            # num1 = 17
            num1 = stack.pop()

            rtnData = 0

            if token == '+':
                # rtnData = 9+3= 12
                # rtnData = 17+0= 17
                # rtnData = 17+5= 22
                rtnData = num1 + num2
            elif token == '-':
                rtnData = num1 - num2
            elif token == '*':
                # rtnData = 12*(-11)= -132
                # rtnData = 10 * 0 = 0
                rtnData = num1 * num2
            else:
                # rtnData = 6/(-132)=0
                rtnData = int(num1 / num2)
            # stack = [22]
            stack.append(rtnData)

        # 22
        return stack.pop()
