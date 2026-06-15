# vllm-project/vllm#17949: [Bug]: Embedding model RoPE scaling factor always None

| 字段 | 值 |
| --- | --- |
| Issue | [#17949](https://github.com/vllm-project/vllm/issues/17949) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Embedding model RoPE scaling factor always None

### Issue 正文摘录

### Your current environment File "/usr/local/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 468, in _compute_cos_sin_cache max_len = self.max_position_embeddings * self.scaling_factor ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~ TypeError: unsupported operand type(s) for *: 'int' and 'NoneType' embedding_engine_args = AsyncEngineArgs( model=EMBEDDING_MODEL_PATH, tensor_parallel_size=1, # gpu_memory_utilization=0.90, # max_model_len=8192, enforce_eager=True, rope_scaling={"rope_type":"dynamic","factor":2.0}, # even with explicit RoPE scaling configuration trust_remote_code=True, task="embed", # Task type for embedding models ) logger.info("Configured embedding engine arguments") embedding_engine = AsyncLLMEngine.from_engine_args( embedding_engine_args, usage_context=UsageContext.OPENAI_API_SERVER ) ### 🐛 Describe the bug Loading embedding models that use DynamicNTKScalingRotaryEmbedding you get this issue. embedding.py", line 1549, in get_rope rotary_emb = DynamicNTKScalingRotaryEmbedding( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 460, in __init__ s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Embedding model RoPE scaling factor always None bug ### Your current environment File "/usr/local/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 468, in _compute_cos_sin_cache...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: rror("unsupported operand type(s) for *: 'int' and 'NoneType'") You can reproduce this issue by trying to do OpenAI-compatible embedding model with https://huggingface.co/nomic-ai/CodeRankEmbed ### Before submitting a n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rope_scaling={"rope_type":"dynamic","factor":2.0}, # even with explicit RoPE scaling configuration trust_remote_code=True, task="embed", # Task type for embedding models ) logger.info("Configured embedding engine argume...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: bed ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
