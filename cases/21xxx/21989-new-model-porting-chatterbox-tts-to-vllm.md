# vllm-project/vllm#21989: [New Model]: Porting Chatterbox TTS to VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#21989](https://github.com/vllm-project/vllm/issues/21989) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Porting Chatterbox TTS to VLLM

### Issue 正文摘录

### The model to consider. Community/unaffiliated effort to port Chatterbox to VLLM. * Original HF: https://huggingface.co/ResembleAI/chatterbox * Original Repo: https://github.com/resemble-ai/chatterbox * Port Repo: https://github.com/randombk/chatterbox-vllm ### The closest model vllm already supports. `vllm.model_executor.models.llama.LlamaModel` ### What's your difficulty of supporting the model you want? Hi folks, I'm looking for advice on implementing a non-standard model architecture (https://github.com/randombk/chatterbox-vllm). It's a Text-to-Speech model applying intermediate fusion multimodal conditioning to a 0.5B parameter Llama model to generate speech tokens. Right now, via a set of horrendous hacks, I have the core running in VLLM for unbatched requests. For batched requests, there are a few API limitations that are causing difficulty. They're solvable via more hacks, but I'd like to see if there are more idiomatic approaches/alternatives I've missed. I'm also willing to help extend/improve VLLM if folks can point me in the right direction. The primary relevant file is at https://github.com/randombk/chatterbox-vllm/blob/master/src/chatterbox_vllm/models/t3/t3.py. F...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: Porting Chatterbox TTS to VLLM ### The model to consider. Community/unaffiliated effort to port Chatterbox to VLLM. * Original HF: https://huggingface.co/ResembleAI/chatterbox * Original Repo: https://githu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: a set of horrendous hacks, I have the core running in VLLM for unbatched requests. For batched requests, there are a few API limitations that are causing difficulty. They're solvable via more hacks, but I'd like to see...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: bk/chatterbox-vllm/blob/master/src/chatterbox_vllm/models/t3/t3.py. For dependency reasons I'm currently using VLLM `0.9.2` There are two blockers right now. # 1: Multimodal embedding The primary blocker lies with the m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Hi folks, I'm looking for advice on implementing a non-standard model architecture (https://github.com/randombk/chatterbox-vllm). It's a Text-to-Speech model applying intermediate fusion multimodal conditioning to a 0.5...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: For dependency reasons I'm currently using VLLM `0.9.2` There are two blockers right now. # 1: Multimodal embedding The primary blocker lies with the multimodal `get_input_embeddings` method, and how it combines prefill...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
