# vllm-project/vllm#11654: [Bug]: Getting error 500 while requesting to `/v1/completions`

| 字段 | 值 |
| --- | --- |
| Issue | [#11654](https://github.com/vllm-project/vllm/issues/11654) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Getting error 500 while requesting to `/v1/completions`

### Issue 正文摘录

### Your current environment 2024-12-31 07:18:52 (16.5 MB/s) - ‘collect_env.py’ saved [26218/26218] 2024-12-31 07:19:05.225054: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-12-31 07:19:05.258365: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2024-12-31 07:19:05.268527: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered 2024-12-31 07:19:05.293788: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable the following instructions: AVX2 AVX512F FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. 2024-12-31 07:19:06.671596: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT Collecting environme...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ble the following instructions: AVX2 AVX512F FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. 2024-12-31 07:19:06.671596: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT W...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 8] 2024-12-31 07:19:05.225054: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: .cc:38] TF-TRT Warning: Could not find TensorRT Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Getting error 500 while requesting to `/v1/completions` bug ### Your current environment 2024-12-31 07:18:52 (16.5 MB/s) - ‘collect_env.py’ saved [26218/26218] 2024-12-31 07:19:05.225054: E external/local_xla/xla...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nvironment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
