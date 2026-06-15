# vllm-project/vllm#26863: [Bug]: Cuda out of memory while inference for Qwen3-VL-4B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#26863](https://github.com/vllm-project/vllm/issues/26863) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cuda out of memory while inference for Qwen3-VL-4B-Instruct

### Issue 正文摘录

torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 232.00 MiB. GPU 0 has a total capacity of 23.57 GiB of which 154.25 MiB is free. Including non-PyTorch memory, this proce ss has 23.40 GiB memory in use. Of the allocated memory 22.88 GiB is allocated by PyTorch, and 188.29 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. I am using RTX 3090 machine and vLLM version was 0.11.0 python3 -m vllm.entrypoints.openai.api_server --model /home/deploy/Workspace/adkWorkSpace/models/krypton3-4b/ --max-model-len 32768 --tensor-parallel-size 1 --gpu-memory-utilization 0.95 --dtype float16 --port 7001 --trust-remote-code --rope-scaling '{"rope_type":"yarn","factor":3.0,"original_max_position_embeddings": 262144,"mrope_section":[24,20,20],"mrope_interleaved": true}' --enforce-eager --no-enable-chunked-prefill ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked que...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: CUDA out of memory. Tried to allocate 232.00 MiB. GPU 0 has a total capacity of 23.57 GiB of which 154.25 MiB is free. Including non-PyTorch memory, this proce ss has 23.40 GiB memory in use. Of the allocated memory 22....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Cuda out of memory while inference for Qwen3-VL-4B-Instruct bug;stale torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 232.00 MiB. GPU 0 has a total capacity of 23.57 GiB of which 154.25 MiB is free....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: model-len 32768 --tensor-parallel-size 1 --gpu-memory-utilization 0.95 --dtype float16 --port 7001 --trust-remote-code --rope-scaling '{"rope_type":"yarn","factor":3.0,"original_max_position_embeddings": 262144,"mrope_s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Cuda out of memory while inference for Qwen3-VL-4B-Instruct bug;stale torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 232.00 MiB. GPU 0 has a total capacity of 23.57 GiB of which 154.25 MiB is free....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Cuda out of memory while inference for Qwen3-VL-4B-Instruct bug;stale torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 232.00 MiB. GPU 0 has a total capacity of 23.57 GiB of which 154.25 MiB is free....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
