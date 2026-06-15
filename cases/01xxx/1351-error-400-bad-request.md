# vllm-project/vllm#1351: [Error] 400 Bad Request

| 字段 | 值 |
| --- | --- |
| Issue | [#1351](https://github.com/vllm-project/vllm/issues/1351) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Error] 400 Bad Request

### Issue 正文摘录

Hey all, I am getting some errors when using the OpenAI api end point: ``` INFO: ::1:51556 - "POST /v1/chat/completions HTTP/1.1" 400 Bad Request ``` Getting that somewhat often (every 15 min or so). And then on the client side: ``` openai.error.APIError: Invalid response object from API: '{"object":"error","message":"max_tokens must be at least 1, got -53.","type":"invalid_request_error","param":null,"code":null}' (HTTP response code was 400) ``` Release 0.2.0 Running on 2x 3090 using: python -m vllm.entrypoints.openai.api_server --model Tostino/Inkbot-13B-8k-0.2 --tensor-parallel-size=2 --conversation-template inkbot.json

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Running on 2x 3090 using: python -m vllm.entrypoints.openai.api_server --model Tostino/Inkbot-13B-8k-0.2 --tensor-parallel-size=2 --conversation-template inkbot.json
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Error] 400 Bad Request Hey all, I am getting some errors when using the OpenAI api end point: ``` INFO: ::1:51556 - "POST /v1/chat/completions HTTP/1.1" 400 Bad Request ``` Getting that somewhat often (every 15 min or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
