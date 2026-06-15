# vllm-project/vllm#36594: [Bug]: DPEngineCoreProc may re-arm DP wave while paused (START_DP_WAVE ignores pause state), causing collective timeout after pause_generation + collective_rpc

| 字段 | 值 |
| --- | --- |
| Issue | [#36594](https://github.com/vllm-project/vllm/issues/36594) |
| 状态 | closed |
| 标签 | cpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DPEngineCoreProc may re-arm DP wave while paused (START_DP_WAVE ignores pause state), causing collective timeout after pause_generation + collective_rpc

### Issue 正文摘录

## Title [Bug]: `DPEngineCoreProc` may re-arm DP wave while paused (`START_DP_WAVE` ignores pause state), causing collective timeout after `pause_generation` + `collective_rpc` ## Your current environment ## Model MoE + DPEP setup (`data_parallel_size > 1`) using coordinator wave handling (internal DP load balancing / `DPLBAsyncMPClient`). ## Bug description With DPEP, calling: 1) `pause_generation(mode="abort")` 2) then `collective_rpc(...)` for online weight update can intermittently fail with NCCL ALLREDUCE timeout (600s). Observed behavior: one engine enters the utility `collective_rpc`, while a peer engine can still be in dummy-batch ALLREDUCE, leading to collective mismatch and timeout. ### Root cause In `DPEngineCoreProc._handle_client_request`, `START_DP_WAVE` can set `engines_running = True` even when scheduler is paused: ```python # vllm/v1/engine/core.py — DPEngineCoreProc._handle_client_request if request_type == EngineCoreRequestType.START_DP_WAVE: new_wave, exclude_eng_index = request if exclude_eng_index != self.engine_index and new_wave >= self.current_wave: self.current_wave = new_wave if not self.engines_running: # no pause-state check self.engines_running = True...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rallel_size > 1`) using coordinator wave handling (internal DP load balancing / `DPLBAsyncMPClient`). ## Bug description With DPEP, calling: 1) `pause_generation(mode="abort")` 2) then `collective_rpc(...)` for online w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: er engine can still be in dummy-batch ALLREDUCE, leading to collective mismatch and timeout. ### Root cause In `DPEngineCoreProc._handle_client_request`, `START_DP_WAVE` can set `engines_running = True` even when schedu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: smatch and timeout. ### Root cause In `DPEngineCoreProc._handle_client_request`, `START_DP_WAVE` can set `engines_running = True` even when scheduler is paused: ```python # vllm/v1/engine/core.py — DPEngineCoreProc._han...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: peer engine can still be in dummy-batch ALLREDUCE, leading to collective mismatch and timeout. ### Root cause In `DPEngineCoreProc._handle_client_request`, `START_DP_WAVE` can set `engines_running = True` even when sche...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: duler()` may return immediately when engine appears idle (`has_work()==False`), i.e. no Future wait path. - A late `START_DP_WAVE` from coordinator can still arrive after pause returns. - Peer engine re-enters running l...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
