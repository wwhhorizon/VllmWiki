# vllm-project/vllm#19791: [Bug]: MP Executor does not correctly handle device allocation for non-CUDA devices (e.g., NPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#19791](https://github.com/vllm-project/vllm/issues/19791) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MP Executor does not correctly handle device allocation for non-CUDA devices (e.g., NPUs)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #### **Problem Description** Currently, the `mp_distributed_executor.py` logic in vLLM explicitly sets the environment variable `CUDA_VISIBLE_DEVICES` when it is not already present in the environment. This implementation inherently assumes the use of CUDA-enabled GPUs. Reference: [https://github.com/vllm-project/vllm/blob/119f683949dfed10df769fe63b2676d7f1eb644e/vllm/executor/mp\_distributed\_executor.py#L52-L55](https://github.com/vllm-project/vllm/blob/119f683949dfed10df769fe63b2676d7f1eb644e/vllm/executor/mp_distributed_executor.py#L52-L55) Specifically, the current implementation looks like this: ```python if "CUDA_VISIBLE_DEVICES" not in os.environ: update_environment_variables({ "CUDA_VISIBLE_DEVICES": (",".join(map(str, range(world_size)))) }) ``` This approach leads to two major limitations: 1. **Non-CUDA devices (e.g., NPUs, TPU)**: The current implementation does not generalize to environments that do not utilize CUDA. For example, when using NPUs, device allocation relies on different environment variables, and the current CUDA-specific logic breaks compatibility. 2. **Explicit device selection**: Even in a CUDA envir...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: iption** Currently, the `mp_distributed_executor.py` logic in vLLM explicitly sets the environment variable `CUDA_VISIBLE_DEVICES` when it is not already present in the environment. This implementation inherently assume...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Ray implementation correctly sets devices based on Ray-provided device information, making it generalizable across CUDA, TPU, NPU, and other custom devices. #### **Proposed Solution (will submit via separate PR)** A gen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: with a separate PR after discussions or feedback on this issue. #### **Request for Comments** Please let me know if there's any additional context or consideration I should be aware of before submitting the PR. I'm happ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: _distributed_executor.py#L332-L335) In this correct implementation, Ray backend respects the platform-specific environment variable defined by: ```python current_platform.device_control_env_var ``` The Ray implementatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: MP Executor does not correctly handle device allocation for non-CUDA devices (e.g., NPUs) bug ### Your current environment ### 🐛 Describe the bug #### **Problem Description** Currently, the `mp_distributed_execut...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
