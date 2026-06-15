# vllm-project/vllm#6988: [Bug]: subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=40', '--target=_moe_C', '--target=_C']' returned non-zero exit status 1.

| 字段 | 值 |
| --- | --- |
| Issue | [#6988](https://github.com/vllm-project/vllm/issues/6988) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;gemm;kernel;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=40', '--target=_moe_C', '--target=_C']' returned non-zero exit status 1.

### Issue 正文摘录

### Your current environment environment: v100 cuda 12.1 ### 🐛 Describe the bug ng int, cute::C , cute::C >, cutlass::bfloat16_t, cute::tuple , cute::C >, cutlass::epilogue::fusion::Sm90TreeVisitor , cutlass::epilogue::fusion::Sm90ColOrScalarBroadcast , cute::C , cute::C >, float, cute::tuple , cute::C , cute::C >, 4>, cutlass::epilogue::fusion::Sm90TreeVisitor , cutlass::epilogue::fusion::Sm90RowOrScalarBroadcast , cute::C , cute::C >, float, cute::tuple , cute::C , cute::C >, 4>, cutlass::epilogue::fusion::Sm90AccFetch> >, cute::SM90_TMA_LOAD, cute::ComposedLayout , cute::smem_ptr_flag_bits , cute::Layout , cute::C >, cute::tuple , cute::C > > >, cute::SM75_U32x4_LDSM_N, cute::SM90_TMA_STORE, cute::ComposedLayout , cute::smem_ptr_flag_bits , cute::Layout , cute::C >, cute::tuple , cute::C > > >, cute::SM90_U32x4_STSM_N>, cutlass::gemm::PersistentScheduler, void>::Arguments; cudaStream_t = CUstream_st*]’ /scratch/AzureNfsServer_INPUT1/vc_data/yingmeiguo2/LLM/vllm/csrc/quantization/cutlass_w8a8/scaled_mm_c3x.cu:289:17: required from ‘void _GLOBAL__N__38c64651_16_scaled_mm_c3x_cu_22d95651::cutlass_gemm_caller(at::Tensor&, const at::Tensor&, const at::Tensor&, EpilogueArgs&& ...) [w...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=40', '--target=_moe_C', '--target=_C']' returned non-zero exit status 1. bug ### Your current environment environment: v100 cuda 12.1 ### 🐛 De...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: uda 12.1 ### 🐛 Describe the bug ng int, cute::C , cute::C >, cutlass::bfloat16_t, cute::tuple , cute::C >, cutlass::epilogue::fusion::Sm90TreeVisitor , cutlass::epilogue::fusion::Sm90ColOrScalarBroadcast , cute::C , cut...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: s::epilogue::fusion::Sm90AccFetch> >, cute::SM90_TMA_LOAD, cute::ComposedLayout , cute::smem_ptr_flag_bits , cute::Layout , cute::C >, cute::tuple , cute::C > > >, cute::SM75_U32x4_LDSM_N, cute::SM90_TMA_STORE, cute::Co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: : v100 cuda 12.1 ### 🐛 Describe the bug ng int, cute::C , cute::C >, cutlass::bfloat16_t, cute::tuple , cute::C >, cutlass::epilogue::fusion::Sm90TreeVisitor , cutlass::epilogue::fusion::Sm90ColOrScalarBroadcast , cute:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: zero exit status 1. bug ### Your current environment environment: v100 cuda 12.1 ### 🐛 Describe the bug ng int, cute::C , cute::C >, cutlass::bfloat16_t, cute::tuple , cute::C >, cutlass::epilogue::fusion::Sm90TreeVisit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
