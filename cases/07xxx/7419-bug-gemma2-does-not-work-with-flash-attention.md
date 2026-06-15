# vllm-project/vllm#7419: [Bug]: `gemma2` does not work with flash attention

| 字段 | 值 |
| --- | --- |
| Issue | [#7419](https://github.com/vllm-project/vllm/issues/7419) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `gemma2` does not work with flash attention

### Issue 正文摘录

### 🐛 Describe the bug Running latest nightly, I see different results for FlashInfer vs FlashAttention Backend even after logits soft capping landing Install: ```bash export VLLM_VERSION=0.5.4 pip install [https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-${VLLM_VERSION}-cp38-abi3-manylinux1_x86_64.whl](https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-$%7BVLLM_VERSION%7D-cp38-abi3-manylinux1_x86_64.whl) pip install lm_eval==0.4.3 pip install https://github.com/flashinfer-ai/flashinfer/releases/download/v0.1.2/flashinfer-0.1.2+cu121torch2.4-cp310-cp310-linux_x86_64.whl ``` - flash attention ```bash MODEL=google/gemma-2-27b-it lm_eval --model vllm --model_args pretrained=$MODEL,add_bos_token=true --tasks gsm8k --num_fewshot 5 --limit 250 --batch_size "auto" |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.196|± |0.0252| | | |strict-match | 5|exact_match|↑ |0.192|± |0.0250| ``` - flash infer ```bash MODEL=google/gemma-2-27b-it VLLM_ATTENTION_BACKEND=FLASHINFER lm_eval --model vllm --model_args pretrained=$MODEL,add_bos_token=true --tas...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: `gemma2` does not work with flash attention bug ### 🐛 Describe the bug Running latest nightly, I see different results for FlashInfer vs FlashAttention Backend even after logits soft capping landing Install: ```b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: hInfer vs FlashAttention Backend even after logits soft capping landing Install: ```bash export VLLM_VERSION=0.5.4 pip install [https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-${VLLM_VERSION}-cp38-abi3-manyl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: `gemma2` does not work with flash attention bug ### 🐛 Describe the bug Running latest nightly, I see different results for FlashInfer vs FlashAttention Backend even after logits soft capping landing Install: ```b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: does not work with flash attention bug ### 🐛 Describe the bug Running latest nightly, I see different results for FlashInfer vs FlashAttention Backend even after logits soft capping landing Install: ```bash export VLLM_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: --model vllm --model_args pretrained=$MODEL,add_bos_token=true --tasks gsm8k --num_fewshot 5 --limit 250 --batch_size "auto" |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|----...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
