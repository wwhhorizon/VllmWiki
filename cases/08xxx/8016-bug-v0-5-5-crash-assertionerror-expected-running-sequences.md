# vllm-project/vllm#8016: [Bug]: v0.5.5 crash: "AssertionError: expected running sequences"

| 字段 | 值 |
| --- | --- |
| Issue | [#8016](https://github.com/vllm-project/vllm/issues/8016) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 34; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.5.5 crash: "AssertionError: expected running sequences"

### Issue 正文摘录

### Your current environment Running the standard v0.5.5 docker image from your Dockerhub repo without anything additional added to it. ### 🐛 Describe the bug When using Llama 3.1 70b AWQ model running on 4 A10G 24Gb GPUs with args: ``` --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --tensor-parallel-size 4 --gpu-memory-utilization 0.95 --enforce-eager --trust-remote-code --worker-use-ray --enable-prefix-caching --num-scheduler-steps 8 --dtype half --max-model-len 32768 ``` vLLM crashes and requires a full restart. Error: ``` INFO 08-29 19:33:37 server.py:222] vLLM ZMQ RPC Server was interrupted. Future exception was never retrieved future: Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/rpc/server.py", line 111, in generate async for request_output in results_generator: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 1064, in generate async for output in await self.add_request( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 113, in generator raise result File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0b AWQ model running on 4 A10G 24Gb GPUs with args: ``` --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --tensor-parallel-size 4 --gpu-memory-utilization 0.95 --enforce-eager --trust-remote-code --worker-use...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: v0.5.5 crash: "AssertionError: expected running sequences" bug;stale ### Your current environment Running the standard v0.5.5 docker image from your Dockerhub repo without anything additional added to it. ### 🐛 D...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: out anything additional added to it. ### 🐛 Describe the bug When using Llama 3.1 70b AWQ model running on 4 A10G 24Gb GPUs with args: ``` --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --tensor-parallel-siz...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: cted running sequences ``` The issue is random, the same query does NOT reproduce it. We have upgraded 6 hours ago and since then this happened 3 times. We now need to downgrade and consider v0.5.5 a buggy release. ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ces" bug;stale ### Your current environment Running the standard v0.5.5 docker image from your Dockerhub repo without anything additional added to it. ### 🐛 Describe the bug When using Llama 3.1 70b AWQ model running on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
