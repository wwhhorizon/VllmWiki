# vllm-project/vllm#28498: [Bug][RL]: Port Conflict

| 字段 | 值 |
| --- | --- |
| Issue | [#28498](https://github.com/vllm-project/vllm/issues/28498) |
| 状态 | open |
| 标签 | bug;help wanted;good first issue |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][RL]: Port Conflict

### Issue 正文摘录

### Your current environment - bug report: ``` Hello vLLM team, I'm running into a suspicious ZMQ socket bug with my 2P 4D configuration for DeepSeek-V3 (see below). I thought it is caused by reusing same nodes for many vLLM launches, but now it happened also at a clean node. Seems like a DP bug of sorts. Please find logs attached. vllm==0.11.0. ``` ```bash [1;36m(APIServer pid=670293)[0;0m File "XXX/.venv/lib/python3.12/site-packages/vllm/v1/engine/async_llm.py", line 134, in __init__ [1;36m(APIServer pid=670293)[0;0m self.engine_core = EngineCoreClient.make_async_mp_client( [1;36m(APIServer pid=670293)[0;0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [1;36m(APIServer pid=670293)[0;0m File "XXX/.venv/lib/python3.12/site-packages/vllm/v1/engine/core_client.py", line 101, in make_async_mp_client [1;36m(APIServer pid=670293)[0;0m return DPLBAsyncMPClient(*client_args) [1;36m(APIServer pid=670293)[0;0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [1;36m(APIServer pid=670293)[0;0m File "XXX/.venv/lib/python3.12/site-packages/vllm/v1/engine/core_client.py", line 1125, in __init__ [1;36m(APIServer pid=670293)[0;0m super().__init__(vllm_config, executor_class, log_stats, [1;36m(APIServer pid=670293)[0;0m...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;0m super().bind(addr) [1;36m(APIServer pid=670293)[0;0m File "zmq/backend/cython/_zmq.py", line 1009, in zmq.backend.cython._zmq.Socket.bind [1;36m(APIServer pid=670293)[0;0m File "zmq/backend/cython/_zmq.py", line 190...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: environment - bug report: ``` Hello vLLM team, I'm running into a suspicious ZMQ socket bug with my 2P 4D configuration for DeepSeek-V3 (see below). I thought it is caused by reusing same nodes for many vLLM launches, b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ntrivial). ``` From Reporter: ``` Received init message: EngineHandshakeMetadata(addresses=EngineZmqAddresses(inputs=['tcp://slurm-h200-207-083:60613'], outputs=['tcp://slurm-h200-207-083:36865'], coordinator_input='tcp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lo vLLM team, I'm running into a suspicious ZMQ socket bug with my 2P 4D configuration for DeepSeek-V3 (see below). I thought it is caused by reusing same nodes for many vLLM launches, but now it happened also at a clea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
