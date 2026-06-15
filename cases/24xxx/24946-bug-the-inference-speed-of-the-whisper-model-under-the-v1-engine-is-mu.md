# vllm-project/vllm#24946: [Bug]: The inference speed of the whisper model under the v1 engine is much slower than v0

| 字段 | 值 |
| --- | --- |
| Issue | [#24946](https://github.com/vllm-project/vllm/issues/24946) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The inference speed of the whisper model under the v1 engine is much slower than v0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using vllm 0.10.2(cuda12.8.1), my device is nvidia A5000, and I use the following command to start server ```bash VLLM_MAX_AUDIO_CLIP_FILESIZE_MB=100 \ vllm serve models/whisper-large-v3 \ --served-model-name whisper-large-v3 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --host 0.0.0.0 --port 21002 ``` I test whisper-large-v3 and whisper-large-v3-turbo, both of them are super slow than v0 engine. The table below shows the approximate speeds（token/s displayed in vllm logs） v0 is test on vllm `0.10.1.1-cuda12.8.1`, v1 is test on vllm `0.10.2-cuda12.8.1` model| v0| v1 -- | -- | -- whisper-large-v3 | 60-70 | 4-5 whisper-large-v3-turbo | 135 | 22-25 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#24989 [Core] Get num_encoder_tokens from scheduler config

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ur current environment ### 🐛 Describe the bug I'm using vllm 0.10.2(cuda12.8.1), my device is nvidia A5000, and I use the following command to start server ```bash VLLM_MAX_AUDIO_CLIP_FILESIZE_MB=100 \ vllm serve models...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The inference speed of the whisper model under the v1 engine is much slower than v0 bug ### Your current environment ### 🐛 Describe the bug I'm using vllm 0.10.2(cuda12.8.1), my device is nvidia A5000, and I use...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency #24989 [Core] Get num_encoder_tokens from scheduler...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency #24989 [Core] Get num_encoder_tokens from scheduler config Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24989](https://github.com/vllm-project/vllm/pull/24989) | mentioned | 0.6 | [Core] Get num_encoder_tokens from scheduler config | scheduler, kv cache manager, and gpu model runner. Related to issue #24946. Signed-off-by: Russell Bryant <rbryant@redhat.com> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
