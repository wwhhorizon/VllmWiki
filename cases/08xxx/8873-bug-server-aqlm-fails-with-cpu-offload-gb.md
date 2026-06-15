# vllm-project/vllm#8873: [Bug]: Server - `aqlm` fails with `--cpu-offload-gb`

| 字段 | 值 |
| --- | --- |
| Issue | [#8873](https://github.com/vllm-project/vllm/issues/8873) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Server - `aqlm` fails with `--cpu-offload-gb`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Model: [ISTA-DASLab/Meta-Llama-3.1-70B-Instruct-AQLM-PV-2Bit-1x16](https://huggingface.co/ISTA-DASLab/Meta-Llama-3.1-70B-Instruct-AQLM-PV-2Bit-1x16) Command: `vllm serve ~/ai/models/Meta-Llama-3.1-70B-Instruct/AQLM-PV-2Bit-1x16/ --max-model-len 8192 --quantization aqlm -tp 2 --host 0.0.0.0 --port 8050 --served-model-name llama3.1-70b --disable-custom-all-reduce --cpu-offload-gb 10` ``` Loading safetensors checkpoint shards: 0% Completed | 0/5 [00:00 sys.exit(main()) ^^^^^^ File "/home/js/.pyenv/vllm/lib/python3.12/site-packages/vllm/scripts.py", line 165, in main args.dispatch_function(args) File "/home/js/.pyenv/vllm/lib/python3.12/site-packages/vllm/scripts.py", line 37, in serve uvloop.run(run_server(args)) File "/home/js/.pyenv/vllm/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.1
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s with `--cpu-offload-gb` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Model: [ISTA-DASLab/Meta-Llama-3.1-70B-Instruct-AQLM-PV-2Bit-1x16](https://huggingface.co/ISTA-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ib/python3.12/site-packages/vllm/scripts.py", line 165, in main args.dispatch_function(args) File "/home/js/.pyenv/vllm/lib/python3.12/site-packages/vllm/scripts.py", line 37, in serve uvloop.run(run_server(args)) File...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Server - `aqlm` fails with `--cpu-offload-gb` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Model: [ISTA-DASLab/Meta-Llama-3.1-70B-Instruct-AQLM-PV-2Bit-1x16](h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
