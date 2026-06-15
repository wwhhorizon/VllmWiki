# vllm-project/vllm#33276: [Usage]: question about gguf gemma3-4b different output from llama_cpp

| 字段 | 值 |
| --- | --- |
| Issue | [#33276](https://github.com/vllm-project/vllm/issues/33276) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: question about gguf gemma3-4b different output from llama_cpp

### Issue 正文摘录

### Your current environment Use the same prompt system_prompt+user_prompt(Always output pure JSON.xxxx) . And model is google/gemma-3-4b-it-qat-q4_0-gguf. It asks output to be json. The llama cpp works well . but vllm does not which output plain text not json format Anyway to adjust context len? ``` from llama_cpp import Llama llm = Llama.from_pretrained( repo_id="google/gemma-3-4b-it-qat-q4_0-gguf", filename="gemma-3-4b-it-q4_0.gguf", n_ctx=4096*2, # set your desired context window n_gpu_layers=-1, # optional: use GPU ) ``` vs ``` from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.7, max_tokens=512) # Create an LLM. llm = LLM( model="./gemma-3-4b-it-q4_0.gguf", tokenizer="google/gemma-3-4b-it", n_ctx=4096*2, ) ``` ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: question about gguf gemma3-4b different output from llama_cpp usage;stale ### Your current environment Use the same prompt system_prompt+user_prompt(Always output pure JSON.xxxx) . And model is google/gemma-3-4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n text not json format Anyway to adjust context len? ``` from llama_cpp import Llama llm = Llama.from_pretrained( repo_id="google/gemma-3-4b-it-qat-q4_0-gguf", filename="gemma-3-4b-it-q4_0.gguf", n_ctx=4096*2, # set you...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Usage]: question about gguf gemma3-4b different output from llama_cpp usage;stale ### Your current environment Use the same prompt system_prompt+user_prompt(Always output pure JSON.xxxx) . And model is google/gemma-3-4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: question about gguf gemma3-4b different output from llama_cpp usage;stale ### Your current environment Use the same prompt system_prompt+user_prompt(Always output pure JSON.xxxx) . And model is google/gemma-3-4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
