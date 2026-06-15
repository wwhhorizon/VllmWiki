# vllm-project/vllm#23834: [Usage]: Load Qwen3 Moe model error when starting the vllm server on TPU

| 字段 | 值 |
| --- | --- |
| Issue | [#23834](https://github.com/vllm-project/vllm/issues/23834) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Load Qwen3 Moe model error when starting the vllm server on TPU

### Issue 正文摘录

### Your current environment **Environment** ``` google tpu v6e * 4 ``` **StartUp follow** ``` https://cloud.google.com/tpu/docs/tutorials/LLM/vllm-inference-v6e?hl=zh-cn ``` **Vllm version** ``` build from source code on main branch commit: a3432f18fdd85eb18e29fc32327507fe1063ad57 ``` **Launch command** ``` vllm serve Qwen/Qwen3-30B-A3B --seed 42 --disable-log-requests --gpu-memory-utilization 0.95 --max-num-batched-tokens 4096 --max-num-seqs 256 --tensor-parallel-size 4 --max-model-len 2048 --no-enable-prefix-caching ``` **Error log** ``` Loading safetensors checkpoint shards: 0% Completed | 0/16 [00:00 (APIServer pid=65774) sys.exit(main()) (APIServer pid=65774) ^^^^^^ (APIServer pid=65774) File "/home/gcpuser/sky_workdir/vllm/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=65774) args.dispatch_function(args) (APIServer pid=65774) File "/home/gcpuser/sky_workdir/vllm/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pid=65774) uvloop.run(run_server(args)) (APIServer pid=65774) File "/home/gcpuser/miniconda3/envs/vllm/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run (APIServer pid=65774) return __asyncio.run( (APIServer pid=65774) ^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: oogle.com/tpu/docs/tutorials/LLM/vllm-inference-v6e?hl=zh-cn ``` **Vllm version** ``` build from source code on main branch commit: a3432f18fdd85eb18e29fc32327507fe1063ad57 ``` **Launch command** ``` vllm serve Qwen/Qwe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Load Qwen3 Moe model error when starting the vllm server on TPU usage;stale ### Your current environment **Environment** ``` google tpu v6e * 4 ``` **StartUp follow** ``` https://cloud.google.com/tpu/docs/tutor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Load Qwen3 Moe model error when starting the vllm server on TPU usage;stale ### Your current environment **Environment** ``` google tpu v6e * 4 ``` **StartUp follow** ``` https://cloud.google.com/tpu/docs/tutorials/L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ntrypoints/cli/main.py", line 54, in main (APIServer pid=65774) args.dispatch_function(args) (APIServer pid=65774) File "/home/gcpuser/sky_workdir/vllm/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pid=6577...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
