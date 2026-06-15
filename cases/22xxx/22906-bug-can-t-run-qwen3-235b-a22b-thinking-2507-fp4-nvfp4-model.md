# vllm-project/vllm#22906: [Bug]: Can't run Qwen3-235B-A22B-Thinking-2507-FP4 NVFP4 model

| 字段 | 值 |
| --- | --- |
| Issue | [#22906](https://github.com/vllm-project/vllm/issues/22906) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't run Qwen3-235B-A22B-Thinking-2507-FP4 NVFP4 model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve /home/Qwen3-235B-A22B-Thinking-2507-FP4 --served-model-name Qwen3-235B-A22B-Thinking-2507-FP4 --max-model-len 201000 --tensor-parallel-size 2 --gpu-memory-utilization 0.9 (APIServer pid=15764) INFO 08-14 20:58:07 [__init__.py:702] Resolved architecture: Qwen3MoeForCausalLM (APIServer pid=15764) INFO 08-14 20:58:07 [__init__.py:1740] Using max model len 201000 (APIServer pid=15764) Traceback (most recent call last): (APIServer pid=15764) File "/root/anaconda3/envs/vllm06/bin/vllm", line 8, in (APIServer pid=15764) sys.exit(main()) (APIServer pid=15764) ^^^^^^ (APIServer pid=15764) File "/home/vllm06/vllm/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=15764) args.dispatch_function(args) (APIServer pid=15764) File "/home/vllm06/vllm/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pid=15764) uvloop.run(run_server(args)) (APIServer pid=15764) File "/root/anaconda3/envs/vllm06/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run (APIServer pid=15764) return __asyncio.run( (APIServer pid=15764) ^^^^^^^^^^^^^^ (APIServer pid=15764) File "/root/anaconda3/envs/vllm06/lib/python3.12/asynci...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Can't run Qwen3-235B-A22B-Thinking-2507-FP4 NVFP4 model bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve /home/Qwen3-235B-A22B-Thinking-2507-FP4 --served-model-name Qwen3-235B-A22B-Thinkin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Can't run Qwen3-235B-A22B-Thinking-2507-FP4 NVFP4 model bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve /home/Qwen3-235B-A22B-Thinking-2507-FP4 --served-model-name Qwen3-235B-A22B-Thinkin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: op/__init__.py", line 109, in run (APIServer pid=15764) return __asyncio.run( (APIServer pid=15764) ^^^^^^^^^^^^^^ (APIServer pid=15764) File "/root/anaconda3/envs/vllm06/lib/python3.12/asyncio/runners.py", line 194, in...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 15764) INFO 08-14 20:58:07 [__init__.py:702] Resolved architecture: Qwen3MoeForCausalLM (APIServer pid=15764) INFO 08-14 20:58:07 [__init__.py:1740] Using max model len 201000 (APIServer pid=15764) Traceback (most recen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ntrypoints/cli/main.py", line 54, in main (APIServer pid=15764) args.dispatch_function(args) (APIServer pid=15764) File "/home/vllm06/vllm/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pid=15764) uvloop.run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
