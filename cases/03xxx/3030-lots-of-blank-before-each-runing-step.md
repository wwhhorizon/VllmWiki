# vllm-project/vllm#3030: lots of blank before each runing step

| 字段 | 值 |
| --- | --- |
| Issue | [#3030](https://github.com/vllm-project/vllm/issues/3030) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;gemm_linear;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;moe;sampling |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> lots of blank before each runing step

### Issue 正文摘录

I use torch.profiler.profile() to profile mixtral based on vllm. And I found lots of blank before each runing step. ![S85Z22{PW)GZ0(E)4AH4AF1](https://uploads.linear.app/342cff15-f40f-4cf7-8bee-343d25adb534/5be37e8a-bfba-42c9-abb1-149bafcbffc1/9c2cc666-a755-4f82-bca0-b059875628a4?signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXRoIjoiLzM0MmNmZjE1LWY0MGYtNGNmNy04YmVlLTM0M2QyNWFkYjUzNC81YmUzN2U4YS1iZmJhLTQyYzktYWJiMS0xNDliYWZjYmZmYzEvOWMyY2M2NjYtYTc1NS00ZjgyLWJjYTAtYjA1OTg3NTYyOGE0IiwiaWF0IjoxNzA5MTAxMTAyLCJleHAiOjMzMjc5NjYxMTAyfQ.TeiuQmBrTyPbZWAeJUQkrEcwDqLjiXcKg7LaGB-NRNA) When i try to compare the time cost of vllm with that of tensorrt-llm. I found that tensorrt-llm is 1.5X faster than vllm. But by comparing the time cost of each component, including the attention, experts, all reduce. vllm and tensorrt-llm perform nearly the same. So I suppose that the blank before each runing step in vllm results in the slower perfomance. But I can found nothing to understand the occur of the blank. Can you give me some help? Here is the code to profile the mixtral ``` from vllm import LLM, SamplingParams import argparse import evaluate from datasets import load_dataset if __name__ == '__m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 9-abb1-149bafcbffc1/9c2cc666-a755-4f82-bca0-b059875628a4?signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXRoIjoiLzM0MmNmZjE1LWY0MGYtNGNmNy04YmVlLTM0M2QyNWFkYjUzNC81YmUzN2U4YS1iZmJhLTQyYzktYWJiMS0xNDliYWZjYmZmYzEvOWM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 00,top_k=1,top_p=1e-5,temperature=1) # Create an LLM. llm = LLM(model="/home/.cache/huggingface/hub/models--mistralai--Mixtral-8x7B-v0.1/snapshots/985aa055896a8f943d4a9f2572e6ea1341823841", tensor_parallel_size=8) # Gen...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: t by comparing the time cost of each component, including the attention, experts, all reduce. vllm and tensorrt-llm perform nearly the same. So I suppose that the blank before each runing step in vllm results in the slo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: lots of blank before each runing step stale I use torch.profiler.profile() to profile mixtral based on vllm. And I found lots of blank before each runing step. ![S85Z22{PW)GZ0(E)4AH4AF1](https://uploads.linear.app/342cf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lots of blank before each runing step stale I use torch.profiler.profile() to profile mixtral based on vllm. And I found lots of blank before each runing step. ![S85Z22{PW)GZ0(E)4AH4AF1](https://uploads.linear.app/342cf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
