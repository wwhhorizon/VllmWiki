# vllm-project/vllm#3663: [Usage]: Cannot access /v1 endpoint (404, "detail not found")

| 字段 | 值 |
| --- | --- |
| Issue | [#3663](https://github.com/vllm-project/vllm/issues/3663) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Cannot access /v1 endpoint (404, "detail not found")

### Issue 正文摘录

I want to run inference using mixtral8x7b (https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) using vllm's openai-compatible api server. I started a server like this: python -m vllm.entrypoints.api_server --port 5950 --model mistralai/Mixtral-8x7B-Instruct-v0.1 --tensor-parallel-size 4 This works fine: curl http://localhost:5950/docs This returns a 404 error, can't seem to find the endpoint v1 even though this is the example from the vllm quickstart guide: curl http://localhost:5950/v1/models Has anyone encountered an issue like this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ail not found") usage I want to run inference using mixtral8x7b (https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) using vllm's openai-compatible api server. I started a server like this: python -m vllm.entrypoints.ap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
