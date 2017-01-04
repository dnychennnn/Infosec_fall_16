#include "FHE.h"
#include "EncryptedArray.h"
#include <NTL/lzz_pXFactoring.h>
#include <fstream>
#include <sstream>
#include <sys/time.h>


int main(int argc, char **argv)
{

 /* On our trusted system we generate a new key
     * (or read one in) and encrypt the secret data set.
     */

    long m=0, p=257, r=1; // Native plaintext space
                        // Computations will be 'modulo p'
    long L=16;          // Levels
    long c=3;           // Columns in key switching matrix
    long w=64;          // Hamming weight of secret key
    long d=0;
    long security = 128;
    ZZX G;
    m = FindM(security,L,c,p, d, 0, 0);

    FHEcontext context(m, p, r);
    // initialize context
    buildModChain(context, L, c);
    // modify the context, adding primes to the modulus chain
    FHESecKey secretKey(context);
    // construct a secret key structure
    const FHEPubKey& publicKey = secretKey;
    // an "upcast": FHESecKey is a subclass of FHEPubKey

    //if(0 == d)
    G = context.alMod.getFactorsOverZZ()[0];

   secretKey.GenSecKey(w);
   // actually generate a secret key with Hamming weight w

   addSome1DMatrices(secretKey);
   cout << "Generated key" << endl;

   EncryptedArray ea(context, G);
   // constuct an Encrypted array object ea that is
   // associated with the given context and the polynomial G

   long nslots = ea.size();
   //cout<<"nslots: "<< nslots << endl;   

 

   vector<long> v1;
   v1.push_back(48);
   for(int i = 0 ; i < nslots-1; i++) {
       v1.push_back(0);
   }
   
   Ctxt ct1(publicKey);
   

   clock_t start = clock();
   ea.encrypt(ct1, publicKey, v1);
   cout << "v1 encrypt time = " << float(clock() - start)/CLOCKS_PER_SEC << endl;

   
   vector<long> dv1;
   start = clock();
   ea.decrypt(ct1, secretKey, dv1);
   cout << "v1 decrypt time = " << float(clock() - start)/CLOCKS_PER_SEC << endl;
   for(int i=0; i<5; i++)
   cout << dv1[i] << endl;
   

   vector<long> v2;
   Ctxt ct2(publicKey);
   v2.push_back(234);
   for(int i=0;i<nslots-1;i++)
	v2.push_back(0);
   ea.encrypt(ct2, publicKey, v2);
   


      // On the public (untrusted) system we
   // can now perform our computation

   Ctxt ctSum = ct1;
   Ctxt ctProd = ct1;


   start = clock();
   ctSum += ct2;
   cout << "sum time = " << float(clock() - start)/CLOCKS_PER_SEC << endl;

   start = clock();
   ctProd *= ct2;
   cout << "product time = " << float(clock() - start)/CLOCKS_PER_SEC << endl;


    vector<long> res;
    start=clock();
    ea.decrypt(ctSum, secretKey, res);
    cout << "sum decrypt time = " << float(clock() - start)/CLOCKS_PER_SEC << endl;


    cout << "All computations are modulo " << p << "." << endl;
   
    cout << v1[0] << " + " << v2[0] << " = " << res[0] << endl;
    
    start = clock();
    ea.decrypt(ctProd, secretKey, res);
    cout << "product decrypt time = " << float(clock() - start)/CLOCKS_PER_SEC << endl;
   

    cout << v1[0] << " * " << v2[0] << " = " << res[0] << endl;
    

    return 0;
}

