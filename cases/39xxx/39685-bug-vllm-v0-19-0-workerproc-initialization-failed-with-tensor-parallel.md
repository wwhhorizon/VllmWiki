# vllm-project/vllm#39685: [Bug]: # vLLM v0.19.0 - WorkerProc initialization failed with Tensor Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#39685](https://github.com/vllm-project/vllm/issues/39685) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: # vLLM v0.19.0 - WorkerProc initialization failed with Tensor Parallelism

### Issue 正文摘录

### Your current environment ## Description vLLM v0.19.0 fails to initialize when using Tensor Parallelism (TP > 1) with certain models. The error occurs during worker process initialization. ## Environment - **vLLM Version**: 0.19.0 - **Docker Image**: vllm/vllm-openai:latest - **GPU**: 4x NVIDIA GPUs (tested with tensor-parallel-size=4) - **Model**: Qwen3-Coder-Next-REAM-AWQ-4bit (~80B parameters, AWQ quantized) ## Command Used ```bash sudo docker run -d --name vllm-qwen3-coder-ream-v2 \ --gpus=all -e CUDA_VISIBLE_DEVICES=4,5,6,7 \ --runtime=nvidia -v /data:/data -p 8008:8000 --ipc=host \ vllm/vllm-openai:latest \ --model /data/models/Qwen3-Coder-Next-REAM-AWQ-4bit \ --tensor-parallel-size 4 --max-model-len 200000 \ --disable-custom-all-reduce --gpu-memory-utilization 0.85 \ --dtype bfloat16 --kv-cache-dtype fp8 --host 0.0.0.0 --port 8000 ``` ### 🐛 Describe the bug ## Error Log ``` (EngineCore pid=335) ERROR 04-11 22:28:52 [core.py:1108] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause. (EngineCore pid=335) Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ize=4) - **Model**: Qwen3-Coder-Next-REAM-AWQ-4bit (~80B parameters, AWQ quantized) ## Command Used ```bash sudo docker run -d --name vllm-qwen3-coder-ream-v2 \ --gpus=all -e CUDA_VISIBLE_DEVICES=4,5,6,7 \ --runtime=nvi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r occurs during worker process initialization. ## Environment - **vLLM Version**: 0.19.0 - **Docker Image**: vllm/vllm-openai:latest - **GPU**: 4x NVIDIA GPUs (tested with tensor-parallel-size=4) - **Model**: Qwen3-Code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : # vLLM v0.19.0 - WorkerProc initialization failed with Tensor Parallelism bug ### Your current environment ## Description vLLM v0.19.0 fails to initialize when using Tensor Parallelism (TP > 1) with certain models. Th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: fails to initialize when using Tensor Parallelism (TP > 1) with certain models. The error occurs during worker process initialization. ## Environment - **vLLM Version**: 0.19.0 - **Docker Image**: vllm/vllm-openai:lates...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e-custom-all-reduce --gpu-memory-utilization 0.85 \ --dtype bfloat16 --kv-cache-dtype fp8 --host 0.0.0.0 --port 8000 ``` ### 🐛 Describe the bug ## Error Log ``` (EngineCore pid=335) ERROR 04-11 22:28:52 [core.py:1108] E...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
