# vllm-project/vllm#24607: [Feature]: Optimize `per_block_cast_to_fp8`

| 字段 | 值 |
| --- | --- |
| Issue | [#24607](https://github.com/vllm-project/vllm/issues/24607) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Optimize `per_block_cast_to_fp8`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vllm/vllm/utils/deep_gemm.py Currently the `per_block_cast_to_fp8` is written by pytorch script, which would be slow We can optimize it using triton kernel or cuda kernel ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h script, which would be slow We can optimize it using triton kernel or cuda kernel ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: written by pytorch script, which would be slow We can optimize it using triton kernel or cuda kernel ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make su...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Optimize `per_block_cast_to_fp8` feature request ### 🚀 The feature, motivation and pitch vllm/vllm/utils/deep_gemm.py Currently the `per_block_cast_to_fp8` is written by pytorch script, which would be slow We...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Optimize `per_block_cast_to_fp8` feature request ### 🚀 The feature, motivation and pitch vllm/vllm/utils/deep_gemm.py Currently the `per_block_cast_to_fp8` is written by pytorch script, which would be slow We...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: re request ### 🚀 The feature, motivation and pitch vllm/vllm/utils/deep_gemm.py Currently the `per_block_cast_to_fp8` is written by pytorch script, which would be slow We can optimize it using triton kernel or cuda kern...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
