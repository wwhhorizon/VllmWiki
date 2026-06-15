# vllm-project/vllm#37400: [Bug]: JAIS: ALiBi is applied even when position_embedding_type="learned"

| 字段 | 值 |
| --- | --- |
| Issue | [#37400](https://github.com/vllm-project/vllm/issues/37400) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: JAIS: ALiBi is applied even when position_embedding_type="learned"

### Issue 正文摘录

### Your current environment None ### 🐛 Describe the bug ### Bug description In `vllm/model_executor/models/jais.py`, ALiBi appears to be constructed and passed into `Attention(...)` unconditionally: ```python alibi_slopes = _get_alibi_slopes(total_num_heads) self.attn = Attention(..., alibi_slopes=alibi_slopes) ``` At the same time, JAISModel still uses learned positional embeddings (wpe) when config.position_embedding_type == "learned". This means that for JAIS configs/checkpoints using learned positional embeddings, vLLM applies both: 1. learned positional embeddings via wpe 2. ALiBi bias in attention That looks like double positional encoding. ### Expected behavior ALiBi and learned positional embeddings should be mutually exclusive, following config.position_embedding_type. If position_embedding_type == "alibi", passing alibi_slopes is correct. If position_embedding_type == "learned", ALiBi should not be enabled in attention. ### Why this matters This likely produces incorrect attention behavior for JAIS variants configured with learned positional embeddings. From what I checked, standard public JAIS checkpoints seem to use position_embedding_type="alibi", so this may not aff...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: = Attention(..., alibi_slopes=alibi_slopes) ``` At the same time, JAISModel still uses learned positional embeddings (wpe) when config.position_embedding_type == "learned". This means that for JAIS configs/checkpoints u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ironment None ### 🐛 Describe the bug ### Bug description In `vllm/model_executor/models/jais.py`, ALiBi appears to be constructed and passed into `Attention(...)` unconditionally: ```python alibi_slopes = _get_alibi_slo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
