# vllm-project/vllm#35624: [Bug]: Qwen3-Omni Model Fails when try to l

| 字段 | 值 |
| --- | --- |
| Issue | [#35624](https://github.com/vllm-project/vllm/issues/35624) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Omni Model Fails when try to l

### Issue 正文摘录

### 🐛 Describe the bug When trying to limit image/video input to 0 per prompt via `--limit-mm-per-prompt`, the engine core fails during model loading. Model: `Qwen/Qwen3-Omni-30B-A3B-Instruct` ``` containers: - image: vllm/vllm-openai:v0.16.0-cu130 command: - /bin/sh - '-c' args: - | pip install "vllm[audio]" && pip install qwen-omni-utils -U && \ vllm serve /mnt/models/qwen3-omni \ --host 0.0.0.0 \ --port 8000 \ '--served-model-name' \ 'qwen3-omni' \ '--uvicorn-log-level' \ 'warning' \ '--enable-log-requests' \ '--trust-remote-code' \ '--async-scheduling' \ '--enable-prefix-caching' \ '--gpu-memory-utilization' \ '0.9' \ '--max-model-len' \ '2048' \ '--limit-mm-per-prompt' \ '{"audio":1,"image":0,"video":0}' \ ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nd: - /bin/sh - '-c' args: - | pip install "vllm[audio]" && pip install qwen-omni-utils -U && \ vllm serve /mnt/models/qwen3-omni \ --host 0.0.0.0 \ --port 8000 \ '--served-model-name' \ 'qwen3-omn
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Qwen3-Omni Model Fails when try to l bug;stale ### 🐛 Describe the bug When trying to limit image/video input to 0 per prompt via `--limit-mm-per-prompt`, the engine core fails during model loading. Model: `Qwen/Q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-Omni Model Fails when try to l bug;stale ### 🐛 Describe the bug When trying to limit image/video input to 0 per prompt via `--limit-mm-per-prompt`, the engine core fails during model loading. Model: `Qwen/Q...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: logits;scheduler_memory;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency <details>

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
