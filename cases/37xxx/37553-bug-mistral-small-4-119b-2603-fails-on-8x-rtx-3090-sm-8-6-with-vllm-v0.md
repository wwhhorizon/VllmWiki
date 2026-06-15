# vllm-project/vllm#37553: [Bug]: Mistral-Small-4-119B-2603 fails on 8x RTX 3090 (SM 8.6) with vLLM v0.17.1: no valid MLA attention backend

| 字段 | 值 |
| --- | --- |
| Issue | [#37553](https://github.com/vllm-project/vllm/issues/37553) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral-Small-4-119B-2603 fails on 8x RTX 3090 (SM 8.6) with vLLM v0.17.1: no valid MLA attention backend

### Issue 正文摘录

### Your current environment - OS: Fedora Linux 42 (Workstation Edition) - Kernel: 6.18.16-100.fc42.x86_64 - GPU: 8x NVIDIA RTX 3090 (SM 8.6, 24 GB each) - Driver: NVIDIA 580.126.09 - CUDA toolkit used for build: 13.1.115 - Compiler: GCC/G++ 14.2.1 - Python: conda env `vllm_env` - vLLM: 0.17.1+cu131 built from source Host memory: 503 GiB DDR4 RAM (~482 GiB available at the time of testing). For context, the host CPU is an AMD EPYC 7532 (Zen 2), which does not provide AVX512 support; however, this issue occurs on the CUDA path during MLA attention backend selection, not on the CPU backend. (vllm_env) admin_ia@MiWiFi-R3600-srv : /tmp $ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Fedora Linux 42 (Workstation Edition) (x86_64) GCC version : (GCC) 15.2.1 20260123 (Red Hat 15.2.1-7) Clang version : Could not collect CMake version : version 4.2.1 Libc version : glibc-2.41 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ==============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: (SM 8.6, 24 GB each) - Driver: NVIDIA 580.126.09 - CUDA toolkit used for build: 13.1.115 - Compiler: GCC/G++ 14.2.1 - Python: conda env `vllm_env` - vLLM: 0.17.1+cu131 built from source Host memory: 503 GiB DDR4 RAM (~4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Bug]: Mistral-Small-4-119B-2603 fails on 8x RTX 3090 (SM 8.6) with vLLM v0.17.1: no valid MLA attention backend bug ### Your current environment - OS: Fedora Linux 42 (Workstation Edition) - Kernel: 6.18.16-100.fc42.x8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ro irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: fails on 8x RTX 3090 (SM 8.6) with vLLM v0.17.1: no valid MLA attention backend bug ### Your current environment - OS: Fedora Linux 42 (Workstation Edition) - Kernel: 6.18.16-100.fc42.x86_64 - GPU: 8x NVIDIA RTX 3090 (S...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: iFi-R3600-srv : /tmp $ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Fedora Linux 42 (Workstation Edition) (x86_64) GCC versio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
