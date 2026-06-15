# vllm-project/vllm#19777: [Bug]: nixl handshake is slow and can accumulate in a batch of requests where each request is pulling from a different prefill node

| 字段 | 值 |
| --- | --- |
| Issue | [#19777](https://github.com/vllm-project/vllm/issues/19777) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nixl handshake is slow and can accumulate in a batch of requests where each request is pulling from a different prefill node

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug So I am seeing that the NIXL handshake can take up to 9 sec for my system on H100s in a 4P2D scenario. This can add up if the requests that are batched together come from different prefill nodes. Imagine a 32P1D situation, and I sent a 32 concurrent requests where r1 -> p1, r2 -> p2, ..., r32 -> p32. Then when they all hit D, the handshake happens during the first fwd pass and can take 32 * 9 = 288 seconds. The issue manifests itself when we use ray compiled graph as there is a timeout set to ~300s (or at least the intention is with this PR to set it to 300s by default). This puts the engine in a brittle situation if you do not warm up the system gradually. The workaround right now is to warm up in a way that does not trigger timeout. Making sure each D knows about all the Ps before sending requests. This issue will come up again when you do aggressive autoscaling on Decode and the newly added decode instance should know about all the Ps before hand. ```bash #!/bin/bash set -xe # Models to run MODELS=( "Qwen/Qwen2.5-0.5B-Instruct" ) export VLLM_LOGGING_LEVEL=debug # Number of prefill and decode instances to create NUM_PREFILL_INS...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: nixl handshake is slow and can accumulate in a batch of requests where each request is pulling from a different prefill node bug;stale ### Your current environment ### 🐛 Describe the bug So I am seeing that the N...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: am seeing that the NIXL handshake can take up to 9 sec for my system on H100s in a 4P2D scenario. This can add up if the requests that are batched together come from different prefill nodes. Imagine a 32P1D situation, a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ould know about all the Ps before hand. ```bash #!/bin/bash set -xe # Models to run MODELS=( "Qwen/Qwen2.5-0.5B-Instruct" ) export VLLM_LOGGING_LEVEL=debug # Number of prefill and decode instances to create NUM_PREFILL_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: take 32 * 9 = 288 seconds. The issue manifests itself when we use ray compiled graph as there is a timeout set to ~300s (or at least the intention is with this PR to set it to 300s by default). This puts the engine in a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: e echo "$($SMI_BIN -l | grep GPU | wc -l)" fi } # Function to run tests for a specific model run_tests_for_model() { local model_name=$1 echo "================================" echo "Testing model: $model_name" echo "==...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
