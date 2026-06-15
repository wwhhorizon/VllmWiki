# vllm-project/vllm#2328: CUDA error when loading mixtral model

| 字段 | 值 |
| --- | --- |
| Issue | [#2328](https://github.com/vllm-project/vllm/issues/2328) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA error when loading mixtral model

### Issue 正文摘录

``` (RayWorkerVllm pid=7009) warnings.warn("Initializing zero-element tensors is a no-op") INFO 01-03 15:52:10 llm_engine.py:223] # GPU blocks: 86934, # CPU blocks: 8192 (RayWorkerVllm pid=7009) INFO 01-03 15:52:13 model_runner.py:394] Capturing the model for CUDA graphs. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set 'enforce_eager=True' or use '--enforce-eager' in the CLI. (RayWorkerVllm pid=7009) [E ProcessGroupNCCL.cpp:915] [Rank 0] NCCL watchdog thread terminated with exception: CUDA error: operation not permitted when stream is capturing (RayWorkerVllm pid=7009) CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. (RayWorkerVllm pid=7009) For debugging consider passing CUDA_LAUNCH_BLOCKING=1. (RayWorkerVllm pid=7009) Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ugging consider passing CUDA_LAUNCH_BLOCKING=1. (RayWorkerVllm pid=7009) Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` correctness ci_build;distributed_parallel;frontend_api;model_support cuda;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: CUDA error when loading mixtral model ``` (RayWorkerVllm pid=7009) warnings.warn("Initializing zero-element tensors is a no-op") INFO 01-03 15:52:10 llm_engine.py:223] # GPU blocks: 86934, # CPU blocks: 8192 (RayWorker
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ted_parallel;frontend_api;model_support cuda;kernel;operator build_error;mismatch ```
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lement tensors is a no-op") INFO 01-03 15:52:10 llm_engine.py:223] # GPU blocks: 86934, # CPU blocks: 8192 (RayWorkerVllm pid=7009) INFO 01-03 15:52:13 model_runner.py:394] Capturing the model for CUDA graphs. This may...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: CUDA error when loading mixtral model ``` (RayWorkerVllm pid=7009) warnings.warn("Initializing zero-element tensors is a no-op") INFO 01-03 15:52:10 llm_engine.py:223] # GPU blocks: 86934, # CPU blocks: 8192 (RayWorkerV...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
