# vllm-project/vllm#36602: [RFC]: Make kernel/op and component tests device-agnostic for OOT plugins

| 字段 | 值 |
| --- | --- |
| Issue | [#36602](https://github.com/vllm-project/vllm/issues/36602) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;hardware_porting |
| 子分类 |  |
| Operator 关键词 | activation;cuda;kernel;operator |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Make kernel/op and component tests device-agnostic for OOT plugins

### Issue 正文摘录

### Motivation. vLLM's kernel/op tests and component tests provide extensive coverage for correctness and regression. However, many of these tests hardcode CUDA assumptions — device strings, `opcheck()` calls, `torch.cuda.*` APIs — which prevents [OOT device plugins](https://docs.vllm.ai/en/latest/design/plugin_system/) from reusing them. This forces OOT plugin developers to duplicate test logic for ops and components that are already well-tested upstream. Making these tests device-agnostic would allow any OOT plugin to validate its implementations against the same upstream suite by simply installing the plugin and running `pytest`. Prior art: [#20169](https://github.com/vllm-project/vllm/pull/20169) applied this pattern to v1 worker and sampler tests for Intel XPU. The kernel/op tests remain unfixed. ### Proposed Change. There are recurring CUDA-hardcoded patterns across the test suite that I could find: **1. `CUDA_DEVICES` list generation** Many test files generate a device list that only includes CUDA devices: ```python CUDA_DEVICES = [f"cuda:{i}" for i in range(1 if torch.cuda.device_count() == 1 else 2)] ``` Proposed change: ```python from vllm.platforms import current_platfo...

## 现有链接修复摘要

#36246 [CI/Build] Updated rmsnorm test to improve OOT device coverage

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: o validate its implementations against the same upstream suite by simply installing the plugin and running `pytest`. Prior art: [#20169](https://github.com/vllm-project/vllm/pull/20169) applied this pattern to v1 worker...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ge for correctness and regression. However, many of these tests hardcode CUDA assumptions — device strings, `opcheck()` calls, `torch.cuda.*` APIs — which prevents [OOT device plugins](https://docs.vllm.ai/en/latest/des...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [RFC]: Make kernel/op and component tests device-agnostic for OOT plugins RFC ### Motivation. vLLM's kernel/op tests and component tests provide extensive coverage for correctness and regression. However, many of these...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ce, but when an OOT plugin registers a custom op, `forward_native()` can dispatch to the override rather than the base implementation, polluting the reference: ```python ref_out = layer.forward_native(..) ``` Proposed c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: VICES = [f"cuda:{i}" for i in range(1 if torch.cuda.device_count() == 1 else 2)] ``` Proposed change: ```python from vllm.platforms import current_platform CUDA_DEVICES = [ f"{current_platform.device_type}:{i}" for i in...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36246](https://github.com/vllm-project/vllm/pull/36246) | mentioned | 0.45 | [CI/Build] Updated rmsnorm test to improve OOT device coverage | ist. tba ### any other things. - poc pr for `test_layernorm.py`: [#36246](https://github.com/vllm-project/vllm/pull/36246) - prior art for v1 worker/sampler tests: [#20169](https:… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
