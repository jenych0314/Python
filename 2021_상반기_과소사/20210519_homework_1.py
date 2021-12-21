def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_tree = ''.join( x for x in skill_tree if x in skill)
        if skill_tree == skill[:len(skill_tree)]:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))