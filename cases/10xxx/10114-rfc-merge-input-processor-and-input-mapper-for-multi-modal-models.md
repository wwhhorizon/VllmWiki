# vllm-project/vllm#10114: [RFC]: Merge input processor and input mapper for multi-modal models

| 字段 | 值 |
| --- | --- |
| Issue | [#10114](https://github.com/vllm-project/vllm/issues/10114) |
| 状态 | closed |
| 标签 | RFC;multi-modality |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Merge input processor and input mapper for multi-modal models

### Issue 正文摘录

## Motivation ### Background To provide more control over the model inputs, we currently define two methods for multi-modal models in vLLM: - The **input processor** is called inside `LLMEngine` to extend the prompt with placeholder tokens which are reserved for vLLM features such as KV cache and chunked prefill. - The **input mapper** is called inside `ModelRunner` to transform multi-modal inputs (e.g. `PIL` images) into tensor inputs, usually via the modality-specific processor (e.g. `AutoImageProcessor`) from HuggingFace. ### Issues with the current design 1. The input processor accepts the output of HF `AutoTokenizer`, a list of token IDs, instead of the text prompt. Since HF `AutoProcessor` doesn’t accept token IDs, we have to write custom code to edit the list of token IDs based on the multi-modal inputs. For some models (such as Phi-3-vision), this means re-implementing code from their HF `AutoProcessor`, complicating the process of porting the model to vLLM. 2. The input mapper, being inside `ModelRunner`, lies on the critical path of vLLM’s model execution. Even when the input mapper is fast, the tail TTFT and TPOT suffers because of this. As the input mapper takes up mor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [RFC]: Merge input processor and input mapper for multi-modal models RFC;multi-modality ## Motivation ### Background To provide more control over the model inputs, we currently define two methods for multi-modal models...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: puts (e.g. `PIL` images) into tensor inputs, usually via the modality-specific processor (e.g. `AutoImageProcessor`) from HuggingFace. ### Issues with the current design 1. The input processor accepts the output of HF `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s model execution. Even when the input mapper is fast, the tail TTFT and TPOT suffers because of this. As the input mapper takes up more time, our overall throughput decreases proportionally which can be avoided if we m...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: mpt with placeholder tokens which are reserved for vLLM features such as KV cache and chunked prefill. - The **input mapper** is called inside `ModelRunner` to transform multi-modal inputs (e.g. `PIL` images) into tenso...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tokens which are reserved for vLLM features such as KV cache and chunked prefill. - The **input mapper** is called inside `ModelRunner` to transform multi-modal inputs (e.g. `PIL` images) into tensor inputs, usually via...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
