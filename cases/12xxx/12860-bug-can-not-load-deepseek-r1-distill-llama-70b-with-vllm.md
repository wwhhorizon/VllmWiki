# vllm-project/vllm#12860: [Bug]:  Can not load DeepSeek-R1-Distill-Llama-70B with VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#12860](https://github.com/vllm-project/vllm/issues/12860) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Can not load DeepSeek-R1-Distill-Llama-70B with VLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-R1-Distill-Llama-70B --tensor-parallel-size 4 --max-model-len 4096 --enforce-eager --port 8001 ``` ``` (VllmWorkerProcess pid=252469) INFO 02-07 08:53:57 model_runner.py:1111] Starting to load model deepseek-ai/DeepSeek-R1-Distill-Llama-70B... (VllmWorkerProcess pid=252470) INFO 02-07 08:53:57 model_runner.py:1111] Starting to load model deepseek-ai/DeepSeek-R1-Distill-Llama-70B... (VllmWorkerProcess pid=252471) INFO 02-07 08:53:57 model_runner.py:1111] Starting to load model deepseek-ai/DeepSeek-R1-Distill-Llama-70B... Loading safetensors checkpoint shards: 0% Completed | 0/16 [00:00 sys.exit(main()) File "/data/miniconda3/envs/fffan_py310/lib/python3.10/site-packages/vllm/scripts.py", line 202, in main args.dispatch_function(args) File "/data/miniconda3/envs/fffan_py310/lib/python3.10/site-packages/vllm/scripts.py", line 42, in serve uvloop.run(run_server(args)) File "/data/miniconda3/envs/fffan_py310/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run return loop.run_until_complete(wrapper()) File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/data/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ntrypoints/openai/api_server.py", line 873, in run_server async with build_async_engine_client(args) as engine_client: File "/data/miniconda3/envs/fffan_py310/lib/python3.10/contextlib.py", line 199, in __aenter__ retur...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ib/python3.10/site-packages/vllm/scripts.py", line 202, in main args.dispatch_function(args) File "/data/miniconda3/envs/fffan_py310/lib/python3.10/site-packages/vllm/scripts.py", line 42, in serve uvloop.run(run_server...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Can not load DeepSeek-R1-Distill-Llama-70B with VLLM bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-R1-Distill-Llama-70B --tensor-parallel-size 4 --max-model-len...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Can not load DeepSeek-R1-Distill-Llama-70B with VLLM bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-R1-Distill-Llama-70B --tensor-parallel-size 4 --max-model-len...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
