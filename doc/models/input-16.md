
# Input 16

## Structure

`Input16`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lang` | `string` | Required | Allowed language code. Refer Allowed languages section. |
| `content_type` | `string` | Required | Allowed values are:html,plaintext, pdf, docx<br>If html is specified all html tags and special characters will be stripped before processing.<br>For PDF and docx, all text will be read. Scanned documents will not work. |
| `url` | `string` | Required | Text from this URL will be read and a translation generated |
| `preserve_format` | `string` | Required | Accepted values are true, false. |

## Example (as JSON)

```json
{
  "lang": "lang2",
  "contentType": "contentType6",
  "url": "url4",
  "preserveFormat": "preserveFormat0"
}
```

