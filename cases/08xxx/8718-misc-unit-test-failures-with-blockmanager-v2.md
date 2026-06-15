# vllm-project/vllm#8718: [Misc]: Unit test failures with BlockManager v2

| 字段 | 值 |
| --- | --- |
| Issue | [#8718](https://github.com/vllm-project/vllm/issues/8718) |
| 状态 | closed |
| 标签 | help wanted |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Unit test failures with BlockManager v2

### Issue 正文摘录

### Anything you want to discuss about vllm. We plan to deprecate BlockManager V1 in favor of BlockManager V2. As part of that deprecation process we want to make sure that all existing tests work with BlockManager V2. We will use this issue to track the unit tests that fail with BlockManager V2 and fix them. To that end we are using https://github.com/vllm-project/vllm/pull/8678 to identify the unit tests that break with BlockManager V2 The unit tests that have identified as failing currently are **tests/basic_correctness** tests/basic_correctness/test_preemption.py::test_swap_infeasible[4-96-float-facebook/opt-125m] **tests/core** test_chunked_prefill_scheduler.py::test_chunk test_chunked_prefill_scheduler.py::test_complex test_chunked_prefill_scheduler.py::test_prompt_limit test_chunked_prefill_scheduler.py::test_swap test_chunked_prefill_scheduler.py::test_running_prefill_prioritized_over_swap test_chunked_prefill_scheduler.py::test_chunked_prefill_preempt test_chunked_prefill_scheduler.py::test_chunked_prefill_max_seqs test_scheduler.py::test_scheduler_prefill_prioritized test_scheduler.py::test_swapped_out_prioritized test_scheduler.py::test_prefill_schedule_token_budget tes...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: _infeasible[4-96-float-facebook/opt-125m] **tests/core** test_chunked_prefill_scheduler.py::test_chunk test_chunked_prefill_scheduler.py::test_complex test_chunked_prefill_scheduler.py::test_prompt_limit test_chunked_pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: est_decode_schedule_preempted test_scheduler.py::test_decode_swap_beam_search test_scheduler.py::test_schedule_decode_blocks_to_copy_update test_scheduler.py::test_schedule_swapped_simple test_scheduler.py::test_schedul...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Misc]: Unit test failures with BlockManager v2 help wanted ### Anything you want to discuss about vllm. We plan to deprecate BlockManager V1 in favor of BlockManager V2. As part of that deprecation process we want to m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Misc]: Unit test failures with BlockManager v2 help wanted ### Anything you want to discuss about vllm. We plan to deprecate BlockManager V1 in favor of BlockManager V2. As part of that deprecation process we want to m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
