# vllm-project/vllm#12954: [Bug]: The output of using DeepSeek-R1 on A100 contains garbled characters

| 字段 | 值 |
| --- | --- |
| Issue | [#12954](https://github.com/vllm-project/vllm/issues/12954) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The output of using DeepSeek-R1 on A100 contains garbled characters

### Issue 正文摘录

### Your current environment vllm 0.7.1 ```text vllm serve /models/DeepSeek-R1/ --trust-remote-code --tensor-parallel-size 8 --pipeline-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.97 --enable-reasoning --reasoning-parser deepseek_r1 ``` ### 🐛 Describe the bug ```text when I run `python openai_chat_completion_with_rasoning.py` , the output contains garbled characters. ``` Output: ```text Okay, so I need to figure out which number is greater between 9.11 and 9.8. Let me start by just looking at them. Both are decimals, right? But 9.11 has two digits after the decimal point, while 9.8 only has one. Hmm, maybe I should compare them by aligning the decimal places to make 价格上涨，价格下跌？Wait, no, I should compare each place value once by once..... ``` ```text Okay, so I need to figure out which number is greater between 9.11 and 9.8. Let me start by just looking at them. Both are decimals, right? But 9.11 has two digits after the decimal point, while 9.8 only has one. Hmm, maybe I should compare them by aligning the decimal places to make 价格上涨，价格下跌？Wait, no, I should compare each place value once by once..... ``` Why does normal output contain various languages ​​such as...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: The output of using DeepSeek-R1 on A100 contains garbled characters bug ### Your current environment vllm 0.7.1 ```text vllm serve /models/DeepSeek-R1/ --trust-remote-code --tensor-parallel-size 8 --pipeline-para...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r between 9.11 and 9.8. Let me start by just looking at them. Both are decimals, right? But 9.11 has two digits after the decimal point, while 9.8 only has one. Hmm, maybe I should compare them by aligning the decimal p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: racters bug ### Your current environment vllm 0.7.1 ```text vllm serve /models/DeepSeek-R1/ --trust-remote-code --tensor-parallel-size 8 --pipeline-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.97 --e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
