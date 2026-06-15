# vllm-project/vllm#192: WSL Ubuntu installation issue

| 字段 | 值 |
| --- | --- |
| Issue | [#192](https://github.com/vllm-project/vllm/issues/192) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | activation;attention;cuda;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> WSL Ubuntu installation issue

### Issue 正文摘录

I get the following error when I try to install vllm on WSL Ubuntu. The main take away is - ```Building wheel for vllm (pyproject.toml) did not run successfully.``` Full Error Report - ```bash ❯ python3 -m pip install vllm Collecting vllm Using cached vllm-0.1.0.tar.gz (83 kB) Installing build dependencies ... done Getting requirements to build wheel ... done Preparing metadata (pyproject.toml) ... done Collecting ninja (from vllm) Using cached ninja-1.11.1-py2.py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (145 kB) Collecting psutil (from vllm) Using cached psutil-5.9.5-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (282 kB) Collecting ray (from vllm) Using cached ray-2.5.0-cp38-cp38-manylinux2014_x86_64.whl (56.2 MB) Collecting sentencepiece (from vllm) Using cached sentencepiece-0.1.99-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB) Collecting numpy (from vllm) Using cached numpy-1.24.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.3 MB) Collecting torch>=2.0.0 (from vllm) Using cached torch-2.0.1-cp38-cp38-manylinux1_x86_64.whl (619.9 MB) Collecting transformers>=4.28.0 (from vllm) U...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: WSL Ubuntu installation issue installation I get the following error when I try to install vllm on WSL Ubuntu. The main take away is - ```Building wheel for vllm (pyproject.toml) did not run successfully.``` Full Error...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: orch>=2.0.0->vllm) Using cached lit-16.0.6-py3-none-any.whl Collecting huggingface-hub =0.14.1 (from transformers>=4.28.0->vllm) Using cached huggingface_hub-0.15.1-py3-none-any.whl (236 kB) Collecting packaging>=20.0 (...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: cies ... done Getting requirements to build wheel ... done Preparing metadata (pyproject.toml) ... done Collecting ninja (from vllm) Using cached ninja-1.11.1-py2.py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.whl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB) Collecting nvidia-cuda-nvrtc-cu11==11.7.99 (from torch>=2.0.0->vllm) Using cached nvidia_cuda_nvrtc_cu11-11.7.99-2-py3-none-manylinux1_x86_64.whl (21.0 MB) Collecting...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: idia_nvtx_cu11-11.7.91-py3-none-manylinux1_x86_64.whl (98 kB) Collecting triton==2.0.0 (from torch>=2.0.0->vllm) Using cached triton-2.0.0-1-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (63.2 MB) Requirement...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
