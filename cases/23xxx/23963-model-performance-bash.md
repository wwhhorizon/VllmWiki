# vllm-project/vllm#23963: Model Performance Bash!

| 字段 | 值 |
| --- | --- |
| Issue | [#23963](https://github.com/vllm-project/vllm/issues/23963) |
| 状态 | closed |
| 标签 | help wanted;performance;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Model Performance Bash!

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Performance continues to be a top priority in the vLLM project. We have recently seen an explosion of models launched in the last few months. We are seeking help to ensure vLLM runs these models as efficiently as possible. To achieve this goal, we are creating a Model Performance Bash! The goal of this bash is to analyze the performance of vLLM's model execution in various configurations to identify opportunities to improve the model side execution. We will perform the following workflow: - start vllm server - hit server with a workload designed to showcase the decode performance - generate a report highlighting opportunities for optimization (for example here is one I made on DeepSeek R1 - https://docs.google.com/presentation/d/1vR0IyeYUKdv4g9pW9jKfgQeegYd_plAF4CSRdRAEXv0/edit?usp=sharing) - work on removing the gaps by implementing kernels (or something else) to hit peak We have created a a slack group (`#sig-model-bash`) to discuss the results of each of these projects: https://vllm-dev.slack.com/archives/C09D4R4MYLR/p1756500163094599 ### Instructions Here's how to do it: - launch the model ```bash VLLM_TORCH_PROFILER_DIR=xxx vllm serve /...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Model Performance Bash! help wanted;performance;feature request ### 🚀 The feature, motivation and pitch Performance continues to be a top priority in the vLLM project. We have recently seen an explosion of models launc
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: structions Here's how to do it: - launch the model ```bash VLLM_TORCH_PROFILER_DIR=xxx vllm serve /path/to/your/model ``` - hit it with load (target simulating decode) ```bash vllm bench serve \ --base-url {{URL}} \ --m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Model Performance Bash! help wanted;performance;feature request ### 🚀 The feature, motivation and pitch Performance continues to be a top priority in the vLLM project. We have recently seen an explosion of models launch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: few months. We are seeking help to ensure vLLM runs these models as efficiently as possible. To achieve this goal, we are creating a Model Performance Bash! The goal of this bash is to analyze the performance of vLLM's...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: iscuss the results of each of these projects: https://vllm-dev.slack.com/archives/C09D4R4MYLR/p1756500163094599 ### Instructions Here's how to do it: - launch the model ```bash VLLM_TORCH_PROFILER_DIR=xxx vllm serve /pa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
