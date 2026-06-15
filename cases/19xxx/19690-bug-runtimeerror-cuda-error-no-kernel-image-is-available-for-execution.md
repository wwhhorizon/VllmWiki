# vllm-project/vllm#19690: [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device using H100 starting RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic

| 字段 | 值 |
| --- | --- |
| Issue | [#19690](https://github.com/vllm-project/vllm/issues/19690) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device using H100 starting RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to run RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic on vllm 0.9.1 (`vllm serve --config llama.yaml`). Vllm does not start and this appears in the log: ``` (VllmWorker rank=1 pid=14283) ERROR 06-16 07:53:45 [multiproc_executor.py:527] RuntimeError: CUDA error: no kernel image is available for execution on the device (VllmWorker rank=1 pid=14283) ERROR 06-16 07:53:45 [multiproc_executor.py:527] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. (VllmWorker rank=1 pid=14283) ERROR 06-16 07:53:45 [multiproc_executor.py:527] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 (VllmWorker rank=1 pid=14283) ERROR 06-16 07:53:45 [multiproc_executor.py:527] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` This model worked fine under 0.8.5.post1. lllama.yaml: ``` model: /opt/llm/models/RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic served-model-name: llama-4-scout max-model-len: 65536 tensor_parallel_size: 2 port: 8002 api_key: XXXXXXX enable_auto_tool_choice: true tool_call_parser: llama4_pythonic chat-template: /opt/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: orker rank=1 pid=14283) ERROR 06-16 07:53:45 [multiproc_executor.py:527] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` This model worked fine under 0.8.5.post1. lllama.yaml: ``` model: /opt/llm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device using H100 starting RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic bug;stale ### Your current environment ### 🐛 Describe the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n the device using H100 starting RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to run RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ge is available for execution on the device using H100 starting RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to run RedHatAI/Llama-4-S...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ng H100 starting RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to run RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic on vllm 0.9.1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
