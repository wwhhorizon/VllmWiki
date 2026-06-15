# vllm-project/vllm#30889: [CI Failure]: distributed-tests-h200

| 字段 | 值 |
| --- | --- |
| Issue | [#30889](https://github.com/vllm-project/vllm/issues/30889) |
| 状态 | closed |
| 标签 | torch.compile;stale;ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;moe |
| 子分类 | debug |
| Operator 关键词 | moe |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: distributed-tests-h200

### Issue 正文摘录

### Name of failing test python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen1.5-MoE-A2.7B --tp-size=1 --dp-size=2 --max-model-len 2048 ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://gist.github.com/zou3519/5f5948902bb59ab95ece6fbbd22404f3 https://buildkite.com/vllm/ci/builds/43854#019b2990-5c28-4d51-a1ed-898f4b88ec51 ``` + CUDA_VISIBLE_DEVICES=1,2 -- + VLLM_ALL2ALL_BACKEND=deepep_high_throughput + VLLM_USE_DEEP_GEMM=1 + VLLM_LOGGING_LEVEL=DEBUG + python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen1.5-MoE-A2.7B --tp-size=1 --dp-size=2 --max-model-len 2048 ``` ### 📝 History of failing test At least in the last day ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: distributed-tests-h200 torch.compile;stale;ci-failure ### Name of failing test python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen1.5-MoE-A2.7B --tp-size=1 --dp-size=2 --max-model-len 2048
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e of failing test python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen1.5-MoE-A2.7B --tp-size=1 --dp-size=2 --max-model-len 2048 ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ]...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen1.5-MoE-A2.7B --tp-size=1 --dp-size=2 --max-model-len 2048 ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: distributed-tests-h200 torch.compile;stale;ci-failure ### Name of failing test python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen1.5-MoE-A2.7B --tp-size=1 --dp-size=2 --max-model-len 204...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d51-a1ed-898f4b88ec51 ``` + CUDA_VISIBLE_DEVICES=1,2 -- + VLLM_ALL2ALL_BACKEND=deepep_high_throughput + VLLM_USE_DEEP_GEMM=1 + VLLM_LOGGING_LEVEL=DEBUG + python3 examples/offline_inference/data_parallel.py --model Qwen/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
