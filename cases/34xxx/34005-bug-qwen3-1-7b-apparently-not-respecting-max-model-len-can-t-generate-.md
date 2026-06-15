# vllm-project/vllm#34005: [Bug]: Qwen3-1.7B apparently not respecting max-model-len (can't generate >2048 tokens)

| 字段 | 值 |
| --- | --- |
| Issue | [#34005](https://github.com/vllm-project/vllm/issues/34005) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-1.7B apparently not respecting max-model-len (can't generate >2048 tokens)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, there seems to be a bug with using max-model-len for some models, such as Qwen/Qwen3-1.7B-Base. While I set the max-model-len to be quite high, whenever a generation reaches 2048, it is automatically cut off in a seemingly silent failure. For example: Starting my server with: `vllm serve Qwen/Qwen3-1.7B-Base --host 0.0.0.0 --max-model-len 24000 --chat-template '{% for message in messages %}{{ message.content }}{% endfor %}' --tensor-parallel-size 2 --port 32056` after I hit the server with a request, the completion tokens is 2048 and seemingly ends mid-response. However, when I use the same command but for `Qwen/Qwen3-1.7B`, the completion tokens is able to exceed 2048 no problem. I'm not sure why this is happening, can you please help debug? Thanks! BTW, I get this server output when using serving the base model, if it helps: ``` (APIServer pid=114089) INFO 02-06 16:45:47 [utils.py:325] (APIServer pid=114089) INFO 02-06 16:45:47 [utils.py:325] █ █ █▄ ▄█ (APIServer pid=114089) INFO 02-06 16:45:47 [utils.py:325] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.1 (APIServer pid=114089) INFO 02-06 16:45:47 [utils.py:325] █▄█▀ █ █ █ █ model Qwen/Q...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: }' --tensor-parallel-size 2 --port 32056` after I hit the server with a request, the completion tokens is 2048 and seemingly ends mid-response. However, when I use the same command but for `Qwen/Qwen3-1.7B`, the complet...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d=114089) INFO 02-06 16:45:47 [utils.py:325] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.1 (APIServer pid=114089) INFO 02-06 16:45:47 [utils.py:325] █▄█▀ █ █ █ █ model Qwen/Qwen3-1.7B-Base (APIServer pid=114089) INFO 02-06 16:45:47...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=24000, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-1.7B apparently not respecting max-model-len (can't generate >2048 tokens) bug ### Your current environment ### 🐛 Describe the bug Hi, there seems to be a bug with using max-model-len for some models, such...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
