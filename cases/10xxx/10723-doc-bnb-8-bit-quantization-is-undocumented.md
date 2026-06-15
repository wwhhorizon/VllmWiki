# vllm-project/vllm#10723: [Doc]: BNB 8 bit quantization is undocumented

| 字段 | 值 |
| --- | --- |
| Issue | [#10723](https://github.com/vllm-project/vllm/issues/10723) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: BNB 8 bit quantization is undocumented

### Issue 正文摘录

### 📚 The doc issue BNB 8 bit quantization is apparently supported as of https://github.com/vllm-project/vllm/pull/7445, but there is no detail on how to load in 8 bit on the [BNB documentation page](https://docs.vllm.ai/en/latest/quantization/bnb.html) ### Suggest a potential alternative/fix Give an example of using `load_in_4bit`/`load_in_8bit` on the documentation page ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Doc]: BNB 8 bit quantization is undocumented documentation ### 📚 The doc issue BNB 8 bit quantization is apparently supported as of https://github.com/vllm-project/vllm/pull/7445, but there is no detail on how to load...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: age ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: load in 8 bit on the [BNB documentation page](https://docs.vllm.ai/en/latest/quantization/bnb.html) ### Suggest a potential alternative/fix Give an example of using `load_in_4bit`/`load_in_8bit` on the documentation pag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
