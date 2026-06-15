# vllm-project/vllm#26612: [Usage]: qwen3vl 30 A3B 启动vllm 服务报错

| 字段 | 值 |
| --- | --- |
| Issue | [#26612](https://github.com/vllm-project/vllm/issues/26612) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: qwen3vl 30 A3B 启动vllm 服务报错

### Issue 正文摘录

### 📚 The doc issue A_A800-SXM4-80GB.json'] (Worker pid=1939690) INFO 10-11 10:42:13 [monitor.py:34] torch.compile takes 85.33 s in total (Worker pid=1939690) INFO 10-11 10:42:14 [gpu_worker.py:298] Available KV cache memory: 13.69 GiB (EngineCore_DP0 pid=1937911) ERROR 10-11 10:42:14 [core.py:708] EngineCore failed to start. (EngineCore_DP0 pid=1937911) ERROR 10-11 10:42:14 [core.py:708] Traceback (most recent call last): (EngineCore_DP0 pid=1937911) ERROR 10-11 10:42:14 [core.py:708] File "/home/ma-user/work/renkexuan/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 699, in run_engine_core (EngineCore_DP0 pid=1937911) ERROR 10-11 10:42:14 [core.py:708] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=1937911) ERROR 10-11 10:42:14 [core.py:708] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=1937911) ERROR 10-11 10:42:14 [core.py:708] File "/home/ma-user/work/renkexuan/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 498, in __init__ (EngineCore_DP0 pid=1937911) ERROR 10-11 10:42:14 [core.py:708] super().__init__(vllm_config, executor_class, log_stats, (EngineCore_DP0 pid=1937911) ERROR 10-11 10:42:14 [core.py:708] File "/home/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: GB.json'] (Worker pid=1939690) INFO 10-11 10:42:13 [monitor.py:34] torch.compile takes 85.33 s in total (Worker pid=1939690) INFO 10-11 10:42:14 [gpu_worker.py:298] Available KV cache memory: 13.69 GiB (EngineCore_DP0 p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: qwen3vl 30 A3B 启动vllm 服务报错 usage ### 📚 The doc issue A_A800-SXM4-80GB.json'] (Worker pid=1939690) INFO 10-11 10:42:13 [monitor.py:34] torch.compile takes 85.33 s in total (Worker pid=1939690) INFO 10-11 10:42:1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rypoints/cli/main.py", line 54, in main (APIServer pid=1929655) args.dispatch_function(args) (APIServer pid=1929655) File "/home/ma-user/work/renkexuan/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: l (Worker pid=1939690) INFO 10-11 10:42:14 [gpu_worker.py:298] Available KV cache memory: 13.69 GiB (EngineCore_DP0 pid=1937911) ERROR 10-11 10:42:14 [core.py:708] EngineCore failed to start. (EngineCore_DP0 pid=1937911...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
