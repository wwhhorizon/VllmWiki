# vllm-project/vllm#31889: [Bug]: KimiLinear MLA: MLAModules init missing indexer_rotary_emb

| 字段 | 值 |
| --- | --- |
| Issue | [#31889](https://github.com/vllm-project/vllm/issues/31889) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KimiLinear MLA: MLAModules init missing indexer_rotary_emb

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary After MLAModules added `indexer_rotary_emb`, KimiLinear’s MLA path still constructs MLAModules without that argument. Model init now fails with `TypeError: MLAModules.__init__() missing 1 required positional argument: 'indexer_rotary_emb'`. ## Steps to Reproduce 1. use vllm 0.12.0+ 2. Load/run a Kimi Linear model (e.g., `KimiMLAAttention` via `KimiDecoderLayer`). 3. Initialization crashes before inference starts. ## Expected Behavior Kimi Linear should initialize MLAModules successfully and run inference. ## Actual Behavior Initialization raises a TypeError because `indexer_rotary_emb` is not passed at MLAModules construction. ## Where - `vllm/model_executor/models/kimi_linear.py`: MLA setup builds `mla_modules` without `indexer_rotary_emb` (around line 247). - DeepSeek V2 already passes this arg; Kimi Linear (and possibly OpenPangu) still need it. ## Proposed Fix Pass the missing argument explicitly, mirroring DeepSeek V2: ```python mla_modules = MLAModules( kv_a_layernorm=self.kv_a_layernorm, kv_b_proj=self.kv_b_proj, rotary_emb=None, o_proj=self.o_proj, fused_qkv_a_proj=None, kv_a_proj_with_mqa=self.kv_a_proj_with_m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: . ## Where - `vllm/model_executor/models/kimi_linear.py`: MLA setup builds `mla_modules` without `indexer_rotary_emb` (around line 247). - DeepSeek V2 already passes this arg; Kimi Linear (and possibly OpenPangu) still...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 1 required positional argument: 'indexer_rotary_emb'`. ## Steps to Reproduce 1. use vllm 0.12.0+ 2. Load/run a Kimi Linear model (e.g., `KimiMLAAttention` via `KimiDecoderLayer`). 3. Initialization crashes before infere...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: oj, indexer=None, indexer_rotary_emb=None, is_sparse=False, topk_indices_buffer=None, ) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: KimiLinear’s MLA path still constructs MLAModules without that argument. Model init now fails with `TypeError: MLAModules.__init__() missing 1 required positional argument: 'indexer_rotary_emb'`. ## Steps to Reproduce 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
