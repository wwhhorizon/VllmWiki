# vllm-project/vllm#27071: Can someone help When I upload an MP4 video, there will be an error that recognizes the video as an image

| 字段 | 值 |
| --- | --- |
| Issue | [#27071](https://github.com/vllm-project/vllm/issues/27071) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can someone help When I upload an MP4 video, there will be an error that recognizes the video as an image

### Issue 正文摘录

### 🚀 The feature, motivation and pitch LLM：Qwen2.5-Omni-7B-AWQ spring-ai: 1.1.0-M2 vllm： 0.11.0 My core code： `String mime; String suffix = requestPojo.getFileName().split("\.")[1]; switch (suffix) { case "png": mime = "image/png"; break; case "mp4": mime = "video/mp4"; break; default: mime = "image/jpeg"; } String finalMime = mime; promptUserSpec = u -> u .text(prompt1.getContents()) .media( Media.builder() .mimeType(MimeType.valueOf(finalMime)) .data(new FileSystemResource(uploadPath + File.separator +requestPojo.getFileName())) .build() );` After uploading to the large model, the error message is as follows： (APIServer pid=196656) ERROR 10-09 16:17:15 [serving_chat.py:245] Error in preprocessing prompt inputs (APIServer pid=196656) ERROR 10-09 16:17:15 [serving_chat.py:245] Traceback (most recent call last): (APIServer pid=196656) ERROR 10-09 16:17:15 [serving_chat.py:245] File "/home/venv_vllm_new/lib/python3.12/site-packages/vllm/multimodal/utils.py", line 244, in fetch_image_async (APIServer pid=196656) ERROR 10-09 16:17:15 [serving_chat.py:245] return await self.load_from_url_async( (APIServer pid=196656) ERROR 10-09 16:17:15 [serving_chat.py:245] ^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: image feature request;stale ### 🚀 The feature, motivation and pitch LLM：Qwen2.5-Omni-7B-AWQ spring-ai: 1.1.0-M2 vllm： 0.11.0 My core code： `String mime; String suffix = requestPojo.getFileName().split("\.")[1]; switch (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: eo, there will be an error that recognizes the video as an image feature request;stale ### 🚀 The feature, motivation and pitch LLM：Qwen2.5-Omni-7B-AWQ spring-ai: 1.1.0-M2 vllm： 0.11.0 My core code： `String mime; String...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: pt1.getContents()) .media( Media.builder() .mimeType(MimeType.valueOf(finalMime)) .data(new FileSystemResource(uploadPath + File.separator +requestPojo.getFileName()))
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
