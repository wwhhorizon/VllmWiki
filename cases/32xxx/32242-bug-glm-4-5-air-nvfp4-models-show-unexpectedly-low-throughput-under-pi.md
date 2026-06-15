# vllm-project/vllm#32242: [Bug]: GLM-4.5-Air-NVFP4 models show unexpectedly low throughput under Pipeline Parallel in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#32242](https://github.com/vllm-project/vllm/issues/32242) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5-Air-NVFP4 models show unexpectedly low throughput under Pipeline Parallel in vLLM

### Issue 正文摘录

### Your current environment The output of python collect_env.py ```text ### Environment Information ### Operating System: `Linux-5.15.0-163-generic-x86_64-with-glibc2.35` Python Version: `3.10.19 (main, Oct 21 2025, 16:43:05) [GCC 11.2.0]` llm-compressor Version: `0.8.1` compressed-tensors Version: `0.12.2` transformers Version: `4.56.2` torch Version: `2.9.0` CUDA Devices: `['NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090']` AMD Devices: `None` ``` I used a locally downloaded Docker image to launch the NVFP4 model quantized with llmcompressor (and also verified using the same NVFP4 model from Hugging Face). The Docker image used is `vllm-openai:nightly-x86_64`. sudo docker run --rm --gpus all -p 8000:8000 -v /datas/model_zoo:/models --ipc=host --shm-size=128G docker.1ms.run/vllm/vllm-openai:nightly-x86_64 /models/MYmodel/NEW1-GLM-4.5-Air-NVFP4 --host 0.0.0.0 --dtype auto --quantization compressed-tensors --max-model-len 128000 --tensor-parallel-size 2 --pipeline-parallel-size 4 --gpu-memory-utilization 0.85 --disabl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Information ### Operating System: `Linux-5.15.0-163-generic-x86_64-with-glibc2.35` Python Version: `3.10.19 (main, Oct 21 2025, 16:43:05) [GCC 11.2.0]` llm-compressor Version: `0.8.1` compressed-tensors Version: `0.12.2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: GLM-4.5-Air-NVFP4 models show unexpectedly low throughput under Pipeline Parallel in vLLM bug;stale ### Your current environment The output of python collect_env.py ```text ### Environment Information ### Operati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Version: `0.12.2` transformers Version: `4.56.2` torch Version: `2.9.0` CUDA Devices: `['NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 5090', 'NVIDIA GeForce RTX 509...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: GLM-4.5-Air-NVFP4 models show unexpectedly low throughput under Pipeline Parallel in vLLM bug;stale ### Your current environment The output of python collect_env.py ```text ### Environment Information ### Operati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: els show unexpectedly low throughput under Pipeline Parallel in vLLM bug;stale ### Your current environment The output of python collect_env.py ```text ### Environment Information ### Operating System: `Linux-5.15.0-163...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
