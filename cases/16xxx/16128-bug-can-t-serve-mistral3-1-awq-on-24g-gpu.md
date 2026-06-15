# vllm-project/vllm#16128: [Bug]: Can't serve mistral3.1-AWQ on 24G GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#16128](https://github.com/vllm-project/vllm/issues/16128) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 32; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't serve mistral3.1-AWQ on 24G GPU

### Issue 正文摘录

### Your current environment vllm `0.8.1` ### 🐛 Describe the bug Can I serve mistral3.1-awq (`OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym `)model on A10 GPU (24G)? I get OOM for the following command: 1. command ``` HF_TOKEN=XX VLLM_USE_V1=0 vllm serve OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym --dtype half \ --tensor-parallel-size 1 --max-model-len 4096 --gpu-memory-utilization 0.95 --distributed-executor-backend mp \ --served-model-name mistral --tokenizer-mode mistral --config-format mistral --load_format mistral \ --hf-config-path mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tokenizer mistralai/Mistral-Small-3.1-24B-Instruct-2503 ``` 1.1. error: ``` torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 320.00 MiB. GPU 0 has a total capacity of 21.99 GiB of which 19.38 MiB is free. Including non-PyTorch memory, this process has 21.96 GiB memory in use. Of the allocated memory 21.67 GiB is allocated by PyTorch, and 5.59 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Managemen...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: awq (`OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym `)model on A10 GPU (24G)? I get OOM for the following command: 1. command ``` HF_TOKEN=XX VLLM_USE_V1=0 vllm serve OPEA/Mistral-Small-3.1-24B-Instruc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: g Can I serve mistral3.1-awq (`OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym `)model on A10 GPU (24G)? I get OOM for the following command: 1. command ``` HF_TOKEN=XX VLLM_USE_V1=0 vllm serve OPEA/Mist...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: .8.1` ### 🐛 Describe the bug Can I serve mistral3.1-awq (`OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym `)model on A10 GPU (24G)? I get OOM for the following command: 1. command ``` HF_TOKEN=XX VLLM_US...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: CUDA out of memory. Tried to allocate 320.00 MiB. GPU 0 has a total capacity of 21.99 GiB of which 19.38 MiB is free. Including non-PyTorch memory, this process has 21.96 GiB memory in use. Of the allocated memory 21.67...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ax-model-len 4096 --gpu-memory-utilization 0.95 --distributed-executor-backend mp \ --served-model-name mistral --tokenizer-mode mistral --config-format mistral --load_format mistral \ --hf-config-path mistralai/Mistral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
