
# URL Input

## Structure

`URLInput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `input` | [`Input1`](/fl-python/doc/models/input-1.md) | Required | Text for processing will be read from the given URL. Only HTML pages or text pages will be processed at this time. |

## Example (as JSON)

```json
{
  "input": {
    "url": "http://news.bbc.co.uk/2/hi/health/2284783.stm",
    "lang": "en",
    "contentType": "html"
  }
}
```

