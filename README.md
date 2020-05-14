# CPSC-452-P3
CPSC 452 Cryptography Project 3

Christopher Phongsa - cphongsa@csu.fullerton.edu

Theresa Tanubrata - theresatanubrata123@csu.fullerton.edu

Julian Coronado - juliancoronado@csu.fullerton.edu

Andrew Lopez - alopez8969@csu.fullerton.edu

Marianne Tolentino - mariannetolentino@csu.fullerton.edu

## Instructions to run the program

***Prerequisites: files to run the program***
- signer.py
- privKey.pem
- pubKey.pem
- testfile.txt

Here is the template to use when running the commands in the terminal:

```python signer.py <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>```

To use our example file 'testfile.txt' enter in the following commands:

*If you would like to sign the 'testfile.txt'*
> python signer.py privKey.pem test.sig testfile.txt sign

*If you would like to verify the digital signature of 'testfile.txt'*
> python signer.py pubKey.pem test.sig testfile.txt verify
