
# Input 5

## Structure

`Input5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `question` | `string` | Required | Question to be answered from the context given. Only One question can be asked at a time. Special characters will not be stripped. |
| `lang` | `string` | Required | Allowed language code. Refer Allowed languages section. |
| `context` | `string` | Required | Sentence or a paragraph. Special characters will not be stripped. |

## Example (as JSON)

```json
{
  "question": "question8",
  "lang": "lang2",
  "context": "context2"
}
```

