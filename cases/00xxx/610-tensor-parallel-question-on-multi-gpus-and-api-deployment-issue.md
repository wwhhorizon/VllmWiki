# vllm-project/vllm#610: tensor parallel question on multi-GPUs and API deployment issue

| 字段 | 值 |
| --- | --- |
| Issue | [#610](https://github.com/vllm-project/vllm/issues/610) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> tensor parallel question on multi-GPUs and API deployment issue

### Issue 正文摘录

I tried this `NCCL_IGNORE_DISABLED_P2P=1 CUDA_VISIBLE_DEVICES=1,5,6,7 python vllm_inference.py --model_name model_hub/llama2-7B-chat-hf --tp_size 4` and found that the memory usage on GPUs was like this ![image](https://github.com/vllm-project/vllm/assets/106091458/ce3ae834-a43a-4e48-963f-aff280f277d7) This is just a 7B model, did I apply TP strategy incorrectly? Also, I'm very confused that the inference can work on a single GPU actually, but when I try to start an API using llmengine，it always stuck in the process reporting blocks of gpu and cpu like this, ![image](https://github.com/vllm-project/vllm/assets/106091458/d3fc433b-3813-4ac7-86d0-fd33aa7e4123) that's the reason why I tried tensor parallel in API deployment.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: E_DISABLED_P2P=1 CUDA_VISIBLE_DEVICES=1,5,6,7 python vllm_inference.py --model_name model_hub/llama2-7B-chat-hf --tp_size 4` and found that the memory usage on GPUs was like this ![image](https://github.com/vllm-project...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Us and API deployment issue bug I tried this `NCCL_IGNORE_DISABLED_P2P=1 CUDA_VISIBLE_DEVICES=1,5,6,7 python vllm_inference.py --model_name model_hub/llama2-7B-chat-hf --tp_size 4` and found that the memory usage on GPU...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: to start an API using llmengine，it always stuck in the process reporting blocks of gpu and cpu like this, ![image](https://github.com/vllm-project/vllm/assets/106091458/d3fc433b-3813-4ac7-86d0-fd33aa7e4123) that's the r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
