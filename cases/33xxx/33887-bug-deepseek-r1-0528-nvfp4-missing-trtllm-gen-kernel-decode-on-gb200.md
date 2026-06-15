# vllm-project/vllm#33887: [Bug]: DeepSeek-R1-0528-NVFP4  Missing TRTLLM-GEN kernel (decode) on GB200

| 字段 | 值 |
| --- | --- |
| Issue | [#33887](https://github.com/vllm-project/vllm/issues/33887) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-R1-0528-NVFP4  Missing TRTLLM-GEN kernel (decode) on GB200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve /root/workspaces/kebe/models/DeepSeek-R1-0528-NVFP4 --data-parallel-size 8 --data-parallel-size-local 4 --data-parallel-address 10.0.8.18 --data-parallel-rpc-port 23346 -ep --speculative-config.method mtp --speculative-config.num_speculative_tokens 1 --load-format=dummy (EngineCore_DP2 pid=2217760) Process EngineCore_DP2: (EngineCore_DP2 pid=2217760) Traceback (most recent call last): (EngineCore_DP2 pid=2217760) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP2 pid=2217760) self.run() (EngineCore_DP2 pid=2217760) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP2 pid=2217760) self._target(*self._args, **self._kwargs) (EngineCore_DP2 pid=2217760) File "/root/workspaces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/v1/engine/core.py", line 970, in run_engine_core (EngineCore_DP2 pid=2217760) raise e (EngineCore_DP2 pid=2217760) File "/root/workspaces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/v1/engine/core.py", line 949, in run_engine_core (EngineCore_DP2 pid=2217760) engine_core = DPEngineCoreProc(*args, **kwar...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: DeepSeek-R1-0528-NVFP4 Missing TRTLLM-GEN kernel (decode) on GB200 bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve /root/workspaces/kebe/models/DeepSeek-R1-0528-NVFP4 --data-parallel-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: core.py", line 112, in __init__ (EngineCore_DP2 pid=2217760) num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP2 pid=2217760) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP2 pid=221...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: DeepSeek-R1-0528-NVFP4 Missing TRTLLM-GEN kernel (decode) on GB200 bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve /root/workspaces/kebe/models/DeepSeek-R1-0528-NVFP4 --data-parallel-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ronment ### 🐛 Describe the bug ``` vllm serve /root/workspaces/kebe/models/DeepSeek-R1-0528-NVFP4 --data-parallel-size 8 --data-parallel-size-local 4 --data-parallel-address 10.0.8.18 --data-parallel-rpc-port 23346 -ep...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/v1/attention/backends/mla/flashinfer_mla.py", line 183, in forward_mqa (EngineCore_DP2 pid=2217760) o = trtllm_batch_decode_with_kv_cache_mla( (EngineCore_DP2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
