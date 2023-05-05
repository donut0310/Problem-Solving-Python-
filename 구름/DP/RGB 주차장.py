import sys
input = sys.stdin.readline

def solution():
	answer = 0

	n = int(input())
	
	answer = (2 ** (n-1) * 3) % 100000007
	return answer
		
print(solution())

'''
ex) n: 3 => ㅁㅁㅁ 
첫째 칸은 아무 색상이나 들어올 수 있기 때문에 RGB중 하나의 색을 넣었을 때의 전체 경우의 수 * 3이 모든 경우의 수가 된다.
첫재 칸이 R일 때 다음 칸은 B or G 두 가지의 경우가 있다.
두번 째 칸이 B 라면 다음 칸은 G or R, G라면 다음 칸은 B or R이 되고 이는 제곱수의 규칙을 가진다.
따라서 n번째의 칸은 2의 (n-1)제곱만큼의 경우의 수를 가지게 되고, R, G, B 모두 첫째 칸에 들어올 수 있기 때문에 *3을 해야 모든 경우의 수가 된다.
'''