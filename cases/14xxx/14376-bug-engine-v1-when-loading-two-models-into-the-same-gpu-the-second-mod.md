# vllm-project/vllm#14376: [Bug]: Engine V1 When loading two models into the same GPU the second model requires more memory allocation than the first

| 字段 | 值 |
| --- | --- |
| Issue | [#14376](https://github.com/vllm-project/vllm/issues/14376) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Engine V1 When loading two models into the same GPU the second model requires more memory allocation than the first

### Issue 正文摘录

### Your current environment How I`m loading the models: ``` docker run \ --runtime nvidia \ -e VLLM_USE_V1=1 \ --gpus 0 \ --ipc=host \ -v "${HF_HOME}:/root/.cache/huggingface" \ vllm/vllm-openai:latest \ --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \ --max-model-len 1024 \ --gpu-memory-utilization 0.2 ``` ### 🐛 Describe the bug I'm using Docker on a virtual machine with an L40S that has 48GB VRAM to run vllm. If I load a small model such as **TinyLlama/TinyLlama-1.1B-Chat-v1.0 ** into memory and allocate 20% (9GB of VRAM) via --gpu-memory-utilization parameter, the model works fine. My issue is that the same config doesn't work for a second identical model simultaneously (I'm testing running more than one model on the same GPU). If I allocate 20% for the second model, I get the error below: ``` ERROR 03-05 13:46:50 core.py:291] ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine. ``` But if I allocate 20% to the first model and 30% for the second model, it works. But if I try to allocate 30% for the first model and 30% to the second, again I run into out of memory issues. Why does the first model interfere with...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Engine V1 When loading two models into the same GPU the second model requires more memory allocation than the first bug ### Your current environment How I`m loading the models: ``` docker run \ --runtime nvidia \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: irtual machine with an L40S that has 48GB VRAM to run vllm. If I load a small model such as **TinyLlama/TinyLlama-1.1B-Chat-v1.0 ** into memory and allocate 20% (9GB of VRAM) via --gpu-memory-utilization parameter, the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: first bug ### Your current environment How I`m loading the models: ``` docker run \ --runtime nvidia \ -e VLLM_USE_V1=1 \ --gpus 0 \ --ipc=host \ -v "${HF_HOME}:/root/.cache/huggingface" \ vllm/vllm-openai:latest \ --mo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: RROR 03-05 13:46:50 core.py:291] ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine. ``` But if I allocate 20% to the first model and 30% for the s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 3-05 13:46:50 core.py:291] ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine. ``` But if I allocate 20% to the first model and 30% for the second...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
