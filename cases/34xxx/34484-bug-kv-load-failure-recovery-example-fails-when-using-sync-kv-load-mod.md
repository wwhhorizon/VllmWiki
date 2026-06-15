# vllm-project/vllm#34484: [Bug]: kv_load_failure_recovery example fails when using sync KV load mode

| 字段 | 值 |
| --- | --- |
| Issue | [#34484](https://github.com/vllm-project/vllm/issues/34484) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kv_load_failure_recovery example fails when using sync KV load mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Describe the Bug The `kv_load_failure_recovery` example in `examples/offline_inference/kv_load_failure_recovery/` fails to run correctly when using synchronous KV load mode (`--simulate-failure` without `--async-load`). The root cause is that the example does not explicitly set the `async_scheduling` parameter for the `LLM` instance. When `LoadRecoveryExampleConnector` operates in sync mode (`async_load=False`), the scheduler still runs in its default async mode (`async_scheduling=True`). This mismatch causes incorrect handling of KV load failures. ## How to Reproduce ```bash cd examples/offline_inference/kv_load_failure_recovery # First run prefill to generate KV cache python3 prefill_example.py # Then run decode with simulated failure (sync mode) python3 decode_example.py --simulate-failure ``` ## Expected Behavior When KV load fails in sync mode, the scheduler should properly detect the failure, reset the affected request's state, and trigger recomputation. The example should complete successfully with recovered output. ## Actual Behavior The example crashes with the following error: ``` RuntimeError: Invalid token ids befo...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: kv_load_failure_recovery example fails when using sync KV load mode bug;stale ### Your current environment ### 🐛 Describe the bug ## Describe the Bug The `kv_load_failure_recovery` example in `examples/offline_inference...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ler still runs in its default async mode (`async_scheduling=True`). This mismatch causes incorrect handling of KV load failures. ## How to Reproduce ```bash cd examples/offline_inference/kv_load_failure_recovery # First...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: hout `--async-load`). The root cause is that the example does not explicitly set the `async_scheduling` parameter for the `LLM` instance. When `LoadRecoveryExampleConnector` operates in sync mode (`async_load=False`), t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r still runs in its default async mode (`async_scheduling=True`). This mismatch causes incorrect handling of KV load failures. ## How to Reproduce ```bash cd examples/offline_inference/kv_load_failure_recovery # First r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: When `LoadRecoveryExampleConnector` operates in sync mode (`async_load=False`), the scheduler still runs in its default async mode (`async_scheduling=True`). This mismatch causes incorrect handling of KV load failures....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
