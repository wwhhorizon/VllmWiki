# vllm-project/vllm#14429: [Feature]: support tool and reasoning together

| 字段 | 值 |
| --- | --- |
| Issue | [#14429](https://github.com/vllm-project/vllm/issues/14429) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: support tool and reasoning together

### Issue 正文摘录

### 🚀 The feature, motivation and pitch For now `--enable-auto-tool-choice` and `--enable-reasoning` can't enable together, with the following errors: ``` # vllm serve /Qwen/QwQ-32B/ --served-model-name QwQ-32B --gpu-memory-utilization 0.97 --tensor-parallel-size 8 --max-model-len 32768 --enable-reasoning --reasoning-parser deepseek_r1 --enable-auto-tool-choice --tool-call-parser hermes INFO 03-07 18:14:44 [__init__.py:207] Automatically detected platform cuda. Traceback (most recent call last): File "/usr/local/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/usr/local/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 70, in main cmds[args.subparser].validate(args) File "/usr/local/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 36, in validate validate_parsed_serve_args(args) File "/usr/local/lib/python3.12/site-packages/vllm/entrypoints/openai/cli_args.py", line 285, in validate_parsed_serve_args raise TypeError( TypeError: Error: --enable-auto-tool-choice and --enable-reasoning cannot be enabled at the same time ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you a...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es INFO 03-07 18:14:44 [__init__.py:207] Automatically detected platform cuda. Traceback (most recent call last): File "/usr/local/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/usr/local/lib/python3.12/site-packa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing` can't enable together, with the following errors: ``` # vllm serve /Qwen/QwQ-32B/ --served-model-name QwQ-32B --gpu-memory-utilization 0.97 --tensor-parallel-size 8 --max-model-len 32768 --enable-reasoning --reason...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support tool and reasoning together feature request;unstale ### 🚀 The feature, motivation and pitch For now `--enable-auto-tool-choice` and `--enable-reasoning` can't enable together, with the following error...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;frontend_api;model_support cuda crash 🚀 The feature,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
