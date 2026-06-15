# vllm-project/vllm#1054: RuntimeError: CUDA error: OS call failed or operation not supported on this OS 

| 字段 | 值 |
| --- | --- |
| Issue | [#1054](https://github.com/vllm-project/vllm/issues/1054) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: CUDA error: OS call failed or operation not supported on this OS 

### Issue 正文摘录

I get an error when I use Vllm to speed up model inference: When I first use 4 A100*40G graphics cards, I can reason normally, but when I use 8 3090 * 24G graphics cards, I get an error. The specific error information is as follows: ``` (base) root@I1516380d0c001014e6:/hy-tmp/vllm_test# python test.py 2023-09-15 12:33:58,024 INFO worker.py:1621 -- Started a local Ray instance. INFO 09-15 12:33:59 llm_engine.py:72] Initializing an LLM engine with config: model='/hy-tmp/openbuddy-llama2-70b-v10.1-bf16', tokenizer='/hy-tmp/openbuddy-llama2-70b-v10.1-bf16', tokenizer_mode=auto, revision=None, trust_remote_code=True, dtype=torch.bfloat16, download_dir=None, load_format=auto, tensor_parallel_size=8, seed=0) INFO 09-15 12:33:59 tokenizer.py:30] For some LLaMA V1 models, initializing the fast tokenizer may take a long time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. INFO 09-15 12:35:28 llm_engine.py:201] # GPU blocks: 7384, # CPU blocks: 6553 Traceback (most recent call last): File "test3.py", line 22, in llm = LLM(model="/hy-tmp/openbuddy-llama2-70b-v10.1-bf16", tensor_parallel_size=8, trust_remote_code=True)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ally, but when I use 8 3090 * 24G graphics cards, I get an error. The specific error information is as follows: ``` (base) root@I1516380d0c001014e6:/hy-tmp/vllm_test# python test.py 2023-09-15 12:33:58,024 INFO worker.p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ion not supported on this OS I get an error when I use Vllm to speed up model inference: When I first use 4 A100*40G graphics cards, I can reason normally, but when I use 8 3090 * 24G graphics cards, I get an error. The...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ing an LLM engine with config: model='/hy-tmp/openbuddy-llama2-70b-v10.1-bf16', tokenizer='/hy-tmp/openbuddy-llama2-70b-v10.1-bf16', tokenizer_mode=auto, revision=None, trust_remote_code=True, dtype=torch.bfloat16, down...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: RuntimeError: CUDA error: OS call failed or operation not supported on this OS I get an error when I use Vllm to speed up model inference: When I first use 4 A100*40G graphics cards, I can reason normally, but when I us...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: api;model_support;sampling_logits cuda;kernel;sampling build_error;crash;mismatch dtype;env_dependency I get an error when I use Vllm to speed up model inference:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
