# vllm-project/vllm#20426: [Bug]: kv_cache incorrect with cuda graph batch inputs vllm0.6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#20426](https://github.com/vllm-project/vllm/issues/20426) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 | mismatch |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: kv_cache incorrect with cuda graph batch inputs vllm0.6.3

### Issue 正文摘录

### Your current environment vllm0.6.3 about 2024.OCT ### 🐛 Describe the bug Due to some project constraints, I'm currently still using vLLM 0.6.3 and don't have time to upgrade for now. I've noticed that when CUDA Graph is enabled, the output becomes incorrect for some batches in multi-batch inputs. I constructed a batch with identical inputs, so theoretically, the outputs of each batch should be the same. In my testing: Single-batch with CUDA Graph: output is correct Multi-batch without CUDA Graph (eager mode): output is also correct Multi-batch with CUDA Graph: after attention computation, the hidden_states across batches start to differ unexpectedly Interestingly, when I forcibly set the kv_cache values to 1, the hidden_states become identical again after attention. Has anyone encountered this issue before? Are there any related issues or discussions about this? Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: kv_cache incorrect with cuda graph batch inputs vllm0.6.3 bug;stale ### Your current environment vllm0.6.3 about 2024.OCT ### 🐛 Describe the bug Due to some project constraints, I'm currently still using vLLM 0.6...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: requently asked questions. correctness attention_kv_cache attention;cuda mismatch shape Your current environment
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tches start to differ unexpectedly Interestingly, when I forcibly set the kv_cache values to 1, the hidden_states become identical again after attention. Has anyone encountered this issue before? Are there any related i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: kv_cache incorrect with cuda graph batch inputs vllm0.6.3 bug;stale ### Your current environment vllm0.6.3 about 2024.OCT ### 🐛 Describe the bug Due to some project constraints, I'm currently still using vLLM 0.6...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: , so theoretically, the outputs of each batch should be the same. In my testing: Single-batch with CUDA Graph: output is correct Multi-batch without CUDA Graph (eager mode): output is also correct Multi-batch with CUDA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
