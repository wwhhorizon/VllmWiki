# vllm-project/vllm#35286: [Bug]: Qwen3.5-MoE failed with enable_lora

| 字段 | 值 |
| --- | --- |
| Issue | [#35286](https://github.com/vllm-project/vllm/issues/35286) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-MoE failed with enable_lora

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To reproduce: ```bash CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen/Qwen3.5-35B-A3B --max_model_len 8192 --tensor_parallel_size 2 --enable_lora ``` **Error stack trace** ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 1%|▏ | 1/102 [00:01 (APIServer pid=4106442) sys.exit(main()) (APIServer pid=4106442) ^^^^^^ (APIServer pid=4106442) File "/mnt/nas2/hujinghan.hjh/vllm/vllm/entrypoints/cli/main.py", line 73, in main (APIServer pid=4106442) args.dispatch_function(args) (APIServer pid=4106442) File "/mnt/nas2/hujinghan.hjh/vllm/vllm/entrypoints/cli/serve.py", line 112, in cmd (APIServer pid=4106442) uvloop.run(run_server(args)) (APIServer pid=4106442) File "/mnt/nas2/anaconda3/envs/vllm016/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run (APIServer pid=4106442) return runner.run(wrapper()) (APIServer pid=4106442) ^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=4106442) File "/mnt/nas2/anaconda3/envs/vllm016/lib/python3.11/asyncio/runners.py", line 118, in run (APIServer pid=4106442) return self._loop.run_until_complete(task) (APIServer pid=4106442) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=4106442) File "uvloop/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: pid=4106442) File "/mnt/nas2/anaconda3/envs/vllm016/lib/python3.11/asyncio/runners.py", line 118, in run (APIServer pid=4106442) return self._loop.run_until_complete(task) (APIServer pid=4106442) ^^^^^^^^^^^^^^^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5-MoE failed with enable_lora bug ### Your current environment ### 🐛 Describe the bug To reproduce: ```bash CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen/Qwen3.5-35B-A3B --max_model_len 8192 --tensor_parallel_si...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rypoints/cli/main.py", line 73, in main (APIServer pid=4106442) args.dispatch_function(args) (APIServer pid=4106442) File "/mnt/nas2/hujinghan.hjh/vllm/vllm/entrypoints/cli/serve.py", line 112, in cmd (APIServer pid=410...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ur current environment ### 🐛 Describe the bug To reproduce: ```bash CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen/Qwen3.5-35B-A3B --max_model_len 8192 --tensor_parallel_size 2 --enable_lora ``` **Error stack trace** ``` Capt...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Qwen3.5-MoE failed with enable_lora bug ### Your current environment ### 🐛 Describe the bug To reproduce: ```bash CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen/Qwen3.5-35B-A3B --max_model_len 8192 --tensor_parallel_si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
