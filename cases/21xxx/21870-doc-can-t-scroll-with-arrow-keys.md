# vllm-project/vllm#21870: [Doc]: Can't scroll with arrow keys

| 字段 | 值 |
| --- | --- |
| Issue | [#21870](https://github.com/vllm-project/vllm/issues/21870) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Can't scroll with arrow keys

### Issue 正文摘录

### 📚 The doc issue If I visit https://docs.vllm.ai/en/latest/ and press the down arrow key on my keyboard the page doesn't scroll. Page Down does seem to work. ### Suggest a potential alternative/fix It looks like there is a documentation search feature on this page that activates when I type a letter. It must have a broad key event listener to achieve this. It should ignore the arrow keys (i.e. _not_ call `preventDefault()` on their events) until it activates. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: st a potential alternative/fix It looks like there is a documentation search feature on this page that activates when I type a letter. It must have a broad key event listener to achieve this. It should ignore the arrow...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: documentation ### 📚 The doc issue If I visit https://docs.vllm.ai/en/latest/ and press the down arrow key on my keyboard the page doesn't scroll. Page Down does seem to work. ### Suggest a potential alternative/fix It l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
