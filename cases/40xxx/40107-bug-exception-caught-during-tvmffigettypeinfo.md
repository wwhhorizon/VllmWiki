# vllm-project/vllm#40107: [Bug]: Exception caught during TVMFFIGetTypeInfo

| 字段 | 值 |
| --- | --- |
| Issue | [#40107](https://github.com/vllm-project/vllm/issues/40107) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Exception caught during TVMFFIGetTypeInfo

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve /model/minimax-m2.5/MiniMax-M2.5/ --tensor-parallel-size 4 --tool-call-parser minimax_m2 --reasoning-parser minimax_m2 --enable-auto-tool-choice --trust-remote-code` ``` (Worker_TP1 pid=4969) 2026-04-17 05:52:34,084 - INFO - autotuner.py:268 - flashinfer.jit: [Autotuner]: Autotuning process ends Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 88%|███████████████████████████████████████████████████████████████████████████████████████████▊ | 45/51 [00:05 (APIServer pid=4566) sys.exit(main()) (APIServer pid=4566) ^^^^^^ (APIServer pid=4566) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 75, in main (APIServer pid=4566) args.dispatch_function(args) (APIServer pid=4566) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 122, in cmd (APIServer pid=4566) uvloop.run(run_server(args)) (APIServer pid=4566) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 96, in run (APIServer pid=4566) return __asyncio.run( (APIServer pid=4566) ^^^^^^^^^^^^^^ (APIServer pid=4566) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (API...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: Worker_TP1 pid=4969) 2026-04-17 05:52:34,084 - INFO - autotuner.py:268 - flashinfer.jit: [Autotuner]: Autotuning process ends Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 88%|████████████████████████████████...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: loop/__init__.py", line 96, in run (APIServer pid=4566) return __asyncio.run( (APIServer pid=4566) ^^^^^^^^^^^^^^ (APIServer pid=4566) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=4566)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: r.jit: [Autotuner]: Autotuning process ends Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 88%|███████████████████████████████████████████████████████████████████████████████████████████▊ | 45/51 [00:05 (APISe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .py:268 - flashinfer.jit: [Autotuner]: Autotuning process ends Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 88%|███████████████████████████████████████████████████████████████████████████████████████████▊ |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ug ### Your current environment ### 🐛 Describe the bug `vllm serve /model/minimax-m2.5/MiniMax-M2.5/ --tensor-parallel-size 4 --tool-call-parser minimax_m2 --reasoning-parser minimax_m2 --enable-auto-tool-choice --trust...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
