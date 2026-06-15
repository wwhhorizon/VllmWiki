# vllm-project/vllm#29181: [Bug]: Got additional triton kernel when using native rms_norm op matching with all_reduce+rms_norm fusion

| 字段 | 值 |
| --- | --- |
| Issue | [#29181](https://github.com/vllm-project/vllm/issues/29181) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Got additional triton kernel when using native rms_norm op matching with all_reduce+rms_norm fusion

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Native rms_norm op + all_reduce fusion: ``` VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 \ vllm serve \ openai/gpt-oss-20b \ -O.pass_config.enable_noop=True \ -O.pass_config.enable_fi_allreduce_fusion=True \ --kv-cache-dtype fp8 \ --tensor-parallel-size 2 ``` Custom rms_norm op + all_reduce fusion: ``` VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 \ vllm serve \ openai/gpt-oss-20b \ -O.pass_config.enable_noop=True \ -O.pass_config.enable_fi_allreduce_fusion=True \ -O.custom_ops+=+rms_norm \ --kv-cache-dtype fp8 \ --tensor-parallel-size 2 ``` From nsys: Native rms_norm op + all_reduce fusion: ``` fmhaSm100fKernel_QkvE4m3OBfloat16H64PagedKvDenseP16MultiCtasKvCgaVarSeqQ8Kv128Static 7.488 μs nvjet_tst_24x64_64x16_4x1_v_bz_bias_TNN 6.976 μs triton_poi_fused_as_strided_clone_0 1.408 μs void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport 7.168 μs ``` Custom rms_norm op + all_reduce fusion: ``` fmhaSm100fKernel_QkvE4m3OBfloat16H64PagedKvDenseP16MultiCtasKvCgaVarSeqQ8Kv128Static 7.328 μs nvjet_tst_24x64_64x16_4x1_v_bz_bias_TNN 7.200 μs void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport 7.136 μ...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: bug Native rms_norm op + all_reduce fusion: ``` VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 \ vllm serve \ openai/gpt-oss-20b \ -O.pass_config.enable_noop=True \ -O.pass_config.enable_fi_allreduce_fusion=True \ --kv-cache-dty...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ng native rms_norm op matching with all_reduce+rms_norm fusion bug;torch.compile ### Your current environment ### 🐛 Describe the bug Native rms_norm op + all_reduce fusion: ``` VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 \ vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: fusion: ``` VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 \ vllm serve \ openai/gpt-oss-20b \ -O.pass_config.enable_noop=True \ -O.pass_config.enable_fi_allreduce_fusion=True \ --kv-cache-dtype fp8 \ --tensor-parallel-size 2 ``...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Got additional triton kernel when using native rms_norm op matching with all_reduce+rms_norm fusion bug;torch.compile ### Your current environment ### 🐛 Describe the bug Native rms_norm op + all_reduce fusion: ``...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: el-size 2 ``` From nsys: Native rms_norm op + all_reduce fusion: ``` fmhaSm100fKernel_QkvE4m3OBfloat16H64PagedKvDenseP16MultiCtasKvCgaVarSeqQ8Kv128Static 7.488 μs nvjet_tst_24x64_64x16_4x1_v_bz_bias_TNN 6.976 μs triton_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
