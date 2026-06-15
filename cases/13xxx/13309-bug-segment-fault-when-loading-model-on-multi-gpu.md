# vllm-project/vllm#13309: [Bug]: Segment fault when loading model on multi-gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#13309](https://github.com/vllm-project/vllm/issues/13309) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Segment fault when loading model on multi-gpu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Fails when loading model on multi-gpu with `Segmentation fault` ```text INFO 02-14 22:25:47 config.py:131] Replacing legacy 'type' key with 'rope_type' INFO 02-14 22:25:51 config.py:510] This model supports multiple tasks: {'embed', 'generate', 'classify', 'reward', 'score'}. Defaulting to 'generate'. WARNING 02-14 22:25:52 config.py:601] CUDA graph is not supported for Deepseek V3 yet, fallback to the eager mode. INFO 02-14 22:25:52 config.py:1310] Defaulting to use mp for distributed inference WARNING 02-14 22:25:52 cuda.py:98] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used WARNING 02-14 22:25:52 config.py:642] Async output processing is not supported on the current platform type cuda. WARNING 02-14 22:25:52 fp8.py:52] Detected fp8 checkpoint. Please note that the format is experimental and subject to change. INFO 02-14 22:25:52 llm_engine.py:234] Initializing an LLM engine (v0.6.6) with config: model='deepseek-ai_DeepSeek-R1/', speculative_config=None, tokenizer='deepseek-ai_DeepSeek-R1/', skip_tokenizer_init=False, tokenizer_mode=auto, revi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: h `Segmentation fault` ```text INFO 02-14 22:25:47 config.py:131] Replacing legacy 'type' key with 'rope_type' INFO 02-14 22:25:51 config.py:510] This model supports multiple tasks: {'embed', 'generate', 'classify', 're...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: not supported on the current platform type cuda. WARNING 02-14 22:25:52 fp8.py:52] Detected fp8 checkpoint. Please note that the format is experimental and subject to change. INFO 02-14 22:25:52 llm_engine.py:234] Initi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Segment fault when loading model on multi-gpu bug;stale ### Your current environment ### 🐛 Describe the bug Fails when loading model on multi-gpu with `Segmentation fault` ```text INFO 02-14 22:25:47 config.py:13...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 22:25:52 config.py:601] CUDA graph is not supported for Deepseek V3 yet, fallback to the eager mode. INFO 02-14 22:25:52 config.py:1310] Defaulting to use mp for distributed inference WARNING 02-14 22:25:52 cuda.py:98]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: score'}. Defaulting to 'generate'. WARNING 02-14 22:25:52 config.py:601] CUDA graph is not supported for Deepseek V3 yet, fallback to the eager mode. INFO 02-14 22:25:52 config.py:1310] Defaulting to use mp for distribu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
