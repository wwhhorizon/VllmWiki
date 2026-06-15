# vllm-project/vllm#3272: Potential state leaks between tests in spec decoding test

| 字段 | 值 |
| --- | --- |
| Issue | [#3272](https://github.com/vllm-project/vllm/issues/3272) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Potential state leaks between tests in spec decoding test

### Issue 正文摘录

https://github.com/vllm-project/vllm/pull/3236 When I ran this test https://github.com/vllm-project/vllm/blob/main/tests/worker/spec_decode/test_multi_step_worker.py e2e, it turns out the last test https://github.com/vllm-project/vllm/blob/1ece1ae829dcbc4b1b19b3e2d3042457615e862f/tests/worker/spec_decode/test_multi_step_worker.py#L147 fails with some kind of CUDA illegal memory access. I found out - if I changed the order of test (for example, run this https://github.com/vllm-project/vllm/blob/1ece1ae829dcbc4b1b19b3e2d3042457615e862f/tests/worker/spec_decode/test_multi_step_worker.py#L70 first and run the multi step after) - OR if I remove these 2 lines https://github.com/vllm-project/vllm/blob/1ece1ae829dcbc4b1b19b3e2d3042457615e862f/tests/worker/spec_decode/test_multi_step_worker.py#L93 the issue is fixed. I am not exactly sure what's going on, but it seems sketchy

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Potential state leaks between tests in spec decoding test stale https://github.com/vllm-project/vllm/pull/3236 When I ran this test https://github.com/vllm-project/vllm/blob/main/tests/worker/spec_decode/test_multi_step...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: orker/spec_decode/test_multi_step_worker.py#L147 fails with some kind of CUDA illegal memory access. I found out - if I changed the order of test (for example, run this https://github.com/vllm-project/vllm/blob/1ece1ae8...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Potential state leaks between tests in spec decoding test stale https://github.com/vllm-project/vllm/pull/3236 When I ran this test https://github.com/vllm-project/vllm/blob/main/tests/worker/spec_decode/test_multi_step...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
