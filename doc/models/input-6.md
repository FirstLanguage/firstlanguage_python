
# Input 6

## Structure

`Input6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `question` | `string` | Required | Question to be answered from the context given. Only One question can be asked at a time. Special characters will not be stripped. |
| `lang` | `string` | Required | Allowed language code. Refer Allowed languages section. |
| `content_type` | `string` | Required | Allowed values are:html,plaintext, pdf, docx<br>If html is specified all html tags and special characters will be stripped before processing.<br>For PDF and docx, all text will be read. Scanned documents will not work. |
| `url` | `string` | Required | URL where the context for the question is stored. |

## Example (as JSON)

```json
{
  "question": "question8",
  "lang": "lang2",
  "contentType": "contentType6",
  "url": "url4"
}
```

