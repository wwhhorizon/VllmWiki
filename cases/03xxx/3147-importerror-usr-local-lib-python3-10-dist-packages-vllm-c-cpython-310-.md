# vllm-project/vllm#3147: ImportError: /usr/local/lib/python3.10/dist-packages/vllm/_C.cpython-310-x86_64-linux-gnu.so:

| 字段 | 值 |
| --- | --- |
| Issue | [#3147](https://github.com/vllm-project/vllm/issues/3147) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ImportError: /usr/local/lib/python3.10/dist-packages/vllm/_C.cpython-310-x86_64-linux-gnu.so:

### Issue 正文摘录

I am trying to use vLLM with Langchain and I am getting this error: `ImportError: /usr/local/lib/python3.10/dist-packages/vllm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE` CUDA: 12.0.1 torch : 2.2.1 transformers: 4.38.2 vllm: 0.3.2 accelerate: 0.27.2 Please help out if anyone solved this issue.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ImportError: /usr/local/lib/python3.10/dist-packages/vllm/_C.cpython-310-x86_64-linux-gnu.so: stale I am trying to use vLLM with Langchain and I am getting this error: `ImportError: /usr/local/lib/python3.10/dist-packag
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: lm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE` CUDA:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE` CUDA: 12.0.1 torch : 2.2.1 transformers: 4.38.2 vllm: 0.3.2 accelerate: 0.27.2 Please help out if anyone solved this issue. development cuda import...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE` CUDA: 12.0....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE` CUDA: 12.0.1 torch : 2.2.1 transformers: 4.38.2 vllm: 0.3.2 accelerate: 0.27.2 Please help out if anyone solved this issue. development...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
