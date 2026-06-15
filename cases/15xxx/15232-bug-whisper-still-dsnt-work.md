# vllm-project/vllm#15232: [Bug]: Whisper still dsnt work

| 字段 | 值 |
| --- | --- |
| Issue | [#15232](https://github.com/vllm-project/vllm/issues/15232) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Whisper still dsnt work

### Issue 正文摘录

### Your current environment I use vLLM 0.8.0. vLLM were running with next params: - "--gpu-memory-utilization=0.2" - "--kv-cache-dtype=auto" - "--dtype=bfloat16" - "--trust-remote-code" - "--max-model-len=448" - "--task=generate" And with local downloaded whisper, config.json: ``` { "_name_or_path": "openai/whisper-large-v3", "activation_dropout": 0, "activation_function": "gelu", "apply_spec_augment": false, "architectures": [ "WhisperForConditionalGeneration" ], "attention_dropout": 0, "begin_suppress_tokens": [ 220, 50257 ], "bos_token_id": 50257, "classifier_proj_size": 256, ...} ``` ### 🐛 Describe the bug Transcription doesnt work, in swagger i got next error: ``` { "object": "error", "message": "[{'type': 'missing', 'loc': ('body', 'file'), 'msg': 'Field required', 'input': {'prompt': '', 'response_format': 'json', 'temperature': 0.0, 'timestamp_granularities[]': [], 'stream': False, 'stream_include_usage': False, 'stream_continuous_usage_stats': False, '------WebKitFormBoundary4AwfFv2uoX6Blo79\\r\\nContent-Disposition: form-data; name': '\"stream\"\\r\\n\\r\\nfalse\\r\\n------WebKitFormBoundary4AwfFv2uoX6Blo79\\r\\nContent-Disposition: form-data; name=\"prompt\"\\r\\n\\r\\...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ith next params: - "--gpu-memory-utilization=0.2" - "--kv-cache-dtype=auto" - "--dtype=bfloat16" - "--trust-remote-code" - "--max-model-len=448" - "--task=generate" And with local downloaded whisper, config.json: ``` {...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: =auto" - "--dtype=bfloat16" - "--trust-remote-code" - "--max-model-len=448" - "--task=generate" And with local downloaded whisper, config.json: ``` { "_name_or_path": "openai/whisper-large-v3", "activation_dropout": 0,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Whisper still dsnt work bug;stale ### Your current environment I use vLLM 0.8.0. vLLM were running with next params: - "--gpu-memory-utilization=0.2" - "--kv-cache-dtype=auto" - "--dtype=bfloat16" - "--trust-remo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ": 0, "activation_function": "gelu", "apply_spec_augment": false, "architectures": [ "WhisperForConditionalGeneration" ], "attention_dropout": 0, "begin_suppress_tokens": [ 220, 50257 ], "bos_token_id": 50257, "classifi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: running with next params: - "--gpu-memory-utilization=0.2" - "--kv-cache-dtype=auto" - "--dtype=bfloat16" - "--trust-remote-code" - "--max-model-len=448" - "--task=generate" And with local downloaded whisper, config.jso...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
