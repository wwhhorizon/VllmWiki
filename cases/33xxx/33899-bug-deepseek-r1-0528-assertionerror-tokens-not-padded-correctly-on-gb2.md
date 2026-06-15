# vllm-project/vllm#33899: [Bug]:  DeepSeek-R1-0528 AssertionError: tokens not padded correctly on GB200

| 字段 | 值 |
| --- | --- |
| Issue | [#33899](https://github.com/vllm-project/vllm/issues/33899) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  DeepSeek-R1-0528 AssertionError: tokens not padded correctly on GB200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve /root/workspaces/models/DeepSeek-R1-0528 --data-parallel-size 8 --data-parallel-size-local 4 --data-parallel-address 10.0.8.18 --data-parallel-rpc-port 30001 -ep --speculative-config.method mtp --speculative-config.num_speculative_tokens 1 vllm serve /root/workspaces/models/DeepSeek-R1-0528 --data-parallel-size 8 --data-parallel-start-rank 4 --data-parallel-size-local 4 --data-parallel-address 10.0.8.18 --data-parallel-rpc-port 30001 -ep --speculative-config.method mtp --speculative-config.num_speculative_tokens 1 --headless ``` ``` ^[[0;36m(EngineCore_DP7 pid=2437344)^[[0;0m ERROR 02-05 10:19:58 [core.py:968] File "/root/workspaces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/v1/engine/core.py", line 959, in run_engine_core^M ^[[0;36m(EngineCore_DP7 pid=2437344)^[[0;0m ERROR 02-05 10:19:58 [core.py:968] engine_core.run_busy_loop()^M ^[[0;36m(EngineCore_DP7 pid=2437344)^[[0;0m ERROR 02-05 10:19:58 [core.py:968] File "/root/workspaces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/v1/engine/core.py", line 1388, in run_busy_loop^M ^[[0;36m(EngineCore_DP7 pid=2437344)^[[0;0m ERROR 02-05 10:19:58 [c...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 4 --data-parallel-address 10.0.8.18 --data-parallel-rpc-port 30001 -ep --speculative-config.method mtp --speculative-config.num_speculative_tokens 1 vllm serve /root/workspaces/models/DeepSeek-R1-0528 --data-parallel-si...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: DeepSeek-R1-0528 AssertionError: tokens not padded correctly on GB200 bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve /root/workspaces/models/DeepSeek-R1-0528 --data-parallel-size 8 --data-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: environment ### 🐛 Describe the bug ``` vllm serve /root/workspaces/models/DeepSeek-R1-0528 --data-parallel-size 8 --data-parallel-size-local 4 --data-parallel-address 10.0.8.18 --data-parallel-rpc-port 30001 -ep --specu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/v1/attention/backends/utils.py", line 531, in split_decodes_and_prefills^M ^[[0;36m(EngineCore_DP7 pid=2437344)^[[0;0m ERROR 02-05 10:19:58 [core.py:968] asser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: )^[[0;0m ERROR 02-05 10:19:58 [core.py:968] attn_metadata, _ = self._build_attention_metadata(^M ^[[0;36m(EngineCore_DP7 pid=2437344)^[[0;0m ERROR 02-05 10:19:58 [core.py:968] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M ^[[0;36m(...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
