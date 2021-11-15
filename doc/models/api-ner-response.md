
# Api Ner Response

## Structure

`ApiNerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_group` | `string` | Required | Entity group inferred.<br>**Constraints**: *Minimum Length*: `1` |
| `word` | `string` | Required | Corresponding word<br>**Constraints**: *Minimum Length*: `1` |
| `start` | `string` | Required | Start position of the entity in the given input.<br>**Constraints**: *Minimum Length*: `1` |
| `end` | `string` | Required | Start position of the entity in the given input.<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "entity_group": "entity_group6",
  "word": "word2",
  "start": "start4",
  "end": "end8"
}
```

