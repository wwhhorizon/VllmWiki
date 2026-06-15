# vllm-project/vllm#17979: [Bug]: available VRAM calculation bug in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#17979](https://github.com/vllm-project/vllm/issues/17979) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: available VRAM calculation bug in V1

### Issue 正文摘录

### Your current environment VLLM openai docker is used: vllm/vllm-openai:v0.8.5.post1 ### 🐛 Describe the bug Running more than 1 vllm instance on a single GPU with VLLM V1 enabled fails. The same setup with `VLLM_USE_V1=False` works. The issue is that VLLM V1 `total_allocated_bytes` mistakenly includes memory consumed by other vLLM instances. The first model starts without an error. The second instance fails due to vram OOO. The documentation on [--gpu-memory-utilization](https://docs.vllm.ai/en/stable/serving/engine_args.html#cacheconfig) it says: > The fraction of GPU memory to be used for the model executor, which can range from 0 to 1. For example, a value of 0.5 would imply 50% GPU memory utilization. If unspecified, will use the default value of 0.9. This is a per-instance limit, and only applies to the current vLLM instance. It does not matter if you have another vLLM instance running on the same GPU. For example, if you have two vLLM instances running on the same GPU, you can set the GPU memory utilization to 0.5 for each instance. > > Default: 0.9 So V1 memory management should reflect this, or update the documentation for V1's new behaviour (of using existing GPU availa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: VRAM calculation bug in V1 bug ### Your current environment VLLM openai docker is used: vllm/vllm-openai:v0.8.5.post1 ### 🐛 Describe the bug Running more than 1 vllm instance on a single GPU with VLLM V1 enabled fails....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mistakenly includes memory consumed by other vLLM instances. The first model starts without an error. The second instance fails due to vram OOO. The documentation on [--gpu-memory-utilization](https://docs.vllm.ai/en/st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m/vllm-openai:v0.8.5.post1 \ --port 8000 \ --model HuggingFaceTB/SmolLM-135M \ --gpu-memory-utilization 0.3 \ --max-num-seqs 256 \ --tensor-parallel-size 1 docker run -d --runtime nvidia --gpus 1 \ --env "HUGGING_FACE_H...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: stable/serving/engine_args.html#cacheconfig) it says: > The fraction of GPU memory to be used for the model executor, which can range from 0 to 1. For example, a value of 0.5 would imply 50% GPU memory utilization. If u...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ingle GPU with VLLM V1 enabled fails. The same setup with `VLLM_USE_V1=False` works. The issue is that VLLM V1 `total_allocated_bytes` mistakenly includes memory consumed by other vLLM instances. The first model starts...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
