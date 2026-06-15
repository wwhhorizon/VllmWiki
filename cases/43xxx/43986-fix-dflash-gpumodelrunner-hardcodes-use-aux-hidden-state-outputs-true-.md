# vllm-project/vllm#43986: fix(dflash): GPUModelRunner hardcodes use_aux_hidden_state_outputs=True for DFlash, ignoring dflash_config.use_aux_hidden_state

| 字段 | 值 |
| --- | --- |
| Issue | [#43986](https://github.com/vllm-project/vllm/issues/43986) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> fix(dflash): GPUModelRunner hardcodes use_aux_hidden_state_outputs=True for DFlash, ignoring dflash_config.use_aux_hidden_state

### Issue 正文摘录

## Summary `GPUModelRunner` unconditionally sets `self.use_aux_hidden_state_outputs = True` when initializing a DFlash drafter, ignoring the `use_aux_hidden_state` field in the draft model's `dflash_config`. ## Code path In `vllm/v1/worker/gpu_model_runner.py`: ```python elif self.speculative_config.use_dflash(): self.drafter = DFlashProposer(self.vllm_config, self.device, self) self.use_aux_hidden_state_outputs = True # <-- hardcoded ``` Compare with the EAGLE3 branch, which correctly reads from the proposer: ```python elif self.speculative_config.use_eagle(): self.drafter = EagleProposer(...) self.use_aux_hidden_state_outputs = self.drafter.eagle3_use_aux_hidden_state ``` ## Why this is wrong `DFlashProposer` already correctly reads `dflash_config.use_aux_hidden_state` via `_get_eagle3_use_aux_hidden_state_from_config` and exposes it as `eagle3_use_aux_hidden_state`. The draft model (`qwen3_dflash.py`) also respects this flag to decide whether to use `fc` and aux hidden states. However, `GPUModelRunner` never reads it — it always requests aux hidden states from the target model, regardless of what the draft config says. ## Proposed fix Mirror the EAGLE3 pattern: ```python elif s...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ts `self.use_aux_hidden_state_outputs = True` when initializing a DFlash drafter, ignoring the `use_aux_hidden_state` field in the draft model's `dflash_config`. ## Code path In `vllm/v1/worker/gpu_model_runner.py`: ```...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: fix(dflash): GPUModelRunner hardcodes use_aux_hidden_state_outputs=True for DFlash, ignoring dflash_config.use_aux_hidden_state ## Summary `GPUModelRunner` unconditionally sets `self.use_aux_hidden_state_outputs = True`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: state`. The draft model (`qwen3_dflash.py`) also respects this flag to decide whether to use `fc` and aux hidden states. However, `GPUModelRunner` never reads it — it always requests aux hidden states from the target mo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: key absent → defaults to `True` - Explicit `True` → `True` - Explicit `False` → `False`
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ite (currently says "True when EAGLE 3 is used"). ## Verification Unit tests can mock the drafter or construct a minimal `dflash_config` — no GPU or large model needed. Tests cover: - No `dflash_config` → defaults to `T...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
