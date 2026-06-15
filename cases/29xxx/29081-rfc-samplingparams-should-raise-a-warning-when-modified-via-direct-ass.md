# vllm-project/vllm#29081: [RFC]: `SamplingParams` should raise a warning when modified via direct assignment on the user side

| 字段 | 值 |
| --- | --- |
| Issue | [#29081](https://github.com/vllm-project/vllm/issues/29081) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: `SamplingParams` should raise a warning when modified via direct assignment on the user side

### Issue 正文摘录

### Motivation. Currently, parameters within `SamplingParams` can be modified even after initialization. Direct assignments such as `sampling_params.attr1 = val1` bypass the logic in `__init__` or `__post_init__`, which makes the behavior unsafe. For example, I encountered this issue in a popular downstream library, Outlines (12.9k+ stars)，https://github.com/dottxt-ai/outlines/issues/1778. They directly assigned a value to a deprecated attribute, causing the replacement attribute to remain uninitialized. In my opinion, direct assignment on the **user side** should be disabled to prevent bypassing validation or standardization. On the **vLLM side**, internal modifications to `SamplingParams` are acceptable. Therefore, I propose that `SamplingParams` should raise a warning when modified via direct assignment on the user side. ### Proposed Change. ```python # lock_example.py import warnings import msgspec class SamplingParams(msgspec.Struct): temperature: float = 1.0 top_p: float = 1.0 _locked: bool = True def __setattr__(self, key, value): if key.startswith("_"): object.__setattr__(self, key, value) return if self._locked: warnings.warn(f"Modifying {key} directly may bypass validati...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nt on the user side. ### Proposed Change. ```python # lock_example.py import warnings import msgspec class SamplingParams(msgspec.Struct): temperature: float = 1.0 top_p: float = 1.0 _locked: bool = True def __setattr__...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: attr__(self, key, value) def unlock(self): self._locked = False params = SamplingParams(temperature=0.7) params.temperature = 0.8 # Warning: Modifying temperature directly may bypass validation # Within an unlocked cont...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
