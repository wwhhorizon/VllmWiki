# vllm-project/vllm#10428: [Doc]: Pages were moved without a redirect

| 字段 | 值 |
| --- | --- |
| Issue | [#10428](https://github.com/vllm-project/vllm/issues/10428) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Pages were moved without a redirect

### Issue 正文摘录

### 📚 The doc issue In #9924, some pages were moved from the `/dev/` directory to the `/design/` directory. However, there's no redirect configured for the moved pages so the old URLs are returning 404 errors (for example: https://docs.vllm.ai/en/latest/dev/kernel/paged_attention.html). ### Suggest a potential alternative/fix For readthedocs, the way to add redirects seems to be https://docs.readthedocs.io/en/stable/guides/redirects.html ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tml ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ev/` directory to the `/design/` directory. However, there's no redirect configured for the moved pages so the old URLs are returning 404 errors (for example: https://docs.vllm.ai/en/latest/dev/kernel/paged_attention.ht...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ld URLs are returning 404 errors (for example: https://docs.vllm.ai/en/latest/dev/kernel/paged_attention.html). ### Suggest a potential alternative/fix For readthedocs, the way to add redirects seems to be https://docs....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
