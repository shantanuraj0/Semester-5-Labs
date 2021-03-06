/*Including necessary header files*/
#include<stdlib.h> 
#include<string.h> 
#include<stdio.h> 
#include<sys/types.h> 
#include<sys/socket.h> 
#include<netinet/in.h> 
#include<arpa/inet.h> 
#include<sys/fcntl.h>
#include <unistd.h>
#include <netdb.h>

/*Maximum capacity of buffer*/
#define MAX_INPUT_SIZE 256


int main(int argc, char *argv[])
{
	int sockfd, portnum, n;
	struct sockaddr_in server_addr;
	
	/*creation of buffer*/
	char inputbuf[MAX_INPUT_SIZE]; 
	if (argc < 3) 
	{
		fprintf(stderr,"usage %s <server-ip-addr> <server-port>\n", argv[0]);
		exit(0);
	}

	portnum = atoi(argv[2]);

	/* Creating client socket */
	sockfd = socket(AF_INET, SOCK_STREAM, 0); 
	if (sockfd < 0)
	{
		fprintf(stderr, "ERROR opening socket\n"); exit(1);
	}

	/* Fill in server address */
	bzero((char *) &server_addr, sizeof(server_addr)); 
	server_addr.sin_family = AF_INET; 
	if(!inet_aton(argv[1], &server_addr.sin_addr))
	{
		fprintf(stderr, "ERROR invalid server IP address\n"); exit(1);
	}
	server_addr.sin_port = htons(portnum);
	
	
	/*Connecting to the server */
	if (connect(sockfd,(struct sockaddr *)&server_addr,sizeof(server_addr))<0)
	{
		fprintf(stderr, "ERROR connecting\n"); exit(1);
 	}
	printf("Connected to server\n");

	
	do
	{
		
		/* Ask user to send message to the server */ 
		printf("Please enter the message to the server: "); 
		/*clearing the buffer*/
		bzero(inputbuf,MAX_INPUT_SIZE); 
		fgets(inputbuf,MAX_INPUT_SIZE-1,stdin);

		/* Writing to server */
		n = write(sockfd,inputbuf,strlen(inputbuf)); 
		if (n < 0)
		{	
			fprintf(stderr, "ERROR writing to socket\n"); exit(1);
		}

		/* Reading reply */ 
		bzero(inputbuf,MAX_INPUT_SIZE);
		n = read(sockfd,inputbuf,(MAX_INPUT_SIZE-1)); 
		if (n < 0)
		{
			fprintf(stderr, "ERROR reading from socket\n"); exit(1);
		}
		printf("Server replied: %s\n",inputbuf);

	} while(1);

return 0;
}
