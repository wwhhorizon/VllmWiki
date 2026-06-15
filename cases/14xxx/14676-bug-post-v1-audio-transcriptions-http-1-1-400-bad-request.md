# vllm-project/vllm#14676: [Bug]: "POST /v1/audio/transcriptions HTTP/1.1" 400 Bad Request

| 字段 | 值 |
| --- | --- |
| Issue | [#14676](https://github.com/vllm-project/vllm/issues/14676) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "POST /v1/audio/transcriptions HTTP/1.1" 400 Bad Request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello I run Vllm with the following command: vllm serve --task transcription openai/whisper-large-v3-turbo --tensor-parallel-size 2 and when I try to use the API v1/audio/transcriptions in POST I systematically get a Badrequest 400 error. “object": ‘error’, “message": ‘[{’type‘: ’missing‘, ’loc‘: (’body‘, ’file‘), ’msg‘: ’Field required‘, ’input‘: {’language‘: ’fr‘, ’prompt': \“I would like the transcription of this file taking into account the fact that it is in stereo”, 'response_format': 'json', 'temperature': '0', 'timestamp_granularities[]': [], 'stream': 'false', 'stream_include_usage': 'false', 'stream_continuous_usage_stats': 'false', 'type': 'mp3'}}]”, “type": ‘BadRequestError’, “param": null, “code": 400 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;na...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: "POST /v1/audio/transcriptions HTTP/1.1" 400 Bad Request bug;stale ### Your current environment ### 🐛 Describe the bug Hello I run Vllm with the following command: vllm serve --task transcription openai/whisper-l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 400 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: this file taking into account the fact that it is in stereo”, 'response_format': 'json', 'temperature': '0', 'timestamp_granularities[]': [], 'stream': 'false', 'stream_include_usage': 'false', 'stream_continuous_usage_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
