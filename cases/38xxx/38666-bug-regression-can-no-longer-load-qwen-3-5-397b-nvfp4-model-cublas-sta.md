# vllm-project/vllm#38666: [Bug]: Regression can no longer load Qwen 3.5 397B nvfp4 model - CUBLAS_STATUS_NOT_INITIALIZED

| 字段 | 值 |
| --- | --- |
| Issue | [#38666](https://github.com/vllm-project/vllm/issues/38666) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;moe;sampling |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Regression can no longer load Qwen 3.5 397B nvfp4 model - CUBLAS_STATUS_NOT_INITIALIZED

### Issue 正文摘录

### Your current environment [env.txt](https://github.com/user-attachments/files/26391842/env.txt) See attached environment and log. Running CI builds and in the last day or so something broke. vllm crashes when attempting to start when loading Qwen 3.5 397B A17B - Seyho. I had been using tensor and expert parallel and other features. I simplified the configuration and it still is failing. This is across 4x RTX 6000 GPUs. `(Worker_TP3 pid=27021) ERROR 03-31 18:15:56 [multiproc_executor.py:949] RuntimeError: CUDA error: CUBLAS_STATUS_NOT_INITIALIZED when calling cublasLtMatmulAlgoGetHeuristic( ltHandle, computeDesc.descriptor(), Adesc.descriptor(), Bdesc.descriptor(), Cdesc.descriptor(), Cdesc.descriptor(), preference.descriptor(), 1, &heuristicResult, &returnedResult)` [log.txt](https://github.com/user-attachments/files/26391970/log.txt) I've simplified my configuration down to: ``` host: 0.0.0.0 # Bind to all interfaces (required for remote access / containers) port: 8081 # HTTP API port model: /mnt/models/Qwen3.5-397B-A17B-NVFP4-sehyo # Active model (absolute path, no trailing slash) served-model-name: qwen3.5-397b-a17b # Name returned by /v1/models and used by clients tensor-pa...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: simplified the configuration and it still is failing. This is across 4x RTX 6000 GPUs. `(Worker_TP3 pid=27021) ERROR 03-31 18:15:56 [multiproc_executor.py:949] RuntimeError: CUDA error: CUBLAS_STATUS_NOT_INITIALIZED whe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Regression can no longer load Qwen 3.5 397B nvfp4 model - CUBLAS_STATUS_NOT_INITIALIZED bug ### Your current environment [env.txt](https://github.com/user-attachments/files/26391842/env.txt) See attached environm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Regression can no longer load Qwen 3.5 397B nvfp4 model - CUBLAS_STATUS_NOT_INITIALIZED bug ### Your current environment [env.txt](https://github.com/user-attachments/files/26391842/env.txt) See attached environm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ents/files/26391842/env.txt) See attached environment and log. Running CI builds and in the last day or so something broke. vllm crashes when attempting to start when loading Qwen 3.5 397B A17B - Seyho. I had been using...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: art when loading Qwen 3.5 397B A17B - Seyho. I had been using tensor and expert parallel and other features. I simplified the configuration and it still is failing. This is across 4x RTX 6000 GPUs. `(Worker_TP3 pid=2702...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
