# vllm-project/vllm#1273: `stream` should only accept type Boolean when using OpenAI API Server spec

| 字段 | 值 |
| --- | --- |
| Issue | [#1273](https://github.com/vllm-project/vllm/issues/1273) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> `stream` should only accept type Boolean when using OpenAI API Server spec

### Issue 正文摘录

The current behaviour of vLLM does not match the behaviour of OpenAI and Azure OpenAI when it comes to the `stream` parameter in the request body. Current behaviour of OpenAI and Azure OpenAI: - Only `"stream": true` or `"stream": false` are accepted. Setting `"stream": "true"` or `"stream": "false"` (or any other non-Boolean values) will raise the following error: ``` { "error": { "message": "'false' is not of type 'boolean' - 'stream'", "type": "invalid_request_error", "param": null, "code": null } } ``` Current behaviour of vLLM: - The following values for the `stream` request body parameter are accepted by vLLM: `true`, `"true"`, `false`, `"false"` - Any other values will raise the following error: ``` { "object": "error", "message": "[{'loc': ('body', 'stream'), 'msg': 'value could not be parsed to a boolean', 'type': 'type_error.bool'}]", "type": "invalid_request_error", "param": null, "code": null } ``` - It seems like this is caused by the use of Pydantic with `stream` variable set to type `bool` instead of `StrictBool` ([source code](https://github.com/vllm-project/vllm/blob/acbed3ef40f015fcf64460e629813922fab90380/vllm/entrypoints/openai/protocol.py#L63)) May I know if t...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: iour of OpenAI and Azure OpenAI: - Only `"stream": true` or `"stream": false` are accepted. Setting `"stream": "true"` or `"stream": "false"` (or any other non-Boolean values) will raise the following error: ``` { "erro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: f OpenAI and Azure OpenAI when it comes to the `stream` parameter in the request body. Current behaviour of OpenAI and Azure OpenAI: - Only `"stream": true` or `"stream": false` are accepted. Setting `"stream": "true"`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
