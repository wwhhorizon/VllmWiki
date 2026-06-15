# vllm-project/vllm#28110: [Bug]: spark can not run MoE GEMM

| 字段 | 值 |
| --- | --- |
| Issue | [#28110](https://github.com/vllm-project/vllm/issues/28110) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: spark can not run MoE GEMM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I successfully ran the Qwen3-32B model with NVFP4 quantization, but when I tried to run GLM4.5 with NVFP4, it raised a RuntimeError: Failed to initialize GEMM. I found run_fp4_blockwise_scaled_group_mm function: ``` template void run_fp4_blockwise_scaled_group_mm( torch::Tensor& output, const torch::Tensor& a, const torch::Tensor& b, const torch::Tensor& a_blockscale, const torch::Tensor& b_blockscales, const torch::Tensor& alphas, const torch::Tensor& problem_sizes, const torch::Tensor& expert_offsets, const torch::Tensor& sf_offsets, int M, int N, int K) { using ProblemShape = cutlass::gemm::GroupProblemShape >; using ElementType = cutlass::float_e2m1_t; using ElementSFType = cutlass::float_ue4m3_t; using ElementA = cutlass::nv_float4_t ; using ElementB = cutlass::nv_float4_t ; using ElementC = OutType; using ElementD = ElementC; using ElementAccumulator = float; // Layout definitions using LayoutA = cutlass::layout::RowMajor; using LayoutB = cutlass::layout::ColumnMajor; using LayoutC = cutlass::layout::RowMajor; using LayoutD = LayoutC; // Alignment constraints static constexpr int AlignmentA = 32; static constexpr int Alignm...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ### 🐛 Describe the bug I successfully ran the Qwen3-32B model with NVFP4 quantization, but when I tried to run GLM4.5 with NVFP4, it raised a RuntimeError: Failed to initialize GEMM. I found run_fp4_blockwise_scaled_gro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: using KernelSchedule = cutlass::gemm:: KernelPtrArrayTmaWarpSpecialized1SmNvf4Sm100; // Kernel to launch using EpilogueSchedule = cutlass::epilogue::PtrArrayTmaWarpSpecialized1Sm; // Epilogue to launch }; using Collecti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tic constexpr int AlignmentD = 128 / cutlass::sizeof_bits ::value; // Architecture definitions using ArchTag = cutlass::arch::Sm100; using EpilogueOperatorClass = cutlass::arch::OpClassTensorOp; // Epilogue Operator cla...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: P4, it raised a RuntimeError: Failed to initialize GEMM. I found run_fp4_blockwise_scaled_group_mm function: ``` template void run_fp4_blockwise_scaled_group_mm( torch::Tensor& output, const torch::Tensor& a, const torc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r current environment ### 🐛 Describe the bug I successfully ran the Qwen3-32B model with NVFP4 quantization, but when I tried to run GLM4.5 with NVFP4, it raised a RuntimeError: Failed to initialize GEMM. I found run_fp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
