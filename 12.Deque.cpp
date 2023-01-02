#include<iostream>
using namespace std;
class deque
{
    int a;
    deque *next;
    public:
    static deque *front,*rear;
    void enqueFront()
    {
        cout<<"Enter the Number:";
        cin>>a;
        if(front==NULL)
            rear=this;
            next=front;
            front=this;
            cout<<"Node is successfully added at front."<<endl;
    }
    void enqueRear()
    {
        cout<<"Enter the Number:";
        cin>>a;
        next=NULL;

        rear->next=this;
        rear=this;
        cout<<"The Node is successfully added at rear."<<endl;
    }
    void display()
    {
        deque *ptr=front;
        while(ptr!=NULL)
        {
            cout<<"| "<<ptr->a<<" |->";
            ptr=ptr->next;
        }
        cout<<"NULL"<<endl;
    }
    void dequeFront()
    {
        if (front==NULL)
            cout<<"The Deque is Empty."<<endl;
        else
        {
            deque *ptr=front;
            int value=ptr->a;
            front=front->next;
            delete(ptr);
            cout<<"The Node having value "<<value<<" is successfully deleted."<<endl;
            if(front==NULL)
                rear =NULL;
        }
    }
    void dequeRear()
    {
        if(rear==NULL)
            cout<<"The deque is Empty.";
        else
        {
            deque *ptr=front,*prev=NULL;
            int value=rear->a;
            while(ptr!=rear)
            {
                prev=ptr;
                ptr=ptr->next;
            }
        if(prev!=rear)
        {
            rear=prev;
            rear->next=NULL;
            delete(ptr);
        }
        else
        {
            delete(rear);
            front=rear=NULL;
        }
        cout<<"The code having value "<<value<<" is successfully Deleted."<<endl;
        }
    }
};
deque *deque::front=NULL;
deque *deque::rear=NULL;
int main()
{
    int choice;
    deque *obj;
    while(1)
    {
        cout<<"\n1.Add from Front(Enque Front)\n2.Add from Rear(Enque Rear)\n3.Delete from Front(Deque Front)";
        cout<<"\n4.Delete from Rear(Deque Rear)\n5.Display\n6.Exit";
        cout<<"\nEnter your Choice:";
        cin>>choice;
        switch(choice)
        {
            case 1:
            obj=new deque();
            obj->enqueFront();
            break;
            case 2:
            obj=new deque();
            obj->enqueRear();
            break;
            case 3:
                obj->dequeFront();
                break;
            case 4:
                obj->dequeRear();
                break;
            case 5:
            obj->display();
            break;
            case 6:
                exit(0);
        }
    }
}
