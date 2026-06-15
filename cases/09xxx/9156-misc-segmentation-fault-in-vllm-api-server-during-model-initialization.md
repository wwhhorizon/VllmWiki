# vllm-project/vllm#9156: [Misc]: Segmentation Fault in vLLM API Server during Model Initialization (NCCL Error: Unhandled System Error)

| 字段 | 值 |
| --- | --- |
| Issue | [#9156](https://github.com/vllm-project/vllm/issues/9156) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Segmentation Fault in vLLM API Server during Model Initialization (NCCL Error: Unhandled System Error)

### Issue 正文摘录

### Anything you want to discuss about vllm. I'm experiencing a segmentation fault while running the vLLM API server with Ray for distributed inference. The issue seems to be related to NCCL initialization, resulting in an "unhandled system error" during distributed execution, causing the process to fail with a segmentation fault (SIGSEGV). Command I am running: `python -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3.1-70B-Instruct --trust-remote-code --device cuda --tensor-parallel-size 4 --gpu-memory-utilization 0.9 --swap-space 10 --dtype bfloat16 --api-key --enforce-eager --pipeline-parallel-size 2 --max-model-len 110000 --max-seq-len-to-capture 1100 --disable-custom-all-reduce ` Error Logs: `INFO vLLM API server version 0.6.0 INFO args: Namespace(...) INFO Started engine process with PID INFO Connecting to existing Ray cluster at address: ... INFO vLLM is using nccl==2.20.5 ERROR NCCL error: unhandled system error (run with NCCL_DEBUG=INFO for details) Fatal Python error: Segmentation fault ` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docum...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: m Error) stale ### Anything you want to discuss about vllm. I'm experiencing a segmentation fault while running the vLLM API server with Ray for distributed inference. The issue seems to be related to NCCL initializatio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --tensor-parallel-size 4 --gpu-memory-utilization 0.9 --swap-space 10 --dtype bfloat16 --api-key --enforce-eager --pipeline-parallel-size 2 --max-model-len 110000 --max-seq-len-to-capture 1100 --disable-custom-all-reduc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: odel meta-llama/Meta-Llama-3.1-70B-Instruct --trust-remote-code --device cuda --tensor-parallel-size 4 --gpu-memory-utilization 0.9 --swap-space 10 --dtype bfloat16 --api-key --enforce-eager --pipeline-parallel-size 2 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Misc]: Segmentation Fault in vLLM API Server during Model Initialization (NCCL Error: Unhandled System Error) stale ### Anything you want to discuss about vllm. I'm experiencing a segmentation fault while running the v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Server during Model Initialization (NCCL Error: Unhandled System Error) stale ### Anything you want to discuss about vllm. I'm experiencing a segmentation fault while running the vLLM API server with Ray for distributed...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
