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
---

### Server에서 Client의 접속 여부를 확인하는 관리자 모드 GUI
![Screenshot from 2024-03-23 21-24-35](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/f579c752-11d7-41ef-8522-69cf0d6fb7e7)

- Server의 IP를 Open / Closed 할 수 있으며, 현재 Table에 Client의 정보를 저장하여 DB로 관리 가능하다
- 또한, 접속한 Client끼리 통신하고 싶으면 Send info 버튼을 통해 요청한 client에게 상대방의 Client information을 보내줄 수 있다


### Client측 GUI (LOGIN / Check Information / Face Chat (개발 진행중))

![Screenshot from 2024-03-23 21-43-03](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/e7156f18-02db-4f26-b10f-3960a21b1373)

- Client에서 Server측으로 login하면 Client에서 내부 정보를 Server에서 확인 가능.
- Server에서 어떤 유저가 접속하였고, 해당 유저의 접속 시점을 파악할 수 있다
- 또한 Server에서 상대 Client의 정보를 보내주면 상대방과 화상통화할 수 있다.

--- 
#### ROS를 사용하여 분산 시스템에서 다중 로봇 통신 가능
- 노드들을 이용하여 TCP/IP 소켓 통신을 통해 서로 통신하고 데이터를 교환할 수 있다
- 다중 로봇 제어 및 다중 시스템 제어 가능

![Screencast from 03-24-2024 01_11_26 PM](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/f72b76c0-cb5d-4866-8395-25ce35c47d1e)


#### 추가적으로 할 수 있는 점
- 각 Client들의 DB를 서로 Share할 수 있음 -> 데이터 공유 가능
- 권한 부여 가능
- 실시간 데이터 적용 -> 모니터링 가능 및 유용한 서비스 제작 가능
