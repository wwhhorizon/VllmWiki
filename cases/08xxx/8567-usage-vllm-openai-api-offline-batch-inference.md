# vllm-project/vllm#8567: [Usage]: vllm OpenAI API Offline Batch Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#8567](https://github.com/vllm-project/vllm/issues/8567) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm OpenAI API Offline Batch Inference

### Issue 正文摘录

### Your current environment ```text 2024-09-18 13:46:38.125558: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-09-18 13:46:38.139942: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2024-09-18 13:46:38.144110: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered 2024-09-18 13:46:38.156547: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. 2024-09-18 13:46:41.410252: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM us...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: . To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. 2024-09-18 13:46:41.410252: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT W...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: ext 2024-09-18 13:46:38.125558: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: A runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA A100 80GB PCIe GPU 4: NVIDIA RTX A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca Virtualizat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.2 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
