# vllm-project/vllm#20791: [Usage]: How to combine TOKEN PRUNING methods with MLLM in VLLM? Like combine [ECCV 2024] FastV, [CVPR 2025] PyramidDrop with LLaVA or other MLLMS?

| 字段 | 值 |
| --- | --- |
| Issue | [#20791](https://github.com/vllm-project/vllm/issues/20791) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to combine TOKEN PRUNING methods with MLLM in VLLM? Like combine [ECCV 2024] FastV, [CVPR 2025] PyramidDrop with LLaVA or other MLLMS?

### Issue 正文摘录

### Your current environment This issue is not related to the environment setting. ### How would you like to use vllm Nowadays, numerous vision token compression methods have been proposed, which aim to accelerate multi-modal large models at the algorithmic level. However, these methods are typically implemented by directly modifying the internal logic of the model code — for example, by altering the `modeling_llama.py` file in the Hugging Face Transformers library. Specifically, some approaches remove certain visual tokens within specific layers of the LLM decoder and manually adjust the corresponding position IDs. Although these modifications can improve inference efficiency, they are often deeply tied to the original model implementation and do not fundamentally differ from the baseline architecture. My question is: how can such methods be efficiently adapted to work with the VLLM library, which has a different execution engine and memory management system? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on methods have been proposed, which aim to accelerate multi-modal large models at the algorithmic level. However, these methods are typically implemented by directly modifying the internal logic of the model code — for...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: CV 2024] FastV, [CVPR 2025] PyramidDrop with LLaVA or other MLLMS? usage;stale ### Your current environment This issue is not related to the environment setting. ### How would you like to use vllm Nowadays, numerous vis...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he `modeling_llama.py` file in the Hugging Face Transformers library. Specifically, some approaches remove certain visual tokens within specific layers of the LLM decoder and manually adjust the corresponding position I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l model implementation and do not fundamentally differ from the baseline architecture. My question is: how can such methods be efficiently adapted to work with the VLLM library, which has a different execution engine an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
