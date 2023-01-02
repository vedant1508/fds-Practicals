#include<iostream>
using namespace std;
class que
{
    int jobId,jobTime;
    que *next;
public:
    static que *front,*rear;
    que()
    {
        cout<<"\nEnter the Job ID:";
        cin>>jobId;
        cout<<"\nEnter the Job time:";
        cin>>jobTime;
        next=NULL;

        if(front==NULL)
        {
            front=rear=this;
        }
        else
        {
            rear->next=this;
            rear=this;
        }
        cout<<"\n The Job ID is "<<jobId<<" is successfully added in the Queue.";
    }
    void processjob()
    {
        if(front==NULL)
        {
            cout<<"\nThe job Queue is empty.";
        }
        else
        {
            cout<<"The Job with ID "<<front->jobId<<" is successfully processed and will be removed from the queue.";
            que *ptr=front;
            front=front->next;
            delete(ptr);
            cout<<"\nThe Job is successfully removed from the queue.";
        }
    }
    void displayJobQue()
    {
        que *ptr=front;
        cout<<"\nThe Job Queue is:";
        while(ptr!=NULL)
        {
            cout<<ptr->jobId<<" ";
            ptr=ptr->next;
        }
    }
};
que *que::front=NULL;
que *que::rear=NULL;
int main()
{
    que *obj;
    int choice;
    while(1)
    {
        cout<<"\n1.Add job in queue\n2.Process the job and delete\n3.Display\n4.Exit";
        cout<<"\nEnter your choice";
        cin>>choice;
        switch(choice)
        {
        case 1:
            obj=new que();
            break;
        case 2:
            obj->processjob();
            break;
        case 3:
            obj->displayJobQue();
            break;
        case 4:
            exit(0);
        }
    }
    return 0;
}
