# vllm-project/vllm#25113: [Bug]: Ray distributed executor backend: CUDA device mismatch when using multiple GPUs on a single node

| 字段 | 值 |
| --- | --- |
| Issue | [#25113](https://github.com/vllm-project/vllm/issues/25113) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ray distributed executor backend: CUDA device mismatch when using multiple GPUs on a single node

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’m running on a single node with multiple GPUs and trying to use Ray as the distributed backend. The problem seems to be that Ray launches each TP/PP actor pinned to a single GPU ([code](https://github.com/vllm-project/vllm/blob/main/vllm/executor/ray_distributed_executor.py#L205-L211)), but then vLLM overwrites CUDA_VISIBLE_DEVICES with all available GPUs on the node ([code](https://github.com/vllm-project/vllm/blob/main/vllm/executor/ray_distributed_executor.py#L332-L336)). This leads to a mismatch between what the actor is assigned to and what it attempts to access. This issue only arises when multiple GPUs are used on a single node. If both TP and PP are set to 1, or if only one GPU is used per node, the problem does not occur. With vLLM==0.10.2 and the latest ray (master), the following command results in the error below. ``` vllm serve facebook/opt-125m \ --tensor-parallel-size 2 \ --pipeline-parallel-size 1 \ --distributed-executor-backend ray ``` ``` (EngineCore_DP0 pid=145286) INFO 09-17 06:19:22 [ray_distributed_executor.py:122] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGT...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 27] File "/home/ubuntu/.local/lib/python3.11/site-packages/ray/util/tracing/tracing_helper.py", line 461, in _resume_span (EngineCore_DP0 pid=145286) (RayWorkerWrapper pid=146286) ERROR 09-17 06:19:22 [worker_base.py:62...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Ray distributed executor backend: CUDA device mismatch when using multiple GPUs on a single node bug;ray ### Your current environment ### 🐛 Describe the bug I’m running on a single node with multiple GPUs and try...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Ray distributed executor backend: CUDA device mismatch when using multiple GPUs on a single node bug;ray ### Your current environment ### 🐛 Describe the bug I’m running on a single node with multiple GPUs and try...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rker_base.py:627] Error executing method 'init_device'. This might cause deadlock in distributed execution. (EngineCore_DP0 pid=145286) (RayWorkerWrapper pid=146286) ERROR 09-17 06:19:22 [worker_base.py:627] Traceback (...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Ray distributed executor backend: CUDA device mismatch when using multiple GPUs on a single node bug;ray ### Your current environment ### 🐛 Describe the bug I’m running on a single node with multiple GPUs and try...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
