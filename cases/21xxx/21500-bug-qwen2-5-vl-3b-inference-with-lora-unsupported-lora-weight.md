# vllm-project/vllm#21500: [Bug]: qwen2.5-vl-3B inference with lora  "unsupported LoRA weight"

| 字段 | 值 |
| --- | --- |
| Issue | [#21500](https://github.com/vllm-project/vllm/issues/21500) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen2.5-vl-3B inference with lora  "unsupported LoRA weight"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug File "/home/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/lora/worker_manager.py", line 119, in _load_adapter ERROR 07-24 13:45:59 [core.py:517] lora = self._lora_model_cls.from_local_checkpoint( ERROR 07-24 13:45:59 [core.py:517] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-24 13:45:59 [core.py:517] File "/home/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/lora/models.py", line 264, in from_local_checkpoint ERROR 07-24 13:45:59 [core.py:517] check_unexpected_modules(f) ERROR 07-24 13:45:59 [core.py:517] File "/home/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/lora/models.py", line 229, in check_unexpected_modules ERROR 07-24 13:45:59 [core.py:517] module_name, _, _ = parse_fine_tuned_lora_name( ERROR 07-24 13:45:59 [core.py:517] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-24 13:45:59 [core.py:517] File "/home/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/lora/utils.py", line 148, in parse_fine_tuned_lora_name ERROR 07-24 13:45:59 [core.py:517] raise ValueError(f"{name} is unsupported LoRA weight") ERROR 07-24 13:45:59 [core.py:517] ValueError: base_model.model.language_model.lm_head.base_layer.w...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen2.5-vl-3B inference with lora "unsupported LoRA weight" bug ### Your current environment ### 🐛 Describe the bug File "/home/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/lora/worker_manager.py", line...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ght ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
