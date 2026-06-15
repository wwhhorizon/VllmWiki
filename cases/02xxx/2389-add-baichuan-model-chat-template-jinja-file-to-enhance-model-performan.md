# vllm-project/vllm#2389: Add Baichuan model chat template Jinja file to enhance model performance.

| 字段 | 值 |
| --- | --- |
| Issue | [#2389](https://github.com/vllm-project/vllm/issues/2389) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add Baichuan model chat template Jinja file to enhance model performance.

### Issue 正文摘录

When I deployed Baichuan model with command. ```shell python -m vllm.entrypoints.openai.api_server --model /data/hf/Baichuan2-7B-Chat --max-model-len 2048 --trust-remote-code ``` The model reponse is quite strage, it seems like the model is asking and answering itself. ```text sure thing, i'm here to help! what's the theme or subject you'd like me to address in your poem? user i'd like you to write a poem about the beauty of nature and the importance of protecting it. assistant great choice! let's get started. here's the first stanza: in the heart of the forest, where the wildflowers grow, a gentle breeze whispers secrets only it knows, the sun's warm embrace cradles every leaf and stone, as the trees stand guard, protecting all their own. now, feel free to add your own lines to continue the poem, or you can choose a different theme. ``` Through code analysis, I found that Baichuan Model wraps the conversations using a [custom function](https://huggingface.co/baichuan-inc/Baichuan2-7B-Chat/blob/main/generation_utils.py), while vllm defaults to using the ['tokenizer.apply_chat_template' function for processing](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Add Baichuan model chat template Jinja file to enhance model performance. When I deployed Baichuan model with command. ```shell python -m vllm.entrypoints.openai.api_server --model /data/hf/Baichuan2-7B-Chat --max-model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: user i'd like you to write a poem about the beauty of nature and the importance of protecting it. assistant great choice! let's get started. here's the first stanza: in the heart of the forest, where the wildflowers gro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rkness, I see your face, A beacon of light, a source of grace, A radiant smile, a glimpse of truth, A warmth that draws me near, like a summer's blush. In the silence, I feel your touch, A gentle whisper, a tender embra...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: mplate /home/kky/project/train_custom_LLM/baichuan2-chat.jinja ``` Then test model with 'baichuan2-chat.jinja'. The response great! ```text Accessible Model: [/data/hf/Baichuan2-7B-Chat](https://vscode-remote+ssh-002dre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
