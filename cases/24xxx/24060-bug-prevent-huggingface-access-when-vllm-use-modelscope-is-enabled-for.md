# vllm-project/vllm#24060: [Bug]: prevent HuggingFace access when VLLM_USE_MODELSCOPE is enabled for gpt-oss-20b

| 字段 | 值 |
| --- | --- |
| Issue | [#24060](https://github.com/vllm-project/vllm/issues/24060) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: prevent HuggingFace access when VLLM_USE_MODELSCOPE is enabled for gpt-oss-20b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When VLLM_USE_MODELSCOPE =true is set, the system was still making calls to HuggingFace endpoints during model configuration loading, which could lead to Network access issues in environments where HuggingFace is blocked To reproduce the error: ``` # HF_ENDPOINT=http://127.0.0.1 VLLM_USE_MODELSCOPE=true VLLM_USE_V1=1 vllm serve openai-mirror/gpt-oss-20b (APIServer pid=2468433) ERROR 09-02 01:27:54 [config.py:124] Error retrieving safetensors: (MaxRetryError("HTTPConnectionPool(host='127.0.0.1', port=80): Max retries exceeded with url: /openai-mirror/gpt-oss-20b/resolve/main/model.safetensors (Caused by NewConnectionError(' : Failed to establish a new connection: [Errno 111] Connection refused'))"), '(Request ID: 208e9bd0-8df9-40a2-91d4-a05d5561fd68)'), retrying 1 of 2 (APIServer pid=2468433) ERROR 09-02 01:27:56 [config.py:122] Error retrieving safetensors: (MaxRetryError("HTTPConnectionPool(host='127.0.0.1', port=80): Max retries exceeded with url: /openai-mirror/gpt-oss-20b/resolve/main/model.safetensors (Caused by NewConnectionError(' : Failed to establish a new connection: [ ``` However, if you run `HF_ENDPOINT=http://127.0.0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: prevent HuggingFace access when VLLM_USE_MODELSCOPE is enabled for gpt-oss-20b bug;stale ### Your current environment ### 🐛 Describe the bug When VLLM_USE_MODELSCOPE =true is set, the system was still making call...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ggingFace access when VLLM_USE_MODELSCOPE is enabled for gpt-oss-20b bug;stale ### Your current environment ### 🐛 Describe the bug When VLLM_USE_MODELSCOPE =true is set, the system was still making calls to HuggingFace...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ur. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
