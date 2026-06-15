# vllm-project/vllm#16712: [Bug]: meta-llama/Llama-4-Scout-17B-16E-Instruct not supported on VLLM, 2xH100 NVL 196GB

| 字段 | 值 |
| --- | --- |
| Issue | [#16712](https://github.com/vllm-project/vllm/issues/16712) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: meta-llama/Llama-4-Scout-17B-16E-Instruct not supported on VLLM, 2xH100 NVL 196GB

### Issue 正文摘录

### Your current environment Running on 2xH100 NVL with the latest master branch (16.04.2025) code. ``` extraArgs: [ # "--enforce-eager", # disable cuda graphs. lowers token/s. reduce memory. # "--max_num_seqs=1", # # Number of concurrent requests. reduce kv cache size. "--gpu-memory-utilization=0.99", "--max-model-len=1000", # context length # reduce kv cache size. "--tensor-parallel-size=2", # "--quantization=fp8", # quantization of the model weights "--kv-cache-dtype=fp8" #dynamic quantization of the KV cache ] ``` I tried multile combinations of the above parameters (including the ones commented), all of which result in this ``` VllmWorker rank=1 pid=254) torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.25 GiB. GPU 1 has a total capacity of 93.02 GiB of which 1.18 GiB is free. Process 2752205 has 91.82 GiB memory in use. Of the allocated memory 90.63 GiB is allocated by PyTorch, and 120.54 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-var...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: text length # reduce kv cache size. "--tensor-parallel-size=2", # "--quantization=fp8", # quantization of the model weights "--kv-cache-dtype=fp8" #dynamic quantization of the KV cache ] ``` I tried multile combinations...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Bug]: meta-llama/Llama-4-Scout-17B-16E-Instruct not supported on VLLM, 2xH100 NVL 196GB bug ### Your current environment Running on 2xH100 NVL with the latest master branch (16.04.2025) code. ``` extraArgs: [ # "--enfor...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: mory. # "--max_num_seqs=1", # # Number of concurrent requests. reduce kv cache size. "--gpu-memory-utilization=0.99", "--max-model-len=1000", # context length # reduce kv cache size. "--tensor-parallel-size=2", # "--qua...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r: CUDA out of memory. Tried to allocate 1.25 GiB. GPU 1 has a total capacity of 93.02 GiB of which 1.18 GiB is free. Process 2752205 has 91.82 GiB memory in use. Of the allocated memory 90.63 GiB is allocated by PyTorc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: meta-llama/Llama-4-Scout-17B-16E-Instruct not supported on VLLM, 2xH100 NVL 196GB bug ### Your current environment Running on 2xH100 NVL with the latest master branch (16.04.2025) code. ``` extraArgs: [ # "--enfo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
