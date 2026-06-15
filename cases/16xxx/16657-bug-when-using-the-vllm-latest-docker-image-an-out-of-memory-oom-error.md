# vllm-project/vllm#16657: [Bug]:When using the vllm:latest Docker image, an Out-Of-Memory (OOM) error occurs.

| 字段 | 值 |
| --- | --- |
| Issue | [#16657](https://github.com/vllm-project/vllm/issues/16657) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:When using the vllm:latest Docker image, an Out-Of-Memory (OOM) error occurs.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the `vllm:latest` Docker image, an Out-Of-Memory (OOM) error occurs. **Model Used:** Qwen2.5-VL-3B-Instruct-AWQ **GPUs:** 3060 and 4060 Ti **Command Line:** `--served-model-name qwen2.5-vl-3b-instruct --model /models --gpu-memory-utilization 0.9 --max-model-len 64000 --limit-mm-per-prompt "image=100"` **Issue:** After multiple tests, the memory usage keeps increasing and does not get released, leading to an OOM error. However, GPU memory usage remains normal during the tests. This behavior has been observed on both **Windows Docker** and **Linux Docker** environments. --- **Test Parameters (curl request):** ```json { "messages": [ { "role": "user", "content": [ { "type": "image_url", "image_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAAAD/..." }, { "type": "image_url", "image_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAAAD/..." }, { "type": "text", "text": "How many people?" } ] } ] } ``` (Note: Replace `/9j/4AAQSkZJRgABAQEAAAAAAAD/...` with the actual base64-encoded image data.) --- In my testing environment, I used vision and ran over 10 images simultaneously. The memory usage keeps increasing cont...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]:When using the vllm:latest Docker image, an Out-Of-Memory (OOM) error occurs. bug;stale ### Your current environment ### 🐛 Describe the bug When using the `vllm:latest` Docker image, an Out-Of-Memory (OOM) error o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: g the vllm:latest Docker image, an Out-Of-Memory (OOM) error occurs. bug;stale ### Your current environment ### 🐛 Describe the bug When using the `vllm:latest` Docker image, an Out-Of-Memory (OOM) error occurs. **Model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ps. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]:When using the vllm:latest Docker image, an Out-Of-Memory (OOM) error occurs. bug;stale ### Your current environment ### 🐛 Describe the bug When using the `vllm:latest` Docker image, an Out-Of-Memory (OOM) error o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the `vllm:latest` Docker image, an Out-Of-Memory (OOM) error occurs. **Model Used:** Qwen2.5-VL-3B-Instruct-AWQ **GPUs:** 3060 and 4060 Ti **Command Line:** `--served-model-name qwen2.5-vl-3b-instruct --model /models --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
