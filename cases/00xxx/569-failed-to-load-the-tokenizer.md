# vllm-project/vllm#569: Failed to load the tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#569](https://github.com/vllm-project/vllm/issues/569) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failed to load the tokenizer

### Issue 正文摘录

Traceback (most recent call last): File "src/inference_sft3.py", line 25, in main() File "src/inference_sft3.py", line 14, in main llm = LLM(model="/dev/shm/LLaMA-Efficient-Tuning/output/ziya_llama_13b_merged") File "/home/house365ai/anaconda3/envs/vllm/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 62, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/home/house365ai/anaconda3/envs/vllm/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 154, in from_engine_args engine = cls(*engine_configs, File "/home/house365ai/anaconda3/envs/vllm/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 80, in __init__ self.tokenizer = get_tokenizer( File "/home/house365ai/anaconda3/envs/vllm/lib/python3.8/site-packages/vllm/transformers_utils/tokenizer.py", line 42, in get_tokenizer raise RuntimeError(err_msg) from e RuntimeError: Failed to load the tokenizer. If you are using a LLaMA-based model, use 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: main() File "src/inference_sft3.py", line 14, in main llm = LLM(model="/dev/shm/LLaMA-Efficient-Tuning/output/ziya_llama_13b_merged") File "/home/house365ai/anaconda3/envs/vllm/lib/python3.8/site-packages/vllm/entrypoin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rence_sft3.py", line 14, in main llm = LLM(model="/dev/shm/LLaMA-Efficient-Tuning/output/ziya_llama_13b_merged") File "/home/house365ai/anaconda3/envs/vllm/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 62,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ad the tokenizer. If you are using a LLaMA-based model, use 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
