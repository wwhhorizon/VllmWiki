# vllm-project/vllm#3633: [Bug]: run vllm locally error, shows "socket.gaierror "

| 字段 | 值 |
| --- | --- |
| Issue | [#3633](https://github.com/vllm-project/vllm/issues/3633) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: run vllm locally error, shows "socket.gaierror "

### Issue 正文摘录

### Your current environment I use the following command to start a model locally: ``` python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.7 --max-model-len 29856 --model path/Qwen1__8B-Chat --tensor-parallel-size 4 --trust-remote-code ``` But vllm tries to connect with "dns.google". It shows the error as follows: s.connect(("dns.google", 80)) socket.gaierror: [Errno -2] Name or service not known I have searched the issues, but what is the exact solution for this ? ### 🐛 Describe the bug ![webwxgetmsgimg](https://github.com/vllm-project/vllm/assets/20237650/bc591fb7-f9c4-437c-b8d3-5b3302296c8e)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: bug ### Your current environment I use the following command to start a model locally: ``` python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.7 --max-model-len 29856 --m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le", 80)) socket.gaierror: [Errno -2] Name or service not known I have searched the issues, but what is the exact solution for this ? ### 🐛 Describe the bug ![webwxgetmsgimg](https://github.com/vllm-project/vllm/assets/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
