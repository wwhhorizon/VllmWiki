# vllm-project/vllm#7891: [Usage]: how to test the time of response about minicpm-v-2.6 served by VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7891](https://github.com/vllm-project/vllm/issues/7891) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to test the time of response about minicpm-v-2.6 served by VLLM

### Issue 正文摘录

### Your current environment I depoly minicpmv though VLLM, but I want to test the the time of response. First, I use OpenAI.chat.completions.create() to access the server. It response the result successfully. Code in the following: ![image](https://github.com/user-attachments/assets/07587d62-97e2-482a-8390-81af8365c3bc) And then, I use post request to access the server. Code is in the following: ![image](https://github.com/user-attachments/assets/fb0e5f31-1b9b-4684-8cf0-81acee7f5e24) ![image](https://github.com/user-attachments/assets/ef3c2597-176a-4c71-811f-bfbec2c20bf9) The log of server is ![image](https://github.com/user-attachments/assets/96fb271d-daf4-4e8b-b6d6-0399be667e0a) How can I send the request of json to server? ### 🐛 Describe the bug How can I send the request of json to server? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ments/assets/07587d62-97e2-482a-8390-81af8365c3bc) And then, I use post request to access the server. Code is in the following: ![image](https://github.com/user-attachments/assets/fb0e5f31-1b9b-4684-8cf0-81acee7f5e24) !...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Usage]: how to test the time of response about minicpm-v-2.6 served by VLLM usage ### Your current environment I depoly minicpmv though VLLM, but I want to test the the time of response. First, I use OpenAI.chat.comple...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
