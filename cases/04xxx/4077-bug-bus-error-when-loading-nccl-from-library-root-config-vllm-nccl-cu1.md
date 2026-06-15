# vllm-project/vllm#4077: [Bug]: bus error  when  Loading nccl from library /root/.config/vllm/nccl/cu12/libnccl.so.2.18.1

| 字段 | 值 |
| --- | --- |
| Issue | [#4077](https://github.com/vllm-project/vllm/issues/4077) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: bus error  when  Loading nccl from library /root/.config/vllm/nccl/cu12/libnccl.so.2.18.1

### Issue 正文摘录

### Your current environment python3 collect_env.py Collecting environment information... INFO 04-15 10:56:57 pynccl.py:58] Loading nccl from library /root/.config/vllm/nccl/cu12/libnccl.so.2.18.1 [1] 842586 bus error python3 collect_env.py ### 🐛 Describe the bug INFO 04-15 10:54:04 pynccl.py:58] Loading nccl from library /root/.config/vllm/nccl/cu12/libnccl.so.2.18.1 [1] 817166 bus error python3

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: bus error when Loading nccl from library /root/.config/vllm/nccl/cu12/libnccl.so.2.18.1 bug ### Your current environment python3 collect_env.py Collecting environment information... INFO 04-15 10:56:57 pynccl.py:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
