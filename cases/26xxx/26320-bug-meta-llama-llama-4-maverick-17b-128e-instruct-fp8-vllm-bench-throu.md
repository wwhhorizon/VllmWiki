# vllm-project/vllm#26320: [Bug]: meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 vllm bench throughput regression on 2.9 RC on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#26320](https://github.com/vllm-project/vllm/issues/26320) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 32; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 vllm bench throughput regression on 2.9 RC on B200

### Issue 正文摘录

### Your current environment The env comes from `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:e7064b4dc8e0a7ed633de52fe69871591fdb6cc2` ### 🐛 Describe the bug When benchmark PyTorch 2.9.0 RC from https://github.com/vllm-project/vllm/pull/24994 against the current 2.8.0 baseline from vLLM main branch, I notice that there is throughput regression for [meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8](https://hud.pytorch.org/benchmark/llms?startTime=Mon%2C%2029%20Sep%202025%2020%3A41%3A58%20GMT&stopTime=Mon%2C%2006%20Oct%202025%2020%3A41%3A58%20GMT&granularity=day&lBranch=main&lCommit=119f00630b8b6aea29b5c3141728f96963521df1&rBranch=pull/24994/head&rCommit=e7064b4dc8e0a7ed633de52fe69871591fdb6cc2&repoName=vllm-project%2Fvllm&benchmarkName=&modelName=meta-llama%2FLlama-4-Maverick-17B-128E-Instruct-FP8&backendName=All%20Backends&modeName=All%20Modes&dtypeName=All%20DType&deviceName=All%20Devices&archName=All%20Platforms) where the request/s and total token/s drop more than 40%. This doesn't seem like a fluke because I have consistently seen this issue in the last 2 RCs and several rebases on https://github.com/vllm-project/vllm/pull/24994. The vllm bench throughput configuration for `met...

## 现有链接修复摘要

#26395 [Bugfix] Incorrect MM data format in `vllm bench throughput`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ur current environment The env comes from `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:e7064b4dc8e0a7ed633de52fe69871591fdb6cc2` ### 🐛 Describe the bug When benchmark PyTorch 2.9.0 RC from https://github.com/vllm-project/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 vllm bench throughput regression on 2.9 RC on B200 bug ### Your current environment The env comes from `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:e7064b4dc8e0a7ed...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 vllm bench throughput regression on 2.9 RC on B200 bug ### Your current environment The env comes from `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:e7064b4dc8e0a7ed...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 vllm bench throughput regression on 2.9 RC on B200 bug ### Your current environment The env comes from `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:e7064b4dc8e0a7ed...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rick-17B-128E-Instruct-FP8 vllm bench throughput regression on 2.9 RC on B200 bug ### Your current environment The env comes from `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:e7064b4dc8e0a7ed633de52fe69871591fdb6cc2` ###...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26395](https://github.com/vllm-project/vllm/pull/26395) | closes_keyword | 0.95 | [Bugfix] Incorrect MM data format in `vllm bench throughput` | FIX #26320 According to the definition of `TextPrompt`/`TokensPrompt`, `multi_modal_data` is marked as `NotRequired[MultiModalDataDict]`, which means that if the item exists in th |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
