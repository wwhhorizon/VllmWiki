# vllm-project/vllm#8227: [Bug]: In the case of quantization=compressed-tensors, Qwen2-57B-A14B-Instruct is not supported.

| 字段 | 值 |
| --- | --- |
| Issue | [#8227](https://github.com/vllm-project/vllm/issues/8227) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;fp8;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In the case of quantization=compressed-tensors, Qwen2-57B-A14B-Instruct is not supported.

### Issue 正文摘录

### Your current environment conda create -n Fp_8 python=3.10 -y conda env list conda activate Fp_8 pip install vllm pip install nvidia-cublas-cu12==12.3.4.1（H20） pip install llmcompressor==0.1.0 $conda list # packages in environment at /home/adc/.conda/envs/Vllm: # # Name Version Build Channel _libgcc_mutex 0.1 main _openmp_mutex 5.1 1_gnu aiohappyeyeballs 2.4.0 pypi_0 pypi aiohttp 3.10.5 pypi_0 pypi aiosignal 1.3.1 pypi_0 pypi annotated-types 0.7.0 pypi_0 pypi anyio 4.4.0 pypi_0 pypi async-timeout 4.0.3 pypi_0 pypi attrs 24.2.0 pypi_0 pypi bzip2 1.0.8 h5eee18b_6 ca-certificates 2024.7.2 h06a4308_0 certifi 2024.8.30 pypi_0 pypi charset-normalizer 3.3.2 pypi_0 pypi click 8.1.7 pypi_0 pypi cloudpickle 3.0.0 pypi_0 pypi datasets 2.21.0 pypi_0 pypi dill 0.3.8 pypi_0 pypi diskcache 5.6.3 pypi_0 pypi distro 1.9.0 pypi_0 pypi exceptiongroup 1.2.2 pypi_0 pypi fastapi 0.112.2 pypi_0 pypi filelock 3.15.4 pypi_0 pypi frozenlist 1.4.1 pypi_0 pypi gguf 0.9.1 pypi_0 pypi h11 0.14.0 pypi_0 pypi httpcore 1.0.5 pypi_0 pypi httptools 0.6.1 pypi_0 pypi httpx 0.27.2 pypi_0 pypi huggingface-hub 0.24.6 pypi_0 pypi idna 3.8 pypi_0 pypi importlib-metadata 8.4.0 pypi_0 pypi interegular 0.3.3 pypi_0 pypi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nda create -n Fp_8 python=3.10 -y conda env list conda activate Fp_8 pip install vllm pip install nvidia-cublas-cu12==12.3.4.1（H20） pip install llmcompressor==0.1.0 $conda list # packages in environment at /home/adc/.co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: In the case of quantization=compressed-tensors, Qwen2-57B-A14B-Instruct is not supported. bug;stale ### Your current environment conda create -n Fp_8 python=3.10 -y conda env list conda activate Fp_8 pip install...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: In the case of quantization=compressed-tensors, Qwen2-57B-A14B-Instruct is not supported. bug;stale ### Your current environment conda create -n Fp_8 python=3.10 -y conda env list conda activate Fp_8 pip install...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nvidia-cublas-cu12 12.3.4.1 pypi_0 pypi nvidia-cuda-cupti-cu12 12.1.105 pypi_0 pypi nvidia-cuda-nvrtc-cu12 12.1.105 pypi_0 pypi nvidia-cuda-runtime-cu12 12.1.105 pypi_0 pypi nvidia-cudnn-cu12 9.1
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: zation=compressed-tensors, Qwen2-57B-A14B-Instruct is not supported. bug;stale ### Your current environment conda create -n Fp_8 python=3.10 -y conda env list conda activate Fp_8 pip install vllm pip install nvidia-cubl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
