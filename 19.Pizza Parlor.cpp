#include<iostream>
using namespace std;
#define M 10
class cqueue
{
    int pizzaorder_id[M];
    int front;
    int rear;
public:
    cqueue()
    {
        cout<<"The Circular is successfully created  and front rear points at same location."<<endl;
        front =rear=-1;
    }
    void add_order()
    {
        if((rear+1)%M==front)
        {
            cout<<"The circular queue is full.";

        }
        else
        {
            cout<<"Enter the Pizza Order Number:";
            rear=(rear+1)%M;
            cin>>pizzaorder_id[rear];
            cout<<"\nThe order is successfully added.";
        }
    }
    void serveorder()
    {
        if(front==rear)
        {
            cout<<"There are No orders !It is Empty.";
        }
        else
        {
            front=(front+1)%M;
            cout<<"\nThe Pizza Order ID "<<pizzaorder_id[front]<<" is successfully served.";
        }
    }
    void display()
    {
        int i=0;
        if(front==-1&&rear==-1)
        {
            cout<<"\nNo Orders\n";
            return;
        }
        else
        {
            cout<<"Order Id's: \n";
            for(i=front;i!=rear;i=((i+1)%M))
            {
                cout<<pizzaorder_id[i]<<"  ";
            }
            cout<<pizzaorder_id[rear];
        }
 }
};
int main()
{
    cqueue obj;
    int choice;
    while(1)
    {
        cout<<"\n1.Add Pizza Order\n2.Serve Order\n3.Display Order\n4.Exit";
        cout<<"\nEnter your choice:";
        cin>>choice;
        switch(choice)
        {
        case 1:
            obj.add_order();
            break;
        case 2:
            obj.serveorder();
            break;
        case 3:
            obj.display();
            break;
        case 4:
            exit(0);

        }
    }
}
