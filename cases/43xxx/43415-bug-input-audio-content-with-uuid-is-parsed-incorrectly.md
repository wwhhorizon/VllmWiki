# vllm-project/vllm#43415: [Bug]: input_audio content with uuid is parsed incorrectly

| 字段 | 值 |
| --- | --- |
| Issue | [#43415](https://github.com/vllm-project/vllm/issues/43415) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: input_audio content with uuid is parsed incorrectly

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When a request to the OpenAI-compatible `/v1/chat/completions` endpoint contains an `input_audio` content part with a `uuid`, vLLM returns HTTP 500: ```text AssertionError: Expected code to be unreachable, but got: None ``` This happens because the `uuid` case enters the multimodal compatibility parsing path. In that path, vLLM passes the whole content part to the audio parser instead of the nested `input_audio` object. Current behavior: ```python input_audio_params = cast(dict[str, str], part) ``` Expected behavior: ```python input_audio_params = cast(InputAudio, part["input_audio"]) ``` The non-uuid `input_audio` path already returns `part["input_audio"]`, so the uuid path should use the same payload shape. ### Minimal Reproducible Example Send this request to `/v1/chat/completions`: ```json { "model": "gemma-4-E2B-it", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "Please describe this audio in one sentence." }, { "type": "input_audio", "input_audio": { "data": " ", "format": "wav" }, "uuid": "audio-smoke-uuid-001" } ] } ], "max_tokens": 16, "temperature": 0 } ``` The key part is that the same `input_a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: able, but got: None ``` This happens because the `uuid` case enters the multimodal compatibility parsing path. In that path, vLLM passes the whole content part to the audio parser instead of the nested `input_audio` obj...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: so the uuid path should use the same payload shape. ### Minimal Reproducible Example Send this request to `/v1/chat/completions`: ```json { "model": "gemma-4-E2B-it", "messages": [ { "role": "user", "content": [ { "type...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : " ", "format": "wav" }, "uuid": "audio-smoke-uuid-001" } ] } ], "max_tokens": 16, "temperature": 0 } ``` The key part is that the same `input_audio` content part carries a `uuid`: ```json { "type": "input_audio", "inp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d_api;hardware_porting;model_support;multimodal_vlm;sampling_logits cuda;triton build_error env_dependency;shape Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: dio"]`, so the uuid path should use the same payload shape. ### Minimal Reproducible Example Send this request to `/v1/chat/completions`: ```json { "model": "gemma-4-E2B-it", "messages": [ { "role": "user", "content": [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
