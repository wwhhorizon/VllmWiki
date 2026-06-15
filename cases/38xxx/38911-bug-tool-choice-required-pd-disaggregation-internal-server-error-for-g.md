# vllm-project/vllm#38911: [Bug]: tool_choice='required'+PD disaggregation; internal server error for GLM-5

| 字段 | 值 |
| --- | --- |
| Issue | [#38911](https://github.com/vllm-project/vllm/issues/38911) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tool_choice='required'+PD disaggregation; internal server error for GLM-5

### Issue 正文摘录

### Your current environment We initially used the vllm-ascend framework, and finally found that the error reported by APIServer was caused by vllm itself. Function Call is the service-oriented part. vllm-ascend did not override the logic of this part. The basic configuration is as follows: ```text Device: 910C -npu A3 Image: vllm-ascend 0.18.0rc1 built based on vllm v0.18.0 Model: GLM-5 PD disaggregation ``` ### 🐛 Describe the bug It's just a guess: when we set "tool_choice = required" and "max_tokens = 1", error "500 Internal Server Error" should be reported at least for GLM-5. I have checked the related issues, but it does not seem to be the same issue, so I am raising this issue. The error information is as follows: ``` (APIServer pid=2884) INFO 03-27 02:48:38 [loggers.py:259] Engine 000: Avg prompt throughput: 23.4 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0% (EngineCore_DP0 pid=3011) INFO 03-27 02:48:38 [mooncake_connector.py:1057] Delaying free of 2 blocks for request chatcmpl-757ea62e-0333-4a39-997e-20fc198be9ee-a8412f1e (APIServer pid=2884) I...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ted part. vllm-ascend did not override the logic of this part. The basic configuration is as follows: ```text Device: 910C -npu A3 Image: vllm-ascend 0.18.0rc1 built based on vllm v0.18.0 Model: GLM-5 PD disaggregation...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 23.4 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0% (EngineCore_DP0 pid=3011) INFO 03-27...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0% (EngineCore_DP0 pid=3011) INFO 03-27 02:48:38 [mooncake_co...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 011) INFO 03-27 02:48:38 [mooncake_connector.py:1057] Delaying free of 2 blocks for request chatcmpl-757ea62e-0333-4a39-997e-20fc198be9ee-a8412f1e (APIServer pid=2884) INFO: 100.124.195.xxx:51156 - "POST /v1/chat/comple...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: er pid=2884) INFO 03-27 02:48:38 [loggers.py:259] Engine 000: Avg prompt throughput: 23.4 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
