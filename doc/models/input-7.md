
# Input 7

## Structure

`Input7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `flattable` | `object` | Required | Table if JSON format |
| `send_back_rows` | `bool` | Required | Send back original rows from which the answer was extracted. Input either true or false. |
| `questions` | `List of string` | Required | Array of questions. |

## Example (as JSON)

```json
{
  "flattable": {
    "key1": "val1",
    "key2": "val2"
  },
  "sendBackRows": false,
  "questions": [
    "questions1"
  ]
}
```

