# vllm-project/vllm#13262: [Usage]: For Embedding model, how to reduce the number of decimal places in the output?

| 字段 | 值 |
| --- | --- |
| Issue | [#13262](https://github.com/vllm-project/vllm/issues/13262) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: For Embedding model, how to reduce the number of decimal places in the output?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` NOT related ### How would you like to use vllm Serve Embedding Model 、、、 vllm serve BAAI/bge-m3 \ --served-model-name BAAI/bge-m3 \ --gpu-memory-utilization 0.95 \ --enforce-eager \ --host 0.0.0.0 --port 10003 、、、 using cURL to get vec ``` curl -X POST http://172.31.0.11:10003/v1/embeddings \ -H "Content-Type: application/json" \ -d '{ "input": "你的输入文本", "model": "BAAI/bge-m3" }' {"id":"embd-0ab62bb0a94e4dabb62d6b24749ce07c","object":"list","created":1739514487,"model":"BAAI/bge-m3","data":[{"index":0,"object":"embedding","embedding":[-0.061981201171875,0.0093536376953125,-0.02978515625,-0.0003428459167480469,0.006381988525390625,-0.0097198486328125,0.0242156982421875,-0.01424407958984375,0.0117034912109375,-0.01605224609375,0.01363372802734375,0.0017538070678710938,0.0156402587890625,-0.0235443115234375,0.004955291748046875,-0.00653839111328125,-0.0183563232421875,-0.0166168212890625,-0.004138946533203125,-0.01276397705078125,-0.03350830078125,0.0245819091796875,0.03546142578125,0.02154541015625,0.02362060546875,0.0238189697265625,-0.0013427734375,-0.003650665283203125,-0.026092529296875,-0.00688171386...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: For Embedding model, how to reduce the number of decimal places in the output? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` NOT related ### How would you like to us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: For Embedding model, how to reduce the number of decimal places in the output? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` NOT related ### How would you like to us...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: al? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g model, how to reduce the number of decimal places in the output? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` NOT related ### How would you like to use vllm Serve Embeddin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
