#include <stdio.h>

#define MAX 100

typedef struct {
    int bt, wt, tat;
} Process;

Process p[MAX];
int n;

void input() {
    scanf("%d", &n);
    for(int i=0;i<n;i++){
        scanf("%d",&p[i].bt);
    }
}

void adaptiveHybrid() {
    int total = 0;
    for(int i=0;i<n;i++) total += p[i].bt;

    int avg = total / n;

    int time = 0;

    printf("\n=== Adaptive Hybrid Scheduling ===\n");
    printf("Gantt Chart:\n| ");

    for(int i=0;i<n;i++){
        if(p[i].bt <= avg){
            printf("P%d | ", i+1);
            p[i].wt = time;
            time += p[i].bt;
        }
    }

    for(int i=0;i<n;i++){
        if(p[i].bt > avg){
            printf("P%d | ", i+1);
            p[i].wt = time;
            time += p[i].bt;
        }
    }

    float avg_wt=0, avg_tat=0;

    for(int i=0;i<n;i++){
        p[i].tat = p[i].wt + p[i].bt;
        avg_wt += p[i].wt;
        avg_tat += p[i].tat;
    }

    printf("\nAverage WT = %.2f", avg_wt/n);
    printf("\nAverage TAT = %.2f\n", avg_tat/n);
}

int main(){
    input();
    adaptiveHybrid();
    return 0;
}