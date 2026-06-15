# vllm-project/vllm#39900: [Bug]: Ray Compiled DAG PP channel crashes with AssertionError on concurrent requests (>=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#39900](https://github.com/vllm-project/vllm/issues/39900) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Ray Compiled DAG PP channel crashes with AssertionError on concurrent requests (>=2)

### Issue 正文摘录

### Your current environment ## Environment - vLLM: 0.19.0 - Ray: 2.43.0 - GPUs: 2 nodes × 8 GPUs (16 total) - Config: `--tensor-parallel-size 8 --pipeline-parallel-size 2 --distributed-executor-backend ray` （GLM5.1） ### 🐛 Describe the bug ## Description When running multi-node PP=2 inference with Ray backend, the engine crashes with the following error **only when request concurrency >= 2**. Single requests work fine. ## Error AssertionError: ('placeholder', 0, 'out_of_band_tensors', []) File "ray/_private/serialization.py", line 383, in _deserialize_msgpack_data python_objects = self._deserialize_pickle5_data( File "ray/_private/serialization.py", line 365, in _deserialize_pickle5_data obj = pickle.loads(in_band) File "ray/experimental/channel/torch_tensor_type.py", line 128, in deserialize return ctx.serialization_context.deserialize_tensor(b, self.device) File "ray/experimental/channel/serialization_context.py", line 154, in deserialize_tensor assert placeholder < len(self._out_of_band_tensors), ( AssertionError: ('placeholder', 0, 'out_of_band_tensors', []) ## Root Cause Analysis The `SerializationContext` in Ray's compiled DAG uses a **global (non-isolated) state** for `_out...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Ray Compiled DAG PP channel crashes with AssertionError on concurrent requests (>=2) bug ### Your current environment ## Environment - vLLM: 0.19.0 - Ray: 2.43.0 - GPUs: 2 nodes × 8 GPUs (16 total) - Config: `--t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tensor-parallel-size 8 --pipeline-parallel-size 2 --distributed-executor-backend ray` （GLM5.1） ### 🐛 Describe the bug ## Description When running multi-node PP=2 inference with Ray backend, the engine crashes with the f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nment - vLLM: 0.19.0 - Ray: 2.43.0 - GPUs: 2 nodes × 8 GPUs (16 total) - Config: `--tensor-parallel-size 8 --pipeline-parallel-size 2 --distributed-executor-backend ray` （GLM5.1） ### 🐛 Describe the bug ## Description Wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Ray Compiled DAG PP channel crashes with AssertionError on concurrent requests (>=2) bug ### Your current environment ## Environment - vLLM: 0.19.0 - Ray: 2.43.0 - GPUs: 2 nodes × 8 GPUs (16 total) - Config: `--tenso...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
