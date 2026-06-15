# vllm-project/vllm#26458: [Bug][Deepseek-v32-exp]: import `DeepseekV32IndexerCache` from `model registry` in gpu_model_runner

| 字段 | 值 |
| --- | --- |
| Issue | [#26458](https://github.com/vllm-project/vllm/issues/26458) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Deepseek-v32-exp]: import `DeepseekV32IndexerCache` from `model registry` in gpu_model_runner

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We encounter a problem while adapting deepseek v32 on plugin system: Currently the line [here](https://github.com/vllm-project/vllm/blob/releases/v0.11.0/vllm/v1/worker/gpu_model_runner.py#L43) directly import ed the `DeepseekV32IndexerCache` from vllm's deepseek_v2 model which is not registered by plugin. And in `get_kv_cache_spec` [here](https://github.com/vllm-project/vllm/blob/releases/v0.11.0/vllm/v1/worker/gpu_model_runner.py#L4141), the `DeepseekV32IndexerCache` was directly used, which type is: > ***vllm.model_executor.models***.deepseek_v2.DeepseekV32IndexerCache and in plugin we registered the *deepseek_v2.py* model file and the type should be: > ***vllm_plugin.xxx.models***.deepseek_v2.DeepseekV32IndexerCache This made the `k_cache` attn not added to forward_context() and caused some error. I know a possible way to fix this is to rewrite the `gpu_model_runner` and update it through check_and_update_config in plugin platform. Could make the `DeepseekV32IndexerCache` got from model_registry? Kind of like: ```python from vllm.model_executor.model_loader.utils import get_model_cls DeepseekV32IndexerCache = get_model_cls(se...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug][Deepseek-v32-exp]: import `DeepseekV32IndexerCache` from `model registry` in gpu_model_runner bug;stale ### Your current environment ### 🐛 Describe the bug We encounter a problem while adapting deepseek v32 on plu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug][Deepseek-v32-exp]: import `DeepseekV32IndexerCache` from `model registry` in gpu_model_runner bug;stale ### Your current environment ### 🐛 Describe the bug We encounter a problem while adapting deepseek v32 on plu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: `DeepseekV32IndexerCache` from `model registry` in gpu_model_runner bug;stale ### Your current environment ### 🐛 Describe the bug We encounter a problem while adapting deepseek v32 on plugin system: Currently the line [...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
