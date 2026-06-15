# vllm-project/vllm#3488: [Bug]: DynamicNTKScalingRotaryEmbedding implementation is different from Transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#3488](https://github.com/vllm-project/vllm/issues/3488) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DynamicNTKScalingRotaryEmbedding implementation is different from Transformers

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug There is a difference in the vLLM implementation of DynamicNTKScalingRotaryEmbedding from the Transformer implementation that causes performance degradation for inputs that fit into the _original context length_. Specifically, the Transformer implementation initializes the base for the Rope embedding with the original max_position_embeddings and re-computes the base for inputs that surpass the original max_position_embeddings (hence the name _dynamic_), as detailed below. ```python # taken from https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/modeling_llama.py#L158 class LlamaDynamicNTKScalingRotaryEmbedding(LlamaRotaryEmbedding): """LlamaRotaryEmbedding extended with Dynamic NTK scaling. Credits to the Reddit users /u/bloc97 and /u/emozilla""" def forward(self, x, position_ids): # difference to the original RoPE: inv_freq is recomputed when the sequence length > original length seq_len = torch.max(position_ids) + 1 if seq_len > self.max_position_embeddings: base = self.base * ( (self.scaling_factor * seq_len / self.max_position_embeddings) - (se...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _dynamic_), as detailed below. ```python # taken from https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/modeling_llama.py#L158 class LlamaDynamicNTKScalingRotaryEmbedding(LlamaRotaryEmb...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: degradation for inputs that fit into the _original context length_. Specifically, the Transformer implementation initializes the base for the Rope embedding with the original max_position_embeddings and re-computes the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: inv_freq = 1.0 / ( base ** (torch.arange(0, self.dim, 2, dtype=torch.int64).float().to(x.device) / self.dim) ) self.register_buffer("inv_freq", inv_freq, persistent=False) # TODO joao: this may break with compilation co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: of the input, as detailed below. This means that for inputs with lengths smaller than the original context length, the outputs from pre-/post-rope scaling will differ, sometimes by large amounts. ```python # taken from...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ) self.register_buffer("inv_freq", inv_freq, persistent=False) # TODO joao: this may break with compilation cos, sin = super().forward(x, position_ids) return cos, sin ``` In contrast, the vLLM implementation initialize...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
