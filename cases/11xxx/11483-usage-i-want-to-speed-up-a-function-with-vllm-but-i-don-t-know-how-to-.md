# vllm-project/vllm#11483: [Usage]: I want to speed up a function with VLLM, but I don't know how to do it

| 字段 | 值 |
| --- | --- |
| Issue | [#11483](https://github.com/vllm-project/vllm/issues/11483) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: I want to speed up a function with VLLM, but I don't know how to do it

### Issue 正文摘录

### Your current environment ```text 0.6.6 ``` ### How would you like to use vllm I have a Class now ``` from transformers import Qwen2ForCausalLM class Qwen2Encoder(torch.nn.Module): def __init__(self, pretrain_path): super().__init__() self.model = Qwen2ForCausalLM.from_pretrained(pretrain_path) def forward_one_step(self, xs, masks, cache=None): input_masks = masks[:, -1, :] outs = self.model( inputs_embeds=xs, attention_mask=input_masks, output_hidden_states=True, return_dict=True, use_cache=True, past_key_values=cache, ) xs = outs.hidden_states[-1] new_cache = outs.past_key_values return xs, new_cache ``` I only want to use VLLM to accelerate self.model(), while the rest of the process is different from the traditional big model flow, and I do it myself in python I don't know how to speed it up with vllm ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ld you like to use vllm I have a Class now ``` from transformers import Qwen2ForCausalLM class Qwen2Encoder(torch.nn.Module): def __init__(self, pretrain_path): super().__init__() self.model = Qwen2ForCausalLM.from_pret...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: How would you like to use vllm I have a Class now ``` from transformers import Qwen2ForCausalLM class Qwen2Encoder(torch.nn.Module): def __init__(self, pretrain_path): super().__init__() self.model = Qwen2ForCausalLM.fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
