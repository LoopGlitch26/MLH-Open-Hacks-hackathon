## Inspiration
Blockchain had always fascinated me. The immutability is the most amazing feature this technology provides. We wondered what if we can secure the data of an organization by keeping a safe record of the hash values so that all data is secured. That's where DataBlock comes in.

## What it does
For the implementation, our decided organization is Hospital, so keeping this in mind, we built the program. **This is not a database management program but rather a tool to keep the authenticity of data. The source code should never be used directly (because of easy manipulation with code) but a program build on it can use ** This program was created to act as an API so that anyone can use it easily. It uses the hashing technique to check the authenticity. In our Hospital organization scenario, there must be some employees and patient, so with this app, once anyone is registered in hospital, It generates a secure hash of that data, and on the basis of that hash and a new employee/patient detail, a new hash is generated. The hash does take some time and its time consumption can be easily modified with the source code.

## How I built it
I'd used a few built-in python libraries such as JSON, hashlib, and some custom created libraries.

## What I learned
My skills and concepts on blockchain had improved.

## What's next for DataBlock
That's something I'll be working on for a long time. I have an idea to use it for product management, i.e, securing the detail and origin of a consumer product such as manufacturing date, expiry date, product_id and many more. This will help us from those retailers and dealers who changes the product. This would provide a robust platform for industry and make them look more authentic.
