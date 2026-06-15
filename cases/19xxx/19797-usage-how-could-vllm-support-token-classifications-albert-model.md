# vllm-project/vllm#19797: [Usage]: How could vllm support token classifications(albert model)?

| 字段 | 值 |
| --- | --- |
| Issue | [#19797](https://github.com/vllm-project/vllm/issues/19797) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How could vllm support token classifications(albert model)?

### Issue 正文摘录

### Your current environment run: python3 -m vllm.entrypoints.openai.api_server \ --model "/home/zhanghanwen07/disfluency-detection/checkpoint/temp" \ --tensor-parallel-size 1 \ --served-model-name "albert_base" \ --host 0.0.0.0 \ --hf_overrides '{"architectures": ["AlbertForTokenClassification"]}' \ --gpu-memory-utilization 0.2 \ --task classify \ --port 8084 error: ![Image](https://github.com/user-attachments/assets/61fe31a6-4616-4143-9f68-60155e2d6251) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 1) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How could vllm support token classifications(albert model)? usage;stale ### Your current environment run: python3 -m vllm.entrypoints.openai.api_server \ --model "/home/zhanghanwen07/disfluency-detection/checkp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed-model-name "albert_base" \ --host 0.0.0.0 \ --hf_overrides '{"architectures": ["AlbertForTokenClassification"]}' \ --gpu-memory-utilization 0.2 \ --task classify \ --port 8084 error: ![Image](https://github.com/user-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sage]: How could vllm support token classifications(albert model)? usage;stale ### Your current environment run: python3 -m vllm.entrypoints.openai.api_server \ --model "/home/zhanghanwen07/disfluency-detection/checkpoi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
