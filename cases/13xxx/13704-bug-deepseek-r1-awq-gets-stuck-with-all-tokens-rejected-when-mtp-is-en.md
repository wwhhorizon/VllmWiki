# vllm-project/vllm#13704: [Bug]: DeepSeek-R1-AWQ gets stuck with all tokens rejected when MTP is enabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#13704](https://github.com/vllm-project/vllm/issues/13704) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-R1-AWQ gets stuck with all tokens rejected when MTP is enabled.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run command: ``` vllm serve --enable-chunked-prefill --enable-prefix-caching -tp 8 cognitivecomputations/DeepSeek-R1-AWQ --dtype float16 --trust-remote-code --max-model-len 131072 --max-seq-len-to-capture 131072 --num-speculative-tokens 1 ``` Symptom: Upon receiving a request, only the first word (for example "Okay") is generated, then the generation is stuck and no new tokens are streamed. ![Image](https://github.com/user-attachments/assets/035934c3-12ec-44f7-a333-fe8fbd9e987d) As can see from the console log, number of accepted tokens remains 0 while number draft tokens increases. After removing `--num-speculative-tokens 1` vllm works fine. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ### 🐛 Describe the bug Run command: ``` vllm serve --enable-chunked-prefill --enable-prefix-caching -tp 8 cognitivecomputations/DeepSeek-R1-AWQ --dtype float16 --trust-remote-code --max-model-len 131072 --max-seq-len-to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ll --enable-prefix-caching -tp 8 cognitivecomputations/DeepSeek-R1-AWQ --dtype float16 --trust-remote-code --max-model-len 131072 --max-seq-len-to-capture 131072 --num-speculative-tokens 1 ``` Symptom: Upon receiving a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vecomputations/DeepSeek-R1-AWQ --dtype float16 --trust-remote-code --max-model-len 131072 --max-seq-len-to-capture 131072 --num-speculative-tokens 1 ``` Symptom: Upon receiving a request, only the first word (for exampl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
