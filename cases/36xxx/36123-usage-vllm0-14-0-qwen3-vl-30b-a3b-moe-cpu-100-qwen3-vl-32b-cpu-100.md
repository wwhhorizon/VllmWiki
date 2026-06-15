# vllm-project/vllm#36123: [Usage]: 为什么vllm0.14.0部署Qwen3-VL-30B-A3B的MOE模型时，模型在初始化时CPU负载几乎100%，相同的环境部署Qwen3-VL-32B的模型时，不会出现CPU负载100%的情况

| 字段 | 值 |
| --- | --- |
| Issue | [#36123](https://github.com/vllm-project/vllm/issues/36123) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 为什么vllm0.14.0部署Qwen3-VL-30B-A3B的MOE模型时，模型在初始化时CPU负载几乎100%，相同的环境部署Qwen3-VL-32B的模型时，不会出现CPU负载100%的情况

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: 为什么vllm0.14.0部署Qwen3-VL-30B-A3B的MOE模型时，模型在初始化时CPU负载几乎100%，相同的环境部署Qwen3-VL-32B的模型时，不会出现CPU负载100%的情况 usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: 为什么vllm0.14.0部署Qwen3-VL-30B-A3B的MOE模型时，模型在初始化时CPU负载几乎100%，相同的环境部署Qwen3-VL-32B的模型时，不会出现CPU负载100%的情况 usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
