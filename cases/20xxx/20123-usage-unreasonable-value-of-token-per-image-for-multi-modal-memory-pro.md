# vllm-project/vllm#20123: [Usage]: Unreasonable value of token per image for multi-modal memory profiling

| 字段 | 值 |
| --- | --- |
| Issue | [#20123](https://github.com/vllm-project/vllm/issues/20123) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Unreasonable value of token per image for multi-modal memory profiling

### Issue 正文摘录

### Your current environment Run the official [demo script](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language.py) for using Qwen 2.5 VL 3B. When specifying `limit_mm_per_prompt={"image": 1}`, I got ``` WARNING 06-26 07:12:07 [profiling.py:245] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 5120) is too short to hold the multi-modal embeddings in the worst case (32768 tokens in total, out of which {'image': 16384, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`. ``` Where does this (approx.) 16384 tokens per image come from?? If I remember correctly, Qwen 2.5 VL uses 28*28 patch for an image token. `16384*28*28` is an image `3584*3584` image. This is an extremely unreasonbaly large size for VL LLM use cases. This very large hard-coded value blocks me from using multiple images as it will cause OOM _**during memory profiling**_. But it's acutally ok during inference since I can resize my images. How c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: /vllm/blob/main/examples/offline_inference/vision_language.py) for using Qwen 2.5 VL 3B. When specifying `limit_mm_per_prompt={"image": 1}`, I got ``` WARNING 06-26 07:12:07 [profiling.py:245] The sequence length used f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: Unreasonable value of token per image for multi-modal memory profiling usage ### Your current environment Run the official [demo script](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: i-modal memory profiling usage ### Your current environment Run the official [demo script](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language.py) for using Qwen 2.5 VL 3B. When spe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: age ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e hard-coded value blocks me from using multiple images as it will cause OOM _**during memory profiling**_. But it's acutally ok during inference since I can resize my images. How can I set it by myself? ### How would y...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
