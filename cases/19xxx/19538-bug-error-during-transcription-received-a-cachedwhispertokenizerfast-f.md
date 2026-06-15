# vllm-project/vllm#19538: [Bug]: Error during transcription: Received a CachedWhisperTokenizerFast for argument tokenizer, but a WhisperTokenizer was expected.

| 字段 | 值 |
| --- | --- |
| Issue | [#19538](https://github.com/vllm-project/vllm/issues/19538) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;quantization;sampling |
| 症状 | nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error during transcription: Received a CachedWhisperTokenizerFast for argument tokenizer, but a WhisperTokenizer was expected.

### Issue 正文摘录

I have a simple inferencing script available on vLLM github repo to transcript audio file using vLLM-wrapped Whisper. Getting this issue even if I run on vanilla Whisper-models which seemed to work before. ``` INFO 06-12 08:26:56 [config.py:823] This model supports multiple tasks: {'generate', 'embed', 'score', 'reward', 'classify', 'transcription'}. Defaulting to 'transcription'. INFO 06-12 08:26:56 [config.py:3268] Downcasting torch.float32 to torch.bfloat16. INFO 06-12 08:26:56 [config.py:1559] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor WARNING 06-12 08:26:56 [cuda.py:91] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used INFO 06-12 08:26:56 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.1) with config: model='whisper-medium', speculative_config=None, tokenizer='whisper-medium', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=448, downlo...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: 'transcription'. INFO 06-12 08:26:56 [config.py:3268] Downcasting torch.float32 to torch.bfloat16. INFO 06-12 08:26:56 [config.py:1559] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boos...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: rFast for argument tokenizer, but a WhisperTokenizer was expected. usage;stale I have a simple inferencing script available on vLLM github repo to transcript audio file using vLLM-wrapped Whisper. Getting this issue eve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: but a WhisperTokenizer was expected. usage;stale I have a simple inferencing script available on vLLM github repo to transcript audio file using vLLM-wrapped Whisper. Getting this issue even if I run on vanilla Whisper-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: LLM-wrapped Whisper. Getting this issue even if I run on vanilla Whisper-models which seemed to work before. ``` INFO 06-12 08:26:56 [config.py:823] This model supports multiple tasks: {'generate', 'embed', 'score', 're...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor WARNING 06-12 08:26:56 [cuda.py:91] To see benefits of async output processing, enable CUDA graph. S...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
