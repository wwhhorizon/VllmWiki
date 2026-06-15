# vllm-project/vllm#574: Error loading Llama2 model 

| 字段 | 值 |
| --- | --- |
| Issue | [#574](https://github.com/vllm-project/vllm/issues/574) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error loading Llama2 model 

### Issue 正文摘录

Hi, I'm using the latest version of vllm, which should in principle support the `meta-llama/Llama-2-7b-chat-hf`, but when I tried to load it through the LLM entrypoint I get the following error: ``` File "/home/pierluca/micromamba/envs/llm_planning/lib/python3.11/site-packages/vllm/worker/worker.py", line 45, in __init__ self.model = get_model(model_config) ^^^^^^^^^^^^^^^^^^^^^^^ File "/home/pierluca/micromamba/envs/llm_planning/lib/python3.11/site-packages/vllm/model_executor/model_loader.py", line 49, in get_model model.load_weights(model_config.model, model_config.download_dir, File "/home/pierluca/micromamba/envs/llm_planning/lib/python3.11/site-packages/vllm/model_executor/models/llama.py", line 282, in load_weights assert param_slice.shape == loaded_weight.shape ``` Is there anything I'm doing wrong? I can load the 7b and 13b models without any problems.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Error loading Llama2 model Hi, I'm using the latest version of vllm, which should in principle support the `meta-llama/Llama-2-7b-chat-hf`, but when I tried to load it through the LLM entrypoint I get the following erro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Error loading Llama2 model Hi, I'm using the latest version of vllm, which should in principle support the `meta-llama/Llama-2-7b-chat-hf`, but when I tried to load it through the LLM entrypoint I get the following erro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Error loading Llama2 model Hi, I'm using the latest version of vllm, which should in principle support the `meta-llama/Llama-2-7b-chat-hf`, but when I tried to load it through the LLM entrypoint I get the following erro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
