# vllm-project/vllm#7745: [Bug]: llama 3.1 405B RuntimeError: start (1024) + length (256) exceeds dimension size (1024)

| 字段 | 值 |
| --- | --- |
| Issue | [#7745](https://github.com/vllm-project/vllm/issues/7745) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: llama 3.1 405B RuntimeError: start (1024) + length (256) exceeds dimension size (1024)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug originally found by https://github.com/vllm-project/vllm/issues/6732#issuecomment-2301552168 this is because the model checkpoint is the old one (before [huggingface.co/meta-llama/Meta-Llama-3.1-405B-FP8/tree/main](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-FP8/tree/main) ) , but the config is already updated. solution: re-download the whole model

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: llama 3.1 405B RuntimeError: start (1024) + length (256) exceeds dimension size (1024) bug ### Your current environment ### 🐛 Describe the bug originally found by https://github.com/vllm-project/vllm/issues/6732#...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nt is the old one (before [huggingface.co/meta-llama/Meta-Llama-3.1-405B-FP8/tree/main](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-FP8/tree/main) ) , but the config is already updated. solution: re-download t...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
