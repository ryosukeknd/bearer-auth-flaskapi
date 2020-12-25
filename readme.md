# bearer-auth-flaskapi
Flaskでbearer認証[^1]式のAPIを実装するテストプロジェクトです

## 動かしてみる
1. コンテナを起動する
    ```
    docker-compose up -d
    ```
2. 認証無しで呼べるAPIを呼び出してみる
    ```
    curl -i localhost:5000
    ```
    下記の結果になるはず
    ```
    HTTP/1.0 200 OK
    Content-Type: application/json
    WWW-Authenticate: Bearer realm=""
    Content-Length: 32
    Server: Werkzeug/0.11.10 Python/3.8.3
    Date: Fri, 25 Dec 2020 09:20:03 GMT

    {
    "message": "Hello World!"
    }
    ```
3. 認証が必要なAPIを呼び出してみる
    1. 認証情報なしで呼び出してみる
    ```
    curl -i localhost:5000/token_auth
    ```
    下記の結果になるはず
    ```
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: application/json
    WWW-Authenticate: Bearer realm="example"
    Content-Length: 3
    Server: Werkzeug/0.11.10 Python/3.8.3
    Date: Fri, 25 Dec 2020 09:24:23 GMT

    {}
    ```
    2. 認証情報を付けて呼び出してみる
    ```
    curl -i localhost:5000/token_auth -H "Authorization:Bearer 44KI44GP44GC44KL44Go44O844GP44KT"
    ```
    下記の結果になるはず
    ```
    HTTP/1.0 200 OK
    Content-Type: application/json
    WWW-Authenticate: Bearer realm=""
    Content-Length: 47
    Server: Werkzeug/0.11.10 Python/3.8.3
    Date: Fri, 25 Dec 2020 09:25:24 GMT

    {
    "message": "Token Authorization Sample."
    }
    ```
4. コンテナを終了する
    ```
    docker-compose down
    ```

## 認証に使用するトークンについて
認証に使用するトークンは [docker-compose.yml](docker-compose.yml) の ``` environment ``` で定義しています。

今回のテストではAuthenticationリスエストヘッダフィールドにトークンを設定しています。
この時のトークンはtoken68形式であることが定められています。[^2]


[^1]: [RFC 6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://tools.ietf.org/html/rfc6750)
[^2]: [Hypertext Transfer Protocol (HTTP/1.1): Authentication](https://tools.ietf.org/html/rfc7235)
