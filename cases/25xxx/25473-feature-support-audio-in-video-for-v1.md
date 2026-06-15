# vllm-project/vllm#25473: [Feature]: Support `audio_in_video` for V1

| 字段 | 值 |
| --- | --- |
| Issue | [#25473](https://github.com/vllm-project/vllm/issues/25473) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support `audio_in_video` for V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When testing a single video with audio using only_thinker.py, I encountered the following error: use_audio_in_video,enforce_eager=False use_audio_in_video,enforce_eager=True ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#27721 [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1 engine.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency #27721 [Multimodal][Qwen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency #27721 [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency #27721 [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1 engine. Your current envir...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , I encountered the following error: use_audio_in_video,enforce_eager=False use_audio_in_video,enforce_eager=True ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27721](https://github.com/vllm-project/vllm/pull/27721) | closes_keyword | 0.95 | [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1 engine.   | CLOSE #25473 CLOSE https://github.com/vllm-project/vllm/issues/28046 ## Test Plan ``` HF_HUB_DISABLE_XET=1 VLLM_ATTENTION_BACKEND=TORCH_SDPA python examples/offline_inference/qwen |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
