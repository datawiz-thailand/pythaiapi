# PyThaiAPI
> PyThaiNLP based REST API

## API Reference

```bash
Method: POST
Endpoint: /api/word_tokenize
Header: "Content-Type: application/json"
Params: ?engine=newmm&keep_whitespace=false
Body: {"text": "ทดสอบการตัดคำ"}
```

### Using cURL request

```bash
curl -X POST \
https://pythaiapi.herokuapp.com/api/word_tokenize?engine=newmm&keep_whitespace=true \
-H 'Content-Type: application/json' \
-d '{"text":"ทดสอบภาษาไทย"}' | json_pp
```
