# vllm-project/vllm#23025: [Bug]: KeyError: 'layers.1.mlp.experts.w13_weight' for serving GLM 4.5 air

| 字段 | 值 |
| --- | --- |
| Issue | [#23025](https://github.com/vllm-project/vllm/issues/23025) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;moe;operator;quantization |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'layers.1.mlp.experts.w13_weight' for serving GLM 4.5 air

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash vllm serve QuantTrio/GLM-4.5-Air-AWQ-FP16Mix --enable-expert-parallel --swap-space 16 --max-num-seqs 512 --max-model-len 32000 --max-seq-len-to-capture $CONTEXT_LENGTH --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --trust-remote-code --disable-log-requests --host 0.0.0.0 --port 7654 ``` ```bash Worker rank=1 pid=3781016) INFO 08-16 11:44:55 [gpu_model_runner.py:1875] Loading model from scratch... (VllmWorker rank=0 pid=3781015) INFO 08-16 11:44:55 [gpu_model_runner.py:1875] Loading model from scratch... (VllmWorker rank=1 pid=3781016) INFO 08-16 11:44:55 [cuda.py:290] Using Flash Attention backend on V1 engine. (VllmWorker rank=0 pid=3781015) INFO 08-16 11:44:55 [cuda.py:290] Using Flash Attention backend on V1 engine. Loading safetensors checkpoint shards: 0% Completed | 0/15 [00:00 sys.exit(main()) ^^^^^^ File "/home/datnvt/.conda/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 54, in main args.dispatch_function(args) File "/home/datnvt/.conda/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 52, in cmd uvloop.run(run_server(args)) File "/home/datnvt/.conda/en...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: (VllmWorker rank=1 pid=3781016) INFO 08-16 11:44:55 [cuda.py:290] Using Flash Attention backend on V1 engine. (VllmWorker rank=0 pid=3781015) INFO 08-16 11:44:55 [cuda.py:290] Using Flash Attention backend on V1 engine....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/home/datnvt/.conda/envs/vllm/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ble-expert-parallel --swap-space 16 --max-num-seqs 512 --max-model-len 32000 --max-seq-len-to-capture $CONTEXT_LENGTH --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --trust-remote-code --disable-log-requests --ho...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: KeyError: 'layers.1.mlp.experts.w13_weight' for serving GLM 4.5 air bug;stale ### Your current environment ### 🐛 Describe the bug ```bash vllm serve QuantTrio/GLM-4.5-Air-AWQ-FP16Mix --enable-expert-parallel --sw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: KeyError: 'layers.1.mlp.experts.w13_weight' for serving GLM 4.5 air bug;stale ### Your current environment ### 🐛 Describe the bug ```bash vllm serve QuantTrio/GLM-4.5-Air-AWQ-FP16Mix --enable-expert-parallel --swap-spac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
