# vllm-project/vllm#2184: AssertionError: assert output == other_output

| 字段 | 值 |
| --- | --- |
| Issue | [#2184](https://github.com/vllm-project/vllm/issues/2184) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AssertionError: assert output == other_output

### Issue 正文摘录

I'm running `TheBloke/deepseek-coder-33B-instruct-AWQ` ``` python3 -m vllm.entrypoints.openai.api_server --model=TheBloke/deepseek-coder-33B-instruct-AWQ --gpu-memory-utilization 1.0 --served-model-name "gpt-3.5-turbo-16k" --tensor-parallel-size 2 ``` For an example input like the following: ``` diff --git a/configs/configs_1702899130.yaml b/configs/configs_1702899130.yaml new file mode 100644 index 0000000..97543a6 --- /dev/null +++ b/configs/configs_1702899130.yaml @@ -0,0 +1,14 @@ +adam_epsilon: 1.0e-08 +batch_size: 1024 +data_path: data.csv Write a short, specific (less than 50 chars) commit message about the above changes: ``` I get the following error ``` Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/home/user/projects/repos/transformers/.venv/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/home/user/projects/repos/transformers/.venv/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/home/user/projects/repos/transfor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: er-33B-instruct-AWQ` ``` python3 -m vllm.entrypoints.openai.api_server --model=TheBloke/deepseek-coder-33B-instruct-AWQ --gpu-memory-utilization 1.0 --served-model-name "gpt-3.5-turbo-16k" --tensor-parallel-size 2 ``` F...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: silon: 1.0e-08 +batch_size: 1024 +data_path: data.csv Write a short, specific (less than 50 chars) commit message about the above changes: ``` I get the following error ``` Exception in callback functools.partial( , req...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: get the following error ``` Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/home/user/projects/repos/transformers/.venv/lib/python3.1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
