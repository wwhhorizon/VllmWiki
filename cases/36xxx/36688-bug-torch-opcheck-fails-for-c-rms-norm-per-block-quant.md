# vllm-project/vllm#36688: [Bug]: torch.opcheck fails for `_C.rms_norm_per_block_quant`

| 字段 | 值 |
| --- | --- |
| Issue | [#36688](https://github.com/vllm-project/vllm/issues/36688) |
| 状态 | closed |
| 标签 | bug;help wanted |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: torch.opcheck fails for `_C.rms_norm_per_block_quant`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In the unit test for `torch.ops._C.rms_norm_per_block_quant` custom kernel, for some reason opcheck fails because it thinks the weight tensor got mutated. A closer look reveals a weird issue: the cloned weight arg is the one that gets modified, and the original weight arg stays intact. I could not find a memory issue, I manually confirmed the original weight stays intact when not using opcheck, and E2E evals look good. ``` torch.testing._internal.optests.generate_tests.OpCheckError: opcheck(op, ...): test_schema failed with Argument weight is not defined as mutable but was mutated (scroll up for stack trace) ``` https://github.com/vllm-project/vllm/blob/0ebf4e969b43d99c240fd085703ea1ed97897499/tests/kernels/core/test_fused_quant_layernorm.py#L291-L304 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ted ### Your current environment ### 🐛 Describe the bug In the unit test for `torch.ops._C.rms_norm_per_block_quant` custom kernel, for some reason opcheck fails because it thinks the weight tensor got mutated. A closer...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: torch.opcheck fails for `_C.rms_norm_per_block_quant` bug;help wanted ### Your current environment ### 🐛 Describe the bug In the unit test for `torch.ops._C.rms_norm_per_block_quant` custom kernel, for some reaso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 304 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: torch.opcheck fails for `_C.rms_norm_per_block_quant` bug;help wanted ### Your current environment ### 🐛 Describe the bug In the unit test for `torch.ops._C.rms_norm_per_block_quant` custom kernel, for some reaso...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
