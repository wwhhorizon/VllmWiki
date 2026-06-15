# vllm-project/vllm#32252: [Bug]: self.stats_update_address is None for non-Moe and external LB

| 字段 | 值 |
| --- | --- |
| Issue | [#32252](https://github.com/vllm-project/vllm/issues/32252) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: self.stats_update_address is None for non-Moe and external LB

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the following scripts `CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen2.5-7B-Instruct --port 8001 --data-parallel-size 2 --data-parallel-rank 0 --enforce-eager` `CUDA_VISIBLE_DEVICES=1 vllm serve Qwen/Qwen2.5-7B-Instruct --port 8002 --data-parallel-size 2 --data-parallel-rank 1 --enforce-eager` I receive the following assert: ``` (APIServer pid=1463124) Traceback (most recent call last): (APIServer pid=1463124) File "/mnt/pyenv_vllm/bin/vllm", line 8, in (APIServer pid=1463124) sys.exit(main()) (APIServer pid=1463124) ^^^^^^ (APIServer pid=1463124) File "/mnt/vllm/vllm/entrypoints/cli/main.py", line 73, in main (APIServer pid=1463124) args.dispatch_function(args) (APIServer pid=1463124) File "/mnt/vllm/vllm/entrypoints/cli/serve.py", line 60, in cmd (APIServer pid=1463124) uvloop.run(run_server(args)) (APIServer pid=1463124) File "/mnt/pyenv_vllm/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run (APIServer pid=1463124) return __asyncio.run( (APIServer pid=1463124) ^^^^^^^^^^^^^^ (APIServer pid=1463124) File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run (APIServer pid=1463124) return runner.r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /__init__.py", line 109, in run (APIServer pid=1463124) return __asyncio.run( (APIServer pid=1463124) ^^^^^^^^^^^^^^ (APIServer pid=1463124) File "/usr/lib/
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ironment ### 🐛 Describe the bug When running the following scripts `CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen2.5-7B-Instruct --port 8001 --data-parallel-size 2 --data-parallel-rank 0 --enforce-eager` `CUDA_VISIBLE_DEV...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: When running the following scripts `CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen2.5-7B-Instruct --port 8001 --data-parallel-size 2 --data-parallel-rank 0 --enforce-eager` `CUDA_VISIBLE_DEVICES=1 vllm serve Qwen/Qwen2.5-7...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rypoints/cli/main.py", line 73, in main (APIServer pid=1463124) args.dispatch_function(args) (APIServer pid=1463124) File "/mnt/vllm/vllm/entrypoints/cli/serve.py", line 60, i
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ject/vllm/issues/30739 `run_coordinator` in `launch_core_engines()` is False, so that `addresses.frontend_stats_publish_address` is None, and trigger this issue. ### Before submitting a new issue... - [x] Make sure you...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
