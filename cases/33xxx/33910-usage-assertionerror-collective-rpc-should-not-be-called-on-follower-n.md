# vllm-project/vllm#33910: [Usage]: AssertionError: collective_rpc should not be called on follower node

| 字段 | 值 |
| --- | --- |
| Issue | [#33910](https://github.com/vllm-project/vllm/issues/33910) |
| 状态 | open |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;moe;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: AssertionError: collective_rpc should not be called on follower node

### Issue 正文摘录

### Your current environment ```text Is CUDA available : True CUDA runtime version : 13.1.80 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidia driver version : 535.161.07 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.17.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.17.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.17.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.17.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.17.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.17.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.17.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.17.0 ============================== vLLM Info ============================== ROCM Version : Could not collect vLLM Version : 0.15.0 vLLM Build Flags: CUDA Archs: 7.5 8.0 8.6 9.0 10.0 12.0+PTX; ROCm: Disabled ``` ### How would you like to use vllm I want to run inference of DeepSeek R1 with 671B parameters on 2 H20 clusters. I have encountered a problem which might be caused by my exec...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: 152564) INFO 02-05 11:55:06 [cuda.py:364] Using FLASH_ATTN_MLA attention backend out of potential backends: ('FLASH_ATTN_MLA', 'FLASHMLA', 'TRITON_MLA') (Worker_TP8 pid=152564) INFO 02-05 11:55:06 [mla_attention.py:1399...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nt environment ```text Is CUDA available : True CUDA runtime version : 13.1.80 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: shAttention prefill for MLA (Worker_TP8 pid=152564) INFO 02-05 11:55:06 [fp8.py:328] Using FLASHINFER_CUTLASS Fp8 MoE backend out of potential backends: ['AITER', 'FLASHINFER_TRTLLM', 'FLASHINFER_CUTLASS', 'DEEPGEMM', '...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e called on follower node usage ### Your current environment ```text Is CUDA available : True CUDA runtime version : 13.1.80 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVID...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ngineCore_DP0 pid=152285) ERROR 02-05 11:55:35 [core.py:947] num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=152285) ERROR 02-05 11:55:35 [core.py:947] ^^^^^^^^^^^^^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
