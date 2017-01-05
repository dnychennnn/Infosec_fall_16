#include <pbc.h>
#include <pbc_test.h>
#include <stdio.h>
#include <time.h>

FILE *pFile1;
FILE *pFile2;
FILE *pFile3;
FILE *pFile4;
FILE *pFile5;
FILE *pFile6;
FILE *pFile7;

void bilinear(int setSize, int argc, char **argv) {
        clock_t startTime, endTime;

        pairing_t pairing;
        element_t g;
        element_t public_key;
        element_t secret_key;
        element_t public_public_key;

        element_t h_pri[setSize];
        element_t h_pub[setSize];
        element_t sig_pri[setSize];
        element_t sig_pub[setSize];
        element_t temp1_pri[setSize];
        element_t temp2_pri[setSize];
        element_t temp1_pub[setSize];
        element_t temp2_pub[setSize];

        pbc_demo_pairing_init(pairing, argc, argv);

        element_init_G2(g, pairing);
        element_init_G2(public_key, pairing);
        element_init_G2(public_public_key, pairing);
        for (int i = 0; i < setSize; i++) {
                element_init_G1(h_pri[i], pairing);
                element_init_G1(h_pub[i], pairing);
                element_init_G1(sig_pri[i], pairing);
                element_init_G1(sig_pub[i], pairing);
                element_init_GT(temp1_pri[i], pairing);
                element_init_GT(temp2_pri[i], pairing);
                element_init_GT(temp1_pub[i], pairing);
                element_init_GT(temp2_pub[i], pairing);
        }
        element_init_Zr(secret_key, pairing);

	
        startTime = clock();
        element_random(g); // generate system parameters
        element_random(secret_key); // generate private key
        element_pow_zn(public_key, g, secret_key); // and the corresponding public ket
        element_pow_zn(public_public_key, g, public_key); // and the corresponding public ket
        endTime = clock();
        printf("Key generation took: %f seconds\n", ((float)(endTime - startTime) / CLOCKS_PER_SEC ));
	
	fprintf(pFile1, "%d\t%f\n", setSize, (float)(endTime - startTime) / CLOCKS_PER_SEC);

	fprintf(pFile2, "%d\t%f\n", setSize, (float)0);

        startTime = clock();
        for (int i = 0; i < setSize; i++) {
                element_from_hash(h_pri[i], "", i);
                element_pow_zn(sig_pri[i], h_pri[i], secret_key);
        }
        endTime = clock();
        printf("Accumulated %d elements in %f seconds with private key\n", setSize, ((float)(endTime - startTime) / CLOCKS_PER_SEC ));
	fprintf(pFile3, "%d\t%f\n", setSize, (float)(endTime - startTime) / CLOCKS_PER_SEC);	

        startTime = clock();
        for (int i = 0; i < setSize; i++) {
                element_from_hash(h_pub[i], "", i);
                element_pow_zn(sig_pub[i], h_pub[i], public_key);
        }
        endTime = clock();
        printf("Accumulated %d elements in %f seconds with public key\n", setSize, ((float)(endTime - startTime) / CLOCKS_PER_SEC ));
	fprintf(pFile4, "%d\t%f\n", setSize, (float)(endTime - startTime) / CLOCKS_PER_SEC);

        startTime = clock();
        for (int i = 0; i < setSize; i++) {
                pairing_apply(temp1_pri[i], sig_pri[i], g, pairing);
                pairing_apply(temp2_pri[i], h_pri[i], public_key, pairing);
        }
        endTime = clock();
        printf("Generated %d witnesses in %f seconds with private key\n", setSize, ((float)(endTime - startTime) / CLOCKS_PER_SEC ));
	fprintf(pFile5, "%d\t%f\n", setSize, (float)(endTime - startTime) / CLOCKS_PER_SEC);

        startTime = clock();
        for (int i = 0; i < setSize; i++) {
                pairing_apply(temp1_pub[i], sig_pub[i], g, pairing);
                pairing_apply(temp2_pub[i], h_pub[i], public_public_key, pairing);
        }
        endTime = clock();
        printf("Generated %d witnesses in %f seconds with public key\n", setSize, ((float)(endTime - startTime) / CLOCKS_PER_SEC ));
	fprintf(pFile6, "%d\t%f\n", setSize, (float)(endTime - startTime) / CLOCKS_PER_SEC);

        startTime = clock();
        for (int i = 0; i < setSize; i++) {
                if (!element_cmp(temp1_pri[i], temp2_pri[i])) {
                        continue;
                } else {
                        printf("signature does not verify\n");
                        return;
                }
        }
        endTime = clock();
        printf("Verified %d elements in %f seconds against private accumulator\n", setSize, ((float)(endTime - startTime) / CLOCKS_PER_SEC ));
	fprintf(pFile7, "%d\t%f\n", setSize, (float)(endTime - startTime) / CLOCKS_PER_SEC);

        startTime = clock();
        for (int i = 0; i < setSize; i++) {
                // element_printf("%B\n", temp1_pub[i]);
                // element_printf("%B\n", temp2_pub[i]);
                if (!element_cmp(temp1_pub[i], temp2_pub[i])) {
                        continue;
                } else {
                        printf("signature does not verify\n");
                }
        }
        endTime = clock();
        printf("Verified %d elements in %f seconds against public accumulator\n", setSize, ((float)(endTime - startTime) / CLOCKS_PER_SEC ));

        element_clear(public_key);
        element_clear(public_public_key);
        element_clear(secret_key);
        element_clear(g);
        for (int i = 0; i < setSize; i++) {
                element_clear(sig_pri[i]);
                element_clear(sig_pub[i]);
                element_clear(h_pri[i]);
                element_clear(h_pub[i]);
                element_clear(temp1_pri[i]);
                element_clear(temp2_pri[i]);
                element_clear(temp1_pub[i]);
                element_clear(temp2_pub[i]);
        }
        pairing_clear(pairing);
}

int main(int argc, char **argv) {
	pFile1 = fopen("../output/output_keygen.txt", "w");
        pFile2 = fopen("../output/output_prime.txt", "w");
        pFile3 = fopen("../output/output_accpriv.txt", "w");
        pFile4 = fopen("../output/output_accpub.txt", "w");
        pFile5 = fopen("../output/output_witpriv.txt", "w");
        pFile6 = fopen("../output/output_witpub.txt", "w");
        pFile7 = fopen("../output/output_verif.txt", "w");


	
	for(int i=1;i<=9;i++){
	    bilinear(i*1000, argc, argv);
	}

        fclose(pFile1);
	fclose(pFile2);
	fclose(pFile3);
	fclose(pFile4);
	fclose(pFile5);
	fclose(pFile6);
	fclose(pFile7);

        return 0;
}
