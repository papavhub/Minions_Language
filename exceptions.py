class MainException(Exception): # 시작 인사와 끝 인사가 맞지 않는 경우 발생
    def __init__(self):
        super().__init__('Bello! Poopaye!')

class NumberException(Exception): # Hana, Dul, Sae, Muak 이 외의 숫자를 사용한 경우
    def __init__(self):
        super().__init__('Hana! Dul! Sae!!')
        
class InputException(Exception): # Input 갯수가 잘못되었을 때, 발생
    def __init__(self):
        super().__init__('Tulaliloo ti amo! Input')