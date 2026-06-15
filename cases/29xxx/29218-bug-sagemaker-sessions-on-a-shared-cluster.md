# vllm-project/vllm#29218: [Bug]: sagemaker_sessions on a shared cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#29218](https://github.com/vllm-project/vllm/issues/29218) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: sagemaker_sessions on a shared cluster

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using a shared cluster with different users have different user accounts. I can't run any vllm serve command as `/dev/shm/sagemaker_sessions` is created by another user running vllm. The permission of this file is ``` drwx------ 2 another-user another-user 40 Nov 15 01:58 sagemaker_sessions ``` The error log: ``` File "/data/***/vllm/.venv/bin/vllm", line 10, in sys.exit(main()) ^^^^^^ File "/data/***/vllm/vllm/entrypoints/cli/main.py", line 21, in main import vllm.entrypoints.cli.serve File "/data/***/vllm/vllm/entrypoints/cli/serve.py", line 12, in from vllm.entrypoints.openai.api_server import ( File "/data/***/vllm/vllm/entrypoints/openai/api_server.py", line 23, in import model_hosting_container_standards.sagemaker as sagemaker_standards File "/data/***/vllm/.venv/lib/python3.12/site-packages/model_hosting_container_standards/sagemaker/__init__.py", line 24, in from .sessions import create_session_transform_decorator File "/data/***/vllm/.venv/lib/python3.12/site-packages/model_hosting_container_standards/sagemaker/sessions/__init__.py", line 2, in from .transform import SessionApiTransform File "/data/***/vllm/.venv/lib...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: sagemaker_sessions on a shared cluster bug;stale ### Your current environment ### 🐛 Describe the bug I'm using a shared cluster with different users have different user accounts. I can't run any vllm serve comman...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: File "/data/***/vllm/vllm/entrypoints/cli/main.py", line 21, in main import vllm.entrypoints.cli.serve File "/data/***/vllm/vllm/entrypoints/cli/serve.py", line 12, in from vllm.entrypoints.openai.api_server import ( Fi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: **/vllm/vllm/entrypoints/openai/api_server.py", line 23, in import model_hosting_container_standards.sagemaker as sagemaker_standards File "/data/***/vllm/.venv/lib/python3.12/site-packages/model_hosting_container_stand...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
