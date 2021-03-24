#include <iostream>
#define COLS 5

void print(int arr[][COLS], int n){
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            std::cout << arr[i][j] << " ";
        }
        std::cout << "\n";
    }
}

int main(){
    int n = 5;
    int p[] = {5, 4, 6,2,7};
    int m[5][5] = {0};
    int s[5][5] = {0};

    int j, min, q;

    for (int d = 1; d < n - 1; d++)
    {
        for (int i = 1; i < n-d ; i++)
        {
            j = i + d;

            min = 32767;

            for (int k = i; k <= j-1; k++)
            {
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j];
                
                if (q < min) 
                {
                    min = q;
                    s[i][j] = k;
                }
            }
            m[i][j] = min;
        }
        print(m, 5);
        std::cout << "\n";
    }
    
    std::cout << m[1][n-1] << std::endl;

    return 0;
}

