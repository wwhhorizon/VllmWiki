# vllm-project/vllm#3283: Order of keys for guided JSON

| 字段 | 值 |
| --- | --- |
| Issue | [#3283](https://github.com/vllm-project/vllm/issues/3283) |
| 状态 | closed |
| 标签 | good first issue |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Order of keys for guided JSON

### Issue 正文摘录

Hi Trying to use a json template with a mixtral 7x8b model. However the model generates the json with keys in alphabetic order which has a significant impact on generation quality (for my task at least). ```python json_template= { "type": "object", "properties": { "first_key": { "type": "array", "items": {"type": "string"}, "minItems": 1 }, "another_key": { "type": "array", "items": {"type": "string"}, "minItems": 1 }, "required": ["first_key", "another_key"] } chat_response = client.chat.completions.create( model=model, messages=[ {"role": "user", "content": prompt}, ], max_tokens=256, temperature=0.7, top_p=1, extra_body=dict(guided_json=json_template) ) # The returned JSON is in alphabetic order > "{'another_key': ['some_output'], 'first_key': ['another_output']}" ``` Is there a way to force the generation to follow the initial pattern (without alphabetic order)?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: N good first issue Hi Trying to use a json template with a mixtral 7x8b model. However the model generates the json with keys in alphabetic order which has a significant impact on generation quality (for my task at leas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
