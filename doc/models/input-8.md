
# Input 8

## Structure

`Input8`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `string` | Required | URL of the CSV file. |
| `send_back_rows` | `bool` | Required | Send back original rows from which the answer was extracted. Input either true or false. |
| `questions` | `List of string` | Required | Array of questions |

## Example (as JSON)

```json
{
  "url": "url4",
  "sendBackRows": false,
  "questions": [
    "questions1"
  ]
}
```

