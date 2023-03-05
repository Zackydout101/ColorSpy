# ColorSpy

More than just Red, Green, and Blue

- uses RSA and AES to encrypt and decrypt images between client and server

## Setup

Run the following commands to install the dependencies

```bash
. ./install.sh
```

```
./run.sh

```

## Endpoints

|           | -      |                   |
| --------- | ------ | ----------------- |
| Endpoint  | Method | Description       |
| `/ `      | GET    | index             |
| `/key `   | GET    | get AES key       |
| `/image ` | POST   | send image to API |
