# vllm-project/vllm#26041: [Bug]: Error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized1Sm"

| 字段 | 值 |
| --- | --- |
| Issue | [#26041](https://github.com/vllm-project/vllm/issues/26041) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized1Sm"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While compiling vllm main, we meet error in B200 ```bash /data/vllm-community-homes/vllm-user-6/vllm-source/csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh(234): error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized1Sm" Shape , cutlass::epilogue::BlockwiseNoSmemWarpSpecialized1Sm, ^ /data/vllm-community-homes/vllm-user-6/vllm-source/csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh(248): error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized1Sm" Shape , cutlass::epilogue::BlockwiseNoSmemWarpSpecialized1Sm, ^ /data/vllm-community-homes/vllm-user-6/vllm-source/csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh(262): error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized2Sm" Shape , cutlass::epilogue::BlockwiseNoSmemWarpSpecialized2Sm, ^ /data/vllm-community-homes/vllm-user-6/vllm-source/csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh(274): error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized1Sm" Shape , cu...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: in B200 ```bash /data/vllm-community-homes/vllm-user-6/vllm-source/csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh(234): error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemW...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized1Sm" bug ### Your current environment ### 🐛 Describe the bug While compiling vllm main, we meet error in B200 ```bash /data/vllm-c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized1Sm" bug ### Your current environment ### 🐛 Describe the bug While compiling vllm main, we meet error in B200 ```bash /data/vllm-c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rror: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized1Sm" bug ### Your current environment ### 🐛 Describe the bug While compiling vllm main, we meet error in B200 ```bash /data/vllm-community...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Error: namespace "cutlass::epilogue" has no member "BlockwiseNoSmemWarpSpecialized1Sm" bug ### Your current environment ### 🐛 Describe the bug While compiling vllm main, we meet error in B200 ```bash /data/vllm-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
