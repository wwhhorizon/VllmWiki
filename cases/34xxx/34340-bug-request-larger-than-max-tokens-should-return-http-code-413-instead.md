# vllm-project/vllm#34340: [Bug]: request larger than max_tokens should return http code 413 instead of 400

| 字段 | 值 |
| --- | --- |
| Issue | [#34340](https://github.com/vllm-project/vllm/issues/34340) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: request larger than max_tokens should return http code 413 instead of 400

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug Now, when user request with a large content, vllm return http code 400 as follow. ```json {"detail":"Upstream[decode] error, b'{\"error\":{\"message\":\"\\'max_tokens\\' or \\'max_completion_tokens\\' is too large: 65536. This model\\'s maximum context length is 262144 tokens and your request has 203462 input tokens (65536 > 262144 - 203462). None\",\"type\":\"BadRequestError\",\"param\":null,\"code\":400}}'"}, ``` According to Web standard, [http code 400](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/400) indicates that the server would not process the request due to something the server considered to be a client error. The reason for a 400 response is typically due to malformed request syntax, invalid request message framing, or deceptive request routing. While [http code 413](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/413) indicates that the request entity was larger than limits defined by server. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](http...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: request larger than max_tokens should return http code 413 instead of 400 bug;stale ### Your current environment N/A ### 🐛 Describe the bug Now, when user request with a large content, vllm return http code 400 a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ed request syntax, invalid request message framing, or deceptive request routing. While [http code 413](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/413) indicates that the request entity was large...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: \'max_tokens\\' or \\'max_completion_tokens\\' is too large: 65536. This model\\'s maximum context length is 262144 tokens and your request has 203462 input tokens (65536 > 262144 - 203462). None\",\"type\":\"BadRequest...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ed request syntax, invalid request message framing, or deceptive request routing. While [http code 413](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/413) indicates that the request entity was large...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
