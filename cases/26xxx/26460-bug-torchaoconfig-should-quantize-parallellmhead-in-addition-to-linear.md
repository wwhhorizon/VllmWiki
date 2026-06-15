# vllm-project/vllm#26460: [Bug]: TorchAOConfig should quantize ParallelLMHead in addition to LinearBase

| 字段 | 值 |
| --- | --- |
| Issue | [#26460](https://github.com/vllm-project/vllm/issues/26460) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TorchAOConfig should quantize ParallelLMHead in addition to LinearBase

### Issue 正文摘录

### Problem In Qwen3-8B, `model.lm_head` is a `ParallelLMHead`, which looks like an embedding layer but is actually a linear layer: https://github.com/vllm-project/vllm/blob/467a4f98f17b74b620963d6032c0e457900f8c8a/vllm/model_executor/models/qwen3.py#L289 (See the transformers [definition](https://github.com/huggingface/transformers/blob/7aa888b7fa477d13153ffbfe107dfbd6c696014a/src/transformers/models/qwen3/modeling_qwen3.py#L435 ) for more details) When we try to load a quantized checkpoint, we end up trying to `copy_` a quantized tensor into a bf16 tensor. For `NVFP4Tensor` this results in the following error: ``` File "/home/andrewor/local/ao/torchao/prototype/mx_formats/nvfp4_tensor.py", line 338, in nvfp4_copy_ if NVFP4Tensor._same_metadata(self, src): File "/home/andrewor/local/ao/torchao/prototype/mx_formats/nvfp4_tensor.py", line 268, in _same_metadata self._per_tensor_scale is None and src._per_tensor_scale is None ``` ### Cause Today we only quantize `LinearBase` and ignore all other layers, including `ParallelLMHead`: https://github.com/vllm-project/vllm/blob/467a4f98f17b74b620963d6032c0e457900f8c8a/vllm/model_executor/layers/quantization/torchao.py#L184 ### Simple fix...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: TorchAOConfig should quantize ParallelLMHead in addition to LinearBase bug ### Problem In Qwen3-8B, `model.lm_head` is a `ParallelLMHead`, which looks like an embedding layer but is actually a linear layer: https...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: TorchAOConfig should quantize ParallelLMHead in addition to LinearBase bug ### Problem In Qwen3-8B, `model.lm_head` is a `ParallelLMHead`, which looks like an embedding layer but is actually a linear layer: https...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ats/nvfp4_tensor.py", line 338, in nvfp4_copy_ if NVFP4Tensor._same_metadata(self, src): File "/home/andrewor/local/ao/torchao/prototype/mx_formats/nvfp4_tensor.py", line 268, in _same_metadata self._per_tensor_scale is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
