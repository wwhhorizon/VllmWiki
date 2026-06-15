# vllm-project/vllm#20429: [Usage]: why vllm bug? env:vllm 0.8.3+pytorch2.6.0+cuda12.6

| 字段 | 值 |
| --- | --- |
| Issue | [#20429](https://github.com/vllm-project/vllm/issues/20429) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: why vllm bug? env:vllm 0.8.3+pytorch2.6.0+cuda12.6

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` 2025-07-03 17:20:11.408074: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`. 2025-07-03 17:20:11.422500: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:467] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered WARNING: All log messages before absl::InitializeLog() is called are written to STDERR E0000 00:00:1751534411.438935 575805 cuda_dnn.cc:8579] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered E0000 00:00:1751534411.443698 575805 cuda_blas.cc:1407] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered W0000 00:00:1751534411.456067 575805 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once. W000...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once. W0000 00:00:1751534411.456091 575805 computation_placer.cc:177] computation placer alrea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: .12/site-packages/vllm/engine/arg_utils.py", line 15, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "/usr/local/lib/python3.12/site-packages/vllm/config.py", line 29, in from vllm.model_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: .cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s. To enable the following instructions: AVX2 AVX512F AVX512_VNNI AVX512_BF16 AVX512_FP16 AVX_VNNI AMX_TILE AMX_INT8 AMX_BF16 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. INFO 07-03...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: why vllm bug? env:vllm 0.8.3+pytorch2.6.0+cuda12.6 usage ### Your current environment ```text The output of `python collect_env.py` ``` 2025-07-03 17:20:11.408074: I tensorflow/core/util/port.cc:153] oneDNN cus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
