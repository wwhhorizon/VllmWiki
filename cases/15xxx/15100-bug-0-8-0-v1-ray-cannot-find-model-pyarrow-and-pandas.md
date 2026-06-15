# vllm-project/vllm#15100: [Bug]: 0.8.0(V1) Ray cannot find model pyarrow and pandas

| 字段 | 值 |
| --- | --- |
| Issue | [#15100](https://github.com/vllm-project/vllm/issues/15100) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.8.0(V1) Ray cannot find model pyarrow and pandas

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Firstly I follow the doc https://docs.vllm.ai/en/latest/serving/distributed_serving.html to setup the distributed environment(2 nodes with 8 GPUs per node), and then run the api_server as below: ```bash python3 -m vllm.entrypoints.openai.api_server --port 18011 --model /models/DeepSeek-V3 --tensor-parallel-size 16 --gpu-memory-utilization 0.92 --dtype auto --served-model-name deepseekv3 --max-num-seqs 50 --max-model-len 16384 --trust-remote-code --disable-log-requests --enable-chunked-prefill --enable-prefix-caching ``` Then I got the following error in Ray module when handling the requests: ```text RayWorkerWrapper pid=243, ip=10.99.48.141) ERROR:root:Compiled DAG task exited with exception (RayWorkerWrapper pid=243, ip=10.99.48.141) Traceback (most recent call last): (RayWorkerWrapper pid=243, ip=10.99.48.141) File "/usr/local/lib/python3.12/dist-packages/ray/dag/compiled_dag_node.py", line 230, in do_exec_tasks (RayWorkerWrapper pid=243, ip=10.99.48.141) done = tasks[operation.exec_task_idx].exec_operation( (RayWorkerWrapper pid=243, ip=10.99.48.141) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (RayWorkerWrapper pid=243, ip=...

## 现有链接修复摘要

#15283 Add missed ray[data] dependence in cuda.txt

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: requests: ```text RayWorkerWrapper pid=243, ip=10.99.48.141) ERROR:root:Compiled DAG task exited with exception (RayWorkerWrapper pid=243, ip=10.99.48.141) Traceback (most recent call last): (RayWorkerWrapper pid=243, i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: 0.8.0(V1) Ray cannot find model pyarrow and pandas bug;ray;stale ### Your current environment ### 🐛 Describe the bug Firstly I follow the doc https://docs.vllm.ai/en/latest/serving/distributed_serving.html to set...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 0.8.0(V1) Ray cannot find model pyarrow and pandas bug;ray;stale ### Your current environment ### 🐛 Describe the bug Firstly I follow the doc https://docs.vllm.ai/en/latest/serving/distributed_serving.html to set...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;import_error;nan_inf dtype;env_dependency #15283 Add missed ray[data] dependence in cuda.txt Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#15283](https://github.com/vllm-project/vllm/pull/15283) | closes_keyword | 0.95 | Add missed ray[data] dependence in cuda.txt | FIX #15100 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
