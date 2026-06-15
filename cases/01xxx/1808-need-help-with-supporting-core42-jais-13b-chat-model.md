# vllm-project/vllm#1808: Need help with supporting "core42/jais-13b-chat" model

| 字段 | 值 |
| --- | --- |
| Issue | [#1808](https://github.com/vllm-project/vllm/issues/1808) |
| 状态 | closed |
| 标签 |  |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Need help with supporting "core42/jais-13b-chat" model

### Issue 正文摘录

Hello Team, I am attempting to add support for "core42/jais-13b-chat" model for vLLM. I have completed most of the required changes except for `AliBi embeddings`. This is how the model looks like if loaded with HF: ``` JAISLMHeadModel( (transformer): JAISModel( (wte): Embedding(84992, 5120) (drop): Dropout(p=0.0, inplace=False) (h): ModuleList( (0-39): 40 x JAISBlock( (ln_1): LayerNorm((5120,), eps=1e-05, elementwise_affine=True) (attn): JAISAttention( (c_attn): Conv1D() (c_proj): Conv1D() (attn_dropout): Dropout(p=0.0, inplace=False) (resid_dropout): Dropout(p=0.0, inplace=False) ) (ln_2): LayerNorm((5120,), eps=1e-05, elementwise_affine=True) (mlp): JAISMLP( (c_fc): Conv1D() (c_fc2): Conv1D() (c_proj): Conv1D() (act): SwiGLUActivation() (dropout): Dropout(p=0.0, inplace=False) ) ) ) (ln_f): LayerNorm((5120,), eps=1e-05, elementwise_affine=True) (relative_pe): AlibiPositionEmbeddingLayer() ) (lm_head): Linear(in_features=5120, out_features=84992, bias=False) ) ``` and this is how it looks after I made the necessary changes for vLLM 0.2.1-post1: ``` JAISLMHeadModel( (transformer): JAISModel( (wte): VocabParallelEmbedding() (h): ModuleList( (0-39): 40 x JAISBlock( (ln_1): LayerNorm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Need help with supporting "core42/jais-13b-chat" model Hello Team, I am attempting to add support for "core42/jais-13b-chat" model for vLLM. I have completed most of the required changes except for `AliBi embeddings`. T...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ( (wte): Embedding(84992, 5120) (drop): Dropout(p=0.0, inplace=False) (h): ModuleList( (0-39): 40 x JAISBlock( (ln_1): LayerNorm((5120,), eps=1e-05, elementwise_affine=True) (attn): JAISAttention( (c_attn): Conv1D() (c_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: looks like if loaded with HF: ``` JAISLMHeadModel( (transformer): JAISModel( (wte): Embedding(84992, 5120) (drop): Dropout(p=0.0, inplace=False) (h): ModuleList( (0-39): 40 x JAISBlock( (ln_1): LayerNorm((5120,), eps=1e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
