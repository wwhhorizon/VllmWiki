# vllm-project/vllm#2312: out of memory with mixtral AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#2312](https://github.com/vllm-project/vllm/issues/2312) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> out of memory with mixtral AWQ

### Issue 正文摘录

Error: ``` torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 24.00 MiB. GPU 0 has a total capacty of 23.69 GiB of which 24.56 MiB is free. Process 106008 has 23.66 GiB memory in use. Of the allocated memory 23.19 GiB is allocated by PyTorch, and 32.44 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF ``` Model: https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ Command: ``` docker run --runtime nvidia --gpus all \ -v [...]:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=[...]" \ -p 10080:8000 --ipc=host vllm/vllm-openai:latest --trust-remote-code \ --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ \ --dtype auto --gpu-memory-utilization 0.5 --max-model-len 4096 --quantization awq ``` Does not work without the extra parameters either. HW: RTX 3090 (24GB). Looks similar to https://github.com/vllm-project/vllm/issues/188 but https://github.com/vllm-project/vllm/issues/188#issuecomment-1785991729 didn't work here.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ Command: ``` docker run --runtime nvidia --gpus all \ -v [...]:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=[...]" \ -p 10080:8000 --ipc=host vllm/vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: trust-remote-code \ --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ \ --dtype auto --gpu-memory-utilization 0.5 --max-model-len 4096 --quantization awq ``` Does not work without the extra parameters either. HW: RTX 3090...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: out of memory with mixtral AWQ Error: ``` torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 24.00 MiB. GPU 0 has a total capacty of 23.69 GiB of which 24.56 MiB is free. Process 106008 has 23.66 GiB mem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF ``` Model: https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ Command: ``` docker run --runtime nvidia --gpus all \ -v [...]:/root/.cache/h...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e ci_build;model_support;quantization;scheduler_memory cuda;quantization oom dtype;env_dependency Error:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
