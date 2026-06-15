# vllm-project/vllm#12437: [Bug]: HFValidationError when loading model from S3

| 字段 | 值 |
| --- | --- |
| Issue | [#12437](https://github.com/vllm-project/vllm/issues/12437) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: HFValidationError when loading model from S3

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug What I did (using a ray cluster of 2 nodes) ``` NCCL_DEBUG=info VLLM_NCCL_SO_PATH=/root/miniforge3/envs/vllm/lib/libnccl.so vllm serve s3:// /base_models/deepseek-ai/DeepSeek-V3/ --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code --load-format runai_streamer --model-loader-extra-config '{"concurrency":16,"memory_limit":5368709120}' ``` What happened: ``` Traceback (most recent call last): File "/root/miniforge3/envs/vllm/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/root/miniforge3/envs/vllm/lib/python3.11/site-packages/vllm/scripts.py", line 201, in main args.dispatch_function(args) File "/root/miniforge3/envs/vllm/lib/python3.11/site-packages/vllm/scripts.py", line 42, in serve uvloop.run(run_server(args)) File "/root/miniforge3/envs/vllm/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run return runner.run(wrapper()) ^^^^^^^^^^^^^^^^^^^^^ File "/root/miniforge3/envs/vllm/lib/python3.11/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: HFValidationError when loading model from S3 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug What I did (using a ray cluster of 2 nodes) ``` NCCL_DEBUG=info VLLM_NCCL_SO
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ^^^^^^^^^^^^^^^^^^ File "/root/miniforge3/envs/vllm/lib/python3.11/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ib/python3.11/site-packages/vllm/scripts.py", line 201, in main args.dispatch_function(args) File "/root/miniforge3/envs/vllm/lib/python3.11/site-packages/vllm/scripts.py", line 42, in serve uvloop.run(run_server(args))...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
