# vllm-project/vllm#19867: [Bug]: AiterFlashAttentionImpl.__init__() got multiple values for argument 'use_irope' for llama4 model

| 字段 | 值 |
| --- | --- |
| Issue | [#19867](https://github.com/vllm-project/vllm/issues/19867) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AiterFlashAttentionImpl.__init__() got multiple values for argument 'use_irope' for llama4 model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We hit an exception on running llama4 models with latest code on ROCm V1: ``` (VllmWorker rank=2 pid=267) ERROR 06-19 01:00:39 [multiproc_executor.py:488] TypeError: AiterFlashAttentionImpl.__init__() got multiple values for argument 'use_irope' ``` Current work-around: To turn off AITER_MHA, with VLLM_ROCM_USE_AITER_MHA=0 Proposal: - [ ] Fix the bug (the team is working on it) - [ ] Add a end-to-end test for one of the small llama4 models - [ ] The motivation for adding an end to end test for a small version of llama4 models, is that we have seen issues of breaking llama4 models in the past because of lacking such tests. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: it__() got multiple values for argument 'use_irope' for llama4 model bug;rocm ### Your current environment ### 🐛 Describe the bug We hit an exception on running llama4 models with latest code on ROCm V1: ``` (VllmWorker...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: AiterFlashAttentionImpl.__init__() got multiple values for argument 'use_irope' for llama4 model bug;rocm ### Your current environment ### 🐛 Describe the bug We hit an exception on running llama4 models with late...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ttentionImpl.__init__() got multiple values for argument 'use_irope' for llama4 model bug;rocm ### Your current environment ### 🐛 Describe the bug We hit an exception on running llama4 models with latest code on ROCm V1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: models - [ ] The motivation for adding an end to end test for a small version of llama4 models, is that we have seen issues of breaking llama4 models in the past because of lacking such tests. ### Before submitting a ne...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 🐛 Describe the bug We hit an exception on running llama4 models with latest code on ROCm V1: ``` (VllmWorker rank=2 pid=267) ERROR 06-19 01:00:39 [multiproc_executor.py:488] TypeError: AiterFlashAttentionImpl.__init__()...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
