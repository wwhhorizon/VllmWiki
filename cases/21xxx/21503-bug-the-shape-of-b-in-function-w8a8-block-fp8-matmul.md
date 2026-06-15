# vllm-project/vllm#21503: [Bug]: the shape of b in function w8a8_block_fp8_matmul

| 字段 | 值 |
| --- | --- |
| Issue | [#21503](https://github.com/vllm-project/vllm/issues/21503) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: the shape of b in function w8a8_block_fp8_matmul

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The function `w8a8_block_fp8_matmul` ([https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model\_executor/layers/quantization/utils/fp8\_utils.py#L534](https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model_executor/layers/quantization/utils/fp8_utils.py#L534)) takes its input `B` with shape `[N, K]`. Why, then, when `B` is passed to the helper `_w8a8_block_fp8_matmul` ([https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model\_executor/layers/quantization/utils/fp8\_utils.py#L409](https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model_executor/layers/quantization/utils/fp8_utils.py#L409)), does it show up as shape `[K, N]`—even though there’s no explicit transpose in between? As you can see at [https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model\_executor/layers/quantization/utils/fp8\_utils.py#L459](https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model_executor/layers/quantization/utils/fp8_utils.py#L459), inside the helper the matrix is indeed `[K, N]`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right co...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: the shape of b in function w8a8_block_fp8_matmul bug ### Your current environment ### 🐛 Describe the bug The function `w8a8_block_fp8_matmul` ([https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model\_executo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: py#L409)), does it show up as shape `[K, N]`—even though there’s no explicit transpose in between? As you can see at [https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model\_executor/layers/quantization/utils/fp8\_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ]`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: the shape of b in function w8a8_block_fp8_matmul bug ### Your current environment ### 🐛 Describe the bug The function `w8a8_block_fp8_matmul` ([https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model\_executo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lock_fp8_matmul` ([https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model\_executor/layers/quantization/utils/fp8\_utils.py#L534](https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/model_executor/layers/quantiza...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
