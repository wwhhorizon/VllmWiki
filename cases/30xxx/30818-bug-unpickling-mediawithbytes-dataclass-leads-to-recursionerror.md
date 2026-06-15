# vllm-project/vllm#30818: [Bug]: Unpickling MediaWithBytes dataclass leads to RecursionError

| 字段 | 值 |
| --- | --- |
| Issue | [#30818](https://github.com/vllm-project/vllm/issues/30818) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unpickling MediaWithBytes dataclass leads to RecursionError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Introduced in https://github.com/vllm-project/vllm/pull/29621/, unpickling`MediaWithBytes` leads to `RecursionError`s. This is seen when using vLLM with Ray. `pickle` attempts to access members like `__setstate__` while re-instantiating objects. These `__getattr__`s are redirected to the `MediaWithBytes`'s `__getattr__` override. Since `self.media` is not set, another `__getattr__` will be triggered to find it, leading to infinite recursion. For example: ``` E File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/air/util/object_extensions/arrow.py", line 96, in as_py E return pickle.load(pa.BufferReader(self.value.as_buffer())) E ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ E File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/multimodal/base.py", line 38, in __getattr__ E return getattr(self.media, name) E ^^^^^^^^^^ E File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/multimodal/base.py", line 38, in __getattr__ E return getattr(self.media, name) E ^^^^^^^^^^ E File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/multimodal/base.py", line 38, in __getattr__ E return getattr(self.media, name...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: python """Minimal reproducer for pickle + __getattr__ recursion bug.""" import pickle from dataclasses import dataclass @dataclass class BrokenWrapper: """Wrapper that delegates attribute access - but breaks during unpi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/multimodal/base.py", line 38, in __getattr__ E return getattr(self.media, name) E ^^^^^^^^^^ E File "/home/ray/anaconda3/lib/python3.11/site-packages/vll
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Error: maximum recursion depth exceeded ``` Repro: ```python """Minimal reproducer for pickle + __getattr__ recursion bug.""" import pickle from dataclasses import dataclass @dataclass class BrokenWrapper: """Wrapper th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
