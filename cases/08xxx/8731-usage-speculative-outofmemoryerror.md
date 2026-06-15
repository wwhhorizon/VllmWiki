# vllm-project/vllm#8731: [Usage]: speculative OutOfMemoryError:

| 字段 | 值 |
| --- | --- |
| Issue | [#8731](https://github.com/vllm-project/vllm/issues/8731) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: speculative OutOfMemoryError:

### Issue 正文摘录

### Your current environment I deploy Qwen2.5-32B-Instruct with speculative_model Qwen2.5-7B-Instruct, and my gpu is NVIDIA A100-SXM4-40GB; And get OutOfMemoryError; In my opinion，32B model will be deployed in 4 GPUs due to tensor parallelism and will allocate about 16G memory；However, I am not sure how the speculative model is deployed. Will it be deployed on GPU0? But GPU0 should still have around 24GB of memory, which should be sufficient to deploy a 7B model. ``` CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9000 --model Qwen2.5-32B-Instruct -tp 4 --max-model-len 1000 --speculative_model Qwen2.5-7B-Instruct --use-v2-block-manager --num_speculative_tokens 5 --speculative-max-model-len 1000 --gpu_memory_utilization 0.9 ``` ``` torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 72.00 MiB. GPU 0 has a total capacity of 39.56 GiB of which 60.81 MiB is free. Process 3179876 has 1.62 GiB memory in use. Process 3179877 has 1.62 GiB memory in use. Including non-PyTorch memory, this process has 34.61 GiB memory in use. Process 3179875 has 1.62 GiB memory in use. Of the allocated memory 28.75 GiB is allocated by PyTorch, with 2...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: nstruct with speculative_model Qwen2.5-7B-Instruct, and my gpu is NVIDIA A100-SXM4-40GB; And get OutOfMemoryError; In my opinion，32B model will be deployed in 4 GPUs due to tensor parallelism and will allocate about 16G...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ? But GPU0 should still have around 24GB of memory, which should be sufficient to deploy a 7B model. ``` CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9000 --model Qwen2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: speculative OutOfMemoryError: usage;stale ### Your current environment I deploy Qwen2.5-32B-Instruct with speculative_model Qwen2.5-7B-Instruct, and my gpu is NVIDIA A100-SXM4-40GB; And get OutOfMemoryError; In...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 4 --max-model-len 1000 --speculative_model Qwen2.5-7B-Instruct --use-v2-block-manager --num_speculative_tokens 5 --speculative-max-model-len 1000 --gpu_memory_utilization 0.9 ``` ``` torch.OutOfMemoryError: CUDA out of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ive OutOfMemoryError: usage;stale ### Your current environment I deploy Qwen2.5-32B-Instruct with speculative_model Qwen2.5-7B-Instruct, and my gpu is NVIDIA A100-SXM4-40GB; And get OutOfMemoryError; In my opinion，32B m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
