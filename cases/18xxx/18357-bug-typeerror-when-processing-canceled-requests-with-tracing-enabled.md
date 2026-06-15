# vllm-project/vllm#18357: [Bug]: TypeError When Processing Canceled Requests with Tracing Enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#18357](https://github.com/vllm-project/vllm/issues/18357) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError When Processing Canceled Requests with Tracing Enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Report: TypeError When Processing Canceled Requests with Tracing Enabled ### Your current environment **Environment:** - vLLM version: 0.8.5.post1 - Docker image: vllm/vllm-openai:latest - Hardware: 8x NVIDIA H100 GPUs ### 🐛 Describe the bug **Description:** When running vLLM with tracing enabled through the `--otlp-traces-endpoint` parameter, the engine crashes with a `TypeError` when processing a canceled request. The error occurs because the code attempts to calculate end-to-end processing time by subtracting `metrics.arrival_time` (a float) from `metrics.finished_time` (which is `None` for canceled requests). **Steps to Reproduce:** 1. Start vLLM server with tracing enabled: ```bash vllm serve /mnt/models/Qwen3-235B-A22B-FP8 --enable-reasoning --reasoning-parser deepseek_r1 --enable-expert-parallel --tensor-parallel-size 8 --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' --max-model-len 131072 --enable-prefix-caching --enable-chunked-prefill --otlp-traces-endpoint "collector.tracing.cloud.yandex.net:4317" --kv-cache-dtype fp8 --trust-remote-code --enable-server-load-tracking -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: TypeError When Processing Canceled Requests with Tracing Enabled bug;stale ### Your current environment ### 🐛 Describe the bug ## Bug Report: TypeError When Processing Canceled Requests with Tracing Enabled ### Y...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: TypeError When Processing Canceled Requests with Tracing Enabled bug;stale ### Your current environment ### 🐛 Describe the bug ## Bug Report: TypeError When Processing Canceled Requests with Tracing Enabled ### Y...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ver with tracing enabled: ```bash vllm serve /mnt/models/Qwen3-235B-A22B-FP8 --enable-reasoning --reasoning-parser deepseek_r1 --enable-expert-parallel --tensor-parallel-size 8 --rope-scaling '{"rope_type":"yarn","facto...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: .8.5.post1 - Docker image: vllm/vllm-openai:latest - Hardware: 8x NVIDIA H100 GPUs ### 🐛 Describe the bug **Description:** When running vLLM with tracing enabled through the `--otlp-traces-endpoint` parameter, the engin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ce:** 1. Start vLLM server with tracing enabled: ```bash vllm serve /mnt/models/Qwen3-235B-A22B-FP8 --enable-reasoning --reasoning-parser deepseek_r1 --enable-expert-parallel --tensor-parallel-size 8 --rope-scaling '{"r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
