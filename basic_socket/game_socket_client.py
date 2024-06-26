import socket

HOST = '192.168.0.31'
PORT = 50008

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        n = input("1-99사이의 숫자를 입력하세요(0은 게임포기):")
        if not n.strip():
            print("입력값이 잘못되었습니다.")
            continue
        s.sendall(n.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(f'서버응답:{data}')
        if data == "정답" or data == "종료":
            break