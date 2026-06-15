# vllm-project/vllm#4663: [RFC]: Inline Golden (Expected) Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#4663](https://github.com/vllm-project/vllm/issues/4663) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Inline Golden (Expected) Tests

### Issue 正文摘录

### Motivation. Some of tests in vllm is neither sufficient nor easy to read, e.g. https://github.com/vllm-project/vllm/blob/8344f7742b794ca6ec9bcb891c178cd0551f23d0/tests/core/test_scheduler.py#L293-L297 The test `assert out.blocks_to_swap_out != {}` is insufficient, and these lines only test certain properties of the output. ### Proposed Change. We can use inline golden tests (a.k.a. expected tests) from https://github.com/ezyang/expecttest, which is used heavily in pytorch: https://github.com/pytorch/pytorch/blob/8b4d62009ddbc24a69dfcdbebc2cc84e4b2ee8f5/test/test_python_dispatch.py#L645-L654 ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Inline Golden (Expected) Tests RFC;stale ### Motivation. Some of tests in vllm is neither sufficient nor easy to read, e.g. https://github.com/vllm-project/vllm/blob/8344f7742b794ca6ec9bcb891c178cd0551f23d0/tests...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: h/pytorch/blob/8b4d62009ddbc24a69dfcdbebc2cc84e4b2ee8f5/test/test_python_dispatch.py#L645-L654 ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ) Tests RFC;stale ### Motivation. Some of tests in vllm is neither sufficient nor easy to read, e.g. https://github.com/vllm-project/vllm/blob/8344f7742b794ca6ec9bcb891c178cd0551f23d0/tests/core/test_scheduler.py#L293-L...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cd0551f23d0/tests/core/test_scheduler.py#L293-L297 The test `assert out.blocks_to_swap_out != {}` is insufficient, and these lines only test certain properties of the output. ### Proposed Change. We can use inline golde...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [RFC]: Inline Golden (Expected) Tests RFC;stale ### Motivation. Some of tests in vllm is neither sufficient nor easy to read, e.g. https://github.com/vllm-project/vllm/blob/8344f7742b794ca6ec9bcb891c178cd0551f23d0/tests...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
