# vllm-project/vllm#731: Run error

| 字段 | 值 |
| --- | --- |
| Issue | [#731](https://github.com/vllm-project/vllm/issues/731) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Run error

### Issue 正文摘录

``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m", tensor_parallel_size=8) ``` ``` root@dell:/workspace# python test.py 2023-08-10 17:15:34,725 ERROR services.py:1207 -- Failed to start the dashboard , return code 1 2023-08-10 17:15:34,726 ERROR services.py:1232 -- Error should be written to 'dashboard.log' or 'dashboard.err'. We are printing the last 20 lines for you. See 'https://docs.ray.io/en/master/ray-observability/ray-logging.html#logging-directory-structure' to find where the log file is. 2023-08-10 17:15:34,727 ERROR services.py:1276 -- The last 20 lines of /tmp/ray/session_2023-08-10_17-15-32_212987_31479/logs/dashboard.log (it contains the error message from the dashboard): from ray.util.state.common import ( File "/usr/local/lib/python3.8/dist-packages/ray/util/state/__init__.py", line 1, in from ray.util.state.api import ( File "/usr/local/lib/python3.8/dist-packages/ray/util/state/api.py", line 17, in from ray.util.state.common import ( File "/usr/local/l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Run error ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m", tensor_parallel_size=8) ``` ``` root@dell:/workspace# python test.py 2023-08-10 17:15:34,725 ERROR services.py:1207 -- F...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: opt-125m", tensor_parallel_size=8) ``` ``` root@dell:/workspace# python test.py 2023-08-10 17:15:34,725 ERROR services.py:1207 -- Failed to start the dashboard , return code 1 2023-08-10 17:15:34,726 ERROR services.py:1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
