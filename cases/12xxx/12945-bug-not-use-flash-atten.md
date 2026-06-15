# vllm-project/vllm#12945: [Bug]: Not use flash_atten

| 字段 | 值 |
| --- | --- |
| Issue | [#12945](https://github.com/vllm-project/vllm/issues/12945) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Not use flash_atten

### Issue 正文摘录

### Your current environment Hello, this is the error message: ImportError: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.26' not found (required by /usr/local/lib/python3.9/site-packages/flash_attn_2_cuda.cpython-39-x86_64-linux-gnu.so) I am currently unable to solve this problem due to some reasons. Can I not use flash_atten? How can I turn it off? ### 🐛 Describe the bug Hello, this is the error message: ImportError: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.26' not found (required by /usr/local/lib/python3.9/site-packages/flash_attn_2_cuda.cpython-39-x86_64-linux-gnu.so) I am currently unable to solve this problem due to some reasons. Can I not use flash_atten? How can I turn it off? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tten bug ### Your current environment Hello, this is the error message: ImportError: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.26' not found (required by /usr/local/lib/python3.9/site-packages/flash_attn_2_cuda.cp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t found (required by /usr/local/lib/python3.9/site-packages/flash_attn_2_cuda.cpython-39-x86_64-linux-gnu.so) I am currently unable to solve this problem due to some reasons. Can I not use flash_atten? How can I turn it...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
