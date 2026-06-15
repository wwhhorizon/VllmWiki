# vllm-project/vllm#21592: [Bug]: Failed to execute_model with logprobs on v0.10.0rc2

| 字段 | 值 |
| --- | --- |
| Issue | [#21592](https://github.com/vllm-project/vllm/issues/21592) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failed to execute_model with logprobs on v0.10.0rc2

### Issue 正文摘录

### Your current environment test passed on: v0.10.0rc1 but failed on: v0.10.0 / v0.10.0rc2 ### 🐛 Describe the bug https://github.com/vllm-project/vllm-ascend/actions/runs/16513637152/job/46700281259?pr=1927 With initial invistigation the problem should reproduce after: https://github.com/vllm-project/vllm/pull/21283 Solution: ```diff diff --git a/vllm/v1/sample/ops/logprobs.py b/vllm/v1/sample/ops/logprobs.py index a4d65485140e..8a52dba109b2 100644 --- a/vllm/v1/sample/ops/logprobs.py +++ b/vllm/v1/sample/ops/logprobs.py @@ -3,9 +3,10 @@ """Some utilities for logprobs, including logits.""" import torch +from vllm.platforms import current_platform -@torch.compile(dynamic=True) +@torch.compile(dynamic=True, backend=current_platform.simple_compile_backend) def batched_count_greater_than(x: torch.Tensor, values: torch.Tensor) -> torch.Tensor: """ ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: @ -3,9 +3,10 @@ """Some utilities for logprobs, including logits.""" import torch +from vllm.platforms import current_platform -@torch.compile(dynamic=True) +@torch.compile(dynamic=True, backend=current_platform.simple_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: platform -@torch.compile(dynamic=True) +@torch.compile(dynamic=True, backend=current_platform.simple_compile_backend) def batched_count_greater_than(x: torch.Tensor, values: torch.Tensor) -> torch.Tensor: """ ``` ### Be...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 2/job/46700281259?pr=1927 With initial invistigation the problem should reproduce after: https://github.com/vllm-project/vllm/pull/21283 Solution: ```diff diff --git a/vllm/v1/sample/ops/logprobs.py b/vllm/v1/sample/ops...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Failed to execute_model with logprobs on v0.10.0rc2 bug ### Your current environment test passed on: v0.10.0rc1 but failed on: v0.10.0 / v0.10.0rc2 ### 🐛 Describe the bug https://github.com/vllm-project/vllm-asce...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
