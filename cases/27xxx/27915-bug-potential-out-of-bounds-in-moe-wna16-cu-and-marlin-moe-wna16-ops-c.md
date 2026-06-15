# vllm-project/vllm#27915: [Bug]: Potential Out-of-bounds in moe_wna16.cu and marlin_moe_wna16/ops.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#27915](https://github.com/vllm-project/vllm/issues/27915) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;moe;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe;operator;sampling |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential Out-of-bounds in moe_wna16.cu and marlin_moe_wna16/ops.cu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified multiple potential out-of-bounds accesses in the moe_wna16_gemm and moe_wna16_marlin_gemm. ### 1. moe_wna16_gemm #### (1) expert_ids[blockIdx.x] https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/moe/moe_wna16.cu#L39-L42 expert_ids[blockIdx.x] may lead to an out-of-bounds access. By executing a concrete model, I observed that the input has the shape: [batch_size*seq_len, 2048]. Example Scenario: ``` blockIdx.x: 4 expert_ids.shape: [4] BLOCK_SIZE_M: 16 top_k: 4 batch_size: 2 seq_len: 1 sorted_token_ids.shape: [128] ``` expert_ids[blockIdx.x] accesses invalid memory when blockIdx.x exceeds the size of expert_ids. #### (2) sorted_token_ids[offset_m] https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/moe/moe_wna16.cu#L50-L52 sorted_token_ids[offset_m] may lead to an out-of-bounds access. index: blockIdx.x * BLOCK_SIZE_M + m Example Scenario: ``` sorted_token_ids.shape: [17] blockIdx.x: 1 BLOCK_SIZE_M: 16 m: 1 ``` The computed index is out of bounds. #### (3) reinterpret_cast (expert_scales)[scales_o...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: Potential Out-of-bounds in moe_wna16.cu and marlin_moe_wna16/ops.cu bug;stale ### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified multiple potential...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ironment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified multiple potential out-of-bounds accesses in the moe_wna16_gemm and moe_wna16_marlin_gemm. ### 1. moe_wna16_gemm #### (1) ex...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: model_support;moe;sampling_logits cuda;kernel;moe;operator;sampling env_dependency;shape Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ` The computed index is out of bounds. #### (3) reinterpret_cast (expert_scales)[scales_offset_tmp] https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/moe/moe_wna16.cu#L112-L116 rein...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: emm and moe_wna16_marlin_gemm. ### 1. moe_wna16_gemm #### (1) expert_ids[blockIdx.x] https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/moe/moe_wna16.cu#L39-L42 expert_ids[blockIdx.x...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
