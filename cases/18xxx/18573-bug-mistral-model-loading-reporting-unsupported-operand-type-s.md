# vllm-project/vllm#18573: [Bug]: Mistral model loading reporting unsupported operand type(s)

| 字段 | 值 |
| --- | --- |
| Issue | [#18573](https://github.com/vllm-project/vllm/issues/18573) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mistral model loading reporting unsupported operand type(s)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If you run the script of ``` LLM( model="mistralai/Mistral-7B-Instruct-v0.2", **vllm_kwargs, ) ``` or any models based on Mistral, you would encounter the issue ``` TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'` ``` in `vllm/model_executor/models/llama.py` line 135. --- ### Solution: I think VLLM is trying to be efficient in terms of loading Mistral model using their source code from Llama, which is totally fine. The real issue lies in the line 131 in `vllm/model_executor/models/llama.py`, where they have this line of ``` self.head_dim = getattr(config, "head_dim", self.hidden_size // self.total_num_heads) ``` The interesting thing here is that MistralConfig does seem to contain the key of `head_dim` (corresponding to a value of `null`), which means that it will get the value of NoneType. Therefore, a simple and quick fix is to replace the line 131 by ``` if not getattr(config, "head_dim"): self.head_dim = self.hidden_size // self.total_num_heads else: self.head_dim = getattr(config, "head_dim", self.hidden_size // self.total_num_heads) ``` Hope this helps! --- ### Official Fix: The issue has been fixed in a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Mistral model loading reporting unsupported operand type(s) bug ### Your current environment ### 🐛 Describe the bug If you run the script of ``` LLM( model="mistralai/Mistral-7B-Instruct-v0.2", **vllm_k
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ama.py` line 135. --- ### Solution: I think VLLM is trying to be efficient in terms of loading Mistral model using their source code from Llama, which is totally fine. The real issue lies in the line 131 in `vllm/model_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ): self.head_dim = self.hidden_size // self.total_num_heads else: self.head_dim = getattr(config, "head_dim", self.hidden_size // self.total_num_heads) ``` Hope this helps! --- ### Official Fix: The issue has been fixed...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
