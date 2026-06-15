# vllm-project/vllm#26598: [Bug]: Pipeline parallelism skips GPUs and hangs during model load

| 字段 | 值 |
| --- | --- |
| Issue | [#26598](https://github.com/vllm-project/vllm/issues/26598) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pipeline parallelism skips GPUs and hangs during model load

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug * **vLLM version:** `0.11.0` * **Hardware:** 9x NVIDIA GeForce RTX 3090 * **Executor:** `MultiprocExecutor` (default for single-node) #### **Code to reproduce** This issue is reproducible with a standard launch command for pipeline parallelism on a single node with 8+ GPUs. The issue occurs both with and without a custom `VLLM_PP_LAYER_PARTITION`. ```bash #!/bin/bash source /path/to/venv/bin/activate # Use 8 GPUs visible to the process export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 export CUDA_DEVICE_ORDER=PCI_BUS_ID python -m vllm.entrypoints.openai.api_server \ --model /path/to/Qwen3-VL-235B-A22B-Instruct-AWQ \ --pipeline-parallel-size 8 \ --tensor-parallel-size 1 \ --max-model-len 20000 \ --gpu-memory-utilization 0.94 ``` #### **Logs** **Summary of Findings:** When launching with `pipeline-parallel-size=8`, the vLLM engine hangs during the model loading phase. `nvidia-smi` shows that 2 of the 8 GPUs are not utilized. The specific GPUs that hang can vary between runs, but the behavior is consistent. * This issue occurs regardless of whether `VLLM_PP_LAYER_PARTITION` is set. * The physical GPUs are confirmed to be healthy and work...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tale ### Your current environment ### 🐛 Describe the bug * **vLLM version:** `0.11.0` * **Hardware:** 9x NVIDIA GeForce RTX 3090 * **Executor:** `MultiprocExecutor` (default for single-node) #### **Code to reproduce** T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Pipeline parallelism skips GPUs and hangs during model load bug;stale ### Your current environment ### 🐛 Describe the bug * **vLLM version:** `0.11.0` * **Hardware:** 9x NVIDIA GeForce RTX 3090 * **Executor:** `M...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Pipeline parallelism skips GPUs and hangs during model load bug;stale ### Your current environment ### 🐛 Describe the bug * **vLLM version:** `0.11.0` * **Hardware:** 9x NVIDIA GeForce RTX 3090 * **Executor:** `M...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Pipeline parallelism skips GPUs and hangs during model load bug;stale ### Your current environment ### 🐛 Describe the bug * **vLLM version:** `0.11.0` * **Hardware:** 9x NVIDIA GeForce RTX 3090 * **Executor:** `M...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: xecutor:** `MultiprocExecutor` (default for single-node) #### **Code to reproduce** This issue is reproducible with a standard launch command for pipeline parallelism on a single node with 8+ GPUs. The issue occurs both...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
