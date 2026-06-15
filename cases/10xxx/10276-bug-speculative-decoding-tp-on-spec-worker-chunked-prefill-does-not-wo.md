# vllm-project/vllm#10276: [Bug]: Speculative Decoding + TP on Spec Worker + Chunked Prefill does not work.

| 字段 | 值 |
| --- | --- |
| Issue | [#10276](https://github.com/vllm-project/vllm/issues/10276) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding + TP on Spec Worker + Chunked Prefill does not work.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The server will start but fail immediately on any prompt when spec decoding, tp on spec model, and chunked prefill are enabled together. Sample error: ``` vllm serve meta-llama/Llama-3.1-405B-Instruct-FP8 --tensor-parallel-size 8 --max-num-seqs 32 --block-size 32 --speculative-model meta-llama/Llama-3.1-8B-Instruct --num-speculative-tokens 8 --gpu-memory-utilization 0.98 --use-v2-block-manager --distributed-executor-backend ray --enable-chunked-prefill --max-num-batched-tokens 4096 --max-model-len 32768 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#10232 [Bugfix] Fix for Spec model TP + Chunked Prefill

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: gether. Sample error: ``` vllm serve meta-llama/Llama-3.1-405B-Instruct-FP8 --tensor-parallel-size 8 --max-num-seqs 32 --block-size 32 --speculative-model meta-llama/Llama-3.1-8B-Instruct --num-speculative-tokens 8 --gp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Speculative Decoding + TP on Spec Worker + Chunked Prefill does not work. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The server will start but fail immediately on a
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: u-memory-utilization 0.98 --use-v2-block-manager --distributed-executor-backend ray --enable-chunked-prefill --max-num-batched-tokens 4096 --max-model-len 32768 ``` ### Before submitting a new issue... - [X] Make sure y...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10232](https://github.com/vllm-project/vllm/pull/10232) | closes_keyword | 0.95 | [Bugfix] Fix for Spec model TP + Chunked Prefill | FIX #10276 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
