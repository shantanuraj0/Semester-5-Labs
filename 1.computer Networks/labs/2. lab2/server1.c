/*Single client can connect to this server at same time*/

/*Including Necessary Header files*/
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

/*Maximum size of buffer*/
#define MAX_INPUT_SIZE 256


int main(int argc, char *argv[]) 
{ 
      int fd,sockfd, newsockfd, clilen,portno,n,flag; 
      struct sockaddr_in serv_addr,cli_addr; 
      
	  /*creation of buffer and handling errors*/
	  char buffer[MAX_INPUT_SIZE]; 
	  if(argc<2) 
      { 
        fprintf(stderr," no port\n"); 
        exit(1); 
      } 

      portno=atoi(argv[1]); 
	
	  /* Creating server socket */
      sockfd=socket(AF_INET, SOCK_STREAM,0); 
	  if(sockfd<0)
	  {	 
          perror("error opening socket");
		  exit(1); 
	  }


	  bzero((char*)&serv_addr,sizeof(serv_addr)); 
      serv_addr.sin_family=AF_INET; 
      serv_addr.sin_addr.s_addr=(htonl)INADDR_ANY; 
      serv_addr.sin_port=htons(portno); 

	 /*Bind the socket to the port number known to all clients*/  
	  if(bind(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr))<0) 
      {
		  perror("error binding");
 		  exit(0);
	  }
 
      /*Listen for the connection request*/
	  if(listen(sockfd,4)<0)
	  {
		  perror("listen");
		  exit(1);
	  }  
	
      
	  /*Accept connection request*/
	  clilen=sizeof(serv_addr); 
      newsockfd = accept(sockfd,(struct sockaddr *)&cli_addr,(socklen_t*)&clilen); 
      
	  if(newsockfd<0) 
      {
	 	perror("error on accept");
		exit(1);		
	  } 
 	  else
	  {
			printf("Connected with client socket number: %d \n",newsockfd);		
	  }
      
	  /*clearing the buffer*/
	  bzero(buffer,MAX_INPUT_SIZE) ; 

	  
	  /*Send/Receive data*/
      while(read(newsockfd,buffer,sizeof(buffer)))  
      { 
              
        printf("Client socket %d sent message: %s",newsockfd,buffer); 
		flag=0;
        int num1=0,num2=0;
        int c,j;
	    
		for(int i=0;i<strlen(buffer)-1;i++)
	    {
			if(buffer[i]=='+' || buffer[i]=='-' || buffer[i]=='*' || buffer[i]=='/')
			{
				flag=1;j=i;
			}
            else
			{		    	
		
				if(flag==0)
				{
					num1=(10*num1)+(buffer[i]-'0');
				}
                else if(flag!=0)
				{
					 num2=(10*num2)+(buffer[i]-'0');
				}
			}
        	
	    }
            
            
        int result;
             
		if(buffer[j]=='+')	
		result=num1+num2;
		else if(buffer[j]=='-')	
		result=num1-num2;
		else if(buffer[j]=='/')	
		result=num1/num2;
		else if(buffer[j]=='*')	
		result=num1*num2;	

	    printf("sending reply:%i\n",result);
	    bzero(buffer,MAX_INPUT_SIZE) ; 
	    sprintf(buffer,"%d",result);
	    send(newsockfd , buffer, strlen(buffer),0);
	    bzero(buffer,MAX_INPUT_SIZE) ; 
            
          
      }

	  
      if(read(newsockfd,buffer,sizeof(buffer))<=0)
      printf("client disconneted........\n");
      
	  /* Close the socket*/
      close(newsockfd);
      return 0; 
} 