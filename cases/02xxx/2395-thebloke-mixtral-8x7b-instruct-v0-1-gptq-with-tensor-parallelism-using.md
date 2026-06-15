# vllm-project/vllm#2395: TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ with tensor parallelism using 2 A10 GPU's

| 字段 | 值 |
| --- | --- |
| Issue | [#2395](https://github.com/vllm-project/vllm/issues/2395) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ with tensor parallelism using 2 A10 GPU's

### Issue 正文摘录

Hi, I was able to run _TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ_ model on 2 A10 gpus on AWS Sagemaker. I was using _ml.g5.12xlarge_ instance type. Command to run the code `python3 -m vllm.entrypoints.openai.api_server --model TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ --dtype float16 --max-model-len 1024 --gpu-memory-utilization 0.95 --tensor-parallel-size 2` But when I am trying to run the same model on AWS EKS k8's pod with 2 A10 GPUs, it's getting failed. It was throwing following error `torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 112.00 MiB. GPU 0 has a total capacty of 21.99 GiB of which 45.00 MiB is free. Process 40317 has 21.92 GiB memory in use. Of the allocated memory 20.02 GiB is allocated by PyTorch, and 260.12 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF` After debugging, i realized that the model is running in the **eager_mode**. Here is the working command `python3 -m vllm.entrypoints.openai.api_server --model TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ --dtype float16 --max-model-len 10...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nts.openai.api_server --model TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ --dtype float16 --max-model-len 1024 --gpu-memory-utilization 0.95 --tensor-parallel-size 2` But when I am trying to run the same model on AWS EKS k...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ with tensor parallelism using 2 A10 GPU's stale Hi, I was able to run _TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ_ model on 2 A10 gpus on AWS Sagemaker. I was using _ml.g5.12xlarge...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ixtral-8x7B-Instruct-v0.1-GPTQ with tensor parallelism using 2 A10 GPU's stale Hi, I was able to run _TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ_ model on 2 A10 gpus on AWS Sagemaker. I was using _ml.g5.12xlarge_ instance...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el_support;quantization;scheduler_memory cuda;quantization oom dtype;env_dependency Hi,
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: d_parallel;model_support;quantization;scheduler_memory cuda;quantization oom dtype;env_dependency Hi,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
