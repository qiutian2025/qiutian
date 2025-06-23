import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime, timedelta

class ScheduledShutdownApp:
    def __init__(self, master):
        self.master = master
        master.title("定时关机程序")
        master.geometry("300x250")

        # 时间输入组件
        tk.Label(master, text="关机时间设置").pack(pady=5)
        
        time_frame = tk.Frame(master)
        time_frame.pack()
        
        self.hour_var = tk.StringVar(value=str(datetime.now().hour))
        self.minute_var = tk.StringVar(value="00")
        self.second_var = tk.StringVar(value="00")

        tk.Spinbox(time_frame, from_=0, to=23, width=2, 
                  textvariable=self.hour_var).pack(side=tk.LEFT)
        tk.Label(time_frame, text=":").pack(side=tk.LEFT)
        tk.Spinbox(time_frame, from_=0, to=59, width=2, 
                  textvariable=self.minute_var).pack(side=tk.LEFT)
        tk.Label(time_frame, text=":").pack(side=tk.LEFT)
        tk.Spinbox(time_frame, from_=0, to=59, width=2, 
                  textvariable=self.second_var).pack(side=tk.LEFT)

        # 控制按钮
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=10)
        
        self.start_btn = tk.Button(btn_frame, text="设定关机", command=self.set_shutdown)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.cancel_btn = tk.Button(btn_frame, text="取消关机", command=self.cancel_shutdown)
        self.cancel_btn.pack(side=tk.LEFT, padx=5)

        # 状态显示
        self.status_var = tk.StringVar()
        self.status_var.set("当前状态：未设定")
        tk.Label(master, textvariable=self.status_var).pack(pady=5)

        # 倒计时显示
        self.countdown_var = tk.StringVar()
        self.countdown_var.set("剩余时间：--:--:--")
        tk.Label(master, textvariable=self.countdown_var, font=("Arial", 12)).pack(pady=10)

        # 定时器
        self.timer_id = None
        self.target_time = None

    def validate_time(self):
        try:
            h = int(self.hour_var.get())
            m = int(self.minute_var.get())
            s = int(self.second_var.get())
            if not (0 <= h <=23 and 0 <= m <=59 and 0 <= s <=59):
                raise ValueError
            return True
        except:
            messagebox.showerror("错误", "请输入有效时间（0-23时 0-59分 0-59秒）")
            return False

    def calculate_delta(self):
        now = datetime.now()
        target = now.replace(hour=int(self.hour_var.get()),
                            minute=int(self.minute_var.get()),
                            second=int(self.second_var.get()),
                            microsecond=0)
        
        # 如果目标时间已过，自动顺延到明天
        if target < now:
            target += timedelta(days=1)
        
        return (target - now).total_seconds()

    def update_countdown(self):
        delta = self.target_time - datetime.now()
        if delta.total_seconds() <= 0:
            self.countdown_var.set("正在关机...")
            os.system("shutdown /s /t 0")
            return
        
        # 更新显示
        hours, rem = divmod(int(delta.total_seconds()), 3600)
        mins, secs = divmod(rem, 60)
        self.countdown_var.set(f"剩余时间：{hours:02d}:{mins:02d}:{secs:02d}")
        
        # 每秒更新
        self.timer_id = self.master.after(1000, self.update_countdown)

    def set_shutdown(self):
        if not self.validate_time():
            return
        
        seconds = self.calculate_delta()
        self.target_time = datetime.now() + timedelta(seconds=seconds)
        
        # 设置系统关机任务
        os.system(f"shutdown /s /t {int(seconds)}")
        self.status_var.set(f"已设定 {self.target_time.strftime('%Y-%m-%d %H:%M:%S')} 关机")
        self.update_countdown()

    def cancel_shutdown(self):
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
        os.system("shutdown /a")
        self.status_var.set("已取消关机计划")
        self.countdown_var.set("剩余时间：--:--:--")
        self.target_time = None

if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduledShutdownApp(root)
    root.mainloop()
