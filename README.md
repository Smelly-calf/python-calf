# python-calf

递归和迭代：

递归算法的步骤： 
1~n的和可以拆分成两个部分，1~n-1的和加上n，因此，递归的思想就是：在函数或子过程的内部，直接或者间接地调用自己的算法，从而把问题转化为规模缩小了的同类问题的子问题
1. 确定递归公式，如sum(n) = sum(n-1)+n 
2. 确定递归结束条件，如n=1结束递归


迭代三大步骤：
确定迭代变量：确定一个直接或间接地不断由旧值推断新值的变量，如sum
建立迭代关系式：从变量的旧值推断到新值的公式，如f(n) = f(n-1)+n
对迭代过程进行控制：迭代不可能无限循环下去，需要对何时退出迭代进行控制！如i>n推出循环。



迭代算法效率高，运行时间正比于循环次数，而且没有调用函数引起的额外开销。
递归版本的代码很简介清晰，可读性强。但是递归存在一个致命的缺点就是，递归会产生一个堆栈，递归的深度越深，堆栈的占用就越大，会导致堆栈溢出！
所以，在能够用迭代的地方就不要用递归。


    
