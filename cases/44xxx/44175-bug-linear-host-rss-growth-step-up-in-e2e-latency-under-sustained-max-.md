# vllm-project/vllm#44175: [Bug]: Linear host RSS growth + step-up in E2E latency under sustained `max_tokens=1` classification load (Gemma-3-1b, V1, prefix caching)

| 字段 | 值 |
| --- | --- |
| Issue | [#44175](https://github.com/vllm-project/vllm/issues/44175) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Linear host RSS growth + step-up in E2E latency under sustained `max_tokens=1` classification load (Gemma-3-1b, V1, prefix caching)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```yaml containers: - args: - --model=/data/models/gemma-3-1b-it/ - --served-model-name=gemma-3-1b-it - --gpu-memory-utilization=0.90 - --uvicorn-log-level=warning env: - name: OMP_NUM_THREADS value: "1" image: /serving/vllm:v0.21.0 resources: limits: cpu: "2" memory: 16Gi nvidia.com/mig-1g.10gb: "1" requests: cpu: "2" memory: 16Gi ``` - Engine: V1 (default in 0.21.0). - Prefix caching: default (enabled) — not explicitly disabled. - Chunked prefill: default (enabled). - `/dev/shm`: 16 GiB `emptyDir` (medium: Memory). - 1 replica, no autoscaling. ## 🐛 Describe the bug ### Summary Under a sustained 12-hour stability test, the server shows **a continuous, linear increase in container (host) RSS** and a **step-up in E2E latency after ~7 hours**, while **per-pod CPU usage gradually declines** even though request rate is held constant. Throughput is fixed by the load generator, so the workload itself does not change over time; only the server's internal state does. ### Workload - Prompt length: ~550 tokens average. - `max_tokens: 1` (single output token per request — effectively prefill-dominated). - Load: constant **150 RPS** for **12...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: : V1 (default in 0.21.0). - Prefix caching: default (enabled) — not explicitly disabled. - Chunked prefill: default (enabled). - `/dev/shm`: 16 GiB `emptyDir` (medium: Memory). - 1 replica, no autoscaling. ## 🐛 Describe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: s, Max 0.18 s over the window). - The step is a discrete knee, not a smooth ramp from t=0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cpu: "2" memory: 16Gi nvidia.com/mig-1g.10gb: "1" requests: cpu: "2" memory: 16Gi ``` - Engine: V1 (default in 0.21.0). - Prefix caching: default (enabled) — not explicitly disabled. - Chunked prefill: default (enabled)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Linear host RSS growth + step-up in E2E latency under sustained `max_tokens=1` classification load (Gemma-3-1b, V1, prefix caching) bug ### Your current environment ### 🐛 Describe the bug ```yaml containers: - ar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ep-up in E2E latency under sustained `max_tokens=1` classification load (Gemma-3-1b, V1, prefix caching) bug ### Your current environment ### 🐛 Describe the bug ```yaml containers: - args: - --model=/data/models/gemma-3...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
