# vllm-project/vllm#2417: GPTBigCodeForCausalLM, TP >= 2, output is bloken. Is this BUG?

| 字段 | 值 |
| --- | --- |
| Issue | [#2417](https://github.com/vllm-project/vllm/issues/2417) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPTBigCodeForCausalLM, TP >= 2, output is bloken. Is this BUG?

### Issue 正文摘录

I updated vLLM version from **0.2.1.post1** to **0.2.7**. Model Generation is Broken when tensor_parallel_size >=2. (tensor_parallel_size=1 is NOT bloken） First I found it with my Starchatβ+awq model, and it repro with non awq model [HuggingFaceH4/starchat-beta](https://huggingface.co/HuggingFaceH4/starchat-beta) and [bigcode/starcoderbase-1b](https://huggingface.co/bigcode/starcoderbase-1b) too. ### Base Env - docker image based nvcr.io/nvidia/pytorch:23.08-py3 - Nvidia Driver Version: 525.85.12 - CUDA Version: 12.0 - GPU Tesla T4 - Model [bigcode/starcoderbase-1b](https://huggingface.co/bigcode/starcoderbase-1b) ### Old Env - transformers==4.35.0 - vllm==0.2.1.post1 - xformers==0.0.22 **Engine args** ``` INFO 01-11 07:12:45 llm_engine.py:72] Initializing an LLM engine with config: model='/usr/local/model/llm', tokenizer='/usr/local/model/llm', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) ```` **Input** ``` import numpy as np import scipy as sp def hello_world(): ``` **generated** ``` print('hello world') def show_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: gCodeForCausalLM, TP >= 2, output is bloken. Is this BUG? I updated vLLM version from **0.2.1.post1** to **0.2.7**. Model Generation is Broken when tensor_parallel_size >=2. (tensor_parallel_size=1 is NOT bloken） First...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: . Is this BUG? I updated vLLM version from **0.2.1.post1** to **0.2.7**. Model Generation is Broken when tensor_parallel_size >=2. (tensor_parallel_size=1 is NOT bloken） First I found it with my Starchatβ+awq model, and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) ```` **Input** ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: >=2. (tensor_parallel_size=1 is NOT bloken） First I found it with my Starchatβ+awq model, and it repro with non awq model [HuggingFaceH4/starchat-beta](https://huggingface.co/HuggingFaceH4/starchat-beta) and [bigcode/st...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) ```` **Input**...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
