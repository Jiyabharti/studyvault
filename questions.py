# if __name__ == '__main__':
n = int(input())
arr = list(map(int, input().split()))

max_value = 0 # Initialising max_value to the minimum value in the array

for value in arr:
    if value > max_value:
        max_value = value
    # need to put in amount of ints first
#
# runner_up = 0
runner_up = None
# placeholder?

for value in arr:
    if value < max_value and (runner_up is None or value > runner_up):
        runner_up = value

print(runner_up)

    # can I add an f string which says something like?
    # print(f"the runner up is { runner_up}")4
# 57 57 -57 57




