# PythonTCP_IP_Socket_Communication
TCP/IP 파이썬 소켓 통신을 PyQt6를 사용하여 Server &lt;-> 다중 clients 제어 

### TCP/IP 소켓 통신 :  네트워크를 통해 데이터를 주고받기 위한 표준 프로토콜

- TCP/IP 소켓 통신을 위한 조건
1. Server와 Client 모두 같은 네트워크내에 연결되어 있어야 통신이 가능
2. Server와 Client 서로 통신을 주고받을 수 있는 각각의 network ip주소를 알아야 함
   - Use 'ipconfig' or 'ifconfig' to enable checking your IP address.
3. 포트 번호: Server와 Client 서로가 약속된 port번호 하에 연결이 가능
4. 어떤 프로토콜을 사용하는지에 따라 통신할 수 있음
   - TCP
   - UDP

![그림2](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/1f7047d0-e5cb-4a4f-8caa-af7a0e09885e)

---
### Socket communication 요구사항
-  현재 시스템에서 열린 모든 네트워크를 조회
```sh
$ sudo lsof -i -P -n | grep LISTEN
$ ss -tuln
$ netstat -tuln
```
- 추가적으로 설치해야 할 부분
```sh
$ sudo apt-get install portaudio19-dev
$ pip install pyaudio
$ pip install vidstream
```

- socket이란 모듈은 내장되어있는 모듈이므로 따로 설치해 줄 필요는 없다

---

### Server에서 Client의 접속 여부를 확인하는 관리자 모드 GUI
![Screenshot from 2024-03-30 21-52-25](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/ad331e07-2f74-41b0-931e-7aaec9b69c2a)

- Server의 IP를 Open / Closed 할 수 있으며, 현재 GUI 상 Table에 Client의 정보는 자동적으로 DB에 저장되도록 설정하였다
![Screenshot from 2024-03-30 22-09-45](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/39f6b4c5-a9d8-4391-8247-9d0c2c7fdfa4)

- 추가적으로 ExportCSV 버튼을 누르면 특정 경로를 설정하여 테이블을 CSV FILE 형식으로 저장할 수 있다

### Client측 GUI (LOGIN / Check Information / Face Chat)
![Screenshot from 2024-03-31 19-35-43](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/237edac4-48ab-4000-97c6-7a0a31951233)

![Screenshot from 2024-03-30 22-07-18](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/929bd5e0-139f-48ea-aabe-3b80f5159184)

![GIFMaker_me](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/892624a1-2283-45eb-bef5-25b811f3c4e4) 
![GIFMaker_me (1)](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/f6a5bbc9-7b9c-4aec-bdaf-ddaa6937398f)


- Client에서 Server측으로 login하면 Client에서 내부 정보를 Server에서 확인 가능
- Server에서 어떤 유저가 접속하였고, 해당 유저의 접속 시점을 파악할 수 있다
- 또한 Server에서 상대 Client의 정보를 보내주면 상대방과 화상통화할 수 있다
- 화상통화에 대한 부분은, 최종적으로 정리된 후 업로드 할 예정이다




---

### 최종 구현 영상



#### Face chat 개발 사항 정리
- Face chat 개발 성공
- 현재 수어인식 딥러닝 모델을 활용한 커뮤니케이션 프로그램을 소켓 통신을 활용하여 진행 중이다
- 마무리 단계에 접어들었으며, 상대방 캠 + 자신 캠 띄우기 진행중이다.
---
#### ROS를 사용하여 분산 시스템에서 다중 로봇 통신 가능
- 노드들을 이용하여 TCP/IP 소켓 통신을 통해 서로 통신하고 데이터를 교환할 수 있다
- 다중 로봇 제어 및 다중 시스템 제어 가능

#### 추가적으로 할 수 있는 점
- 각 Client들의 DB를 서로 Share할 수 있음 -> 데이터 공유 가능
- 권한 부여 가능
- 실시간 데이터 적용 -> 모니터링 가능 및 유용한 서비스 제작 가능
