# vllm-project/vllm#17077: [Bug]: Aria model error due to version mismatch with transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#17077](https://github.com/vllm-project/vllm/issues/17077) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Aria model error due to version mismatch with transformers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying the [Aria-Chat ](https://huggingface.co/rhymes-ai/Aria-Chat)model with the vLLM serve, the engine throws an error: `LLAMA_ATTENTION_CLASSES' from 'transformers.models.llama.modeling_llama` Digging into the transformers class I can see that they no longer have such a variable. Last transformers version that had `LLAMA_ATTENTION_CLASSES` is [v0.47.1](https://github.com/huggingface/transformers/blob/v4.47.1/src/transformers/models/llama/modeling_llama.py): Any other version after that does not have it and thus explains the issue. **Manual workaround**: After installing vLLM, downgrade transformers: `pip install transformers<=4.47.1` For reference, here's how I'm deploying the model: ``` python -m vllm.entrypoints.openai.api_server \ --model rhymes-ai/Aria-Chat \ --host 0.0.0.0 --port 8080 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Aria model error due to version mismatch with transformers bug ### Your current environment ### 🐛 Describe the bug When deploying the [Aria-Chat ](https://huggingface.co/rhymes-ai/Aria-Chat)model with the vLLM se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Aria model error due to version mismatch with transformers bug ### Your current environment ### 🐛 Describe the bug When deploying the [Aria-Chat ](https://huggingface.co/rhymes-ai/Aria-Chat)model with the vLLM se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Aria model error due to version mismatch with transformers bug ### Your current environment ### 🐛 Describe the bug When deploying the [Aria-Chat ](https://huggingface.co/rhymes-ai/Aria-Chat)model with the vLLM se...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Aria model error due to version mismatch with transformers bug ### Your current environment ### 🐛 Describe the bug When deploying the [Aria-Chat ](https://huggingface.co/rhymes-ai/Aria-Chat)model with the vLLM se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
