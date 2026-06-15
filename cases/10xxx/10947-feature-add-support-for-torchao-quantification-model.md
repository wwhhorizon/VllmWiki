# vllm-project/vllm#10947: [Feature]: Add support for torchao quantification model

| 字段 | 值 |
| --- | --- |
| Issue | [#10947](https://github.com/vllm-project/vllm/issues/10947) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for torchao quantification model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When I use vllm to deploy a model quantified by the Torchao framework [https://huggingface.co/docs/transformers/v4.46.3/en/quantization/torchao#torchao], an error message shows that the quantization method is not supported. ` ...File "/usr/local/lib/python3.12/dist-packages/vllm/config.py", line 414, in _verify_quantization raise ValueError( ValueError: Unknown quantization method: torchao. Must be one of ['aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'fbgemm_fp8', 'modelopt', 'marlin', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'awq_marlin', 'gptq', 'compressed-tensors', 'bitsandbytes', 'qqq', 'experts_int8', 'neuron_quant', 'ipex']. ` Is there any plan to support torchao quantitative model in the future? Thanks ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Add support for torchao quantification model feature request;stale ### 🚀 The feature, motivation and pitch When I use vllm to deploy a model quantified by the Torchao framework [https://huggingface.co/docs/tr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Add support for torchao quantification model feature request;stale ### 🚀 The feature, motivation and pitch When I use vllm to deploy a model quantified by the Torchao framework [https://huggingface.co/docs/tr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: hao. Must be one of ['aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'fbgemm_fp8', 'modelopt', 'marlin', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'awq_marlin', 'gptq', 'compressed-tensors', 'bitsandbytes', 'qqq', 'expe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add support for torchao quantification model feature request;stale ### 🚀 The feature, motivation and pitch When I use vllm to deploy a model quantified by the Torchao framework [https://huggingface.co/docs/tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
