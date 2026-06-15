# vllm-project/vllm#10525: [Bug]: Gemma2 becomes a fool.

| 字段 | 值 |
| --- | --- |
| Issue | [#10525](https://github.com/vllm-project/vllm/issues/10525) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma2 becomes a fool.

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` ```2024-11-21 16:41:21.863442: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`. 2024-11-21 16:41:21.876552: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-11-21 16:41:21.892988: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2024-11-21 16:41:21.897866: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered 2024-11-21 16:41:21.909651: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: owing instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. 2024-11-21 16:41:22.760068: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT W...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: 0`. 2024-11-21 16:41:21.876552: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma2 becomes a fool. bug;stale ### Your current environment The output of `python collect_env.py` ```2024-11-21 16:41:21.863442: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Mitigation; TSX disabled Versions of relevant libraries: [pip3] flashinfer==0.1.6+cu124torch2.4 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu11==11.11.3.6 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu11...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: .cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
