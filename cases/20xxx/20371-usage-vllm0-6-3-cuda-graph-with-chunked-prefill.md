# vllm-project/vllm#20371: [Usage]: vLLM0.6.3 cuda graph with chunked_prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#20371](https://github.com/vllm-project/vllm/issues/20371) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vLLM0.6.3 cuda graph with chunked_prefill

### Issue 正文摘录

### Your current environment I want to know whether vLLM 0.6.3 supports enabling both CUDA Graph and enable_chunked_prefill at the same time. Right now, I’m seeing incorrect outputs when both are enabled. Are there any related issues that address or resolve this problem?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: vLLM0.6.3 cuda graph with chunked_prefill usage;stale ### Your current environment I want to know whether vLLM 0.6.3 supports enabling both CUDA Graph and enable_chunked_prefill at the same time. Right now, I’m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: vLLM0.6.3 cuda graph with chunked_prefill usage;stale ### Your current environment I want to know whether vLLM 0.6.3 supports enabling both CUDA Graph and enable_chunked_prefill at the same time. Right now, I’m...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ny related issues that address or resolve this problem? correctness cuda mismatch Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
