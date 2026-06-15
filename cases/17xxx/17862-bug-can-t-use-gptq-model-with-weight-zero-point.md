# vllm-project/vllm#17862: [Bug]: Can't use GPTQ model with weight_zero_point

| 字段 | 值 |
| --- | --- |
| Issue | [#17862](https://github.com/vllm-project/vllm/issues/17862) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can't use GPTQ model with weight_zero_point

### Issue 正文摘录

### Your current environment commit a8238bbdb086d2e25a6c1a16b3438e0ffeb0de89 ### 🐛 Describe the bug I found that in vLLM, the shape of qzeros in GPTQ has been divided by pack_factor (as shown in the code snippet below). However, some GPTQ models (e.g., https://huggingface.co/SpiridonSunRotator/DeepSeek-V3-0324-GPTQ-4b-128g/) have the same shape and dtype for weight_zero_point and weight_scale, which can cause a shape mismatch during loading. If possible, I would appreciate it if you could explain why the zero point can be packed. As far as I understand, each quantization group has a zero point with the same dtype as the scale. Thank you. ```python w2_qzeros = torch.nn.Parameter( torch.empty(num_experts, scales_size2, hidden_size // self.quant_config.pack_factor, dtype=params_dtype), requires_grad=False, ) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: iridonSunRotator/DeepSeek-V3-0324-GPTQ-4b-128g/) have the same shape and dtype for weight_zero_point and weight_scale, which can cause a shape mismatch during loading. If possible, I would appreciate it if you could exp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Can't use GPTQ model with weight_zero_point bug;stale ### Your current environment commit a8238bbdb086d2e25a6c1a16b3438e0ffeb0de89 ### 🐛 Describe the bug I found that in vLLM, the shape of qzeros in GPTQ has been...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: dtype for weight_zero_point and weight_scale, which can cause a shape mismatch during loading. If possible, I would appreciate it if you could explain why the zero point can be packed. As far as I understand, each quant...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nd dtype for weight_zero_point and weight_scale, which can cause a shape mismatch during loading. If possible, I would appreciate it if you could explain why the zero point can be packed. As far as I understand, each qu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ich can cause a shape mismatch during loading. If possible, I would appreciate it if you could explain why the zero point can be packed. As far as I understand, each quantization group has a zero point with the same dty...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
