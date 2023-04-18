"""
В программе есть списки тестировщиков (имена, айдишники), которые:

- могут писать тест дизайны

- могут писать тест скрипты

- могут ревьюить скрипты

- сегодня не на работе

Любой тестировщик может входить в одну или несколько групп.



Создать списки:

- всех тестировщиков в команде

- тестировщиков, которые могут только писать скрипты

- тестировщиков, которые сегодня на работе

- тестировщиков, которые могут писать и ревьюить скрипты, и которые сегодня на работе



Полученные списки вывести в отсортиованном виде.



test_design_writers = [1, 3, 5]

scripters = [2, 3, 4, 6, 7, 8]

reviewers = [1, 2, 3, 9, 10]

out_of_office_today = [2, 5, 6, 1]



всех тестировщиков в команде

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



могут писать только тест скрипты

[4, 6, 7, 8]



тестировщиков, которые сегодня на работе

[3, 4, 7, 8, 9, 10]



тестировщиков, которые могут писать и ревьюить скрипты, и которые сегодня на работе

[3]
"""

test_design_writers = [1, 3, 5]
scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_testers = list(set(test_design_writers).union(set(scripters)).union(set(reviewers)).union(set(out_of_office_today)))
can_only_write = list(set(scripters).difference(set(reviewers)).difference(set(test_design_writers)))
testers_on_work = list(set(all_testers).difference(set(out_of_office_today)))
can_review_write_on_work = list(set(scripters).intersection(set(reviewers)).difference(set(out_of_office_today)))

print(sorted(all_testers))
print(sorted(can_only_write))
print(sorted(testers_on_work))
print(sorted(can_review_write_on_work))


