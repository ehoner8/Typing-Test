#include "names.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

/*
bool check_winner(int *nums){
    int noz = 0;
    printf("%d %d\n", (int) (sizeof(nums)), (int) (sizeof(nums[0])));
    int length = ((int) (sizeof(nums)))/((int) (sizeof(nums[0])));
    printf("\n%d\n", length);
    for (int n = 0; n < length; n++){
        if (nums[n] == 0){
            noz += 1;
        }
    }
    if (noz == length - 1){
        return true;
    }
    return false;
}
 * */

int main(void) {
    /*
{
	const char *player_name[] = {
    "Ada Lovelace",
    "Margaret Hamilton",
    "Katherine Johnson",
    "Joy Buolamwini",
    "Grace Hopper",
    "Adele Goldberg",
    "Annie Easley",
    "Jeannette Wing",
    "Mary Kenneth Keller",
    "Megan Smith",
};
*/

    typedef enum { DOT, LEFT, CENTER, RIGHT } Position;
    const Position die[6] = { DOT, DOT, DOT, LEFT, CENTER, RIGHT };

    int num_players = 3;
    printf("Number of players (3 to 10)? ");
    int scanf_result = scanf("%d", &num_players);

    if ((scanf_result < 1) || (num_players < 3) || (num_players > 10)) {
        fprintf(stderr, "Invalid number of players. Using 3 instead.\n");
        num_players = 3;
    }

    unsigned seed = 4823;
    printf("Random-number seed? ");
    scanf_result = scanf("%u", &seed);

    if (scanf_result < 1) {
        fprintf(stderr, "Invalid seed. Using 4823 instead.\n");
        seed = 4823;
    }

    int player_chips[num_players];
    for (int i = 0; i < num_players; i++) {
        player_chips[i] = 3;
    }

    srandom(seed);

    int nor;
    int p = 0;
    int noz = 0;
    int s = 0;
    while (true) {
        nor = 3;
        if (player_chips[p] < 3) {
            nor = player_chips[p];
        }
        if (nor == 0) {
            s = 1;
        }
        while (nor > 0) {
            unsigned int rand = random() % 6;
            int roll = die[rand];
            if (roll == DOT) {
                nor -= 1;
            }
            if (roll == RIGHT) {
                if (p == 0) {
                    player_chips[num_players - 1] += 1;
                } else {
                    player_chips[p - 1] += 1;
                }
                player_chips[p] -= 1;
                nor -= 1;
            }

            if (roll == CENTER) {
                player_chips[p] -= 1;
                nor -= 1;
            }

            if (roll == LEFT) {
                if (p == (num_players - 1)) {
                    player_chips[0] += 1;
                } else {
                    player_chips[p + 1] += 1;
                }
                player_chips[p] -= 1;
                nor -= 1;
            }
        }
        if (s != 1) {
            printf("%s: ends her turn with %d\n", player_name[p], player_chips[p]);
        }
        s = 0;

        for (int num = 0; num < num_players; num++) {
            if (player_chips[num] == 0) {
                noz += 1;
            }
        }
        if (noz == num_players - 1) {
            for (int p = 0; p < num_players; p++) {
                if (player_chips[p] != 0) {
                    printf("%s won!\n", player_name[p]);
                    return 0;
                }
            }
        }
        noz = 0;

        if (p == num_players - 1) {
            p = 0;
        } else {
            p += 1;
        }
    }

    return 0;
}
