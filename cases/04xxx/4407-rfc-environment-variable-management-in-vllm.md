# vllm-project/vllm#4407: [RFC]: environment variable management in vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#4407](https://github.com/vllm-project/vllm/issues/4407) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: environment variable management in vllm

### Issue 正文摘录

### Motivation. As the project move on, we have more and more environment variables, and we have to manage them rather than letting them scatter around. ### Proposed Change. There are three types of environment variables used in vllm: 1. environment variables that are used to control the behavior of code **outside** vllm, e.g. `CUDA_VISIBLE_DEVICES` 2. environment variables that are used to control the behavior of code **inside** vllm, e.g. `VLLM_USE_PRECOMPILED` 3. environment variables that are used for testing, e.g. `TEST_DIST_MODEL` For type-1, gathering all the environment variables in a centralized place would make it easier for users to understand what environment variables vllm uses. For type-2, gathering all the environment variables in a centralized place would make it easier for users to understand what environment variables they can use to control the behavior of vllm. For type-3, it is safe to leave them as they are. There is also some feedback on the naming of environment variables, e.g. https://github.com/vllm-project/vllm/pull/3419#issuecomment-2078712068 states that the environment variable `HOST_IP` used in vllm has conflict with some k8s plugin. And https://gith...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: used to control the behavior of code **inside** vllm, e.g. `VLLM_USE_PRECOMPILED` 3. environment variables that are used for testing, e.g. `TEST_DIST_MODEL` For type-1, gathering all the environment variables in a centr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es that are used to control the behavior of code **outside** vllm, e.g. `CUDA_VISIBLE_DEVICES` 2. environment variables that are used to control the behavior of code **inside** vllm, e.g. `VLLM_USE_PRECOMPILED` 3. envir...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: , e.g. `VLLM_USE_PRECOMPILED` 3. environment variables that are used for testing, e.g. `TEST_DIST_MODEL` For type-1, gathering all the environment variables in a centralized place would make it easier for users to under...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: LED` 3. environment variables that are used for testing, e.g. `TEST_DIST_MODEL` For type-1, gathering all the environment variables in a centralized place would make it easier for users to understand what environment va...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
