# vllm-project/vllm#32368: [Bug]: _CPU_MOE_ACT in cpu_fused_moe_torch cause AssertionError: Current vLLM config is not set

| 字段 | 值 |
| --- | --- |
| Issue | [#32368](https://github.com/vllm-project/vllm/issues/32368) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: _CPU_MOE_ACT in cpu_fused_moe_torch cause AssertionError: Current vLLM config is not set

### Issue 正文摘录

### Your current environment ## 🐛 Describe the bug commit 6cdf015c3cd8ee600dadf17ecd72fc7f44099d03 (PR https://github.com/vllm-project/vllm/pull/31747) cause `_CPU_MOE_ACT` in `cpu_fused_moe_torch` to raise `AssertionError: Current vLLM config is not set`. This PR design `_LazyActivationDict` in `cpu_fused_moe.py`, yet it still triggers the issue that its view was intended to solve. ```python class _LazyActivationDict(dict): """Lazily instantiate activation functions on first access. Avoids triggering CustomOp.__init__() at module import time, which would call get_current_vllm_config() before config is set. """ _factories: dict[str, type[SiluAndMul] | type[SwigluOAIAndMul]] = { "silu": SiluAndMul, "swigluoai": SwigluOAIAndMul, } def __missing__(self, key: str) -> SiluAndMul | SwigluOAIAndMul: if key not in self._factories: raise KeyError(f"{key} is not a supported activation") self[key] = self._factories[key]() return self[key] ``` ## Reproduce Scripts To test `cpu_fused_moe_torch` which uses `_LazyActivationDict`, you need to modify `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py` ```python def check_grouped_gemm( self, layer: torch.nn.Module, ) -> tuple[bool, str]: return...

## 现有链接修复摘要

#32777 [Bugfix] Fix _CPU_MOE_ACT AssertionError when vLLM config not set

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ns on first access. Avoids triggering CustomOp.__init__() at module import time, which would call get_current_vllm_config() before config is set. """ _factories: dict[str, type[SiluAndMul] | type[SwigluOAIAndMul]] = { "...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: : _CPU_MOE_ACT in cpu_fused_moe_torch cause AssertionError: Current vLLM config is not set bug ### Your current environment ## 🐛 Describe the bug commit 6cdf015c3cd8ee600dadf17ecd72fc7f44099d03 (PR https://github.com/vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: _CPU_MOE_ACT in cpu_fused_moe_torch cause AssertionError: Current vLLM config is not set bug ### Your current environment ## 🐛 Describe the bug commit 6cdf015c3cd8ee600dadf17ecd72fc7f44099d03 (PR https://github.c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;speculative_decoding activation;cuda;moe;operator;quantization;sampling;triton build_error;nan_inf env_dependency #32777 [Bugfix] Fix _CPU_MOE_ACT AssertionError when vLLM config not set Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32777](https://github.com/vllm-project/vllm/pull/32777) | closes_keyword | 0.95 | [Bugfix] Fix _CPU_MOE_ACT AssertionError when vLLM config not set | Fixes #32368 ## Problem The `_LazyActivationDict` was designed to lazily instantiate activation functions to avoid calling `get_current_vllm_config()` at module import time. Howev |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
