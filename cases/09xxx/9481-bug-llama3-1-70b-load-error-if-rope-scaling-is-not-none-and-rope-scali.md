# vllm-project/vllm#9481: [Bug]: llama3.1 70B load error:  if rope_scaling is not None and rope_scaling["type"] != "su": KeyError: 'type'

| 字段 | 值 |
| --- | --- |
| Issue | [#9481](https://github.com/vllm-project/vllm/issues/9481) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: llama3.1 70B load error:  if rope_scaling is not None and rope_scaling["type"] != "su": KeyError: 'type'

### Issue 正文摘录

### Your current environment ``` vllm: 0.5.5 GPU: A100 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug The error occurred when I loaded Llama 3.1 70B. This error does not appear when I load qwen2.5 72B or llama 3.1 8B ``` python -m vllm.entrypoints.openai.api_server --model /mnt/workspace/hx/LLaMA-Factory/models/Llama-3.1-70B-Instruct/lora/Llama-3.1-70B-Instruct_sft_lora_deepspeed_offload_10k --served-model-name Llama-3.1-70B-Instruct_sft_lora_deepspeed_offload_10k --tensor-parallel-size 8 --port 40195 --chat-template /mnt/workspace/hx/Agent-all-in-one-eval-intern/core/llm/Llama-3.1-70B-Instruct_sft_lora_deepspeed_offload_10k.jinja /mnt/workspace/hx/anaconda3/envs/aio/lib/python3.10/site-packages/_distutils_hack/__init__.py:55: UserWarning: Reliance on distutils from stdlib is deprecated. Users must rely on setuptools to provide the distutils module. Avoid importing distutils or import setuptools first, and avoid setting SETUPTOOLS_USE_DISTUTILS=stdlib. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml warnings.warn( Traceback (most recent call last): File "/mnt/workspace/hx/anaconda3/envs/aio/lib/python3.10/runpy....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: llama3.1 70B load error: if rope_scaling is not None and rope_scaling["type"] != "su": KeyError: 'type' bug ### Your current environment ``` vllm: 0.5.5 GPU: A100 ``` ### Model Input Dumps _No response_ ### 🐛 Des...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: KeyError: 'type' bug ### Your current environment ``` vllm: 0.5.5 GPU: A100 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug The error occurred when I loaded Llama 3.1 70B. This error does not appear when...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: l-size 8 --port 40195 --chat-template /mnt/workspace/hx/Agent-all-in-one-eval-intern/core/llm/Llama-3.1-70B-Instruct_sft_lora_deepspeed_offload_10k.jinja /mnt/workspace/hx/anaconda3/envs/aio/lib/python3.10/site-packages...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed. Users must rely on setuptools to provide the distutils module. Avoid importing distutils or import setuptools first, and avoid setting SETUPTOOLS_USE_DISTUTILS=stdlib. Register concerns at https://github.com/pypa/se...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ls/Llama-3.1-70B-Instruct/lora/Llama-3.1-70B-Instruct_sft_lora_deepspeed_offload_10k --served-model-name Llama-3.1-70B-Instruct_sft_lora_deepspeed_offload_10k --tensor-parallel-size 8 --port 40195 --chat-template /mnt/w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
