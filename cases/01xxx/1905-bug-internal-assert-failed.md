# vllm-project/vllm#1905: Bug: INTERNAL ASSERT FAILED

| 字段 | 值 |
| --- | --- |
| Issue | [#1905](https://github.com/vllm-project/vllm/issues/1905) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;gemm_linear;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Bug: INTERNAL ASSERT FAILED

### Issue 正文摘录

Model: `TheBloke/Mistral-7B-OpenOrca-AWQ` (and any other Mistral AWQ model of them) Cuda: `12.2` ``` WARNING 12-03 17:13:44 config.py:398] Casting torch.bfloat16 to torch.float16. WARNING 12-03 17:13:44 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 12-03 17:13:44 llm_engine.py:72] Initializing an LLM engine with config: model='TheBloke/Mistral-7B-OpenOrca-AWQ', tokenizer='TheBloke/Mistral-7B-OpenOrca-AWQ', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. Traceback (most recent call last): File "/home/ai/ml/llm/inference/vllm/awq_test.py", line 37, in llm = LLM(model="TheBloke/Mistral-7B-OpenOrca-AWQ", quantization="AWQ", trust_remote_code=True, dtype="half") File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 93, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/home/a...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: m) Cuda: `12.2` ``` WARNING 12-03 17:13:44 config.py:398] Casting torch.bfloat16 to torch.float16. WARNING 12-03 17:13:44 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than non-quan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Bug: INTERNAL ASSERT FAILED Model: `TheBloke/Mistral-7B-OpenOrca-AWQ` (and any other Mistral AWQ model of them) Cuda: `12.2` ``` WARNING 12-03 17:13:44 config.py:398] Casting torch.bfloat16 to torch.float16. WARNING 12-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: , load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. Traceback (most recent call las...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: back (most recent call last): File "/home/ai/ml/llm/inference/vllm/awq_test.py", line 37, in llm = LLM(model="TheBloke/Mistral-7B-OpenOrca-AWQ", quantization="AWQ", trust_remote_code=True, dtype="half") File "/home/ai/....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Bloke/Mistral-7B-OpenOrca-AWQ` (and any other Mistral AWQ model of them) Cuda: `12.2` ``` WARNING 12-03 17:13:44 config.py:398] Casting torch.bfloat16 to torch.float16. WARNING 12-03 17:13:44 config.py:140] awq quantiza...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
