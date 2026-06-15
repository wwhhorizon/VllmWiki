# vllm-project/vllm#2147: GPTQ models don't support CUDA graph

| 字段 | 值 |
| --- | --- |
| Issue | [#2147](https://github.com/vllm-project/vllm/issues/2147) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> GPTQ models don't support CUDA graph

### Issue 正文摘录

Got the following error while running `python examples/llm_engine_example.py --model TheBloke/Mixtral-8x7B-v0.1-GPTQ --dtype half`: ``` File "/home/wskwon/workspace/vllm/vllm/model_executor/layers/sampler.py", line 396, in _random_sample random_samples = torch.multinomial(probs, RuntimeError: probability tensor contains either `inf`, `nan` or element < 0 ``` The error didn't appear when the `--enforce-eager` flag was set. *AWQ models did not raise errors. I guess this is somehow related to exllama v2 kernels.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: examples/llm_engine_example.py --model TheBloke/Mixtral-8x7B-v0.1-GPTQ --dtype half`: ``` File "/home/wskwon/workspace/vllm/vllm/model_executor/layers/sampler.py", line 396, in _random_sample random_samples = torch.mult...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: GPTQ models don't support CUDA graph bug Got the following error while running `python examples/llm_engine_example.py --model TheBloke/Mixtral-8x7B-v0.1-GPTQ --dtype half`: ``` File "/home/wskwon/workspace/vllm/vllm/mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ss model_support;quantization cuda;kernel;quantization nan_inf dtype;env_dependency Got the following error while running `python examples/llm_engine_example.py --model TheBloke/Mixtral-8x7B-v0.1-GPTQ --dtype half`:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: GPTQ models don't support CUDA graph bug Got the following error while running `python examples/llm_engine_example.py --model TheBloke/Mixtral-8x7B-v0.1-GPTQ --dtype half`: ``` File "/home/wskwon/workspace/vllm/vllm/mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
