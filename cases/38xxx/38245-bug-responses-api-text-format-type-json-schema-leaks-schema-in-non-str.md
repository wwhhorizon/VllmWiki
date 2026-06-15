# vllm-project/vllm#38245: [Bug]: Responses API `text.format.type="json_schema"` leaks `schema_` in non-stream responses and breaks streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#38245](https://github.com/vllm-project/vllm/issues/38245) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Responses API `text.format.type="json_schema"` leaks `schema_` in non-stream responses and breaks streaming

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The `/v1/responses` endpoint appears to mishandle `text.format.type="json_schema"`. Using vLLM v0.18.0, using model `Qwen/Qwen3.5-9B`. Observed behavior: - `text.format.type="json_object"` works in both non-stream and stream mode. - `text.format.type="json_schema"`: - non-stream returns `200 OK`, but the response body uses `text.format.schema_` instead of `text.format.schema` - stream starts with `200 OK`, then the connection closes before a complete SSE body is sent This looks like a Responses serialization bug rather than a model-output issue. ### Minimal repro Server launch: ```bash vllm serve Qwen/Qwen3.5-9B \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser qwen3 \ --host 0.0.0.0 \ --port 9876 \ --enable-prefix-caching ``` Case: `json_schema`, non-stream ```bash curl -sS -D - http://192.168.80.2:9876/v1/responses \ -H 'Content-Type: application/json' \ --data-binary @- <<'JSON' {"model":"Qwen/Qwen3.5-9B","input":"return object with x=1","stream":false,"text":{"format":{"type":"json_schema","name":"tool_calling_response_format","schema":{"type":"object","properties":{"x":{"type":"integer"}},"req...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Responses API `text.format.type="json_schema"` leaks `schema_` in non-stream responses and breaks streaming bug ### Your current environment ### 🐛 Describe the bug The `/v1/responses` endpoint appears to mishandl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_deco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lly ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: l;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency Your current...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
