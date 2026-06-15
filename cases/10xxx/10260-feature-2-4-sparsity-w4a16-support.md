# vllm-project/vllm#10260: [Feature]: 2:4 sparsity + w4a16 support

| 字段 | 值 |
| --- | --- |
| Issue | [#10260](https://github.com/vllm-project/vllm/issues/10260) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: 2:4 sparsity + w4a16 support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Here in llm compressor, they say this mode is supported with 2:4 sparsity along with w4a16 quantization. https://github.com/vllm-project/llm-compressor/tree/main/examples/quantization_2of4_sparse_w4a16 I just want to confirm this is supported in official vllm (not nm-vllm). Is there any existing model on huggingface (for llama 3.1 8B preferably) that I can test the speedup with? Thanks ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: this is supported in official vllm (not nm-vllm). Is there any existing model on huggingface (for llama 3.1 8B preferably) that I can test the speedup with? Thanks ### Alternatives _No response_ ### Additional context _...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ation_2of4_sparse_w4a16 I just want to confirm this is supported in official vllm (not nm-vllm). Is there any existing model on huggingface (for llama 3.1 8B preferably) that I can test the speedup with? Thanks ### Alte...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ssor, they say this mode is supported with 2:4 sparsity along with w4a16 quantization. https://github.com/vllm-project/llm-compressor/tree/main/examples/quantization_2of4_sparse_w4a16 I just want to confirm this is supp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: 2:4 sparsity + w4a16 support feature request ### 🚀 The feature, motivation and pitch Here in llm compressor, they say this mode is supported with 2:4 sparsity along with w4a16 quantization. https://github.com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
