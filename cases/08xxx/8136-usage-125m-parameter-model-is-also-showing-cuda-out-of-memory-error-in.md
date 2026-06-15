# vllm-project/vllm#8136: [Usage]: 125m parameter model is also showing CUDA: Out of memory error in a Nvidia16GB 4060 

| 字段 | 值 |
| --- | --- |
| Issue | [#8136](https://github.com/vllm-project/vllm/issues/8136) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: 125m parameter model is also showing CUDA: Out of memory error in a Nvidia16GB 4060 

### Issue 正文摘录

### How would you like to use vllm Even for a smaller model like "facebook/opt-125m" when I am trying to do multiprocessing(even with batch size of 2) on a single 16GB Nvidia 4060, I am encountering CUDA: OUT OF MEMORY ERROR. When I am running the same model sequentially, I am able to run it fine. Can you explain this? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: 125m parameter model is also showing CUDA: Out of memory error in a Nvidia16GB 4060 usage ### How would you like to use vllm Even for a smaller model like "facebook/opt-125m" when I am trying to do multiprocess...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: nswer lots of frequently asked questions. performance model_support cuda oom shape How would you like to use vllm
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: 125m parameter model is also showing CUDA: Out of memory error in a Nvidia16GB 4060 usage ### How would you like to use vllm Even for a smaller model like "facebook/opt-125m" when I am trying to do multiprocess...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance model_support cuda oom shape How would you like to use vllm

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
