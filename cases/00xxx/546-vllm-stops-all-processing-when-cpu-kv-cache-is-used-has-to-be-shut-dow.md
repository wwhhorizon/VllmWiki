# vllm-project/vllm#546: vLLM stops all processing when CPU KV cache is used, has to be shut down and restarted.

| 字段 | 值 |
| --- | --- |
| Issue | [#546](https://github.com/vllm-project/vllm/issues/546) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache |
| 症状 | nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM stops all processing when CPU KV cache is used, has to be shut down and restarted.

### Issue 正文摘录

Hi The issue: with `--swap-space X` specified, as soon as CPU KV cache is used, vLLM stops all processing. CPU and GPU usage go to 0%, and the request never returns. Any future requests are also never answered. There is no error. I am testing the latest vLLM code (commit 6fc2a38) in a Docker container. I have experienced the issue since I first started using vLLM about 4 days ago, so it's not specific to the latest commits. I am launching vLLM with the following args: ``` --model lmsys/vicuna-7b-v1.3 --host 0.0.0.0 --tokenizer hf-internal-testing/llama-tokenizer --swap-space 100 ``` I am currently testing on a 1 x 4090 system, but I have experienced it on all GPU types I've tried, including A6000 and H100. The following test code will quickly trigger the issue on a 1 x 4090 system: ```python import time import requests url = 'http://localhost:8000/v1/completions' headers = {'Content-Type': 'application/json'} data = { "model": "lmsys/vicuna-7b-v1.3", "prompt": " Write a story about a cat named George."*40, "max_tokens": 950, "temperature": 0.7, "n":125 } s=time.time() response = requests.post(url, headers=headers, json=data) print(time.time()-s) ``` Here's a screenshot demonstrati...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: be shut down and restarted. bug Hi The issue: with `--swap-space X` specified, as soon as CPU KV cache is used, vLLM stops all processing. CPU and GPU usage go to 0%, and the request never returns. Any future requests a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the latest commits. I am launching vLLM with the following args: ``` --model lmsys/vicuna-7b-v1.3 --host 0.0.0.0 --tokenizer hf-internal-testing/llama-tokenizer --swap-space 100 ``` I am currently testing on a 1 x 4090...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: is used, vLLM stops all processing. CPU and GPU usage go to 0%, and the request never returns. Any future requests are also never answered. There is no error. I am testing the latest vLLM code (commit 6fc2a38) in a Dock...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t I have experienced it on all GPU types I've tried, including A6000 and H100. The following test code will quickly trigger the issue on a 1 x 4090 system: ```python import time import requests url = 'http://localhost:8...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: vLLM stops all processing when CPU KV cache is used, has to be shut down and restarted. bug Hi The issue: with `--swap-space X` specified, as soon as CPU KV cache is used, vLLM stops all processing. CPU and GPU usage go...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
