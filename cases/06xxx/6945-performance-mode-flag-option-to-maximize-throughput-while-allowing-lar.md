# vllm-project/vllm#6945: [Performance]: Mode/flag/option to maximize throughput while allowing large latency?

| 字段 | 值 |
| --- | --- |
| Issue | [#6945](https://github.com/vllm-project/vllm/issues/6945) |
| 状态 | closed |
| 标签 | performance;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Mode/flag/option to maximize throughput while allowing large latency?

### Issue 正文摘录

### Proposal to improve performance Hi thank you for the great project! I would like to use vllm to run inference to test models on datasets. For example, say evaluating whether a prompt is good or not on the GSM8K dataset. I currently start a vllm openai-compatible server, and let python code to communicate with it. Therefore, I do not care about latency, but only care about throughput. It seems that vllm's openai-compatible server cares about latency, thus I wonder that makes throughput suboptimal? I know there is also a `LLM` class for batch inference. However, I hope to make vllm isolated from my main python environment (since it requires strict cuda/pytorch/etc), thus put it in a separate docker container via the official vllm openai docker image. So another related question is that, will the LLM class be different from using the vllm server and feed in all requests quickly? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Performance]: Mode/flag/option to maximize throughput while allowing large latency? performance;unstale ### Proposal to improve performance Hi thank you for the great project! I would like to use vllm to run inference...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t (since it requires strict cuda/pytorch/etc), thus put it in a separate docker container via the official vllm openai docker image. So another related question is that, will the LLM class be different from using the vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ets. For example, say evaluating whether a prompt is good or not on the GSM8K dataset. I currently start a vllm openai-compatible server, and let python code to communicate with it. Therefore, I do not care about latenc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ption to maximize throughput while allowing large latency? performance;unstale ### Proposal to improve performance Hi thank you for the great project! I would like to use vllm to run inference to test models on datasets...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: for the great project! I would like to use vllm to run inference to test models on datasets. For example, say evaluating whether a prompt is good or not on the GSM8K dataset. I currently start a vllm openai-compatible s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
