# vllm-project/vllm#23050: [Bug]: torch.OutOfMemoryError: CUDA out of memory.

| 字段 | 值 |
| --- | --- |
| Issue | [#23050](https://github.com/vllm-project/vllm/issues/23050) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.OutOfMemoryError: CUDA out of memory.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I tried to deploy a local llm model (Qwen3-30B-A3B-Thinking-2507) by the following command: ```shell vllm serve Qwen3-30B-A3B-Thinking-2507 --max-model-len 262144 ``` it crashed and error messages are as follows: ```text torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 768.00 MiB. GPU 0 has a total capacity of 31.84 GiB of which 0 bytes is free. Including non-PyTorch memory, this process has 17179869184.00 GiB memory in use. Of the allocated memory 52.93 GiB is allocated by PyTorch, and 32.88 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. ``` my gpu is 5090 and I think it is enough for this model. can you help find out why and how can i use this model locally? thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: CUDA out of memory. Tried to allocate 768.00 MiB. GPU 0 has a total capacity of 31.84 GiB of which 0 bytes is free. Including non-PyTorch memory, this process has 17179869184.00 GiB memory in use. Of the allocated memor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: torch.OutOfMemoryError: CUDA out of memory. bug;stale ### Your current environment ### 🐛 Describe the bug when I tried to deploy a local llm model (Qwen3-30B-A3B-Thinking-2507) by the following command: ```shell...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vironment ### 🐛 Describe the bug when I tried to deploy a local llm model (Qwen3-30B-A3B-Thinking-2507) by the following command: ```shell vllm serve Qwen3-30B-A3B-Thinking-2507 --max-model-len 262144 ``` it crashed and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: torch.OutOfMemoryError: CUDA out of memory. bug;stale ### Your current environment ### 🐛 Describe the bug when I tried to deploy a local llm model (Qwen3-30B-A3B-Thinking-2507) by the following command: ```shell...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf;oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
