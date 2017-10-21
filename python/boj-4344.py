#첫째 줄에는 테스트케이스 C가 주어진다.
#둘째 줄부터 각 테스트케이스 마다 첫 수로 정수 N(1 <= N <= 1000)명의 학생이 주어지고 그 다음으로 N명의 0부터 100 사이의 점수가 이어서 주어진다.

# 각 케이스마다 한줄씩 평균을 넘는 학생들의 비율을 소수점 넷째자리에서 반올림하여 출력한다.

C = int(input())

for i in range(C):
	scores = list(map(int, input().split()))[1:]
	avg = sum(scores) / len(scores)
	over_avg_scores = list(filter(lambda x: x > avg, scores))
	over_avg_percent = len(over_avg_scores) / len(scores) * 100
	print("%2.3f%%" % round(over_avg_percent, 4) )
 