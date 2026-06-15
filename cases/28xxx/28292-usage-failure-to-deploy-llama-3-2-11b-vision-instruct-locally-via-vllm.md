# vllm-project/vllm#28292: [Usage]: Failure to Deploy Llama-3.2-11B-Vision-Instruct Locally via vllm Due to OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#28292](https://github.com/vllm-project/vllm/issues/28292) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | activation;attention;cuda;gemm;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Failure to Deploy Llama-3.2-11B-Vision-Instruct Locally via vllm Due to OOM

### Issue 正文摘录

### Your current environment The output of python collect_env.py ```text ============================== System Info ============================== OS : Ubuntu 20.04.5 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.5.1+cu121 Is debug build : False CUDA used to build PyTorch : 12.1 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (main, Jun 5 2025, 13:14:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.250-2-velinux1u1-amd64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.131 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driv...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 20.04.5 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.35 =================
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Not affected Vulnerability Spec store byp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Usage]: Failure to Deploy Llama-3.2-11B-Vision-Instruct Locally via vllm Due to OOM usage ### Your current environment The output of python collect_env.py ```text ============================== System Info ============...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.5.1+cu121 Is debug build : False CUDA used to build PyTorch : 12.1 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 515,driver =515,driver =515,driver =515,driver =515,driver =515,driver , dtype='bfloat16', kv_cache_dtype='auto', max_model_len=2048, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto',...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
