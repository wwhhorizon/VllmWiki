# vllm-project/vllm#10215: [Bug]:  vllm serve Exception in ASGI application 

| 字段 | 值 |
| --- | --- |
| Issue | [#10215](https://github.com/vllm-project/vllm/issues/10215) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  vllm serve Exception in ASGI application 

### Issue 正文摘录

### Your current environment ### Model Input Dumps model：qwen2.5-0.5b-instruct和Llama-3.2-1B-Instruct ### 🐛 Describe the bug **hardware env：Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz sofeware env：vllm6.3 CPU,** **run env： docker （image：inteldpo/vllm-cpu:v0.6.3），dockerhub：https://hub.docker.com/r/inteldpo/vllm-cpu/tags** **Physical machine** ： **when not Set the env TRITON_F32_DEFAULT=ieee and model run not --dtype float32，run server Inference success** **Virtual machine**：vmware **when Set the env TRITON_F32_DEFAULT=ieee，must set --dtype float32，but Very Slow Server Inference 。** **when not Set the env TRITON_F32_DEFAULT=ieee and model run not --dtype float32，run Server Inference error：** ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.10/dist-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tion in ASGI application bug;stale ### Your current environment ### Model Input Dumps model：qwen2.5-0.5b-instruct和Llama-3.2-1B-Instruct ### 🐛 Describe the bug **hardware env：Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz sofe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: eldpo/vllm-cpu/tags** **Physical machine** ： **when not Set the env TRITON_F32_DEFAULT=ieee and model run not --dtype float32，run server Inference success** **Virtual machine**：vmware **when Set the env TRITON_F32_DEFAU...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ： **when not Set the env TRITON_F32_DEFAULT=ieee and model run not --dtype float32，run server Inference success** **Virtual machine**：vmware **when Set the env TRITON_F32_DEFAULT=ieee，must set --dtype float32，but Very S...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm serve Exception in ASGI application bug;stale ### Your current environment ### Model Input Dumps model：qwen2.5-0.5b-instruct和Llama-3.2-1B-Instruct ### 🐛 Describe the bug **hardware env：Intel(R) Xeon(R) Gold...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Xeon(R) Gold 5118 CPU @ 2.30GHz sofeware env：vllm6.3 CPU,** **run env： docker （image：inteldpo/vllm-cpu:v0.6.3），dockerhub：https://hub.docker.com/r/inteldpo/vllm-cpu/tags** **Physical machine** ： **when not Set the env TR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
