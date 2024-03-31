#include <stdio.h>
#include <time.h>

int main() {
    // 현재 시간을 저장하기 위한 time_t 타입 변수 선언
    time_t now;
    // tm 구조체를 사용하여 시간 정보를 담을 구조체 포인터 선언
    struct tm *tm_info;

    // 현재 시간을 time_t 타입 변수에 저장
    time(&now);
    // 현재 지역 시간대로 변환하여 tm 구조체에 저장
    tm_info = localtime(&now);

    // YYYY-MM-DD 형식으로 날짜 출력
    printf("%d-%02d-%02d\n", tm_info->tm_year + 1900, tm_info->tm_mon + 1, tm_info->tm_mday);

    return 0;
}
