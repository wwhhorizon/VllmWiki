# vllm-project/vllm#26121: [Bug]:  vLLM merges special XML-like tags into single tokens, causing tokenization mismatch with HuggingFace

| 字段 | 值 |
| --- | --- |
| Issue | [#26121](https://github.com/vllm-project/vllm/issues/26121) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  vLLM merges special XML-like tags into single tokens, causing tokenization mismatch with HuggingFace

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary When vLLM generates text containing special XML-like tags (e.g., ` `, ` `, ` `), it returns them as **single tokens** with single logprobs. However, retokenizing the same text using the HuggingFace tokenizer produces **multiple tokens**. This creates a position-level mismatch that makes it impossible to align vLLM logprobs with local tokenization for KL divergence computation. ## Steps to Reproduce Step 1: Start vLLM server with: ``` vllm serve Qwen/Qwen2.5-VL-7B-Instruct \ --port 8666 --host 0.0.0.0 \ --dtype bfloat16 \ --api-key token-abc123 \ --tensor-parallel-size 4 \ --limit-mm-per-prompt image=2,video=2 \ --gpu-memory-utilization 0.9 \ --max-model-len 32768 \ --max-num-batched-tokens 65536 \ --max-num-seqs 256 \ --enable-prefix-caching ``` Step 2: Run this script: python reproduce_vllm_token_mismatch.py ``` import json import requests from transformers import AutoTokenizer VLLM_URL = "http://localhost:8666/v1/chat/completions" MODEL_NAME = "Qwen/Qwen2.5-VL-7B-Instruct" API_KEY = "token-abc123" tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct", trust_remote_code=True) print("="*80) print("PAR...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: LM merges special XML-like tags into single tokens, causing tokenization mismatch with HuggingFace bug;stale ### Your current environment ### 🐛 Describe the bug ## Summary When vLLM generates text containing special XML...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rve Qwen/Qwen2.5-VL-7B-Instruct \ --port 8666 --host 0.0.0.0 \ --dtype bfloat16 \ --api-key token-abc123 \ --tensor-parallel-size 4 \ --limit-mm-per-prompt image=2,video=2 \ --gpu-memory-utilization 0.9 \ --max-model-le...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ial XML-like tags into single tokens, causing tokenization mismatch with HuggingFace bug;stale ### Your current environment ### 🐛 Describe the bug ## Summary When vLLM generates text containing special XML-like tags (e....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: vLLM merges special XML-like tags into single tokens, causing tokenization mismatch with HuggingFace bug;stale ### Your current environment ### 🐛 Describe the bug ## Summary When vLLM generates text containing sp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: merges special XML-like tags into single tokens, causing tokenization mismatch with HuggingFace bug;stale ### Your current environment ### 🐛 Describe the bug ## Summary When vLLM generates text containing special XML-li...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
