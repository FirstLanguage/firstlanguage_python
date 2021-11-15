
# Input 2

## Structure

`Input2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `context` | `string` | Required | Word or sentence or a paragraph. Special characters will not be stripped. |
| `lang` | `string` | Required | Allowed language code. Refer Allowed languages section. |
| `labels` | `List of object` | Required | Labels to classify |

## Example (as JSON)

```json
{
  "context": "Let us begin the API development.",
  "lang": "en",
  "labels": [
    "good",
    "bad"
  ]
}
```

