# vllm-project/vllm#35414: [Bug]: 4*2080ti 22g deploy Qwen3.5-35B-A3B fail:2080 Ti does not support bfloat16

| 字段 | 值 |
| --- | --- |
| Issue | [#35414](https://github.com/vllm-project/vllm/issues/35414) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 4*2080ti 22g deploy Qwen3.5-35B-A3B fail:2080 Ti does not support bfloat16

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The vllm version is night, and dtype=float16 is set, but the error "2080 Ti does not support bfloat16" is still reported. **deploy scrpit:** vllm serve Qwen/Qwen3.5-35B-A3B --served-model-name Qwen3-30B-A3B --port 8000 --dtype float16 --tensor-parallel-size 2 --pipeline-parallel-size 2 --max-model-len 8000 --reasoning-parser qwen3 --gpu_memory_utilization 0.85 --distributed-executor-backend ray --max-num-seqs 10 **error msg:** Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorkerWrapper.execute_method() (pid=2578258, ip=192.168.31.8, actor_id=b846a3dd005e394acae84c940b000000, repr= ) (EngineCore_DP0 pid=2577918) File "/home/xuebang/qwen3.5-venv/lib/python3.10/site-packages/vllm/v1/worker/worker_base.py", line 341, in execute_method (EngineCore_DP0 pid=2577918) raise e (EngineCore_DP0 pid=2577918) File "/home/xuebang/qwen3.5-venv/lib/python3.10/site-packages/vllm/v1/worker/worker_base.py", line 330, in execute_method (EngineCore_DP0 pid=2577918) return run_method(self, method, args, kwargs) (EngineCore_DP0 pid=2577918) File "/home/xuebang/qwen3.5-venv/lib/python3.10/site-packages/vllm/v1/serial_utils.py",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 16 bug ### Your current environment ### 🐛 Describe the bug The vllm version is night, and dtype=float16 is set, but the error "2080 Ti does not support bfloat16" is still reported. **deploy scrpit:** vllm serve Qwen/Qwe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: 4*2080ti 22g deploy Qwen3.5-35B-A3B fail:2080 Ti does not support bfloat16 bug ### Your current environment ### 🐛 Describe the bug The vllm version is night, and dtype=float16 is set, but the error "2080 Ti does...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: soning-parser qwen3 --gpu_memory_utilization 0.85 --distributed-executor-backend ray --max-num-seqs 10 **error msg:** Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorkerWrapper.execute_method...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: /home/xuebang/qwen3.5-venv/lib/python3.10/site-packages/vllm/compilation/cuda_graph.py", line 222, in **call** (EngineCore_DP0 pid=2577918) return self.runnable(*args, **kwargs) (EngineCore_DP0 pid=2577918) File "/home/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: 4*2080ti 22g deploy Qwen3.5-35B-A3B fail:2080 Ti does not support bfloat16 bug ### Your current environment ### 🐛 Describe the bug The vllm version is night, and dtype=float16 is set, but the error "2080 Ti does...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
