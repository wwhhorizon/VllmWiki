# vllm-project/vllm#39934: [Bug] Level-2 sleep/wake crashes with KeyError when enable_lora=True

| 字段 | 值 |
| --- | --- |
| Issue | [#39934](https://github.com/vllm-project/vllm/issues/39934) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Level-2 sleep/wake crashes with KeyError when enable_lora=True

### Issue 正文摘录

**Your current environment** - vLLM v0.17.0 - H100 80GB - PyTorch 2.10, CUDA 12.x **Model** Any model with `enable_lora=True` (tested with Qwen3-14B, Qwen3-0.6B) **How to reproduce** ```python from vllm import LLM, SamplingParams llm = LLM("Qwen/Qwen3-0.6B", enable_lora=True, max_lora_rank=8, enable_sleep_mode=True, enforce_eager=True) output1 = llm.generate("Hello", SamplingParams(temperature=0, max_tokens=10)) llm.sleep(level=2) llm.wake_up(tags=["weights"]) llm.collective_rpc("reload_weights") # crashes here llm.wake_up(tags=["kv_cache"]) ``` **Error** ``` File "vllm/model_executor/models/qwen2.py", line 496, in load_weights param = params_dict[name] KeyError: 'layers.0.mlp.gate_up_proj.weight' ``` **Root cause** LoRA wrapping replaces modules with `BaseLayerWithLoRA` wrappers that store the original module as `self.base_layer`. This moves parameters one level deeper in the module tree: `qkv_proj.weight` becomes `qkv_proj.base_layer.weight`. During `reload_weights()`, model-specific `load_weights()` methods build `params_dict = dict(self.named_parameters())` and look up checkpoint names directly — the LoRA-prefixed names don't match. Additionally, LoRA stacked tensors (`lora_a_...

## 现有链接修复摘要

#39935 [Bugfix] Fix level-2 sleep/wake/reload with enable_lora=True

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d with Qwen3-14B, Qwen3-0.6B) **How to reproduce** ```python from vllm import LLM, SamplingParams llm = LLM("Qwen/Qwen3-0.6B", enable_lora=True, max_lora_rank=8, enable_sleep_mode=True, enforce_eager=True) output1 = llm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ror when enable_lora=True **Your current environment** - vLLM v0.17.0 - H100 80GB - PyTorch 2.10, CUDA 12.x **Model** Any model with `enable_lora=True` (tested with Qwen3-14B, Qwen3-0.6B) **How to reproduce** ```python...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t environment** - vLLM v0.17.0 - H100 80GB - PyTorch 2.10, CUDA 12.x **Model** Any model with `enable_lora=True` (tested with Qwen3-14B, Qwen3-0.6B) **How to reproduce** ```python from vllm import LLM, SamplingParams ll...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: el with `enable_lora=True` (tested with Qwen3-14B, Qwen3-0.6B) **How to reproduce** ```python from vllm import LLM, SamplingParams llm = LLM("Qwen/Qwen3-0.6B", enable_lora=True, max_lora_rank=8, enable_sleep_mode=True,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: - PyTorch 2.10, CUDA 12.x **Model** Any model with `enable_lora=True` (tested with Qwen3-14B, Qwen3-0.6B) **How to reproduce** ```python from vllm import LLM, SamplingParams llm = LLM("Qwen/Qwen3-0.6B", enable_lora=True...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39935](https://github.com/vllm-project/vllm/pull/39935) | closes_keyword | 0.95 | [Bugfix] Fix level-2 sleep/wake/reload with enable_lora=True | Fixes #39934. Fix level-2 sleep/wake/reload for LoRA-enabled models. Without this fix, `reload_weights()` crashes with `KeyError` because `named_parameters()` returns LoRA-prefixe |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
