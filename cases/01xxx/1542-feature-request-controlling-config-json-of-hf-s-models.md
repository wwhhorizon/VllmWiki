# vllm-project/vllm#1542: Feature request: Controlling `config.json` of HF's models

| 字段 | 值 |
| --- | --- |
| Issue | [#1542](https://github.com/vllm-project/vllm/issues/1542) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature request: Controlling `config.json` of HF's models

### Issue 正文摘录

Thanks for this great project! A quick feature request: [When loading models from the HuggingFace Hub](https://github.com/vllm-project/vllm/blob/7e90a2d11785b4cba5172f13178adb6d194a867f/vllm/config.py#L79), allow providing custom values to overwrite the default `config.json`. For example, change [the value of `max_position_embeddings` from `32768`](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/blob/7ad5799710574ba1c1d953eba3077af582f3a773/config.json#L11) to `100000`, to allow longer prompts.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Feature request: Controlling `config.json` of HF's models Thanks for this great project! A quick feature request: [When loading models from the HuggingFace Hub](https://github.com/vllm-project/vllm/blob/7e90a2d11785b4cb...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Feature request: Controlling `config.json` of HF's models Thanks for this great project! A quick feature request: [When loading models from the HuggingFace Hub](https://github.com/vllm-project/vllm/blob/7e90a2d11785b4cb...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
