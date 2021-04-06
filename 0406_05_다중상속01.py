# 다중 상속의 문제점

class Tiger:
    def jump(self):
        print("호랑이 점프")
    def cry(self) :
        print("호랑이 어흥~~")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cry(self) :
        print("사자 으르렁~~")

# 다중으로 상속으로 받을 때 이름 충돌

class Liger(Lion, Tiger): # 다중 상속에서 같은 메서드가 있을 때 먼저
    # 상속받은 라이온이 실행이 된다. 단점 : 숨어있는 거 불러올 수가 없음
    # 메서드 이름을 바꾸면 안되냐 크라이1, 크라이2 이런식으로 안됨
    # 예를 들어 깃허브에서 불러온 코드면 수정이 안됨
    # 이름 바꾸기 어려울 상황이 있을 수 있기 때문
    def play(self):
        print("라이거와 놀기")

# 인스턴스 생성
l = Liger()
# l.play()
# l.jump()
# l.bite()
l.cry()
print("내부에 상속 순서 튜플 : {0}".format(Liger.__mro__))


        
