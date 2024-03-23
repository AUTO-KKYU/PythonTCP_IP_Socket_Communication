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
     
![image](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/2e1bd828-5c9a-42fc-a262-3f4dea8504ca)

### Server에서 Client의 접속 여부를 확인하는 관리자 모드 GUI
![Screenshot from 2024-03-23 21-24-35](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/b4d7371b-ff6b-48a9-876c-a0b49a7f9d61)

- Server의 IP를 Open / Closed 할 수 있으며, 현재 Table에 Client의 정보를 저장하여 DB로 관리 가능하다
- 또한, 접속한 Client끼리 통신하고 싶으면 Send info 버튼을 통해 요청한 client에게 상대방의 Client information을 보내줄 수 있다


### Client측 GUI (LOGIN / Check Information / Face Chat (개발 진행중))

![Screenshot from 2024-03-23 21-43-03](https://github.com/AUTO-KKYU/PythonTCP_IP_Socket_Communication/assets/118419026/e7156f18-02db-4f26-b10f-3960a21b1373)

- Client에서 Server측으로 login하면 Client에서 내부 정보를 Server에서 확인 가능.
- Server에서 어떤 유저가 접속하였고, 해당 유저의 접속 시점을 파악할 수 있다
- 또한 Server에서 상대 Client의 정보를 보내주면 상대방과 화상통화할 수 있다.

