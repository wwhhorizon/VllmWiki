# vllm-project/vllm#3013: Large length variance of sampled sequences from llama2 70b model compared to HuggingFace .generate()

| 字段 | 值 |
| --- | --- |
| Issue | [#3013](https://github.com/vllm-project/vllm/issues/3013) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Large length variance of sampled sequences from llama2 70b model compared to HuggingFace .generate()

### Issue 正文摘录

Hi all, thanks for this great inference framework. We enjoy the speedups coming from it, but we are concerned about too high sampling variance. Setting: **Model**: llama2 70b model finetuned on some data in our project. Exactly the same model is used in all of the decoding trials explained below. The dtype config in the model dir says `bfloat16`. **inference**: we test 4 different options: (1) HF generate, (2) HF generate with flash attn 2, (3) our own generation loop, (4) VLLM **Data**: eval set from this paper: 256 eval subset from this paper: https://arxiv.org/pdf/2308.06259.pdf **Compute**: 8 A100 gpus, device_map="auto" + torch.bfloat16 is used on HF side and in our internal generation loop. Sampling parameters are aligned across different decoding setups to be temp=0.7, topp=0.9, max gen length = 2048. We generate samples for eval set of 256 inputs prompts and then we compute the avg length of generated samples (in tokens) over this set. Now we do this 20 times with different random seeds and the expectation is that this the avg. length spread along 20 trials wont be too high. Here are the min->max values from these 20 runs per each decoding variant: 1. HF generate with vani...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Large length variance of sampled sequences from llama2 70b model compared to HuggingFace .generate() stale Hi all, thanks for this great inference framework. We enjoy the speedups coming from it, but we are concerned ab...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: he same model is used in all of the decoding trials explained below. The dtype config in the model dir says `bfloat16`. **inference**: we test 4 different options: (1) HF generate, (2) HF generate with flash attn 2, (3)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ese 20 runs per each decoding variant: 1. HF generate with vanilla attn backend: 441 -> 467 2. HF generate with flash attention 2: 429 -> 464 3. Our own generation loop: 388 -> 422 **4. vLLM: 343 -> 512** vllm shows muc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t from this paper: https://arxiv.org/pdf/2308.06259.pdf **Compute**: 8 A100 gpus, device_map="auto" + torch.bfloat16 is used on HF side and in our internal generation loop. Sampling parameters are aligned across differe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: w. The dtype config in the model dir says `bfloat16`. **inference**: we test 4 different options: (1) HF generate, (2) HF generate with flash attn 2, (3) our own generation loop, (4) VLLM **Data**: eval set from this pa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
