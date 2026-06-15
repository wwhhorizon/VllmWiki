# vllm-project/vllm#4806: [Performance]: Qwen 7b chat model, under 128 concurrency, the CPU utilization rate is 100%, and the GPU SM utilization rate is only about 60%-75%. Is it a CPU bottleneck?

| 字段 | 值 |
| --- | --- |
| Issue | [#4806](https://github.com/vllm-project/vllm/issues/4806) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Qwen 7b chat model, under 128 concurrency, the CPU utilization rate is 100%, and the GPU SM utilization rate is only about 60%-75%. Is it a CPU bottleneck?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am using vllm to deploy the qwen 7b chat model service. In a very high concurrency scenario, such as 128 concurrency, I found that the CPU utilization reached 100%, but I saw the GPU utilization rate is less than 60% My question is, because a lot of vllm's scheduling and calculation logic is implemented by Python coroutines, it can only use the computing power of a single CPU. In a scenario like this with 128 concurrency, is the CPU becoming a computing bottleneck, causing GPU CUDA to be unable to achieve higher performance? Model download address：https://huggingface.co/Qwen/Qwen-7B-Chat/tree/main 1. For sever scenario ![image](https://github.com/vllm-project/vllm/assets/94596925/28d326a1-9d7a-437b-b503-6db4dc559a70) ![image](https://github.com/vllm-project/vllm/assets/94596925/ccda7dcc-b793-4d18-a7bf-096e05be10ff) 2. For offline batch inference scenario ![image](https://github.com/vllm-project/vllm/assets/94596925/92f3e4cd-dce5-4952-89d2-e23622df6d55) ![image](https://github.com/vllm-project/vllm/assets/94596925/37263e7f-3a20-4bbd-9485-b4d29f0c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ct/vllm/assets/94596925/37263e7f-3a20-4bbd-9485-b4d29f0c04a2) ```python import random import json from vllm import LLM, SamplingParams conc = 128 jsonl_path = "xxx.jsonl" # 从jsonl文件中读取concurrent条数据 all_prompts = [] with...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Performance]: Qwen 7b chat model, under 128 concurrency, the CPU utilization rate is 100%, and the GPU SM utilization rate is only about 60%-75%. Is it a CPU bottleneck? performance;stale ### Proposal to improve perfor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: el, under 128 concurrency, the CPU utilization rate is 100%, and the GPU SM utilization rate is only about 60%-75%. Is it a CPU bottleneck? performance;stale ### Proposal to improve performance _No response_ ### Report...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lization rate is only about 60%-75%. Is it a CPU bottleneck? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: =2.19.3 [pip3] nvidia-nccl-cu12==2.19.3 [pip3] torch==2.2.2+cu118 [pip3] triton==2.2.0 [pip3] vllm-nccl-cu11==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu11 2.19.3 pypi_0 pypi [conda] nvidia-nccl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
