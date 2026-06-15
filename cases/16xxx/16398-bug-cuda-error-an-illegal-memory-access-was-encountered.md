# vllm-project/vllm#16398: [Bug]: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#16398](https://github.com/vllm-project/vllm/issues/16398) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered ### 🐛 Describe the bug running Llama-3.3-70B-Instruct-FP8-Dynamic with vllm-0.6.6 , and the server crashed randomly, does anyone has encountered the same problem? And here is the error log: [1;36m(VllmWorkerProcess pid=210)[0;0m WARNING 04-08 01:00:08 model_runner_base.py:143] Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered [1;36m(VllmWorkerProcess pid=210)[0;0m WARNING 04-08 01:00:08 model_runner_base.py:143] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. [1;36m(VllmWorkerProcess pid=210)[0;0m WARNING 04-08 01:00:08 model_runner_base.py:143] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 [1;36m(VllmWorkerProcess pid=210)[0;0m WARNING 04-08 01:00:08 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. [1;36m(VllmWorkerProcess pid=210)[0;0m WARNING 04-08 01:00:08 model_runner_base.py:143] INFO 04-08 01:00:08 model_runner_base.py:120] Writing input of failed execution to /tmp/err_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rProcess pid=210)[0;0m WARNING 04-08 01:00:08 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. [1;36m(VllmWorkerProcess pid=210)[0;0m WARNING 04-08 01:00:08 model_runner_b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: was encountered ### 🐛 Describe the bug running Llama-3.3-70B-Instruct-FP8-Dynamic with vllm-0.6.6 , and the server crashed randomly, does anyone has encountered the same problem? And here is the error log: [1;36m(VllmW...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered ### 🐛 Describe the bug...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n illegal memory access was encountered ### 🐛 Describe the bug running Llama-3.3-70B-Instruct-FP8-Dynamic with vllm-0.6.6 , and the server crashed randomly, does anyone has encountered the same problem? And here is the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: in apply_fp8_linear ERROR 04-08 01:00:08 engine.py:135] output = ops.cutlass_scaled_mm(qinput, ERROR 04-08 01:00:08 engine.py:135] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-08 01:00:08 engine.py:135] File "/usr/local/lib/p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
