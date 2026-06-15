# vllm-project/vllm#22525: [Bug]: (gpt-oss-20b) openai_harmony.HarmonyError: error downloading or loading vocab file

| 字段 | 值 |
| --- | --- |
| Issue | [#22525](https://github.com/vllm-project/vllm/issues/22525) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda |
| 症状 | crash |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (gpt-oss-20b) openai_harmony.HarmonyError: error downloading or loading vocab file

### Issue 正文摘录

### Your current environment - vllm-openai:gptoss official dockerfile - Running in a k8s cluster with NVIDIA A100 GPU. - Air gapped environment ### 🐛 Describe the bug At startup I observe the following issue ``` (Normal startup logs) ... Capturing CUDA graph shapes: 98%|█████████▊| 81/83 [01:40 (APIServer pid=1) sys.exit(main()) (APIServer pid=1) ^^^^^^ (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=1) args.dispatch_function(args) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pid=1) uvloop.run(run_server(args)) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run (APIServer pid=1) return __asyncio.run( (APIServer pid=1) ^^^^^^^^^^^^^^ (APIServer pid=1) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=1) return runner.run(main) (APIServer pid=1) ^^^^^^^^^^^^^^^^ (APIServer pid=1) File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run (APIServer pid=1) return self._loop.run_until_complete(task) (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: openai:gptoss official dockerfile - Running in a k8s cluster with NVIDIA A100 GPU. - Air gapped environment ### 🐛 Describe the bug At startup I observe the following issue ``` (Normal startup logs) ... Capturing CUDA gr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: (gpt-oss-20b) openai_harmony.HarmonyError: error downloading or loading vocab file bug ### Your current environment - vllm-openai:gptoss official dockerfile - Running in a k8s cluster with NVIDIA A100 GPU. - Air...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ng vocab file bug ### Your current environment - vllm-openai:gptoss official dockerfile - Running in a k8s cluster with NVIDIA A100 GPU. - Air gapped environment ### 🐛 Describe the bug At startup I observe the following...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=1) args.dispatch_function(args) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: frequently asked questions. performance attention_kv_cache;model_support;scheduler_memory cache;cuda crash shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
