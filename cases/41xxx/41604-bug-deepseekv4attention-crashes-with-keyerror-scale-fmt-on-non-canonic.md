# vllm-project/vllm#41604: [Bug]: DeepseekV4Attention crashes with KeyError: scale_fmt on non-canonical DSv4 quantizations

| 字段 | 值 |
| --- | --- |
| Issue | [#41604](https://github.com/vllm-project/vllm/issues/41604) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;quantization |
| 症状 | crash;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepseekV4Attention crashes with KeyError: scale_fmt on non-canonical DSv4 quantizations

### Issue 正文摘录

# [Bug]: `DeepseekV4Attention.__init__` crashes with `KeyError: 'scale_fmt'` on quantizations that don't carry the field ## Summary `vllm/model_executor/models/deepseek_v4.py:953` does a bare-key lookup: ```python self.scale_fmt = config.quantization_config["scale_fmt"] ``` This raises `KeyError: 'scale_fmt'` on any DSv4 quantization whose `quantization_config` doesn't include that field — i.e. anything not produced by DeepSeek's own quant pipeline (which uniquely emits `scale_fmt`). All worker processes die during model init; the engine never finishes booting. `scale_fmt` already has a canonical default elsewhere in the same module (`vllm/model_executor/layers/deepseek_v4_attention.py:1006`): ```python self.scale_fmt = "ue8m0" ``` The fix is one line: use the same default at the missing-field site. ## Reproduction Any non-canonical DSv4 W4A16 quantization triggers the crash. For example, `Intel/DeepSeek-V4-Flash-W4A16-AutoRound` (AutoRound 0.13.0): ```bash vllm serve Intel/DeepSeek-V4-Flash-W4A16-AutoRound \ --tensor-parallel-size 8 --enable-expert-parallel \ --gpu-memory-utilization 0.88 --cpu-offload-gb 6 \ --max-num-seqs 2 --max-model-len 16384 \ --quantization gptq_marlin --k...

## 现有链接修复摘要

#41791 [Bugfix][Model] Fix DeepSeek V4 scale_fmt default for non-canonical quant configs

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: DeepseekV4Attention crashes with KeyError: scale_fmt on non-canonical DSv4 quantizations # [Bug]: `DeepseekV4Attention.__init__` crashes with `KeyError: 'scale_fmt'` on quantizations that don't carry the field ##...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: le_fmt' ``` The crash happens before any GPU memory allocation, so it's deterministic regardless of TP / EP / kv-cache-dtype settings. The Intel AutoRound quant config (truncated): ```json { "quant_method": "auto-round"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 8` (also reproduces on `0.20.1` GA tag) - PyTorch: 2.11.0+cu130 - Driver/CUDA: 580.76.05 / 13.0 - Hardware: 8× RTX A4000 (SM86) — but the crash is platform-independent (happens during config parsing, before CUDA touch)...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: -size 8 --enable-expert-parallel \ --gpu-memory-utilization 0.88 --cpu-offload-gb 6 \ --max-num-seqs 2 --max-model-len 16384 \ --quantization gptq_marlin --kv-cache-dtype fp8 --trust-remote-code ``` **Expected**: engine...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ale_fmt'` on quantizations that don't carry the field ## Summary `vllm/model_executor/models/deepseek_v4.py:953` does a bare-key lookup: ```python self.scale_fmt = config.quantization_config["scale_fmt"] ``` This raises...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41791](https://github.com/vllm-project/vllm/pull/41791) | closes_keyword | 0.95 | [Bugfix][Model] Fix DeepSeek V4 scale_fmt default for non-canonical quant configs | Fixes #41604. DeepSeek V4 attention currently reads `quantization_config["scale_fmt"]` directly. Non-canonical DeepSeek V4 quantization configs may omit this DeepSeek-specific f |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
