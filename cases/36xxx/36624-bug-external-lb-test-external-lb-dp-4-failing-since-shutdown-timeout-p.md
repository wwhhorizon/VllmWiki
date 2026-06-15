# vllm-project/vllm#36624: [Bug] External LB test_external_lb_dp[4] failing since shutdown timeout PR #34730

| 字段 | 值 |
| --- | --- |
| Issue | [#36624](https://github.com/vllm-project/vllm/issues/36624) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] External LB test_external_lb_dp[4] failing since shutdown timeout PR #34730

### Issue 正文摘录

## Description `test_external_lb_dp.py` with `api_server_count=4` has been failing consistently in every nightly/daily build since PR #34730 (`27066d1b`) landed on Mar 6. The `[1]` variant (1 API server per DP rank) passes; only `[4]` (4 API servers per DP rank) fails. ## Affected tests - `test_external_lb_server_info[4]` - `test_external_lb_single_completion[4-ibm-research/PowerMoE-3b]` - `test_external_lb_completion_streaming[4-ibm-research/PowerMoE-3b]` ## Error ``` EngineCore_DP1: WorkerProc initialization failed due to an exception in a background process. Worker_DP0_TP0: Parent process exited, terminating worker queues Worker_DP0_TP0: BrokenPipeError: [Errno 32] Broken pipe Failed to start server rank 0: Server exited unexpectedly Exception: Servers failed to start ``` ## Bisection - **Last passing build:** #54783 (daily Mar 5, commit `a97954b6`) - **First failing build:** #54882 (nightly Mar 6, commit `5afb387b`) - **Culprit:** PR #34730 (`27066d1b`) — "[Frontend][Core] Add shutdown timeout - allowing in-flight requests to finish" - **Failing in every nightly/daily since:** #54882, #55011, #55067, #55110, #55120, #55158, #55214, #55354, #55437 ## Analysis PR #34730 changes...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: api_server_count=4` has been failing consistently in every nightly/daily build since PR #34730 (`27066d1b`) landed on Mar 6. The `[1]` variant (1 API server per DP rank) passes; only `[4]` (4 API servers per DP rank) fa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ernal_lb_server_info[4]` - `test_external_lb_single_completion[4-ibm-research/PowerMoE-3b]` - `test_external_lb_completion_streaming[4-ibm-research/PowerMoE-3b]` ## Error ``` EngineCore_DP1: WorkerProc initialization fa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: round process. Worker_DP0_TP0: Parent process exited, terminating worker queues Worker_DP0_TP0: BrokenPipeError: [Errno 32] Broken pipe Failed to start server rank 0: Server exited unexpectedly Exception: Servers failed...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug] External LB test_external_lb_dp[4] failing since shutdown timeout PR #34730 ## Description `test_external_lb_dp.py` with `api_server_count=4` has been failing consistently in every nightly/daily build since PR #34...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: erver_info[4]` - `test_external_lb_single_completion[4-ibm-research/PowerMoE-3b]` - `test_external_lb_completion_streaming[4-ibm-research/PowerMoE-3b]` ## Error ``` EngineCore_DP1: WorkerProc initialization failed due t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
