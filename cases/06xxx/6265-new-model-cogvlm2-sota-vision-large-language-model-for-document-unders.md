# vllm-project/vllm#6265: [New Model]: CogVlm2 - SOTA Vision Large Language Model for Document Understanding

| 字段 | 值 |
| --- | --- |
| Issue | [#6265](https://github.com/vllm-project/vllm/issues/6265) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: CogVlm2 - SOTA Vision Large Language Model for Document Understanding

### Issue 正文摘录

### The model to consider. https://huggingface.co/THUDM/cogvlm2-llama3-chat-19B Already supported by LMDeploy https://huggingface.co/THUDM/cogvlm2-llama3-chat-19B/discussions/11 ### The closest model vllm already supports. Phi-3 Vision ### What's your difficulty of supporting the model you want? They have custom a custom int4 quant which should probably be supported.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: CogVlm2 - SOTA Vision Large Language Model for Document Understanding new-model;stale ### The model to consider. https://huggingface.co/THUDM/cogvlm2-llama3-chat-19B Already supported by LMDeploy https://hu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: difficulty of supporting the model you want? They have custom a custom int4 quant which should probably be supported.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: - SOTA Vision Large Language Model for Document Understanding new-model;stale ### The model to consider. https://huggingface.co/THUDM/cogvlm2-llama3-chat-19B Already supported by LMDeploy https://huggingface.co/THUDM/co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
