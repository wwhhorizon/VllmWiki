# vllm-project/vllm#20160: [Performance]: Query: Memory (VRAM vs. RAM) and Performance Implications of Scaling LoRA Adapters in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#20160](https://github.com/vllm-project/vllm/issues/20160) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Query: Memory (VRAM vs. RAM) and Performance Implications of Scaling LoRA Adapters in vLLM

### Issue 正文摘录

### Proposal to improve performance I would like to inquire about the resource allocation when deploying multiple LoRA adapters using vLLM. I am using the following command to serve the model: Generated bash CUDA_VISIBLE_DEVICES=7 vllm serve /home/gpuserver/Downloads/zzh/Qwen/Qwen2.5-VL-3B-Instruct \ --enable-lora \ --lora-modules lora1=/path/to/lora/sft lora2=/path/to/lora/sft Use code with caution. Bash My primary question is: as the number of LoRA adapters increases, which memory resource is primarily consumed—GPU memory (VRAM) or system memory (RAM)? Furthermore, I am curious about the performance. If there is a mechanism that swaps LoRA adapters from system memory to VRAM on demand, can a reasonable level of inference speed still be guaranteed? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: LLM. I am using the following command to serve the model: Generated bash CUDA_VISIBLE_DEVICES=7 vllm serve /home/gpuserver/Downloads/zzh/Qwen/Qwen2.5-VL-3B-Instruct \ --enable-lora \ --lora-modules lora1=/path/to/lora/s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: LoRA adapters using vLLM. I am using the following command to serve the model: Generated bash CUDA_VISIBLE_DEVICES=7 vllm serve /home/gpuserver/Downloads/zzh/Qwen/Qwen2.5-VL-3B-Instruct \ --enable-lora \ --lora-modules...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: level of inference speed still be guaranteed? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: of LoRA adapters increases, which memory resource is primarily consumed—GPU memory (VRAM) or system memory (RAM)? Furthermore, I am curious about the performance. If there is a mechanism that swaps LoRA adapters from sy...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nd Performance Implications of Scaling LoRA Adapters in vLLM performance;stale ### Proposal to improve performance I would like to inquire about the resource allocation when deploying multiple LoRA adapters using vLLM....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
