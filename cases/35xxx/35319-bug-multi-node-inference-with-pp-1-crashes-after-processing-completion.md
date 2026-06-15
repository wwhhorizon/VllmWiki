# vllm-project/vllm#35319: [Bug]: Multi-Node inference with PP > 1 crashes after processing completions request with non-None `logprobs` parameter.

| 字段 | 值 |
| --- | --- |
| Issue | [#35319](https://github.com/vllm-project/vllm/issues/35319) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-Node inference with PP > 1 crashes after processing completions request with non-None `logprobs` parameter.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There are a lot of *seemingly* related issues, but I couldn't find the one with the exact same context, so I opened up the new one. It looks like multi-node inference via Ray doesn't work correctly for PP > 1, when requests specify non-null "logprobs". For a minimal reproducible example we spin up Ray cluster on two nodes with one H200 each and launch some small model with TP=1 PP=2: 1. Run it on a head node: ```bash export HEAD_POD_IP= # 0. Download 4B model uv run \ --no-project \ --python 3.10 \ --with "huggingface_hub" \ hf download \ --repo-type model "Qwen/Qwen3-4B-Thinking-2507" \ --local-dir /root/.cache/huggingface # 1. https://github.com/vllm-project/vllm/pull/33116 if [ -f /etc/ld.so.conf.d/00-cuda-compat.conf ]; then mv /etc/ld.so.conf.d/{00-,}cuda-compat.conf && ldconfig; fi # 2. Set all the necessary variables export RAY_EXPERIMENTAL_NOSET_CUDA_VISIBLE_DEVICES=1 export NCCL_DEBUG=TRACE export NCCL_DEBUG_SUBSYS=ALL export NCCL_DEBUG_TIMESTAMP_LEVELS=ALL export NCCL_DEBUG_TIMESTAMP_FORMAT="[%F %T.%9f] " export NCCL_NET="Socket" export NCCL_IB_DISABLE=1 export NCCL_NET_GDR_LEVEL=0 export NCCL_NET_PLUGIN=none export NCC...

## 现有链接修复摘要

#35484 [WIP][Bugfix] Fix multi-node PP crash with logprobs due to pinned memory serialization

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: pin up Ray cluster on two nodes with one H200 each and launch some small model with TP=1 PP=2: 1. Run it on a head node: ```bash export HEAD_POD_IP= # 0. Download 4B model uv run \ --no-project \ --python 3.10 \ --with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: de inference via Ray doesn't work correctly for PP > 1, when requests specify non-null "logprobs". For a minimal reproducible example we spin up Ray cluster on two nodes with one H200 each and launch some small model wi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e we spin up Ray cluster on two nodes with one H200 each and launch some small model with TP=1 PP=2: 1. Run it on a head node: ```bash export HEAD_POD_IP= # 0. Download 4B model uv run \ --no-project \ --python 3.10 \ -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ]: Multi-Node inference with PP > 1 crashes after processing completions request with non-None `logprobs` parameter. bug ### Your current environment ### 🐛 Describe the bug There are a lot of *seemingly* related issues,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pus=1 RAY_CGRAPH_get_timeout=30 vllm serve \ --distributed-executor-backend ray \ --tensor-parallel-size 1 \ --pipeline-parallel-size 2 \ --model /root/.cache/huggingface \ --enforce-eager ``` 3. After server spins up o...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35484](https://github.com/vllm-project/vllm/pull/35484) | closes_keyword | 0.95 | [WIP][Bugfix] Fix multi-node PP crash with logprobs due to pinned memory serialization | Fixes #35319 When logprobs are enabled with pipeline parallelism (PP > 1) on multi-node Ray, the `ModelRunnerOutput` returned by `execute_model_ray` contains numpy arrays and torc |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
