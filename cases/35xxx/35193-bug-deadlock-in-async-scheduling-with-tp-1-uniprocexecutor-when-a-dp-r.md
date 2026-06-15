# vllm-project/vllm#35193: [Bug]: Deadlock in async_scheduling with TP=1 (UniProcExecutor) when a DP rank raises exception inside `execute_model`

| 字段 | 值 |
| --- | --- |
| Issue | [#35193](https://github.com/vllm-project/vllm/issues/35193) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deadlock in async_scheduling with TP=1 (UniProcExecutor) when a DP rank raises exception inside `execute_model`

### Issue 正文摘录

### Your current environment vLLM: v0.16.0rc1-424-g228054054 python: 3.12.11 torch: 2.9.1+cu128 os: Ubuntu 22.04.5 LTS ### 🐛 Describe the bug Under `async_scheduling` mode with **TP=1** using `UniProcExecutor`, the `EngineCore` may enter a global deadlock if a single DP rank raises an exception inside `execute_model` in `model_runner`, and the propagation of the exception is blocked afterwards. The key issue is that exceptions raised inside the worker are typically wrapped into a returned `Future` in `collective_rpc` call, but are **not checked in the same scheduling step** by `EngineCore`. As a result, the exception is neither surfaced nor handled in time, which can cause all DP ranks to hang indefinitely. ### Reproduction Scenario Assume: ```text DP_SIZE = 4 TP = 1 Executor = UniProcExecutor ``` To reproduce, inject the following error in `/vllm/v1/worker/dp_utils.py`, inside `_run_ar`, before it returns: ```python def _run_ar( should_ubatch: bool, should_dp_pad: bool, orig_num_tokens_per_ubatch: int, padded_num_tokens_per_ubatch: int, cudagraph_mode: int, parallel_config: ParallelConfig, ) -> torch.Tensor: dp_size = parallel_config.data_parallel_size dp_rank = parallel_config.d...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Deadlock in async_scheduling with TP=1 (UniProcExecutor) when a DP rank raises exception inside `execute_model` bug;stale ### Your current environment vLLM: v0.16.0rc1-424-g228054054 python: 3.12.11 torch: 2.9.1+...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g_num_tokens_per_ubatch: int, padded_num_tokens_per_ubatch: int, cudagraph_mode: int, parallel_config: ParallelConfig, ) -> torch.Tensor: dp_size = parallel_config.data_parallel_size dp_rank = parallel_config.data_paral...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: xecute_model` in `model_runner`, and the propagation of the exception is blocked afterwards. The key issue is that exceptions raised inside the worker are typically wrapped into a returned `Future` in `collective_rpc` c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: h TP=1 (UniProcExecutor) when a DP rank raises exception inside `execute_model` bug;stale ### Your current environment vLLM: v0.16.0rc1-424-g228054054 python: 3.12.11 torch: 2.9.1+cu128 os: Ubuntu 22.04.5 LTS ### 🐛 Desc...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: o Assume: ```text DP_SIZE = 4 TP = 1 Executor = UniProcExecutor ``` To reproduce, inject the following error in `/vllm/v1/worker/dp_utils.py`, inside `_run_ar`, before it returns: ```python def _run_ar( should_ubatch: b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
