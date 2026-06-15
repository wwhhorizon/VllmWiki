# vllm-project/vllm#18075: [New Model]: Multi-channel TTS Model: Speech Embeddings Inconsistent in vllm with Sequence Inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#18075](https://github.com/vllm-project/vllm/issues/18075) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [New Model]: Multi-channel TTS Model: Speech Embeddings Inconsistent in vllm with Sequence Inputs

### Issue 正文摘录

### The model to consider. a new TTS model built by myself ### The closest model vllm already supports. Qwen2.5 ### What's your difficulty of supporting the model you want? # Issue Description When porting my custom multi-channel TTS model to vllm framework (v0.5.3post1), I've encountered a specific inconsistency: with single token inputs, all model layer outputs match the HuggingFace implementation perfectly. However, with sequence inputs, the speech channel embeddings (channels 1-7) produce significantly different outputs, causing generation errors. # Implementation Details My TTS model architecture includes multiple parallel channels: Channel 0: Processes text tokens (vocabulary size: config.vocab_size) Channels 1-7: Process speech feature tokens (vocabulary size: config.speech_vocab_size) ## HuggingFace Implementation ``` # Channel 0: Text embedding self.embedding_list.append(nn.Embedding(config.vocab_size, config.hidden_size, self.text_pad_idx)) # Channels 1-7: Speech embeddings for _ in range(1, config.channels): self.embedding_list.append(nn.Embedding(config.speech_vocab_size, config.hidden_size, self.speech_pad_idx)) # Embedding computation process def _prepare_multi_modal...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [New Model]: Multi-channel TTS Model: Speech Embeddings Inconsistent in vllm with Sequence Inputs stale ### The model to consider. a new TTS model built by myself ### The closest model vllm already supports. Qwen2.5 ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: channel TTS model to vllm framework (v0.5.3post1), I've encountered a specific inconsistency: with single token inputs, all model layer outputs match the HuggingFace implementation perfectly. However, with sequence inpu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tputs, causing generation errors. # Implementation Details My TTS model architecture includes multiple parallel channels: Channel 0: Processes text tokens (vocabulary size: config.vocab_size) Channels 1-7: Process speec...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: puts, the speech channel embeddings (channels 1-7) produce significantly different outputs, causing generation errors. # Implementation Details My TTS model architecture includes multiple parallel channels: Channel 0: P...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: device=input_ids.device, dtype=self.embedding_list[0].weight.dtype) # Accumulate all channels starting from zero for i in range(channels): embed_layer = self.embedding_list[i] channel_input = input_ids[...,i] inpu

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
