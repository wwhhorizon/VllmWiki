# vllm-project/vllm#1990: How to fix incomplete answers?

| 字段 | 值 |
| --- | --- |
| Issue | [#1990](https://github.com/vllm-project/vllm/issues/1990) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to fix incomplete answers?

### Issue 正文摘录

Tried the vllm both with gpt2-xl and llama2-7b-awq and in both cases I get incomplete answers Here's the code: ``` prompt = [ "What is Quantum Computing?", "How are electrons and protons different?", ] llm = LLM(model="TheBloke/Llama-2-7b-Chat-AWQ", quantization="AWQ") answers = llm.generate(prompt) for i in range(2): print("\nPrompt:",prompt[i],"\nGeneration:",answers[i].outputs[0].text) print() ``` Here's the output ``` Prompt: What is Quantum Computing? Generation: Quantum computing is a rapidly developing field that uses the principles of quantum Prompt: How are electrons and protons different? Generation: Electrons and protons are two types of subatomic particles that ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: How to fix incomplete answers? Tried the vllm both with gpt2-xl and llama2-7b-awq and in both cases I get incomplete answers Here's the code: ``` prompt = [ "What is Quantum Computing?", "How are electrons and protons d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ion: Quantum computing is a rapidly developing field that uses the principles of quantum Prompt: How are electrons and protons different? Generation: Electrons and protons are two types of subatomic particles that ```
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s I get incomplete answers Here's the code: ``` prompt = [ "What is Quantum Computing?", "How are electrons and protons different?", ] llm = LLM(model="TheBloke/Llama-2-7b-Chat-AWQ", quantization="AWQ") answers = llm.ge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
