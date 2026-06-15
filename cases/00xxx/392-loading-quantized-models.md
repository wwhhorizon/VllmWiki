# vllm-project/vllm#392: Loading quantized models

| 字段 | 值 |
| --- | --- |
| Issue | [#392](https://github.com/vllm-project/vllm/issues/392) |
| 状态 | closed |
| 标签 |  |
| 评论 | 31; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Loading quantized models

### Issue 正文摘录

Hi, Is there a way to load quantized models using `vLLM`? For e.g. I have been using [AWQ quantization](https://github.com/mit-han-lab/llm-awq) and have released a few models [here](https://huggingface.co/abhinavkulkarni). The model loading process looks like the following: 1. Model is first initialized with empty weights 2. Linear layers are replaced by a custom linear layer that supports zero-point quantization 3. Weights are loaded from a checkpoint onto a GPU Please note the matrix multiplication inside the linear layer is done by a Python extension that uses custom CUDA kernels since AWQ uses 4-bit quantization. Everything else - the attention mechanism, etc. is the same. The model otherwise supports all the HuggingFace `AutoModelForCausalLM` APIs. Thanks!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n inside the linear layer is done by a Python extension that uses custom CUDA kernels since AWQ uses 4-bit quantization. Everything else - the attention mechanism, etc. is the same. The model otherwise supports all the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Loading quantized models Hi, Is there a way to load quantized models using `vLLM`? For e.g. I have been using [AWQ quantization](https://github.com/mit-han-lab/llm-awq) and have released a few models [here](https://hugg...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Loading quantized models Hi, Is there a way to load quantized models using `vLLM`? For e.g. I have been using [AWQ quantization](https://github.com/mit-han-lab/llm-awq) and have released a few models [here](https://hugg...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: uses custom CUDA kernels since AWQ uses 4-bit quantization. Everything else - the attention mechanism, etc. is the same. The model otherwise supports all the HuggingFace `AutoModelForCausalLM` APIs. Thanks!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
