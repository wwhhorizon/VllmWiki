# vllm-project/vllm#3771: [Bug]: docker 启动vllm,配置了host_IP ，还是 [W socket.cpp:663] [c10d] The client socket has failed to connect to [::ffff:172.16.8.232]:39623 (errno: 110 - Connection timed out)

| 字段 | 值 |
| --- | --- |
| Issue | [#3771](https://github.com/vllm-project/vllm/issues/3771) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: docker 启动vllm,配置了host_IP ，还是 [W socket.cpp:663] [c10d] The client socket has failed to connect to [::ffff:172.16.8.232]:39623 (errno: 110 - Connection timed out)

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 1.12.1+cu113 Is debug build: False CUDA used to build PyTorch: 11.3 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.8.16 (default, Mar 2 2023, 03:21:46) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-101-generic-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version: 550.54.14 cuDNN version: Probably one of the following: /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn.so.8.8.0 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.8.0 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.8.0 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.8.0 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.8.0 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.8.0 /usr/local/cuda-12.0/targets/x86_64...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: docker 启动vllm,配置了host_IP ，还是 [W socket.cpp:663] [c10d] The client socket has failed to connect to [::ffff:172.16.8.232]:39623 (errno: 110 - Connection timed out) bug;stale ### Your current environment Collecting...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: nment information... PyTorch version: 1.12.1+cu113 Is debug build: False CUDA used to build PyTorch: 11.3 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ro irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid over...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ed out) bug;stale ### Your current environment Collecting environment information... PyTorch version: 1.12.1+cu113 Is debug build: False CUDA used to build PyTorch: 11.3 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t to [::ffff:172.16.8.232]:39623 (errno: 110 - Connection timed out) bug;stale ### Your current environment Collecting environment information... PyTorch version: 1.12.1+cu113 Is debug build: False CUDA used to build Py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
