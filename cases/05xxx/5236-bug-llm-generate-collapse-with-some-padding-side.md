# vllm-project/vllm#5236: [Bug]: LLM.generate() collapse with some padding side

| 字段 | 值 |
| --- | --- |
| Issue | [#5236](https://github.com/vllm-project/vllm/issues/5236) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LLM.generate() collapse with some padding side

### Issue 正文摘录

### Your current environment ```text Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.2 ``` ### 🐛 Describe the bug Padding the input with some side seems to causes the generation by the LLM to break down. In the examples, I have only run this for one model, but the same phenomenon occurs with other models as well. Reasonable generation results can be obtained by not padding the input, but I would greatly appreciate it if you could explain the cause of this issue. ```python from __future__ import annotations from contextlib import contextmanager from transformers import AutoTokenizer, PreTrainedTokenizer from vllm import LLM, SamplingParams model_name = "Qwen/Qwen1.5-7B-Chat" tokenizer: PreTrainedTokenizer = AutoTokenizer.from_pretrained(model_name) llm = LLM(model_name) print("Original padding side: ", tokenizer.padding_side) prompt1 = "Give me a short introduction to large language model." # prompt2 is short, so padded. prompt2 = "Hello" messages = [ [{"role": "system", "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ollapse with some padding side bug ### Your current environment ```text Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: by the LLM to break down. In the examples, I have only run this for one model, but the same phenomenon occurs with other models as well. Reasonable generation results can be obtained by not padding the input, but I woul...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: iton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.2 ``` ### 🐛 Describe the bug Padding the input with some side seems to c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : prompt2}], ] text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) @contextmanager def set_temporal_padding_side(tokenizer: PreTrainedTokenizer, padding_side: str): """Temporarily...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
