#include <stdio.h>

int main()
{
    int initamount = 30000;
    int withdraw,deposit,a,cont,con,disp;
    rep:
    printf("\nDisplay Balance\nType 0 to Yes and 1 to No: ");
    scanf("%d",&disp);
    if(disp==0)
    printf("\nYour Current Balance : %d",initamount);
    repeat:
    printf("\nPress 0 to Withdraw and 1 to deposit : ");
    scanf("%d",&a);
    if(a==0)
    {
        printf("Enter Withdraw amount : ");
        scanf("%d",&withdraw);
        if(withdraw>initamount)
        {
            printf("\nInsufficient amount");
             goto repeat;
        }
        else if(withdraw<=0)
        {
            printf("\nInvalid Amount entered");
             goto repeat;
        }
        else if(withdraw<initamount)
        {
            initamount=initamount-withdraw;
            printf("Withdraw amount : %d , Balance Amount : %d", withdraw,initamount);
            printf("\nEnter 0 to Finish Transaction , 1 to Continue Transaction : ");
            scanf("%d",&cont);
            if(cont==0)
            printf("\nThank You");
            else
            goto rep;
        }
    }
    else if(a==1)
    {
        printf("\nEnter Deposit amount : ");
        scanf("%d",&deposit);
        if(deposit<=0)
        {
        printf("\nInvalid Amount Entered");
        goto repeat;
        }
        if(deposit>0)
        {
            initamount=initamount+deposit;
             printf("\nDeposit Amount : %d, Balance Amount : %d", deposit, initamount);
            printf("\nEnter 0 to Finish Transaction , 1 to Continue Transaction : ");
            scanf("%d",&con);
            if(con==0)
            printf("\nThank You");
            else
            goto rep;
        }

    }
    else
    printf("\nYou Entered Wrong value ");
    goto repeat;
}
