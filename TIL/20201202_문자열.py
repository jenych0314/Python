# def search():
#         for n in range(len(P_list)):
#             if intext.find(P_list[n]) >= 0:
#                 print (P_list[n])
#                 print ("처음 시작 위치 : %d"%(intext.find(P_list[n])+1))
#             else:
#                 print(P_list[n])
#                 print("문자열 None")
#             print ("경고 발생 횟수 : %d\n"%intext.count(P_list[n]))

# intext = input("메세지를 입력하시오:")
#     search()

text = u"무사시노의 구릉지대에 약 10만평의 광대한 캠퍼스를 갖고있는 조우케이가쿠인대학교. 상류층의 자녀가 모이는 것으로 유명한 대학으로 캠퍼스 주변에는 외제차나 고급대형차가 줄줄이 주차되어있고, 고급브랜드로 몸을 휘감은 학생들이 근심없는 밝은 표정으로 움직이고 있다. 불과 몇 년 전까지만해도 조우케이가쿠인대학교라고 하면 그저 학교 조경이 잘 된 학교로만 알려졌고, 학력쪽의 평가는 별로 대단하지 않았다. 그런데 요 몇 년간 상류명문 브랜드를 지향하자 최근엔 수험생들의 인기가 급격하게 상승해서 지금은 난이도 랭킹에서도 명문 3대사립에 육박할 기세였다."

# print(text.find('.'))
# print(text.find('.',53+1))

# n = 0
# while True:
#     if text in '.':
#         print(text.find('.'), n)
#         n += text.find('.') + 1
#         print(n)
print(text.find('hello'))
#''나 ""는 카운트해서 1번 나오고 다음 2번째가 나오기 전까지는 그냥 읽음
#[], (), 「」 들은
#[, (, 「와 ], ), 」로 나누어서 나오기 전까지는 그냥 읽음