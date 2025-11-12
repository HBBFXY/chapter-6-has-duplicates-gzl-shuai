

def has_duplicates(lst):
    """判断列表中是否存在重复元素，存在则返回True，否则返回False"""
    # 利用集合去重特性：若列表长度大于集合长度，说明有重复元素
    return len(lst) != len(set(lst))


# 测试程序
if __name__ == "__main__":
    # 定义多种测试用例
    test_cases = [
        [1, 2, 3, 4],        # 无重复元素（整数）
        [1, 2, 3, 2],        # 有重复元素（整数）
        [],                   # 空列表
        [5],                  # 单个元素
        [2, 2, 2, 2],         # 多个重复元素
        ['a', 'b', 'a'],      # 有重复元素（字符串）
        [1.5, 2.5, 1.5]       # 有重复元素（浮点数）
    ]
    
    # 遍历测试用例并输出结果
    for case in test_cases:
        result = has_duplicates(case)
        print(f"列表 {case} 中是否存在重复元素？{result}")
