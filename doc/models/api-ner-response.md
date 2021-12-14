
# Api Ner Response

## Structure

`ApiNerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_group` | `string` | Required | Entity group inferred. |
| `word` | `string` | Required | Corresponding word |
| `start` | `string` | Required | Start position of the entity in the given input. |
| `end` | `string` | Required | Start position of the entity in the given input. |

## Example (as JSON)

```json
{
  "entity_group": "entity_group6",
  "word": "word2",
  "start": "start4",
  "end": "end8"
}
```

