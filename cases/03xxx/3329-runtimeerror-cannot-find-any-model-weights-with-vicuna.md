# vllm-project/vllm#3329: RuntimeError: Cannot find any model weights with vicuna

| 字段 | 值 |
| --- | --- |
| Issue | [#3329](https://github.com/vllm-project/vllm/issues/3329) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RuntimeError: Cannot find any model weights with vicuna

### Issue 正文摘录

Does vllm supports vicuna? I check the doc and find it supports, but when I use: `python3 -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --model /home/huggingface_models/models--lmsys--vicuna-13b-v1.5/snapshots/3deb0106f72a3a433f0c6ea0cb978bdf14bcd3a6 --tensor-parallel-size 2 --load-format safe-tensors --port 8401` It returns: `RuntimeError: Cannot find any model weights with `/home/huggingface_models/models--lmsys--vicuna-13b-v1.5/snapshots/3deb0106f72a3a433f0c6ea0cb978bdf14bcd3a6`` In /home/huggingface_models/models--lmsys--vicuna-13b-v1.5/snapshots/3deb0106f72a3a433f0c6ea0cb978bdf14bcd3a6, I have ![image](https://github.com/vllm-project/vllm/assets/56245837/00cc59df-e57f-4791-8e93-5bc8f132df21) Do you know what is wrong?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: RuntimeError: Cannot find any model weights with vicuna Does vllm supports vicuna? I check the doc and find it supports, but when I use: `python3 -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --model /home/hug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
