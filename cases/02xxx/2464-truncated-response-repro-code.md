# vllm-project/vllm#2464: Truncated response -- repro code

| 字段 | 值 |
| --- | --- |
| Issue | [#2464](https://github.com/vllm-project/vllm/issues/2464) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Truncated response -- repro code

### Issue 正文摘录

We noticed mixtral behaving oddly, and narrow down to a (maybe) 100% repro on 0.2.7. Script is in the zip file. Just replace base_url's FILLIN with your endpoint. [testmixnew1.py.zip](https://github.com/vllm-project/vllm/files/13959783/testmixnew1.py.zip) Mixtral was run like: ``` export CUDA_HOME=/usr/local/cuda-12.3 export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu123" pip install git+https://github.com/vllm-project/vllm.git pip install mosaicml-turbo --upgrade pip install git+https://github.com/stanford-futuredata/megablocks.git pip install fschat==0.2.34 export CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --port=5002 --host=0.0.0.0 --model mistralai/Mixtral-8x7B-Instruct-v0.1 --seed 1234 --tensor-parallel-size=2 --max-num-batched-tokens=163840 ``` The output is: ``` The Commonwealth Bank of Australia (CBA) reported strong financial results for the first half of fiscal year 2 ``` This is a bad output compared to normal as it is truncated. The server says it was a normal stop, but I don't believe it. The prompt we used is a bit odd in order to repro what we see with normal prompts, so ignore that aspect. There are several \u encodings in th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu123" pip install git+https://github.com/vllm-project/vllm.git pip install mosaicml-turbo --upgrade pip install git+https://github.com/stanford-futuredata/me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm/files/13959783/testmixnew1.py.zip) Mixtral was run like: ``` export CUDA_HOME=/usr/local/cuda-12.3 export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu123" pip install git+https://github.com/vllm-project/v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rbo --upgrade pip install git+https://github.com/stanford-futuredata/megablocks.git pip install fschat==0.2.34 export CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --port=5002 --host=0.0.0.0 --mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ython -m vllm.entrypoints.openai.api_server --port=5002 --host=0.0.0.0 --model mistralai/Mixtral-8x7B-Instruct-v0.1 --seed 1234 --tensor-parallel-size=2 --max-num-batched-tokens=163840 ``` The output is: ``` The Commonw...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s in the zip file. Just replace base_url's FILLIN with your endpoint. [testmixnew1.py.zip](https://github.com/vllm-project/vllm/files/13959783/testmixnew1.py.zip) Mixtral was run like: ``` export CUDA_HOME=/usr/local/cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
