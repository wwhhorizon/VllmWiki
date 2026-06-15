# vllm-project/vllm#755: cusparse.h

| 字段 | 值 |
| --- | --- |
| Issue | [#755](https://github.com/vllm-project/vllm/issues/755) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | activation;attention;cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> cusparse.h

### Issue 正文摘录

The package generates an error in Ubuntu in my Databricks instance where CUDA is installed. I think the problem is related to CUDA. Any idea? ```!pip install vllm``` ``` Collecting vllm Downloading vllm-0.1.3.tar.gz (102 kB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 102.7/102.7 kB 2.3 MB/s eta 0:00:00a 0:00:01 Installing build dependencies ... done Getting requirements to build wheel ... done Preparing metadata (pyproject.toml) ... done Collecting ninja Using cached ninja-1.11.1-py2.py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (145 kB) Collecting uvicorn Downloading uvicorn-0.23.2-py3-none-any.whl (59 kB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 59.5/59.5 kB 388.2 kB/s eta 0:00:00 0:00:01 Collecting torch>=2.0.0 Using cached torch-2.0.1-cp310-cp310-manylinux1_x86_64.whl (619.9 MB) Requirement already satisfied: pydantic =4.31.0 in /local_disk0/.ephemeral_nfs/cluster_libraries/python/lib/python3.10/site-packages (from vllm) (4.32.0.dev0) Requirement already satisfied: psutil in /databricks/python3/lib/python3.10/site-packages (from vllm) (5.9.0) Collecting fastapi Downloading fastapi-0.101.0-py3-none-any.whl (65 kB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.7/65.7 kB 430.9...

## 现有链接修复摘要

#8751 [Kernel][Quantization] Custom Floating-Point Runtime Quantization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: age generates an error in Ubuntu in my Databricks instance where CUDA is installed. I think the problem is related to CUDA. Any idea? ```!pip install vllm``` ``` Collecting vllm Downloading vllm-0.1.3.tar.gz (102 kB) ━━...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: from transformers>=4.31.0->vllm) (0.13.3) Requirement already satisfied: huggingface-hub =0.15.1 in /local_disk0/.ephemeral_nfs/cluster_libraries/python/lib/python3.10/site-packages (from transformers>=4.31.0->vllm) (0....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: cies ... done Getting requirements to build wheel ... done Preparing metadata (pyproject.toml) ... done Collecting ninja Using cached ninja-1.11.1-py2.py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (145 kB) Col...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O2 -std=c++17 -D_GLIBCXX_USE_CX...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: The package generates an error in Ubuntu in my Databricks instance where CUDA is installed. I think the problem is related to CUDA. Any idea? ```!pip install vllm``` ``` Collecting vllm Downloading vllm-0.1.3.tar.gz (10...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8751](https://github.com/vllm-project/vllm/pull/8751) | mentioned | 0.6 | [Kernel][Quantization] Custom Floating-Point Runtime Quantization | sed on [FP6-LLM](https://arxiv.org/abs/2401.14112v2), and ported from PygmalionAI/aphrodite-engine#755 FIX #8716 FIX #4515 ## Usage ```sh vllm serve NousResearch/Meta-Llama-3.1-8B… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
