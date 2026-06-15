# vllm-project/vllm#36217: [Bug]: The checkpoint you are trying to load has model type `qwen3_5` but Transformers does not recognize this architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#36217](https://github.com/vllm-project/vllm/issues/36217) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The checkpoint you are trying to load has model type `qwen3_5` but Transformers does not recognize this architecture

### Issue 正文摘录

### Your current environment v0.16.0 ### 🐛 Describe the bug ``` 2026-03-06 14:20:18.090661+08:00 - gpustack.worker.backends.base - INFO - Preparing model files... 2026-03-06 14:20:19.523007+08:00 - gpustack.worker.backends.base - INFO - Model files are ready. 2026-03-06 14:20:19.523120+08:00 - gpustack.worker.serve_manager - INFO - Provisioning model instance qwen3.5-4b-kY2xU 2026-03-06 14:20:19.523149+08:00 - gpustack.worker.backends.vllm - INFO - Starting vLLM model instance: qwen3.5-4b-kY2xU Downloading Model from https://www.modelscope.cn to directory: /var/lib/gpustack/cache/modelscope/tempfile/Qwen__Qwen3.5-4B__2tobsgq2 Processing 1 items: 0%| | 0.00/1.00 [00:00 (APIServer pid=50) sys.exit(main()) (APIServer pid=50) ^^^^^^ (APIServer pid=50) File "/usr/local/lib/python3.12/dist-packages/vllm_omni/entrypoints/cli/main.py", line 15, in main (APIServer pid=50) vllm_main() (APIServer pid=50) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 73, in main (APIServer pid=50) args.dispatch_function(args) (APIServer pid=50) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 111, in cmd (APIServer pid=50) uvloop.run(run_se...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: The checkpoint you are trying to load has model type `qwen3_5` but Transformers does not recognize this architecture bug ### Your current environment v0.16.0 ### 🐛 Describe the bug ``` 2026-03-06 14:20:18.090661+...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: uvloop/__init__.py", line 96, in run (APIServer pid=50) return __asyncio.run( (APIServer pid=50) ^^^^^^^^^^^^^^ (APIServer pid=50) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=50) retur...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Describe the bug ``` 2026-03-06 14:20:18.090661+08:00 - gpustack.worker.backends.base - INFO - Preparing model files... 2026-03-06 14:20:19.523007+08:00 - gpustack.worker.backends.base - INFO - Model files are ready. 20...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: o load has model type `qwen3_5` but Transformers does not recognize this architecture bug ### Your current environment v0.16.0 ### 🐛 Describe the bug ``` 2026-03-06 14:20:18.090661+08:00 - gpustack.worker.backends.base...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
