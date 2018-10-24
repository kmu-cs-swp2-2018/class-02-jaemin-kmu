#[20181592 김재민] 보고서
코드 수정을 어떻게 해야할지 몰라서 코드리뷰때 조원들의 코드를 참고하고 교수님의 말씀을 참고하여 코드를 수정했습니다. 오류는 대체로 기존 코드에서 처리가 되어있어서 코드리뷰때 여러 학생들과 마찬가지로 따로 수정하지는 않았습니다. key 버튼이 constantList와 functionList에 존재할 때 값을 올바르게 출력해주는 코드를 수정했는데, 일단 constantList 부분은 교수님의 말씀을 참고하여 딕셔너리가 아닌 리스트 속에 튜플을 사용했습니다. 딕셔너리는 순서가 정해져있지않기 때문에 딕셔너리에서의 value와 key값을 리스트 속에서 튜플을 사용해 묶어서 표현하여 인덱스로 불러오는 방식을 택했습니다. 이때 리스트 역시 튜플과 마찬가지로 순서가 정해져있으므로 튜플대신 리스트를 사용하여 리스트 속에 리스트를 작성할 수도 있음을 확인했습니다.(코드 작성은 튜플로 했습니다) 그리고 keypad에 constantList와 constantValues를 import 해왔는데 constantValues만을 사용할 수는 없을까 생각했습니다.
        elif key in constantList:
            for i in range(0,4):
                if key in constantValues[i]:
                    self.display.setText(self.display.text() + constantValues[i][1])
위 코드의 첫줄에서 constantList 대신 constantValues를 써봤지만 원하는데로 실행되지 않고 else부분으로 넘어가서 key값 그대로를 출력했습니다. key in constantValues라고 했을 때 아마도 묶여있는 튜플이나 리스트 내부까지 고려하지않고 묶인 튜플이나 리스트를 통으로만 고려하는거 같다는 결론을 내렸습니다. 또 다른 방법도 시도해봤습니다.
        for j in range(0,4):
            if key in constantValues:
                for i in range(0,4):
                    if key in constantValues[i]:
                        self.display.setText(self.display.text() + constantValues[i][1])
리스트 속 튜플이나 리스트의 모든 원소까지 다 확인할 수 있도록 이중 포문을 사용해봤지만 이런 경우는 else 부분이 무조건 실행되게 되므로 pi3.14592 이런 식으로 출력이 되어 좋은 코드가 아니었습니다. 그리고 functionList 부분은 딕셔너리를 사용했습니다. constantList 부분처럼 하는게 더 좋은 코드라고 판단되지만 다양한 방식을 보고싶어서 functionList 부분은 딕셔너리로 작성해봤습니다. 확실히 딕셔너리가 모듈에서도 하나의 리스트만 정의해주면 되고 main 코드에서도 더 짧을 수 있다는 장점이 있지만 순서가 정의되어있지 않다는 단점이 매우 아쉬웠습니다. 딕셔너리에 포지션을 추가하여 순서를 정의해서 사용하기엔 차라리 리스트 속 튜플이나 리스트를 사용하는게 나을거라 생각합니다.
