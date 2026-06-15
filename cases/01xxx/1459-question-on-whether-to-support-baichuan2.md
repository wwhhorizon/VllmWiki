# vllm-project/vllm#1459: Question on whether to support Baichuan2

| 字段 | 值 |
| --- | --- |
| Issue | [#1459](https://github.com/vllm-project/vllm/issues/1459) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question on whether to support Baichuan2

### Issue 正文摘录

Excuse me, everyone. I have modified the relevant files based on the solutions in the community, but using the API_ The following error occurred during client.py's inference: ![1b67679c50d282d02e40626260b9742](https://github.com/vllm-project/vllm/assets/138442712/1672c44a-66cd-4a44-8619-6640467d2a07) Then I added a judgment to the file as follows: ![8224a838f0eb05562921befdd5d2a77](https://github.com/vllm-project/vllm/assets/138442712/2e3e4e12-8b9f-4b29-9ac0-a9d0cc1f587d) The inference result was not output: ![c9fa7938a783880585a5c3b476511e5](https://github.com/vllm-project/vllm/assets/138442712/6ce5b235-1e63-4a3b-b0d8-80cfccaf4161) So I would like to ask if the framework's support for Baihuan2 has not yet been launched.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
