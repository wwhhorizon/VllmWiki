# vllm-project/vllm#14644: [Doc]: GPU memory conflict between sleeping and woken vLLM instances

| 字段 | 值 |
| --- | --- |
| Issue | [#14644](https://github.com/vllm-project/vllm/issues/14644) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: GPU memory conflict between sleeping and woken vLLM instances

### Issue 正文摘录

### 📚 The doc issue I can not tell from the documentation whether the following is an issue. In fact, I do not know at all whether it is an issue. I am told what a vLLM instance, when it wakes up, resumes using the same GPU memory addresses for model tensors and KV cache that it did before sleep. I am also told that this is not necessarily so. So I am confused. Following is a scenario that explores the question. One machine, one GPU, no MIG. 1. Create vLLM instance A. Let it get to readiness. 2. Put instance A to sleep. Its CUDA graph will remain in GPU memory. 3. In a separate process, create vLLM isntance B. Let it get to readiness. 4. Put instance B to sleep. Its CUDA graph will remain in GPU memory. 5. /wake_up instance A. Do its model tensors or KV cache space overlap with B's CUDA graph? Admittedly, this one scenario does not fully explore the issue. A vLLM instance A configured to use 90% of the GPU's memory might never touch the addresses that instance B uses for its CUDA graph, as far as I understand. To explore the issue more completely, in addition to instance B, create and sleep several more instances (but not so many that A can't be woken when the others are sleeping)...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LLM instance A. Let it get to readiness. 2. Put instance A to sleep. Its CUDA graph will remain in GPU memory. 3. In a separate process, create vLLM isntance B. Let it get to readiness. 4. Put instance B to sleep. Its C...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Doc]: GPU memory conflict between sleeping and woken vLLM instances documentation;stale ### 📚 The doc issue I can not tell from the documentation whether the following is an issue. In fact, I do not know at all whether...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tance, when it wakes up, resumes using the same GPU memory addresses for model tensors and KV cache that it did before sleep. I am also told that this is not necessarily so. So I am confused. Following is a scenario tha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: memory conflict between sleeping and woken vLLM instances documentation;stale ### 📚 The doc issue I can not tell from the documentation whether the following is an issue. In fact, I do not know at all whether it is an i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance attention_kv_cache;model_support cache;cuda 📚 The doc issue

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
