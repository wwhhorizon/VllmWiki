# vllm-project/vllm#5051: [Feature]: Add num_requests_preempted metric

| 字段 | 值 |
| --- | --- |
| Issue | [#5051](https://github.com/vllm-project/vllm/issues/5051) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add num_requests_preempted metric

### Issue 正文摘录

### 🚀 The feature, motivation and pitch There are metrics that give an idea about the number of requests that are currently running and waiting through the metrics: `num_requests_running` and `num_requests_waiting`. But, these metrics alone does not give an idea about if the requests are getting thrashed and thus underutilizing GPUs. The new proposed metric `num_requests_preempted` that reflects the number of requests preempted and waiting for execution would provide idea about request thrashing. This provides the high-level schedulers to avoid adding new requests to the thrashing GPUs. ### Alternatives _No response_ ### Additional context ``` from openai import OpenAI import threading client = OpenAI( base_url="http://localhost:8000/v1", api_key="token-abc123", ) def query(): client.completions.create( model="facebook/opt-125m", prompt = "Sachin Tendulkar is", max_tokens=2040, n=1 ) threads = [] for i in range(1000): thread = threading.Thread(target=query) threads.append(thread) thread.start() for thread in threads: thread.join() ``` I ran the above script on a vLLM server started with command `python -m vllm.entrypoints.openai.api_server` in a machine with one NVIDIA T400; below...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Add num_requests_preempted metric feature request;stale ### 🚀 The feature, motivation and pitch There are metrics that give an idea about the number of requests that are currently running and waiting through...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### Alternatives _No response_ ### Additional context ``` from openai import OpenAI import threading client = OpenAI( base_url="http://localhost:8000/v1", api_key="token-abc123", ) def query(): client.completions.create...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: i_key="token-abc123", ) def query(): client.completions.create( model="facebook/opt-125m", prompt = "Sachin Tendulkar is", max_tokens=2040, n=1 ) threads = [] for i in range(1000): thread = threading.Thread(target=query...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
