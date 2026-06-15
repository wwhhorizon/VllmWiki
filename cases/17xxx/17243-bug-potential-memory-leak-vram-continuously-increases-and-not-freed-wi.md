# vllm-project/vllm#17243: [Bug]: Potential memory leak: VRAM continuously increases and not freed with deepseek-r1 on vLLM v1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#17243](https://github.com/vllm-project/vllm/issues/17243) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential memory leak: VRAM continuously increases and not freed with deepseek-r1 on vLLM v1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Description **vLLM Version:** v0.8.4 **GPU:** 8 x NVIDIA H20-3e **Model:** deepseekai/DeepSeek-R1 **gpu_memory_utilization:** 0.9 (default) When sending chat requests with long input texts (>= 2048 tokens), initially using 32 concurrent requests, GPU memory increases but stays within a reasonable range (actual VRAM < Total VRAM * `gpu_memory_utilization`). However, after some time, when using 64 concurrent requests, the GPU memory rapidly grows to an alarming level (approximately 98% of Total VRAM, exceeding Total VRAM * `gpu_memory_utilization`). Furthermore, this extra memory is not released even some time after the requests have finished. ## Steps to Reproduce 1. Start the vLLM server using the following command: ```bash source /etc/profile && vllm serve /data/DeepSeek-R1 \ --port 8000 \ --served-model-name deepseekai/DeepSeek-R1 \ --api-key=YOUR_API_KEY \ --tensor-parallel-size 8 \ --max-model-len 163840 \ --max-num-batched-tokens 163840 \ --trust-remote-code \ --enable-prefix-caching \ --enable-reasoning \ --reasoning-parser deepseek_r1 ``` 2. Prepare a ShareGPT dataset with prompts longer than or equal to 2048 tokens...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rrent environment ### 🐛 Describe the bug ## Bug Description **vLLM Version:** v0.8.4 **GPU:** 8 x NVIDIA H20-3e **Model:** deepseekai/DeepSeek-R1 **gpu_memory_utilization:** 0.9 (default) When sending chat requests with...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tinuously increases and not freed with deepseek-r1 on vLLM v1 engine bug;stale ### Your current environment ### 🐛 Describe the bug ## Bug Description **vLLM Version:** v0.8.4 **GPU:** 8 x NVIDIA H20-3e **Model:** deepse...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 31) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: he vLLM server using the following command: ```bash source /etc/profile && vllm serve /data/DeepSeek-R1 \ --port 8000 \ --served-model-name deepseekai/DeepSeek-R1 \ --api-key=YOUR_API_KEY \ --tensor-parallel-size 8 \ --...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
