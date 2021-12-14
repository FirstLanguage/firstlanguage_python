
# Input 1

Text for processing will be read from the given URL. Only HTML pages or text pages will be processed at this time.

## Structure

`Input1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `string` | Required | URL where the content is hosted. |
| `lang` | `string` | Required | Allowed language code. Refer Allowed languages section. |
| `content_type` | `string` | Required | Allowed values or html or text. If html is specified all html tags and special characters will be stripped before processing. |

## Example (as JSON)

```json
{
  "url": "http://news.bbc.co.uk/2/hi/health/2284783.stm",
  "lang": "en",
  "contentType": "html"
}
```

