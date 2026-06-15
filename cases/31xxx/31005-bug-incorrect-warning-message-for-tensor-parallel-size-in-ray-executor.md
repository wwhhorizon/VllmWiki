# vllm-project/vllm#31005: [Bug]: Incorrect warning message for tensor parallel size in Ray executor (ray_utils.py:331-340)

| 字段 | 值 |
| --- | --- |
| Issue | [#31005](https://github.com/vllm-project/vllm/issues/31005) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incorrect warning message for tensor parallel size in Ray executor (ray_utils.py:331-340)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running vLLM with the Ray distributed executor, the WARNING log emitted in `vllm/vllm/v1/executor/ray_utils.py` (lines 331–340) is **incorrect and misleading** under multi-node + pipeline parallel configurations. The issue is limited to the **log message logic** and does not affect actual execution correctness. **Environment** * **Hardware** * Ray cluster with **2 nodes** * Each node has **8 × NVIDIA H20 GPUs** * Total GPUs in cluster: **16** * **Software** * vLLM (Ray distributed executor backend) * Ray **Launch Command** ```bash vllm serve ... \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --distributed-executor-backend ray ``` **Expected Behavior** With Ray backend, the total number of GPUs required is: ``` tensor_parallel_size × pipeline_parallel_size = 8 × 2 = 16 GPUs ``` Since the Ray cluster has 16 GPUs available, this configuration is valid and should **not** trigger a warning about insufficient GPUs. **Actual Behavior** The following warning is logged at startup: ```text (EngineCore_DP0 pid=1912) WARNING 12-16 19:14:46 [ray_utils.py:331] Tensor parallel size (16) exceeds available GPUs (8). This may resul...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s in cluster: **16** * **Software** * vLLM (Ray distributed executor backend) * Ray **Launch Command** ```bash vllm serve ... \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --distributed-executor-backend ray...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: configuration is valid and should **not** trigger a warning about insufficient GPUs. **Actual Behavior** The following warning is logged at startup: ```text (EngineCore_DP0 pid=1912) WARNING 12-16 19:14:46 [ray_utils.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 40) is **incorrect and misleading** under multi-node + pipeline parallel configurations. The issue is limited to the **log message logic** and does not affect actual execution correctness. **Environment** * **Hardware**...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: for tensor parallel size in Ray executor (ray_utils.py:331-340) bug;ray;stale ### Your current environment ### 🐛 Describe the bug When running vLLM with the Ray distributed executor, the WARNING log emitted in `vllm/vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
