# vllm-project/vllm#2680: Support CodeLlama-70b-Instruct-hf

| 字段 | 值 |
| --- | --- |
| Issue | [#2680](https://github.com/vllm-project/vllm/issues/2680) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support CodeLlama-70b-Instruct-hf

### Issue 正文摘录

Hi team, CodeLlama-70b just got released, https://huggingface.co/codellama/CodeLlama-70b-Instruct-hf Can we add support for it? Thank you. I ran into issues trying to run it with vllm ` cache_ops.cpython-38-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorESt8optionalIN3c1010ScalarTypeEES5_INS6_6LayoutEES5_INS6_6DeviceEES5_IbEbbS5_INS6_12MemoryFormatEE `

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Support CodeLlama-70b-Instruct-hf Hi team, CodeLlama-70b just got released, https://huggingface.co/codellama/CodeLlama-70b-Instruct-hf Can we add support for it? Thank you. I ran into issues trying to run it with vllm `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: trying to run it with vllm ` cache_ops.cpython-38-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorESt8optionalIN3c1010ScalarTypeEES5_INS6_6LayoutEES5_INS6_6DeviceEES5_IbEbbS5_INS6_12...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: he_ops.cpython-38-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorESt8optionalIN3c1010ScalarTypeEES5_INS6_6LayoutEES5_INS6_6DeviceEES5_IbEbbS5_INS6_12MemoryFormatEE `
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .cpython-38-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorESt8optionalIN3c1010ScalarTypeEES5_INS6_6LayoutEES5_INS6_6DeviceEES5_IbEbbS5_INS6_12MemoryFormatEE `

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
