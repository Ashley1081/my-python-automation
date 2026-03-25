import ctypes
import time

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def get_mouse_pos():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

print("==================================================")
print(" 🎯 [智能狙击雷达] 已启动！(纯净版无依赖)")
print(" 👉 请将鼠标移动到你要抓取的按钮上。")
print(" 📸 瞄准后，按下【F8】键，自动记录当前坐标。")
print(" 🛑 全部抓完后，按下【ESC】键，安全退出雷达。")
print("==================================================\n")

# Windows 虚拟键码大全 (VK_CODE)
VK_F8 = 0x77     # F8键
VK_ESCAPE = 0x1B # ESC键

count = 1
recorded_coords = []

while True:
    # 1. 监听 ESC 键：如果按下，直接退出循环
    # 0x8000 表示按键当前处于按下状态
    if ctypes.windll.user32.GetAsyncKeyState(VK_ESCAPE) & 0x8000:
        print("\n\n✅ 收到退出指令！雷达已安全关闭。")
        break

    # 2. 监听 F8 键：如果按下，立刻抓取坐标并打印
    if ctypes.windll.user32.GetAsyncKeyState(VK_F8) & 0x8000:
        x, y = get_mouse_pos()
        print(f"📍 成功锁定第 {count} 个目标坐标: ({x}, {y})")
        recorded_coords.append((x, y))
        count += 1
        
        # 扣动扳机后的“防抖”延时，防止你按一下 F8 记录了十几条重复坐标
        time.sleep(0.4) 

    # 短暂休眠，防止 CPU 占用率飙升到 100%
    time.sleep(0.02) 

# 退出前，帮你把所有抓到的坐标汇总打印出来，方便你直接复制
print("\n📝 [战报] 你刚刚抓取的所有坐标如下，可以直接填入主程序：")
for i, coord in enumerate(recorded_coords, 1):
    print(f"坐标 {i}: {coord}")
