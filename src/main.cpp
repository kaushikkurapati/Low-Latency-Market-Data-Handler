#include <iostream>
#include <cstring> // For memset

#ifdef _WIN32
    #include <winsock2.h>
    #pragma comment(lib, "ws2_32.lib") // Link the Winsock library automatically
#else
    #include <sys/socket.h>
    #include <netinet/in.h>
    #include <arpa/inet.h>
    #include <unistd.h>
#endif

int main(int argc) {
    printf("Hello World");
}