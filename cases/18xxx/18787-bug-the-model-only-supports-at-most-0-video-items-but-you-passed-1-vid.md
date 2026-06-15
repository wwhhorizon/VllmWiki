# vllm-project/vllm#18787: [Bug]: "The model only supports at most 0 video items, but you passed 1 video items in the same prompt." in vision_language.py using InternVL3

| 字段 | 值 |
| --- | --- |
| Issue | [#18787](https://github.com/vllm-project/vllm/issues/18787) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "The model only supports at most 0 video items, but you passed 1 video items in the same prompt." in vision_language.py using InternVL3

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.31.7 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform : Linux-6.8.0-59-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version : 570.133.07 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.10.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.10.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.10.1 /usr/lib/x86_64-linux-gnu/libcudnn_engine...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ========= OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.31.7 Libc version : glibc-2.35 =================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: [Bug]: "The model only supports at most 0 video items, but you passed 1 video items in the same prompt." in vision_language.py using InternVL3 bug ### Your current environment ============================== System Info...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.0 (d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: noinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ro irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid over...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
