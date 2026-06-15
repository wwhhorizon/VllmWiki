# vllm-project/vllm#42675: [Bug]: FA4 causes `no module named 'flash_attn.ops'`

| 字段 | 值 |
| --- | --- |
| Issue | [#42675](https://github.com/vllm-project/vllm/issues/42675) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FA4 causes `no module named 'flash_attn.ops'`

### Issue 正文摘录

### 🐛 Describe the bug [vllm/model_executor/layers/rotary_embedding/common.py](https://github.com/vllm-project/vllm/blame/main/vllm/model_executor/layers/rotary_embedding/common.py) conditionally imports `flash_attn.ops.triton.rotary` by: ```python if not current_platform.is_cpu() and find_spec("flash_attn") is not None: from flash_attn.ops.triton.rotary import apply_rotary ``` FA4 contains the module `flash_attn` but not `flash_attn.ops.triton.rotary`, causing the import error. A quick fix is to change the code to `find_spec("flash_attn.ops.triton.rotary")`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: layers/rotary_embedding/common.py) conditionally imports `flash_attn.ops.triton.rotary` by: ```python if not current_platform.is_cpu() and find_spec("flash_attn") is not None: from flash_attn.ops.triton.rotary import ap...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ain/vllm/model_executor/layers/rotary_embedding/common.py) conditionally imports `flash_attn.ops.triton.rotary` by: ```python if not current_platform.is_cpu() and find_spec("flash_attn") is not None: from flash_attn.ops...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: )`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ses `no module named 'flash_attn.ops'` bug ### 🐛 Describe the bug [vllm/model_executor/layers/rotary_embedding/common.py](https://github.com/vllm-project/vllm/blame/main/vllm/model_executor/layers/rotary_embedding/commo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
