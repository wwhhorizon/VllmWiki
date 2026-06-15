# vllm-project/vllm#19833: [Bug]: TypeError: Qwen2_5OmniProcessor.__init__() got multiple values for argument 'image_processor'

| 字段 | 值 |
| --- | --- |
| Issue | [#19833](https://github.com/vllm-project/vllm/issues/19833) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: Qwen2_5OmniProcessor.__init__() got multiple values for argument 'image_processor'

### Issue 正文摘录

### Your current environment ```text INFO 06-19 02:57:16 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.30.2 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.4.0-167-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.6.20 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version : 535.216.03 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.3.0 /usr/lib/x86_64-lin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.30.2 Libc version : glibc-2.35 =================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: TypeError: Qwen2_5OmniProcessor.__init__() got multiple values for argument 'image_processor' bug;stale ### Your current environment ```text INFO 06-19 02:57:16 [__init__.py:244] Automatically detected platform c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: xt INFO 06-19 02:57:16 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: cessor.__init__() got multiple values for argument 'image_processor' bug;stale ### Your current environment ```text INFO 06-19 02:57:16 [__init__.py:244] Automatically detected platform cuda. Collecting environment info...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: l clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
