# vllm-project/vllm#42544: [Bug]: TurboQuant decode attention: workspace allocation not sized during warmup → AssertionError on first decode after lock_workspace()

| 字段 | 值 |
| --- | --- |
| Issue | [#42544](https://github.com/vllm-project/vllm/issues/42544) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TurboQuant decode attention: workspace allocation not sized during warmup → AssertionError on first decode after lock_workspace()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #### Symptom Server loads cleanly, advertises `/v1/models`, then dies on the **first inference request** with: ``` ERROR core.py:1138 AssertionError: Workspace is locked but allocation from 'turboquant_attn.py:879:_decode_attention' requires 0.76 MB, current size is 0.00 MB. Workspace growth is not allowed after locking. ``` EngineCore exits → `AsyncLLM.output_handler` raises `EngineDeadError` → API server returns 500. The assertion is caught inside the Python process so it isn't a crash-restart event; the engine just stays dead. Same backend (`turboquant_k3v4_nc`) on `Qwen3.6-35B-A3B-GPTQ-Int4` runs indefinitely without tripping it. Only the dense 27B reproduces it. #### Failure path `vllm/v1/attention/backends/turboquant_attn.py` `_decode_attention` (lines ~868–890 on upstream main): ```python mid_o_buf = output_buf = lse_buf = None if is_workspace_manager_initialized(): # output_buf in query dtype — matches the in-kernel fp16 cast in stage2. mid_o_buf, output_buf, lse_buf = ( current_workspace_manager().get_simultaneous( ((B, Hq, S, D + 1), torch.float32), ((B, Hq, D), query.dtype), ((B, Hq), torch.float32), ) ) ``` `get_simul...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: TurboQuant decode attention: workspace allocation not sized during warmup → AssertionError on first decode after lock_workspace() ### Your current environment ### 🐛 Describe the bug #### Symptom Server loads clea...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: TurboQuant decode attention: workspace allocation not sized during warmup → AssertionError on first decode after lock_workspace() ### Your current environment ### 🐛 Describe the bug #### Symptom Server loads clea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 00 MB` by the warmup-completion path (`lock_workspace()` after profile + cudagraph capture), so the decode-path's first `get_simultaneous` call asserts. The three scratch tensors are `mid_o_buf` (split-K reduction inter...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ess so it isn't a crash-restart event; the engine just stays dead. Same backend (`turboquant_k3v4_nc`) on `Qwen3.6-35B-A3B-GPTQ-Int4` runs indefinitely without tripping it. Only the dense 27B reproduces it. #### Failure...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 🐛 Describe the bug #### Symptom Server loads cleanly, advertises `/v1/models`, then dies on the **first inference request** with: ``` ERROR core.py:1138 AssertionError: Workspace is locked but allocation from 'turboquan...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
