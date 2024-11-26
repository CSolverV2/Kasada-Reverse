# Kasada-Reverse
Reverse engeneered kasada.io "captcha" / antibot

# Why

Since [@H4cK3dR4Du](https://github.com/H4cK3dR4Du) leaked the kasada encryption and stuff, I thought I would share some of my research too

# Let's Begin
So first we need to ask ourselves, why the fuck am I spending my time on this (who tf cares about twitch?)

Now, let's look into how Kasada functions

- They use a VM for their encryption
  - Vm's are way more advanced and dificult to reverse than just obfuscating javascript
  - They are usually encoded and encrypted wthin a large string known as "bytecode"
  - This bytecode string is decoded for proper initilization to be used by the javascript when needed
- Encryption
  - Payload
    - Payload gets a bunch of data from the browser and uses to confirm if user is a bot or not
    - There is way too much to post everything in this readme, so i'll let you look for yourself
    - Find a copy of a decrypted kasada fingerprint [here](https://github.com/CSolverV2/Kasada-Reverse/blob/main/scripts/payload.json)
  - Kasada is encrypted with the TEA algorithim
    - Uses a **64-bit block cipher** meaning the code processes data in 64-bit blocks
    - Uses a **128-bit key** meaning the key is split into 4 32-bit parts
    - Uses a **Feistel network** meaning the code uses a round-based structure with two 32-bit halves and involves shifts, additions, and XORs, which is like Feistel networks used in ciphers like TEA.
    - Uses multiple **Rounds** the code performs mutliple 32-bit rounds just like in the TEA algo
  - Key/IV
    - The IV in kasada's encryption is dynamically generated
      - This means IV is not static for specific versions or sites, (the key is), but generated differetnly every time it is used
      - This is done to make it more difficult to reverse and keep it secure and hard to recreate their encryption without sandboxing
      - For the encryption, you need the encryption code, you can find this in `scripts/encryption.py` and the original in `scripts/encryption.js`
     
- Dynamic VM
  - Eariler, I said Kasada uses a vm meaning there is bytecode that must be decoded to acces the inner code of the vm
  - Every time kasada is used, the bytecode changes as they have multiple versions, multiple VMs, so we need a way to follow this and decode it no matter what
  - In `scripts/VM.py` you will be able to use that to dynamically dump the contents of the vm, only thing required is the url of the `ips.js` file

# Screenshots (POW)

Dynamic VM Dumper
<img width="710" alt="Screenshot 2024-10-26 165846" src="https://github.com/user-attachments/assets/611e2844-d958-4ff4-80b5-223ae3320e7e">

Encryption 
<img width="364" alt="Screenshot 2024-10-26 192831" src="https://github.com/user-attachments/assets/3a715604-0fa4-4d83-939b-66b1737d85fb">

Decrypted Payload w/ Key/IV
<img width="463" alt="Screenshot 2024-10-26 152748" src="https://github.com/user-attachments/assets/8bc8e40c-c9d5-40ff-8393-be619216b0ce">

# Credit

**Cypher (me)**

`@CSolverV2` - Telegram
`CSolver.ai` - Discord

https://t.me/csolver

https://discord.gg/csolve
