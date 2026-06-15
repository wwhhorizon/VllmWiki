# vllm-project/vllm#15753: [Bug]: TPU 8 parallel option points llama model which not intended

| 字段 | 值 |
| --- | --- |
| Issue | [#15753](https://github.com/vllm-project/vllm/issues/15753) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TPU 8 parallel option points llama model which not intended

### Issue 正文摘录

### Your current environment Hello team, I'm testing PHI-4 model on TPU V5e 8 chip. Actually, the model runs well on Hex-LLM but not VLLM-TPU I installed v0.8.1 and run following command to test model loading vllm serve microsoft/phi-4 --download_dir /tmp --num-scheduler-steps 4 --swap-space 16 --disable-log-requests --tensor_parallel_size=8 --max-model-len=2048 Weird thing is why Phi-4 routed to Llama and failed to load by some divider mismatch. I'm not familiar with to fix the loader. It would be good someone guide me where to fix. ### 🐛 Describe the bug vllm serve microsoft/phi-4 --tensor_parallel_size=8 points Llama loader and failed on --tensor_parallel_size=8 option. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: r current environment Hello team, I'm testing PHI-4 model on TPU V5e 8 chip. Actually, the model runs well on Hex-LLM but not VLLM-TPU I installed v0.8.1 and run following command to test model loading vllm serve micros...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: TPU 8 parallel option points llama model which not intended bug ### Your current environment Hello team, I'm testing PHI-4 model on TPU V5e 8 chip. Actually, the model runs well on Hex-LLM but not VLLM-TPU I inst...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: test model loading vllm serve microsoft/phi-4 --download_dir /tmp --num-scheduler-steps 4 --swap-space 16 --disable-log-requests --tensor_parallel_size=8 --max-model-len=2048 Weird thing is why Phi-4 routed to Llama and...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: rd thing is why Phi-4 routed to Llama and failed to load by some divider mismatch. I'm not familiar with to fix the loader. It would be good someone guide me where to fix. ### 🐛 Describe the bug vllm serve microsoft/phi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 5e 8 chip. Actually, the model runs well on Hex-LLM but not VLLM-TPU I installed v0.8.1 and run following command to test model loading vllm serve microsoft/phi-4 --download_dir /tmp --num-scheduler-steps 4 --swap-space...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
