# vllm-project/vllm#26122: [Performance]: disagg_proxy_demo server request throughput is low

| 字段 | 值 |
| --- | --- |
| Issue | [#26122](https://github.com/vllm-project/vllm/issues/26122) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: disagg_proxy_demo server request throughput is low

### Issue 正文摘录

### Your current environment The use of aiohttp the make ephemeral client connections slows down request handling by both the proxy and underlying api servers running on prefillers and decoders because of connection juggling overhead. Switching to using httpx AsyncClient (or other) to create reusable, long-standing TCP connections might be a better way manage communications. ### 🐛 Describe the bug aiohttp.ClientSession() context manager creates a new connection each time it's called. This can create connection thrash on the prefillers and decoders. ```python url = f"http://{instance}/v1/models" try: async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as client: async with client.get(url) as response: ... ``` Using something like httpx lets you create longstanding clients that can be reused: ```python async def forward_request( self, client: httpx.AsyncClient, url, data): headers = {"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"} response = await client.post( url=url, json=data, headers=headers ) response.raise_for_status() return response ``` Added bonus of easier support for streaming. ### Before submitting a new issue... - [x] Make sure you already searched...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: disagg_proxy_demo server request throughput is low bug;stale ### Your current environment The use of aiohttp the make ephemeral client connections slows down request handling by both the proxy and underly...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: disagg_proxy_demo server request throughput is low bug;stale ### Your current environment The use of aiohttp the make ephemeral client connections slows down request handling by both the proxy and underly...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on the prefillers and decoders. ```python url = f"http://{instance}/v1/models" try: async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as client: async with client.get(url) as response: ... ``` Using something li...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
