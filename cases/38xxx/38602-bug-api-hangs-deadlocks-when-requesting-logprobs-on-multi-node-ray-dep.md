# vllm-project/vllm#38602: [Bug] API hangs/deadlocks when requesting logprobs on multi-node Ray deployment (PP=2, TP=8)

| 字段 | 值 |
| --- | --- |
| Issue | [#38602](https://github.com/vllm-project/vllm/issues/38602) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] API hangs/deadlocks when requesting logprobs on multi-node Ray deployment (PP=2, TP=8)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am encountering a consistently reproducible deadlock/hang issue while using the vLLM multi-node API service. When I send standard text generation requests to the /v1/completions endpoint, the dual-node GPUs return results normally and quickly, even if the prompt is very long. However, the moment I include logprobs in the request parameters, the API request hangs indefinitely. During this time, GPU utilization remains stuck at 0%. **vLLM Deployment Command: (Qwen3-30B model)** ··· vllm serve --model $MODEL_PATH \ --served-model-name $MODEL_NAME \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --distributed-executor-backend ray \ --trust-remote-code \ --host 0.0.0.0 \ --port 8000 \ --gpu-memory-utilization 0.75 \ --max-num-seqs 128 \ --max-num-batched-tokens 8192 \ --max-model-len 4096 ··· **Request Method (Without logprobs - returns results quickly):** ··· curl -s -X POST http://127.0.0.1:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "'$MODEL_NAME'", "prompt": "How are you? What is your name?", "max_tokens": 1024 }' ··· **Request Method (With logprobs - hangs indefinitely):** curl -s -X POST...

## 现有链接修复摘要

#41218 fix: convert LogprobsLists to lists for cross node Ray transport (#38602)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ment ### 🐛 Describe the bug I am encountering a consistently reproducible deadlock/hang issue while using the vLLM multi-node API service. When I send standard text generation requests to the /v1/completions endpoint, t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nvironment Information:** -ray == 2.51.1 -vllm == 0.17.1 -torch == 2.10 -CUDA == 12.8 Hardware: 2x nodes with 8x H100 GPUs each (Ray cluster is already started). ### Before submitting a new issue... - [x] Make sure you...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: time, GPU utilization remains stuck at 0%. **vLLM Deployment Command: (Qwen3-30B model)** ··· vllm serve --model $MODEL_PATH \ --served-model-name $MODEL_NAME \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug] API hangs/deadlocks when requesting logprobs on multi-node Ray deployment (PP=2, TP=8) bug ### Your current environment ### 🐛 Describe the bug I am encountering a consistently reproducible deadlock/hang issue whil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lel-size 8 \ --pipeline-parallel-size 2 \ --distributed-executor-backend ray \ --trust-remote-code \ --host 0.0.0.0 \ --port 8000 \ --gpu-memory-utilization 0.75 \ --max-num-seqs 128 \ --max-num-batched-tokens 8192 \ --...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41218](https://github.com/vllm-project/vllm/pull/41218) | closes_keyword | 0.95 | fix: convert LogprobsLists to lists for cross node Ray transport (#38602) | fix this case. I tested it before going further. - #29373, #37001: related multi node Ray crashes, different code paths. - #38602: the issue this closes. Bisect data and the experi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
