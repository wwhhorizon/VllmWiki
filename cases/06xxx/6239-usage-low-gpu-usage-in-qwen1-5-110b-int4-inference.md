# vllm-project/vllm#6239: [Usage]: low GPU usage in qwen1.5 110b int4 inference

| 字段 | 值 |
| --- | --- |
| Issue | [#6239](https://github.com/vllm-project/vllm/issues/6239) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: low GPU usage in qwen1.5 110b int4 inference

### Issue 正文摘录

### Your current environment When I try to inference qwen1.5 110b int4 (https://modelscope.cn/models/qwen/Qwen1.5-110B-Chat-GPTQ-Int4) with vllm(0.4.2) AsyncLlmEngine on A100 80G, I find the real batch size is just 2. I set the params as follows: gpu_memory_utilization = 0.95 max_parallel_loading_workers = 4 swap_space = 4 max_model_len = 1024 max_num_seqs = 8 I don't use beam search. The prompt is 330 tokens, and the output is about 5 tokens. When the QPS=1, each request takes about 0.45 seconds. When the QPS=2, each request takes about 0.70 seconds. When the QPS=4, each request takes about 1.4 seconds. When the QPS=8, each request takes about 2.9 seconds. And according to the output metrics(vllm.sequence.RequestMetrics), the real batch size is just 2. How to improve it? Thanks! ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s! ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: els/qwen/Qwen1.5-110B-Chat-GPTQ-Int4) with vllm(0.4.2) AsyncLlmEngine on A100 80G, I find the real batch size is just 2. I set the params as follows: gpu_memory_utilization = 0.95 max_parallel_loading_workers = 4 swap_s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: low GPU usage in qwen1.5 110b int4 inference usage;stale ### Your current environment When I try to inference qwen1.5 110b int4 (https://modelscope.cn/models/qwen/Qwen1.5-110B-Chat-GPTQ-Int4) with vllm(0.4.2) A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: low GPU usage in qwen1.5 110b int4 inference usage;stale ### Your current environment When I try to inference qwen1.5 110b int4 (https://modelscope.cn/models/qwen/Qwen1.5-110B-Chat-GPTQ-Int4) with vllm(0.4.2) A...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Usage]: low GPU usage in qwen1.5 110b int4 inference usage;stale ### Your current environment When I try to inference qwen1.5 110b int4 (https://modelscope.cn/models/qwen/Qwen1.5-110B-Chat-GPTQ-Int4) with vllm(0.4.2) A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
