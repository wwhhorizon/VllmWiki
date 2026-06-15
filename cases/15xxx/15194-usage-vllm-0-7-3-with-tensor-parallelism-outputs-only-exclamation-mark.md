# vllm-project/vllm#15194: [Usage]: VLLM 0.7.3 with tensor parallelism outputs only exclamation marks when using multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#15194](https://github.com/vllm-project/vllm/issues/15194) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: VLLM 0.7.3 with tensor parallelism outputs only exclamation marks when using multiple GPUs

### Issue 正文摘录

## Environment - OS: Ubuntu 22.04 - GPUs: 2x NVIDIA L20 (49GB each) - VLLM version: 0.7.3 - CUDA version: 12.4.131 - Driver version: 535.161.08 - Model: QwQ-32B-AWQ (AWQ quantized model) ## Problem Description When running VLLM with tensor parallelism across two GPUs, the model sometimes outputs only exclamation marks (`!`) instead of proper text. This issue only occurs with multiple GPUs and appears to be related to concurrent requests - single GPU deployment works fine. The problem is consistently reproducible when sending concurrent requests with the same prompt to the API endpoint, but non-concurrent requests sometimes produce normal responses. ## Steps to Reproduce 1. Start VLLM server with tensor parallelism: ```bash vllm serve /root/data/models/QwQ-32B-AWQ --api-key dev-key --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --quantization awq --host 0.0.0.0 --port 8877 --served-model-name qwq ``` 2. Send multiple concurrent requests using curl: ```bash curl -X POST "http://localhost:8877/v1/chat/completions" \ -H "Content-Type: application/json" \ -H "Authorization: Bearer dev-key" \ -d '{ "model": "qwq", "messages": [ {"role": "system", "content": "You are a helpful AI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Environment - OS: Ubuntu 22.04 - GPUs: 2x NVIDIA L20 (49GB each) - VLLM version: 0.7.3 - CUDA version: 12.4.131 - Driver version: 535.161.08 - Model: QwQ-32B-AWQ (AWQ quantized model) ## Problem Description When running...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: M version: 0.7.3 - CUDA version: 12.4.131 - Driver version: 535.161.08 - Model: QwQ-32B-AWQ (AWQ quantized model) ## Problem Description When running VLLM with tensor parallelism across two GPUs, the model sometimes out...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: equests - single GPU deployment works fine. The problem is consistently reproducible when sending concurrent requests with the same prompt to the API endpoint, but non-concurrent requests sometimes produce normal respon...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: VLLM 0.7.3 with tensor parallelism outputs only exclamation marks when using multiple GPUs usage;stale ## Environment - OS: Ubuntu 22.04 - GPUs: 2x NVIDIA L20 (49GB each) - VLLM version: 0.7.3 - CUDA version: 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: arallelism outputs only exclamation marks when using multiple GPUs usage;stale ## Environment - OS: Ubuntu 22.04 - GPUs: 2x NVIDIA L20 (49GB each) - VLLM version: 0.7.3 - CUDA version: 12.4.131 - Driver version: 535.161...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
