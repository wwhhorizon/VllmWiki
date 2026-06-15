# vllm-project/vllm#26636: [Bug]: AsyncHttpClient incorrectly decodes URLs via aiohttp, breaking signed URLs (e.g., S3)

| 字段 | 值 |
| --- | --- |
| Issue | [#26636](https://github.com/vllm-project/vllm/issues/26636) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AsyncHttpClient incorrectly decodes URLs via aiohttp, breaking signed URLs (e.g., S3)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Description The `AsyncHttpClient.get_async_response` method in `vllm/connections.py` incorrectly decodes URL-encoded characters in the path component when making requests via `aiohttp`. This behavior is inconsistent with the synchronous counterpart that uses `requests`, which handles the URL correctly. This automatic decoding breaks pre-signed URLs, particularly those from services like AWS S3, which rely on the exact, encoded URL path for signature validation. When a URL like `.../path%2Fto%2Ffile.jpg?signature=...` is passed, the `%2F` (encoded slash) is decoded to / by the client. The server then sees a different path than what was used to generate the signature, causing a signature mismatch and a `403 Forbidden` error. ## To Reproduce The following minimal, reproducible example demonstrates the issue using httpbin.org, which echoes back the request details. This avoids exposing any sensitive URLs. 1. Save the following code as test_vllm_url.py: ``` import asyncio from vllm.connections import AsyncHttpClient async def main(): # The path component '/path%2Fwith%2Fencoded%2Fslash' should be sent as-is. # httpbin.org/anyth...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: t path than what was used to generate the signature, causing a signature mismatch and a `403 Forbidden` error. ## To Reproduce The following minimal, reproducible example demonstrates the issue using httpbin.org, which...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a `403 Forbidden` error. ## To Reproduce The following minimal, reproducible example demonstrates the issue using httpbin.org, which echoes back the request details. This avoids exposing any sensitive URLs. 1. Save the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: AsyncHttpClient incorrectly decodes URLs via aiohttp, breaking signed URLs (e.g., S3) bug;stale ### Your current environment ### 🐛 Describe the bug ## Bug Description The `AsyncHttpClient.get_async_response` meth...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: path than what was used to generate the signature, causing a signature mismatch and a `403 Forbidden` error. ## To Reproduce The following minimal, reproducible example demonstrates the issue using httpbin.org, which ec...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: *, timeout: Optional[float] = None, extra_headers: Optional[Mapping[str, str]] = None, allow_redirects: bool = True, ): self._validate_http_url(url) client = await self.get_async_client() extra_headers = extra_headers o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
