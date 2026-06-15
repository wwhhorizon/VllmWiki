# vllm-project/vllm#799: pip installation error - ERROR: Failed building wheel for vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#799](https://github.com/vllm-project/vllm/issues/799) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | activation;attention;cuda;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> pip installation error - ERROR: Failed building wheel for vllm

### Issue 正文摘录

Dear the team, Thank you for your great work. I have tried to install vllm on my server Linux environment. I got an unexpected error. Could you please advise soon? Thanks! ENV: ``` Pytorch: pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118 Python: 3.8.17 CUDA: 12 ``` ERROR: ``` pip install vllm Collecting vllm Using cached vllm-0.1.3.tar.gz (102 kB) Installing build dependencies ... done Getting requirements to build wheel ... done Preparing metadata (pyproject.toml) ... done Collecting ninja (from vllm) Using cached ninja-1.11.1-py2.py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (145 kB) Collecting psutil (from vllm) Using cached psutil-5.9.5-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (282 kB) Collecting ray>=2.5.1 (from vllm) Obtaining dependency information for ray>=2.5.1 from https://files.pythonhosted.org/packages/2a/9c/4ab1fe33db75eab17d6ef2822c3d418ba47a1a487653b24e5de694410aa4/ray-2.6.3-cp38-cp38-manylinux2014_x86_64.whl.metadata Using cached ray-2.6.3-cp38-cp38-manylinux2014_x86_64.whl.metadata (12 kB) Collecting sentencepiece (from...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: pip installation error - ERROR: Failed building wheel for vllm Dear the team, Thank you for your great work. I have tried to install vllm on my server Linux environment. I got an unexpected error. Could you please advis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: .whl (282 kB) Collecting ray>=2.5.1 (from vllm) Obtaining dependency information for ray>=2.5.1 from https://files.pythonhosted.org/packages/2a/9c/4ab1fe33db75eab17d6ef2822c3d418ba47a1a487653b24e5de694410aa4/ray-2.6.3-c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: cies ... done Getting requirements to build wheel ... done Preparing metadata (pyproject.toml) ... done Collecting ninja (from vllm) Using cached ninja-1.11.1-py2.py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.whl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: idia_nvtx_cu11-11.7.91-py3-none-manylinux1_x86_64.whl (98 kB) Collecting triton==2.0.0 (from torch>=2.0.0->vllm) Using cached triton-2.0.0-1-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (63.2 MB) Requirement...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =2.0.1 --index-url https://download.pytorch.org/whl/cu118 Python: 3.8.17 CUDA: 12 ``` ERROR: ``` pip install vllm Collecting vllm Using cached vllm-0.1.3.tar.gz (102 kB) Installing build dependencies ... done Getting re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
