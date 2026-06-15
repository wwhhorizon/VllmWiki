# vllm-project/vllm#27269: [Bug]: Hang issue for offline inference when using DP

| 字段 | 值 |
| --- | --- |
| Issue | [#27269](https://github.com/vllm-project/vllm/issues/27269) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Hang issue for offline inference when using DP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```py import os from vllm import LLM, SamplingParams if __name__ == "__main__": # os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER_MLA" os.environ["VLLM_ATTENTION_BACKEND"] = "CUTLASS_MLA" llm = LLM( model="deepseek-ai/DeepSeek-V2-lite", tensor_parallel_size=1, data_parallel_size=2, max_num_seqs=32, max_model_len=8192, enforce_eager=True, ) sp = SamplingParams( temperature=0.6, top_p=1.0, max_tokens=8, seed=1234, logprobs=5, ) outs = llm.generate(["There once was a "], sp, use_tqdm=True) print(outs) ``` Hanging here forever ```bash Adding requests: 100%|█████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 68.39it/s] Processed prompts: 0%| | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s] ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: plingParams if __name__ == "__main__": # os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER_MLA" os.environ["VLLM_ATTENTION_BACKEND"] = "CUTLASS_MLA" llm = LLM( model="deepseek-ai/DeepSeek-V2-lite", tensor_parallel_size...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng DP bug ### Your current environment ### 🐛 Describe the bug ```py import os from vllm import LLM, SamplingParams if __name__ == "__main__": # os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER_MLA" os.environ["VLLM_AT...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nviron["VLLM_ATTENTION_BACKEND"] = "CUTLASS_MLA" llm = LLM( model="deepseek-ai/DeepSeek-V2-lite", tensor_parallel_size=1, data_parallel_size=2, max_num_seqs=32, max_model_len=8192, enforce_eager=True, ) sp = SamplingPar...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: use_tqdm=True) print(outs) ``` Hanging here forever ```bash Adding requests: 100%|█████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 68.39it/s] Processed prompts: 0%| | 0/1 [00:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
