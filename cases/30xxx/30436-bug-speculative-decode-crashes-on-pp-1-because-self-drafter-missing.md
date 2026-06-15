# vllm-project/vllm#30436: [Bug]: Speculative decode crashes on PP>1 because self.drafter missing

| 字段 | 值 |
| --- | --- |
| Issue | [#30436](https://github.com/vllm-project/vllm/issues/30436) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative decode crashes on PP>1 because self.drafter missing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Reproduction run `vllm serve ... --pipeline-parallel-size 2 --tensor-parallel-size 2 ... --speculative-config '{"method":"ngram",...}'` with speculative decoding enabled and PP > 1. ## Issue Workers on PP stage 0 raise `AttributeError: 'GPUModelRunner' object has no attribute 'drafter'` ## Root cause In `GPUModelRunner.__init__` (`vllm/v1/worker/gpu_model_runner.py` [lines 381-404](https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L381)), `self.drafter` is created only on the last PP rank. Yet later code assumes it exists on all PP ranks when `self.speculative_config` is set. Example: `_build_attention_metadata` (`vllm/v1/worker/gpu_model_runner.py` [line 1648](https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L1648)) does `if isinstance(self.drafter, EagleProposer)` without guarding on PP rank or existence. ## Proposed fix a) Initialize `self.drafter = None` before the last-PP-only block and guard all speculative decode accesses with either `if get_pp_group().is_last_rank and self.drafter is not None` or `hasattr(self, "drafter")`. b) Alternatively, restrict spec...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Speculative decode crashes on PP>1 because self.drafter missing bug;stale ### Your current environment ### 🐛 Describe the bug ## Reproduction run `vllm serve ... --pipeline-parallel-size 2 --tensor-parallel-size 2
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: exists on all PP ranks when `self.speculative_config` is set. Example: `_build_attention_metadata` (`vllm/v1/worker/gpu_model_runner.py` [line 1648](https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_mode...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ranks when `self.speculative_config` is set. Example: `_build_attention_metadata` (`vllm/v1/worker/gpu_model_runner.py` [line 1648](https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L1648...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .. --pipeline-parallel-size 2 --tensor-parallel-size 2 ... --speculative-config '{"method":"ngram",...}'` with speculative decoding enabled and PP > 1. ## Issue Workers on PP stage 0 raise `AttributeError: 'GPUModelRunn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
