
# Input 12

## Structure

`Input12`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lang` | `string` | Required | Allowed language code. Refer Allowed languages section. |
| `content_type` | `string` | Required | Allowed values are:html,plaintext, pdf, docx<br>If html is specified all html tags and special characters will be stripped before processing.<br>For PDF and docx, all text will be read. Scanned documents will not work. |
| `url` | `string` | Required | URL where the text for the NER task is stored. |

## Example (as JSON)

```json
{
  "lang": "lang2",
  "contentType": "contentType6",
  "url": "url4"
}
```

