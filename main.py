def has_duplicate(lst):
    # 利用集合去重特性，若长度不同则存在重复元素
    return len(lst) != len(set(lst))

# 测试用例
test_cases = [
    [1, 2, 3, 4],       # 无重复
    [1, 2, 2, 3],       # 有重复
    [],                 # 空列表
    [True, False, True],# 布尔值重复
    ["a", "b", "a"],    # 字符串重复
    [5, 5, 5, 5],       # 全重复
    [1, "1", 2]         # 不同类型不视为重复
]

# 调用函数并输出测试结果
for i, case in enumerate(test_cases, 1):
    result = has_duplicate(case)
    print(f"测试用例{i}：{case} → {'存在重复元素' if result else '无重复元素'}（返回值：{result}）")

