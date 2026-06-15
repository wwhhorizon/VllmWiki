# vllm-project/vllm#3519: [New Model]: Please support CogVLM

| 字段 | 值 |
| --- | --- |
| Issue | [#3519](https://github.com/vllm-project/vllm/issues/3519) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Please support CogVLM

### Issue 正文摘录

### The model to consider. https://huggingface.co/THUDM/cogvlm-chat-hf ### The closest model vllm already supports. LLama ### What's your difficulty of supporting the model you want? - The visual module leads to modify vLLM engine

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: Please support CogVLM new-model;stale ### The model to consider. https://huggingface.co/THUDM/cogvlm-chat-hf ### The closest model vllm already supports. LLama ### What's your difficulty of supporting the mo
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Please support CogVLM new-model;stale ### The model to consider. https://huggingface.co/THUDM/cogvlm-chat-hf ### The closest model vllm already supports. LLama ### What's your difficulty of supporting the m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
