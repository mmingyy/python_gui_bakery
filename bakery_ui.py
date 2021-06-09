import tkinter
from tkinter import *
from tkinter import ttk


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        #추가 코드
        # --------ttk써도 상관은 없음--------------------
        # num_san=StringVar()
        # self.entry_san=ttk.Entry(window,width=7,textvariable=num_san)
        # self.entry_san.grid(column=2,row=1,sticky=W) #서쪽으로 붙어라
        # --------------------------------------------
        self.entry_san=Entry(window,width=7)
        self.entry_san.grid(column=2,row=1,sticky=W) #서쪽으로 붙어라

        self.entry_cake=Entry(window,width=7)
        self.entry_cake.grid(column=2,row=2,sticky=W) #서쪽으로 붙어라

        ttk.Label(window, text="샌드위치 (5000원)").grid(column=1, row=1, sticky=W)
        ttk.Label(window, text="케이크 (20000원)").grid(column=1, row=2, sticky=W)
        ttk.Button(window, text="주문하기",
                   command=self.send_order).grid(column=1, row=3, sticky=W)
        #send_order에서도 이용할 수 있도록 self.nSan해주기


    def send_order(self):
        order_text = ''
        # 샌드위치 int변환 성공 시 success_san = 1
        try:
            getSan = int(self.entry_san.get())
            success_san = 1
        except:
            # int 변환 시 에러 발생 시 success_san = 0
            success_san = 0
            pass
        # 케이크 int변환 성공 시 success_cake = 1
        try:
            getCake = int(self.entry_cake.get())
            success_cake = 1
        except:
            success_cake = 0
            pass

        # san, cake 둘 다 잘 들어왔을 때
        if (success_san==1 and getSan > 0
            and success_cake==1 and getCake > 0):
            order_text = self.name + ' : ' + '샌드위치 (5000원) ' + str(getSan) + '개, 케이크 (20000원) ' + str(getCake) + '개'

        # san만 잘 들어왔을 때
        #                                           정수가 아니거나 | 정수여도 0보다 큰게 아님
        elif (success_san==1 and getSan > 0 and (success_cake==0 or not getCake > 0)):
            order_text = self.name + ' : ' + '샌드위치 (5000원) ' + str(getSan) + '개'

        # cake만 잘 들어왔을 때
        elif (success_cake==1 and getCake > 0 and (success_san==0 or not getSan > 0)):
            order_text = self.name + ' : ' + '케이크 (20000원) ' + str(getCake) + '개'

        # -3 같은 애들은 int여서 여전히 order_text=''임
        # 그런 애들은 출력 조차 안 되게!
        if (order_text != ''):
            self.bakeryView.add_order(order_text)

if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
