# vllm-project/vllm#22814: [Bug]: Excess system memory usage during GGUF loading

| 字段 | 值 |
| --- | --- |
| Issue | [#22814](https://github.com/vllm-project/vllm/issues/22814) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Excess system memory usage during GGUF loading

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After upgrading my docker build from 0.7.3 -> 0.10.1, large GGUF models now fail to load due to running out of system memory. Prior to upgrading only ~18 GB total ram was used, which is approximately the 8 GB base usage + ~10 GB (the size of each GPU's shard of the model). After upgrading, the system OOMs 96 GB of memory when TP = 4, and uses 80 GB+ with TP = 2. For reference, Llama 3.1 8B GGUF Q4 consumes over 23 GB under the new loader and each GPU only gets 1.25 GB of weights. This happens in both V1 and V0 modes. Loading the GPTQ version of the same model barely touches 10 GB and finishes almost instantly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug After upgrading my docker build from 0.7.3 -> 0.10.1, large GGUF models now fail to load due to running out of system memory. Prior to upgrading only ~18 GB total ram was...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: he bug After upgrading my docker build from 0.7.3 -> 0.10.1, large GGUF models now fail to load due to running out of system memory. Prior to upgrading only ~18 GB total ram was used, which is approximately the 8 GB bas...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Excess system memory usage during GGUF loading bug;stale ### Your current environment ### 🐛 Describe the bug After upgrading my docker build from 0.7.3 -> 0.10.1, large GGUF models now fail to load due to running...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: g_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
