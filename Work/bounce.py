# bounce.py
#
# Exercise 1.5
# 고무 공을 100 미터 높이에서 떨어뜨린다. 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오른다. 
# 공이 열 번 튈 동안, 그때마다 높이를 나타내는 테이블을 프린팅하는 프로그램 bounce.py를 작성하라.
height = 100
for i in range(10) :
    height *= (3/5)
    print(i+1, " ", round(height, 4))