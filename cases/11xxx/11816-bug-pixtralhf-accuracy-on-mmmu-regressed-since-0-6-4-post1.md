# vllm-project/vllm#11816: [Bug]: PixtralHF accuracy on MMMU regressed since 0.6.4.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#11816](https://github.com/vllm-project/vllm/issues/11816) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: PixtralHF accuracy on MMMU regressed since 0.6.4.post1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems to be that pixtral_hf accuracy has been affected since the last known good result from 0.6.4.post1. [Reference results on HF model card](https://huggingface.co/neuralmagic/pixtral-12b-FP8-dynamic#multimodal-benchmarks), we will look at `MMMU (CoT) ~= 51%. Evals ran using [mistral-evals](https://github.com/mistralai/mistral-evals) vLLM 0.6.4.post1, server and eval: ```console > uv pip install vllm==0.6.4.post1 > vllm serve nm-testing/pixtral-12b-FP8-dynamic --max-num-seqs 30 --max-model-len 30000 --limit-mm-per-prompt image=5 --port 9000 > python -m eval.run eval_vllm --model_name nm-testing/pixtral-12b-FP8-dynamic --url http://0.0.0.0:9000 --output_dir output/ --eval_name "mmmu" ... ================================================================================ Metrics: { "explicit_prompt_relaxed_correctness": 0.5044444444444445, "anywhere_in_answer_relaxed_correctness": 0.5044444444444445 } ================================================================================ ``` vLLM 0.6.5, server and eval: ```console > uv pip install vllm==0.6.5 > vllm serve nm-testing/pixtral-12b-FP8-dy...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: PixtralHF accuracy on MMMU regressed since 0.6.4.post1 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems to be that pixtral_hf accuracy has been affected since t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: PixtralHF accuracy on MMMU regressed since 0.6.4.post1 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems to be that pixtral_hf accuracy has been affected since t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: i/mistral-evals) vLLM 0.6.4.post1, server and eval: ```console > uv pip install vllm==0.6.4.post1 > vllm serve nm-testing/pixtral-12b-FP8-dynamic --max-num-seqs 30 --max-model-len 30000 --limit-mm-per-prompt image=5 --p...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: PixtralHF accuracy on MMMU regressed since 0.6.4.post1 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems to be that pixtral_hf accuracy has been affected since t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: results on HF model card](https://huggingface.co/neuralmagic/pixtral-12b-FP8-dynamic#multimodal-benchmarks), we will look at `MMMU (CoT) ~= 51%. Evals ran using [mistral-evals](https://github.com/mistralai/mistral-evals...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
