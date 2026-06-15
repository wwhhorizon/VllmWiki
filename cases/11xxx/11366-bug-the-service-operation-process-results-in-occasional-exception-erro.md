# vllm-project/vllm#11366: [Bug]: The service operation process results in occasional exception errors RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#11366](https://github.com/vllm-project/vllm/issues/11366) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The service operation process results in occasional exception errors RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Use the following command to start the service, and call the service. The following error will occasionally occur, and the service will be shut down `python -m vllm.entrypoints.api_server --host 127.0.0.1 --tensor-parallel-size 1 --enforce-eager --trust-remote-code --gpu-memory-utilization 0.9 --model ./Qwen2_5_7b_awq --port 9122` 2024-12-19 21:40:35 WARNING 56542 [model_runner_base.py:143] Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered^M 2024-12-19 21:40:35 WARNING 56542 [model_runner_base.py:143] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.^M 2024-12-19 21:40:35 WARNING 56542 [model_runner_base.py:143] For debugging consider passing CUDA_LAUNCH_BLOCKING=1^M 2024-12-19 21:40:35 WARNING 56542 [model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.^M 2024-12-19 21:40:35 WARNING 56542 [model_runner_base.py:143] 2024-12-19 21:40:35 ERROR 56542 [async_llm_engine.py:64] Engine background task failed^M 2024-12-19 21:40:35 ERROR 56542 [asy...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: LOCKING=1^M 2024-12-19 21:40:35 WARNING 56542 [model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.^M 2024-12-19 21:40:35 WARNING 56542 [model_runner_base.py:143] 2024-12-19 21:4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e operation process results in occasional exception errors RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 42 [model_runner_base.py:143] For debugging consider passing CUDA_LAUNCH_BLOCKING=1^M 2024-12-19 21:40:35 WARNING 56542 [model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.^M 20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ry access was encountered bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Use the following command to start the service, and call the service. The following error will...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Use the following command to start the service, and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
