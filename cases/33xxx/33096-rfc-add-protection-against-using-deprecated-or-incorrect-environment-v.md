# vllm-project/vllm#33096: [RFC]: Add protection against using deprecated or incorrect environment variables

| 字段 | 值 |
| --- | --- |
| Issue | [#33096](https://github.com/vllm-project/vllm/issues/33096) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 |  |
| Operator 关键词 | attention;kernel |
| 症状 | build_error;mismatch |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Add protection against using deprecated or incorrect environment variables

### Issue 正文摘录

### Motivation. There is a multitude of [environment variables](vllm/envs.py) used to control vLLM behavior, such as feature enablement, configuration changes, kernel dispatching, platform specific settings, etc. Over time many of the variables can get: - Renamed ([VLLM_RPC_GET_DATA_TIMEOUT_MS](https://github.com/vllm-project/vllm/commit/7c7714d856eee6fa94aade729b67f00584f72a4c#diff-b7538eee1327212c7cfbe3f7874600dfcd41b5fb5662695cd5f396294610ddf9L60-L400)) - Replaced with command line arguments ([Profiler](https://github.com/vllm-project/vllm/commit/e858bfe05167a3bbb064e283da5a1a7709dee24e)) - Deprecated ([VLLM_USE_V1](https://github.com/vllm-project/vllm/pull/28204)) With other configuration mechanisms such as command line arguments, any change typically follows the pattern of 1. Implement the new approach and add a warning that a change is coming within a given timeframe. 1. Start alerting the user in case the old method is being used. Usually through 1. Remove the old method from the codebase. A good example of such gradual change is the refactoring of the compilation config parameters, which allowed the users to detect the change and adjust the workflows. With environment vari...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ature enablement, configuration changes, kernel dispatching, platform specific settings, etc. Over time many of the variables can get: - Renamed ([VLLM_RPC_GET_DATA_TIMEOUT_MS](https://github.com/vllm-project/vllm/commi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vLLM behavior, such as feature enablement, configuration changes, kernel dispatching, platform specific settings, etc. Over time many of the variables can get: - Renamed ([VLLM_RPC_GET_DATA_TIMEOUT_MS](https://github.co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: thub.com/vllm-project/vllm/pull/28204)) With other configuration mechanisms such as command line arguments, any change typically follows the pattern of 1. Implement the new approach and add a warning that a change is co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 2695cd5f396294610ddf9L60-L400)) - Replaced with command line arguments ([Profiler](https://github.com/vllm-project/vllm/commit/e858bfe05167a3bbb064e283da5a1a7709dee24e)) - Deprecated ([VLLM_USE_V1](https://github.com/vl...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ns. correctness attention_kv_cache;ci_build attention;kernel build_error;mismatch Motivation.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
