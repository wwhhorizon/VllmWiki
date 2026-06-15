# vllm-project/vllm#42314: [Bug]: 使用0.18.0版本vllm-ascend，A3单机部署GLM5，dp2 tp8启动报错

| 字段 | 值 |
| --- | --- |
| Issue | [#42314](https://github.com/vllm-project/vllm/issues/42314) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 使用0.18.0版本vllm-ascend，A3单机部署GLM5，dp2 tp8启动报错

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 报错日志如下： n operator()) [rank6]:[W511 11:38:06.006805438 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator()) [rank9]:[W511 11:38:06.008215514 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator()) [rank14]:[W511 11:38:06.008481939 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator()) Capturing CUDA graphs (decode, FULL): 72%|███████████████████████████████████████████████████ | 18/25 [00:59 sys.exit(main()) ^^^^^^ File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 75, in main args.dispatch_function(args) File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 114, in cmd run_multi_api_server(args) File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 317, in run_multi_api_server wait_for_completion_or_failure( File "/vllm-workspace/vllm/vllm/v1/utils.py", line 278, in wait_for_completion_or_failure raise RuntimeError( RuntimeError: Process ApiServer_0 (PID: 359) died with exit code 1 [ERRO...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Describe the bug 报错日志如下： n operator()) [rank6]:[W511 11:38:06.006805438 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator()) [rank9]:[W511 11:38:0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: tor()) [rank6]:[W511 11:38:06.006805438 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator()) [rank9]:[W511 11:38:06.008215514 compiler_depend.ts:2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -workspace/vllm/vllm/entrypoints/cli/main.py", line 75, in main args.dispatch_function(args) File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 114, in cmd run_multi_api_server(args) File "/vllm-workspace/v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;moe;operator;quantization;sampling;triton build_error;crash;nan_inf;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: to finish before starting graph capture. (function operator()) Capturing CUDA graphs (decode, FULL): 72%|███████████████████████████████████████████████████ | 18/25 [00:59 sys.exit(main()) ^^^^^^ File "/vllm-workspace/v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
