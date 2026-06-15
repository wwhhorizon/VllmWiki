# vllm-project/vllm#7767: [Bug]: for mistral-7B, local batch inference mode causes OOM error, while serving mode does not cause error

| 字段 | 值 |
| --- | --- |
| Issue | [#7767](https://github.com/vllm-project/vllm/issues/7767) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: for mistral-7B, local batch inference mode causes OOM error, while serving mode does not cause error

### Issue 正文摘录

### Your current environment vllm version: 0.5.4 gpu 24GB memory ### 🐛 Describe the bug ```bash CUDA_VISIBLE_DEVICES=0 vllm serve mistralai/Mistral-7B-Instruct-v0.3 --api-key yyy --port 1704 --gpu_memory_utilization 0.95 --max_model_len 8000 --dtype bfloat16 ``` works fine. ```bash CUDA_VISIBLE_DEVICES=0 vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --api-key yyy --port 1704 --gpu_memory_utilization 0.95 --max_model_len 8000 --dtype bfloat16 ``` also works fine. however, ```python llm = LLM(model= mistralai/Mistral-7B-Instruct-v0.3, dtype='bfloat16', max_model_len=8000, tensor_parallel_size=torch.cuda.device_count(), gpu_memory_utilization=0.95 ) responses = llm.generate(prompts, sampling_params ) ``` will always cause error of OOM, no mater on single gpu (24GB) or on two gpus.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: key yyy --port 1704 --gpu_memory_utilization 0.95 --max_model_len 8000 --dtype bfloat16 ``` works fine. ```bash CUDA_VISIBLE_DEVICES=0 vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --api-key yyy --port 1704 --gpu_mem...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g mode does not cause error bug;stale ### Your current environment vllm version: 0.5.4 gpu 24GB memory ### 🐛 Describe the bug ```bash CUDA_VISIBLE_DEVICES=0 vllm serve mistralai/Mistral-7B-Instruct-v0.3 --api-key yyy --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: truct-v0.3 --api-key yyy --port 1704 --gpu_memory_utilization 0.95 --max_model_len 8000 --dtype bfloat16 ``` works fine. ```bash CUDA_VISIBLE_DEVICES=0 vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --api-key yyy --po...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t vllm version: 0.5.4 gpu 24GB memory ### 🐛 Describe the bug ```bash CUDA_VISIBLE_DEVICES=0 vllm serve mistralai/Mistral-7B-Instruct-v0.3 --api-key yyy --port 1704 --gpu_memory_utilization 0.95 --max_model_len 8000 --dt...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: for mistral-7B, local batch inference mode causes OOM error, while serving mode does not cause error bug;stale ### Your current environment vllm version: 0.5.4 gpu 24GB memory ### 🐛 Describe the bug ```bash CUDA_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
