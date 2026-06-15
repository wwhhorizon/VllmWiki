# vllm-project/vllm#20051: [New Model]: mxbai-rerank-large-v2

| 字段 | 值 |
| --- | --- |
| Issue | [#20051](https://github.com/vllm-project/vllm/issues/20051) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: mxbai-rerank-large-v2

### Issue 正文摘录

### The model to consider. https://huggingface.co/mixedbread-ai/mxbai-rerank-large-v2 ### The closest model vllm already supports. This model is built on Qwen2 ### What's your difficulty of supporting the model you want? When adding the `--task score` argument to enable the various `/rerank` endpoints, I get this error: ``` WARNING 06-24 19:02:15 [api_server.py:816] To indicate that the rerank API is not part of the standard OpenAI API, we have located it at `/rerank`. Please update your client accordingly. (Note: Conforms to JinaAI rerank API) INFO: 10.130.5.5:0 - "POST /v1/rerank HTTP/1.1" 500 Internal Server Error ERROR 06-24 19:02:15 [engine.py:165] AttributeError("'Qwen2ForCausalLM' object has no attribute 'pooler'") ERROR 06-24 19:02:15 [engine.py:165] Traceback (most recent call last): ERROR 06-24 19:02:15 [engine.py:165] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 163, in start ERROR 06-24 19:02:15 [engine.py:165] self.run_engine_loop() ERROR 06-24 19:02:15 [engine.py:165] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 226, in run_engine_loop ERROR 06-24 19:02:15 [engine.py:165] requ...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: mxbai-rerank-large-v2 ### The model to consider. https://huggingface.co/mixedbread-ai/mxbai-rerank-large-v2 ### The closest model vllm already supports. This model is built on Qwen2 ### What's your difficul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ", line 226, in run_engine_loop ERROR 06-24 19:02:15 [engine.py:165] request_outputs = self.engine_step() ERROR 06-24 19:02:15 [engine.py:165] ^^^^^^^^^^^^^^^^^^ ERROR 06-24 19:02:15 [engine.py:165] File "/usr/local/lib...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
