# vllm-project/vllm#39163: [Bug]: First request after startup is unexpectedly slow with Qwen3.5-27B-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#39163](https://github.com/vllm-project/vllm/issues/39163) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: First request after startup is unexpectedly slow with Qwen3.5-27B-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The first request after healthy startup has TTFT around `43 s`, while the second and later requests are normal. I reproduced this with `vllm/vllm-openai:v0.19.0-cu130` serving `Qwen/Qwen3.5-27B-FP8` on a single `NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition` GPU with driver `580.95.05`. This does not look like normal startup spillover because: - `/health` is already `200` before the first request - the engine is awake - `prefix_cache_hits_total=0` - queue time is effectively zero - the delay is almost entirely first-request prefill time ### How to reproduce? Start the server like this: The arguments below are adapted from the official Qwen3.5 recipe to match this single-GPU reproduction: ```bash docker run --rm --gpus '"device=0"' \ -p 8002:8000 \ -e VLLM_LOGGING_LEVEL=INFO \ -e VLLM_NO_USAGE_STATS=1 \ vllm/vllm-openai:v0.19.0-cu130 \ vllm serve Qwen/Qwen3.5-27B-FP8 \ --served-model-name Qwen3.5-27B-FP8 \ --tensor-parallel-size 1 \ --trust-remote-code \ --gpu-memory-utilization 0.95 \ --max-model-len 128000 \ --reasoning-parser qwen3 \ --enable-prefix-caching \ --mm-encoder-tp-mode data \ --mm-processor-cache-type shm \...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tart the server like this: The arguments below are adapted from the official Qwen3.5 recipe to match this single-GPU reproduction: ```bash docker run --rm --gpus '"device=0"' \ -p 8002:8000 \ -e VLLM_LOGGING_LEVEL=INFO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: openai:v0.19.0-cu130` serving `Qwen/Qwen3.5-27B-FP8` on a single `NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition` GPU with driver `580.95.05`. This does not look like normal startup spillover because: - `/healt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: First request after startup is unexpectedly slow with Qwen3.5-27B-FP8 bug ### Your current environment ### 🐛 Describe the bug The first request after healthy startup has TTFT around `43 s`, while the second and l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: First request after startup is unexpectedly slow with Qwen3.5-27B-FP8 bug ### Your current environment ### 🐛 Describe the bug The first request after healthy startup has TTFT around `43 s`, while the second and l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: First request after startup is unexpectedly slow with Qwen3.5-27B-FP8 bug ### Your current environment ### 🐛 Describe the bug The first request after healthy startup has TTFT around `43 s`, while the second and l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
