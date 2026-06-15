# vllm-project/vllm#39603: [Performance]: [Bug]: meet same thread as registerClien when start_profile

| 字段 | 值 |
| --- | --- |
| Issue | [#39603](https://github.com/vllm-project/vllm/issues/39603) |
| 状态 | open |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: [Bug]: meet same thread as registerClien when start_profile

### Issue 正文摘录

### Proposal to improve performance vllm + 1p1d + ds3.2 decode="10.233.83.96" curl -X POST http://${decode}:8200/start_profile curl -X POST http://${decode}:8200/stop_profile (ApiServer_2 pid=468) INFO 04-12 03:02:55 [api_router.py:23] Starting profiler... ERROR: External init callback must run in same thread as registerClient (327136832 != -2017364160) (ApiServer_2 pid=468) INFO 04-12 03:02:55 [api_router.py:25] Profiler started. (ApiServer_4 pid=470) INFO 04-12 03:03:10 [api_router.py:31] Stopping profiler... ### Report of performance regression decode="10.233.83.96" curl -X POST http://${decode}:8200/start_profile curl -X POST http://${decode}:8200/stop_profile (ApiServer_2 pid=468) INFO 04-12 03:02:55 [api_router.py:23] Starting profiler... ERROR: External init callback must run in same thread as registerClient (327136832 != -2017364160) (ApiServer_2 pid=468) INFO 04-12 03:02:55 [api_router.py:25] Profiler started. (ApiServer_4 pid=470) INFO 04-12 03:03:10 [api_router.py:31] Stopping profiler... ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a n...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: [Bug]: meet same thread as registerClien when start_profile performance ### Proposal to improve performance vllm + 1p1d + ds3.2 decode="10.233.83.96" curl -X POST http://${decode}:8200/start_profile curl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ecode}:8200/stop_profile (ApiServer_2 pid=468) INFO 04-12 03:02:55 [api_router.py:23] Starting profiler... ERROR: External init callback must run in same thread as registerClient (327136832 != -2017364160) (ApiServer_2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: le performance ### Proposal to improve performance vllm + 1p1d + ds3.2 decode="10.233.83.96" curl -X POST http://${decode}:8200/start_profile curl -X POST http://${decode}:8200/stop_profile (ApiServer_2 pid=468) INFO 04...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
