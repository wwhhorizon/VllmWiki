# vllm-project/vllm#8030: [Installation]: LGPL license in dependencies

| 字段 | 值 |
| --- | --- |
| Issue | [#8030](https://github.com/vllm-project/vllm/issues/8030) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: LGPL license in dependencies

### Issue 正文摘录

### Your current environment Since vLLM 0.5.5 there is a [dependency](https://github.com/vllm-project/vllm/blob/2148441fd371faf3e90748b310fdb4500939e527/requirements-common.txt#L25C12-L25C13) on Librosa, which in turn [depends](https://github.com/librosa/librosa/blob/main/setup.cfg#L74) on soxr. Soxr is LGPL licensed which is a big red flag for many corporations. I'm not a legal expert but I do understand that LGPL is more permissive than regular GPL or AGPL. However many large firms still consider it too risky and block any LGPL license by default and as a result I am now no longer able to install vLLM in my firm (Fortune 50 size). I would kindly request to reconsider the use of Librosa.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: LGPL license in dependencies installation ### Your current environment Since vLLM 0.5.5 there is a [dependency](https://github.com/vllm-project/vllm/blob/2148441fd371faf3e90748b310fdb4500939e527/requireme
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ar GPL or AGPL. However many large firms still consider it too risky and block any LGPL license by default and as a result I am now no longer able to install vLLM in my firm (Fortune 50 size). I would kindly request to...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: licensed which is a big red flag for many corporations. I'm not a legal expert but I do understand that LGPL is more permissive than regular GPL or AGPL. However many large firms still consider it too risky and block an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: onger able to install vLLM in my firm (Fortune 50 size). I would kindly request to reconsider the use of Librosa.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
