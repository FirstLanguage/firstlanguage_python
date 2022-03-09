
# Input 3

## Structure

`Input3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `string` | Required | URL where the content is hosted. |
| `lang` | `string` | Required | Allowed language code. Refer Allowed languages section. |
| `content_type` | `string` | Required | Allowed values are:html,plaintext, pdf, docx<br>If html is specified all html tags and special characters will be stripped before processing.<br>For PDF and docx, all text will be read. Scanned documents will not work. |
| `labels` | `List of object` | Required | Labels to classify |

## Example (as JSON)

```json
{
  "url": "http://news.bbc.co.uk/2/hi/health/2284783.stm",
  "lang": "en",
  "contentType": "html",
  "labels": [
    "good",
    "bad"
  ]
}
```

